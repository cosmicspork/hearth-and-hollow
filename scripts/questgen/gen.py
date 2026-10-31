"""Generate the Hearth & Hollow quest book into config/ftbquests/quests.

usage: python3 gen.py [REPO_DIR]   (default: the repository this script is in)

Chapters live in chapters/NN_name.py, each defining CHAPTER (see README.md).
Crate tables and chapter groups live in content.py.
"""
import importlib.util
import math
import re
import sys
from pathlib import Path

from snbt import B, D, F, L, qid, write
import content

HERE = Path(__file__).parent

# Layout spacing, in quest-book grid units.
SPINE_DX = 2.0
BRANCH_DY = 1.5
LINE_GAP = 2.5     # between stacked lines, and above them for info quests
GRID_DX = 1.75
GRID_DY = 1.75
HUB_R = 4.5         # radius of the first ring of spokes
HUB_STAGGER = 1.0   # alternate spokes start this much further out
HUB_DR = 1.75       # each step further out along a spoke


def load_chapters():
    out = []
    for p in sorted((HERE / "chapters").glob("[0-9][0-9]_*.py")):
        spec = importlib.util.spec_from_file_location(p.stem, p)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        out.append(mod.CHAPTER)
    return out


def item(i, count=1, components=None):
    d = {"id": i, "count": count}
    if components:
        d["components"] = components
    return d


def filt(expr):
    """An FTB Filter System smart filter, for tags and either-of tasks."""
    return item("ftbfiltersystem:smart_filter", components={"ftbfiltersystem:filter": expr})


def crate(name, n=1):
    return item("ftbquests:lootcrate", n, {"ftbquests:loot_crate": name})


def book(enchant, level):
    return item("minecraft:enchanted_book", components={
        "minecraft:stored_enchantments": {"levels": {enchant: level}}})


def escape(v):
    """FTB Quests reads & as a formatting code, so a literal one must be \\&."""
    if isinstance(v, list):
        return [escape(x) for x in v]
    return re.sub(r"&(?![0-9a-fk-or])", r"\\&", v)


class Book:
    def __init__(self):
        self.lang = {}

    # ---- crate tables -------------------------------------------------------
    def tables(self, root):
        for order, t in enumerate(content.TABLES):
            tid = qid(f"table:{t['name']}")
            rewards = []
            for n, (it, count, weight) in enumerate(t["rewards"]):
                stack = book(*it[1:]) if isinstance(it, tuple) and it[0] == "book" else (
                    it if isinstance(it, dict) else item(it))
                r = {"id": qid(f"table:{t['name']}:{n}"), "item": stack}
                if count != 1:
                    r["count"] = count
                if weight != 1:
                    r["weight"] = F(weight)
                rewards.append(r)
            write(root / f"reward_tables/{t['name']}.snbt", {
                "id": tid,
                "loot_crate": {
                    "color": t["color"],
                    # FTB's own crate drops stay off: they count every dying mob as a boss.
                    # Mob and boss drops are global loot modifiers in kubejs/data/hearthandhollow.
                    "drops": {"boss": 0, "monster": 0, "passive": 0},
                    "glow": B(1 if t["glow"] else 0),
                    "string_id": t["name"],
                },
                "loot_size": t["rolls"],
                "order_index": order,
                "rewards": rewards,
                "use_title": True,
            })
            self.lang[f"reward_table.{tid}.title"] = t["title"]

    # ---- tasks and rewards --------------------------------------------------
    def reward(self, qkey, n, r):
        d = {"id": qid(f"{qkey}:reward:{n}")}
        if "xp" in r:
            d.update(type="xp", xp=r["xp"])
        elif "xp_levels" in r:
            d.update(type="xp_levels", xp_levels=r["xp_levels"])
        elif "crate" in r:
            d.update(type="item", item=crate(r["crate"]))
        elif "book" in r:
            d.update(type="item", item=book(r["book"], r.get("level", 1)))
        elif "item" in r:
            d.update(type="item", item=item(r["item"], components=r.get("components")))
        elif "command" in r:
            # {p} is the player's name. Level 2 runs as an operator would.
            d.update(type="command", command=r["command"], permission_level=2)
        else:
            raise ValueError(f"{qkey}: unknown reward {r}")
        if r.get("count", 1) != 1:
            d["count"] = r["count"]
        return d

    def task(self, qkey, n, t, consume):
        d = {"id": qid(f"{qkey}:task:{n}")}
        count = t.get("count", 1)
        if "check" in t:
            d["type"] = "checkmark"
            title = t["check"]
        elif "item" in t or "tag" in t or "any" in t or "filter" in t:
            if "item" in t:
                stack = item(t["item"], components=t.get("components"))
                if t.get("components"):
                    d["match_components"] = "fuzzy"
            elif "tag" in t:
                stack = filt(f"item_tag({t['tag']})")
            elif "any" in t:
                stack = filt("or(" + "".join(f"item({i})" for i in t["any"]) + ")")
            else:
                stack = filt(t["filter"])
            d.update(type="item", item=stack)
            if count != 1:
                d["count"] = L(count)
            if consume:
                d["consume_items"] = True
            title = t.get("title")
        elif "kill" in t:
            d.update(type="kill", entity=t["kill"], value=L(count))
            title = t.get("title")
        elif "structure" in t:
            d.update(type="structure", structure=t["structure"])
            title = t.get("title")
        elif "biome" in t:
            d.update(type="biome", biome=t["biome"])
            title = t.get("title")
        elif "dimension" in t:
            d.update(type="dimension", dimension=t["dimension"])
            title = t.get("title")
        elif "advancement" in t:
            d.update(type="advancement", advancement=t["advancement"], criterion="")
            title = t.get("title")
        elif "stat" in t:
            d.update(type="stat", stat=t["stat"], value=t.get("value", 1))
            title = t.get("title")
        else:
            raise ValueError(f"{qkey}: unknown task {t}")
        if t.get("icon"):
            d["icon"] = item(t["icon"], components=t.get("icon_components"))
        if title:
            self.lang[f"task.{d['id']}.title"] = title
        return d

    # ---- layout -------------------------------------------------------------
    @staticmethod
    def layout(ch):
        """Positions and dependencies from the chapter's layout block.

        spine:    keys left to right, each depending on the one before.
        branches: {spine_key: {"up": [...], "down": [...]}}, columns hanging off
                  a spine quest, each depending on the one nearer the spine.
        direction: "right" (default), "down" or "up" turns the whole spine; "up"
                  branches then go left and "down" branches go right.
        hub:      True places spine[0] in the middle with straight spokes around it:
                  each spine quest followed by its "up" branch, and each "down"
                  branch as a spoke of its own. Spokes depend only on the middle.
        lines:    several spines stacked top to bottom, each {"spine": [...], "branches": {...}}
                  laid out as above, all starting at the same left edge. Each line is a
                  separate track with no dependency on the others.
        grid:     rows of keys with no dependencies (the Bounty Board).
        free:     exact positions, with dependencies given separately in deps.
        info:     with any of the above but free, keys set in a row above everything else,
                  with no dependencies: explainers that belong to no line.
        """
        pos, deps = {}, {}
        lay = ch["layout"]
        if "free" in lay:
            # Hand-placed: {"free": {key: (x, y)}, "deps": {key: [keys]}}.
            pos = {k: (float(x), float(y)) for k, (x, y) in lay["free"].items()}
            return pos, {k: list(v) for k, v in lay.get("deps", {}).items()}
        if "grid" in lay:
            for r, row in enumerate(lay["grid"]):
                if not row:
                    continue
                width = (len(row) - 1) * GRID_DX
                for c, k in enumerate(row):
                    pos[k] = (c * GRID_DX - width / 2, r * GRID_DY)
        elif "lines" in lay:
            top = 0.0
            for line in lay["lines"]:
                lpos, ldeps = Book.spine_layout(line["spine"], line.get("branches", {}))
                ys = [y for _, y in lpos.values()]
                shift = top - min(ys)
                pos.update({k: (x, y + shift) for k, (x, y) in lpos.items()})
                deps.update(ldeps)
                top = max(ys) + shift + LINE_GAP
        elif lay.get("hub"):
            pos, deps = Book.hub_layout(lay["spine"], lay.get("branches", {}))
        else:
            pos, deps = Book.spine_layout(lay["spine"], lay.get("branches", {}))
            turn = {"right": lambda x, y: (x, y), "down": lambda x, y: (y, x), "up": lambda x, y: (y, -x)}
            f = turn[lay.get("direction", "right")]
            pos = {k: f(*xy) for k, xy in pos.items()}
        if lay.get("info"):
            x0 = min(x for x, _ in pos.values())
            y = min(y for _, y in pos.values()) - LINE_GAP
            for i, k in enumerate(lay["info"]):
                pos[k] = (x0 + i * SPINE_DX, y)
        return pos, deps

    @staticmethod
    def spine_layout(spine, branches):
        """One spine left to right, with branches hanging up and down off it."""
        pos, deps = {}, {}
        for i, k in enumerate(spine):
            pos[k] = (i * SPINE_DX, 0.0)
            if i:
                deps[k] = [spine[i - 1]]
        for root, arms in branches.items():
            x = pos[root][0]
            for direction, sign in (("up", -1), ("down", 1)):
                prev = root
                for j, k in enumerate(arms.get(direction, []), 1):
                    pos[k] = (x, sign * j * BRANCH_DY)
                    deps[k] = [prev]
                    prev = k
        return pos, deps

    @staticmethod
    def hub_layout(spine, branches):
        center = spine[0]
        pos, deps = {center: (0.0, 0.0)}, {}
        # Every spoke is a straight chain out from the center: a spine quest and its
        # "up" branch, then its "down" branch as a spoke of its own, then any chains
        # hanging straight off the center.
        spokes = []
        for k in spine[1:]:
            arms = branches.get(k, {})
            spokes.append([k] + arms.get("up", []))
            if arms.get("down"):
                spokes.append(arms["down"])
        for direction in ("up", "down"):
            if branches.get(center, {}).get(direction):
                spokes.append(branches[center][direction])
        for i, chain in enumerate(spokes):
            ang = -90.0 + i * 360.0 / len(spokes)
            # Alternate spokes start further out so neighbours don't crowd the ring.
            r0 = HUB_R + (HUB_STAGGER if i % 2 else 0.0)
            prev = center
            for j, k in enumerate(chain):
                pos[k] = Book.polar(r0 + j * HUB_DR, ang)
                deps[k] = [prev]
                prev = k
        return pos, deps

    @staticmethod
    def polar(r, deg):
        t = math.radians(deg)
        return (round(r * math.cos(t), 2), round(r * math.sin(t), 2))

    # ---- chapters -----------------------------------------------------------
    def chapter(self, root, ch, order):
        cid = qid(f"chapter:{ch['file']}")
        pos, deps = self.layout(ch)
        ids = {q["key"]: qid(f"{ch['file']}:{q['key']}") for q in ch["quests"]}
        missing = set(ids) - set(pos)
        extra = set(pos) - set(ids)
        if missing or extra:
            raise ValueError(f"{ch['file']}: not placed {sorted(missing)}; unknown in layout {sorted(extra)}")
        quests = []
        for q in ch["quests"]:
            qkey = f"{ch['file']}:{q['key']}"
            x, y = pos[q["key"]]
            repeat = q.get("repeat", False)
            d = {
                "id": ids[q["key"]],
                "x": D(x),
                "y": D(y),
                "tasks": [self.task(qkey, n, t, repeat) for n, t in enumerate(q["tasks"])],
                "rewards": [self.reward(qkey, n, r) for n, r in enumerate(q.get("rewards", []))],
            }
            if deps.get(q["key"]):
                d["dependencies"] = [ids[k] for k in deps[q["key"]]]
            if repeat:
                d["can_repeat"] = True
            if q.get("shape"):
                d["shape"] = q["shape"]
            if q.get("size"):
                d["size"] = D(q["size"])
            if q.get("icon"):
                d["icon"] = item(q["icon"], components=q.get("icon_components"))
            if q.get("optional"):
                d["optional"] = True
            if q.get("wide"):
                d["min_width"] = 300
            quests.append(d)
            self.lang[f"quest.{d['id']}.title"] = q["title"]
            if q.get("subtitle"):
                self.lang[f"quest.{d['id']}.quest_subtitle"] = q["subtitle"]
            self.lang[f"quest.{d['id']}.quest_desc"] = q["desc"]
        links = [self.link(ch["file"], l) for l in ch.get("links", [])]
        write(root / f"chapters/{ch['file']}.snbt", {
            "default_hide_dependency_lines": False,
            "default_quest_shape": "",
            "filename": ch["file"],
            "group": qid(f"group:{ch['group']}"),
            "icon": item(ch["icon"]),
            "id": cid,
            "order_index": order,
            "progression_mode": "flexible",
            "quest_links": links,
            "quests": quests,
        })
        self.lang[f"chapter.{cid}.title"] = ch["title"]
        if ch.get("subtitle"):
            self.lang[f"chapter.{cid}.chapter_subtitle"] = [ch["subtitle"]]

    @staticmethod
    def link(file, l):
        """A quest from another chapter shown here too: {"quest": "chapter_file:key", "pos": (x, y)}.
        The position is in final chapter coordinates, and a link has no dependency lines."""
        x, y = l["pos"]
        d = {"id": qid(f"{file}:link:{l['quest']}"), "linked_quest": qid(l["quest"]), "x": D(x), "y": D(y)}
        if l.get("size"):
            d["size"] = D(l["size"])
        return d

    def build(self, root, chapters):
        write(root / "data.snbt", {
            "default_autoclaim_rewards": "disabled",
            "default_consume_items": False,
            "default_quest_disable_jei": False,
            "default_quest_shape": "circle",
            "default_reward_team": False,
            "detection_delay": 20,
            "disable_gui": False,
            "drop_book_on_death": False,
            "drop_loot_crates": False,
            "emergency_items_cooldown": 300,
            "fallback_locale": "",
            "grid_scale": D(0.5),
            "hide_excluded_quests": False,
            "icon": item("minecraft:campfire"),
            "lock_message": "",
            "loot_crate_no_drop": {"boss": 0, "monster": 600, "passive": 4000},
            "pause_game": False,
            "progression_mode": "flexible",
            "show_lock_icons": True,
            "verify_on_load": False,
            "version": 13,
        })
        self.lang["file.0000000000000001.title"] = "Hearth & Hollow"
        groups = []
        for g in content.GROUPS:
            gid = qid(f"group:{g['key']}")
            groups.append({"id": gid})
            self.lang[f"chapter_group.{gid}.title"] = g["title"]
        write(root / "chapter_groups.snbt", {"chapter_groups": groups})
        self.tables(root)
        for order, ch in enumerate(chapters):
            self.chapter(root, ch, order)
        write(root / "lang/en_us.snbt", {k: escape(v) for k, v in self.lang.items()})


def main():
    repo = Path(sys.argv[1]) if sys.argv[1:] else HERE.parents[1]
    root = repo / "config/ftbquests/quests"
    for old in list(root.glob("chapters/*.snbt")) + list(root.glob("reward_tables/*.snbt")):
        old.unlink()
    Book().build(root, load_chapters())


if __name__ == "__main__":
    main()
