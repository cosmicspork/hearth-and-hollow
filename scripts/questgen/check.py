"""Validate chapter files: ids exist in the pack, layout is complete, text follows the rules.

usage: python3 check.py [chapters/NN_name.py ...]   (default: every chapter)
Exit status 1 if anything is wrong. Needs index/, which `just quest-index` builds from the mod jars.
"""
import importlib.util
import re
import sys
import tempfile
from pathlib import Path

import content
from gen import Book, load_chapters

HERE = Path(__file__).parent
IDX = HERE / "index"


if not (IDX / "items.tsv").exists():
    sys.exit("check.py: no index/ yet. Run `just sync` and then `just quest-index` to build it.")


def lines(name):
    return {l.split("\t")[0] for l in (IDX / name).read_text().splitlines() if l}


ITEMS = lines("items.tsv")
# Items the pack registers itself in KubeJS aren't in any mod jar, so the index can't see them.
ITEMS |= {m for p in (HERE.parents[1] / "kubejs/startup_scripts").glob("*.js")
          for m in re.findall(r"""\.create\(['"]([a-z0-9_]+:[a-z0-9_/]+)['"]\)""", p.read_text())}
ITEM_TAGS = {t.lstrip("#") for t in lines("item_tags.txt")}
ENTITIES = lines("entities.tsv")
STRUCTURES = lines("structures.txt")
STRUCTURE_TAGS = lines("structure_tags.txt")
BIOMES = lines("biomes.txt")
BIOME_TAGS = lines("biome_tags.txt")
ADVANCEMENTS = lines("advancements.txt")
DIMENSIONS = lines("dimensions.txt") | {"minecraft:the_nether"}
CRATES = {t["name"] for t in content.TABLES}
THEMES = {t["name"]: t for t in content.THEMES}
GROUPS = {g["key"] for g in content.GROUPS}

# Generation for these is switched off in the pack; don't send players looking for them.
DISABLED_ORES = re.compile(
    r"^(alltheores:.*(cinnabar|iridium|peridot|ruby|sapphire).*_ore"
    r"|mekanism:.*_ore|oritech:.*(nickel|platinum).*ore|xycraft_world:.*aluminum.*ore)$")
DASHES = re.compile("[–—]")
QUEST_KEYS = {"key", "title", "subtitle", "desc", "tasks", "rewards", "shape", "size", "icon",
              "icon_components", "optional", "wide", "repeat"}
SHAPES = {"circle", "square", "rsquare", "diamond", "pentagon", "hexagon", "octagon", "heart", "gear"}


def load(path):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.CHAPTER


def check_chapter(ch, errs, warns):
    where = ch.get("file", "?")

    def err(msg):
        errs.append(f"{where}: {msg}")

    def item_ok(i, ctx):
        if i not in ITEMS:
            err(f"{ctx}: unknown item {i}")
        elif DISABLED_ORES.match(i):
            err(f"{ctx}: {i} doesn't generate in this pack")

    def text_ok(s, ctx):
        if DASHES.search(s):
            err(f"{ctx}: no em or en dashes in text")

    for k in ("file", "title", "icon", "layout", "quests"):
        if k not in ch:
            err(f"missing chapter key {k}")
    if ch.get("group") and ch["group"] not in GROUPS:
        err(f"unknown group {ch.get('group')}")
    if ch.get("theme") and ch["theme"] not in THEMES:
        err(f"unknown theme {ch.get('theme')}")
    item_ok(ch.get("icon"), "chapter icon")
    text_ok(ch.get("title", "") + ch.get("subtitle", ""), "chapter title")
    keys = [q.get("key") for q in ch.get("quests", [])]
    dupes = {k for k in keys if keys.count(k) > 1}
    if dupes:
        err(f"duplicate quest keys {sorted(dupes)}")
    deps = {}
    try:
        pos, deps = Book.layout(ch)
        missing, extra = set(keys) - set(pos), set(pos) - set(keys)
        if missing:
            err(f"quests not in layout: {sorted(missing)}")
        if extra:
            err(f"layout names unknown quests: {sorted(extra)}")
        for l in ch.get("links", []):
            pos[f"link to {l.get('quest')}"] = tuple(l.get("pos", (0, 0)))
        items = list(pos.items())
        for n, (k, p) in enumerate(items):
            for k2, p2 in items[n + 1:]:
                if abs(p[0] - p2[0]) < 1.2 and abs(p[1] - p2[1]) < 1.2:
                    err(f"{k} {p} and {k2} {p2} are too close together")
    except Exception as e:  # noqa: BLE001
        err(f"layout: {e!r}")

    for q in ch.get("quests", []):
        ctx = f"quest {q.get('key')}"
        for k in q:
            if k not in QUEST_KEYS:
                err(f"{ctx}: unknown key {k}")
        if not q.get("title") or not isinstance(q.get("desc"), list) or not q["desc"]:
            err(f"{ctx}: needs a title and a non-empty desc list")
        for s in [q.get("title", ""), q.get("subtitle", "")] + list(q.get("desc", [])):
            if not isinstance(s, str):
                err(f"{ctx}: desc lines must be strings")
            else:
                text_ok(s, ctx)
        if q.get("shape") and q["shape"] not in SHAPES:
            err(f"{ctx}: unknown shape {q['shape']}")
        if q.get("icon"):
            item_ok(q["icon"], ctx + " icon")
        if not q.get("tasks"):
            err(f"{ctx}: no tasks")
        for t in q.get("tasks", []):
            tc = f"{ctx} task {t}"
            if t.get("icon"):
                item_ok(t["icon"], tc)
            if "item" in t:
                item_ok(t["item"], tc)
            elif "tag" in t:
                if t["tag"].lstrip("#") not in ITEM_TAGS:
                    err(f"{tc}: unknown item tag")
                if not t.get("icon"):
                    err(f"{tc}: tag tasks need an icon")
            elif "any" in t:
                for i in t["any"]:
                    item_ok(i, tc)
                if not t.get("icon"):
                    err(f"{tc}: 'any' tasks need an icon")
            elif "filter" in t:
                for i in re.findall(r"\bitem\(([^)]+)\)", t["filter"]):
                    item_ok(i, tc)
                for g in re.findall(r"\bitem_tag\(([^)]+)\)", t["filter"]):
                    if g not in ITEM_TAGS:
                        err(f"{tc}: unknown item tag {g}")
            elif "kill" in t:
                if t["kill"] not in ENTITIES:
                    err(f"{tc}: unknown entity")
            elif "structure" in t:
                s = t["structure"]
                if s not in (STRUCTURE_TAGS if s.startswith("#") else STRUCTURES):
                    err(f"{tc}: unknown structure")
            elif "biome" in t:
                b = t["biome"]
                if b not in (BIOME_TAGS if b.startswith("#") else BIOMES):
                    err(f"{tc}: unknown biome")
            elif "dimension" in t:
                if t["dimension"] not in DIMENSIONS:
                    err(f"{tc}: unknown dimension")
            elif "advancement" in t:
                if t["advancement"] not in ADVANCEMENTS:
                    err(f"{tc}: unknown advancement")
            elif "stat" in t or "check" in t:
                pass
            else:
                err(f"{tc}: unknown task type")
            for k in ("structure", "biome", "dimension", "kill", "advancement", "stat", "tag", "any", "filter"):
                if k in t and not t.get("title") and k not in ("kill", "advancement"):
                    err(f"{tc}: give this task a title")
        for r in q.get("rewards", []):
            rc = f"{ctx} reward {r}"
            for k in ("crate", "crate_item"):
                if k in r and r[k] not in CRATES:
                    err(f"{rc}: unknown crate")
            if "item" in r:
                item_ok(r["item"], rc)
            if "command" in r and not r["command"].startswith("/"):
                err(f"{rc}: commands start with /")
        # A checkmark quest with nothing before it can be clicked on day one, so it must
        # not pay out, and it keeps the plain checkmark icon to read as information.
        # Welcome Home is the exception: it's the first thing a player sees.
        if (where != "welcome_home" and not deps.get(q.get("key"))
                and q.get("tasks") and all("check" in t for t in q["tasks"])):
            if q.get("rewards"):
                err(f"{ctx}: ungated checkmark quests can't have rewards")
            if q.get("icon"):
                err(f"{ctx}: ungated checkmark quests use the plain checkmark icon")
        if q.get("repeat") and not any(k in t for t in q["tasks"] for k in ("item", "tag", "any", "filter", "kill")):
            warns.append(f"{where}: {ctx} repeats but has nothing to turn in")


def check_links(ch, errs):
    """Links name a quest as chapter_file:key; the target must exist in some chapter."""
    targets = {f"{c['file']}:{q['key']}" for c in load_chapters() for q in c["quests"]}
    for l in ch.get("links", []):
        if l.get("quest") not in targets:
            errs.append(f"{ch.get('file')}: link to unknown quest {l.get('quest')}")
        if l.get("quest", "").split(":")[0] == ch.get("file"):
            errs.append(f"{ch.get('file')}: link {l.get('quest')} points into its own chapter")


def table_item(row):
    it = row[0]
    return None if isinstance(it, tuple) else it


def check_tables(errs):
    """Every item a reward table can give, or shows as its icon, must exist."""
    for t in content.TABLES + content.THEMES + [{"name": "jackpots", "rewards": content.JACKPOTS},
                                                {"name": "staples", "rewards": content.STAPLES}]:
        for row in t["rewards"]:
            i = table_item(row)
            if i and i not in ITEMS:
                errs.append(f"table {t['name']}: unknown item {i}")
            if not 3 <= len(row) <= 4:
                errs.append(f"table {t['name']}: {row} should be (item, count, weight[, bonus])")
        if t.get("icon") and t["icon"] not in ITEMS:
            errs.append(f"table {t['name']}: unknown icon {t['icon']}")


def check_theme_skips(ch, warns):
    """A theme shouldn't hand out what its own chapters ask for: it would skip the quest.
    Jackpots and staples are left out; they're the same in every theme."""
    theme = THEMES.get(ch.get("theme"))
    if not theme:
        return
    gives = {table_item(r) for r in theme["rewards"]} - {None} - theme.get("allow", set())
    for q in ch["quests"]:
        for t in q["tasks"]:
            # A task on a specific variant (an Almanac page) isn't met by the plain item.
            if t.get("components"):
                continue
            for i in ([t["item"]] if "item" in t else []) + t.get("any", []):
                if i in gives:
                    warns.append(f"{ch['file']}: theme {theme['name']} gives {i}, which {q['key']} asks for")


def main():
    paths = [Path(a) for a in sys.argv[1:]]
    chapters = [load(p) for p in paths] if paths else load_chapters()
    errs, warns = [], []
    check_tables(errs)
    for ch in chapters:
        check_chapter(ch, errs, warns)
        check_links(ch, errs)
        check_theme_skips(ch, warns)
    if not errs:
        with tempfile.TemporaryDirectory() as d:
            try:
                Book().build(Path(d), chapters)
            except Exception as e:  # noqa: BLE001
                errs.append(f"build failed: {e!r}")
    for w in warns:
        print("warning:", w)
    for e in errs:
        print("error:", e)
    total = sum(len(c.get("quests", [])) for c in chapters)
    print(f"{len(chapters)} chapter(s), {total} quests, {len(errs)} error(s)")
    sys.exit(1 if errs else 0)


if __name__ == "__main__":
    main()
