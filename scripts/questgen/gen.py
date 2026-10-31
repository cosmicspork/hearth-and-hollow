"""Generate the Hearth & Hollow quest book into config/ftbquests/quests.

usage: python3 gen.py [REPO_DIR]   (default: the repository this script is in)

Chapters live in chapters/NN_name.py, each defining CHAPTER (see README.md).
Crate tables, themed tables and chapter groups live in content.py.
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
    # 09a_x sorts after 09_y, so a chapter can slot in after another without renumbering.
    for p in sorted((HERE / "chapters").glob("[0-9][0-9]*_*.py")):
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


def table_ref(name):
    """A reward table's id as the long FTB stores in table_id. qid clears the top bit, so it fits."""
    return L(int(qid(f"table:{name}"), 16))


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

    # ---- reward tables ------------------------------------------------------
    def tables(self, root):
        """The four crate tables, then the themes, which have an icon instead of a crate."""
        for order, t in enumerate(content.TABLES + content.THEMES):
            rows = list(t["rewards"])
            if "color" not in t:
                # A theme's own entry for a shared item wins, so a theme can make a jackpot likelier.
                own = {repr(r[0]) for r in rows}
                shared = content.JACKPOTS + (content.STAPLES if t.get("staples") else [])
                rows += [r for r in shared if repr(r[0]) not in own]
            d = {
                "id": qid(f"table:{t['name']}"),
                "loot_size": t.get("rolls", 2),
                "order_index": order,
                "rewards": [self.table_entry(t["name"], n, row) for n, row in enumerate(rows)],
                "use_title": True,
            }
            if "color" in t:
                d["loot_crate"] = {
                    "color": t["color"],
                    # FTB's own crate drops stay off: they count every dying mob as a boss.
                    # Mob and boss drops are global loot modifiers in kubejs/data/hearthandhollow.
                    "drops": {"boss": 0, "monster": 0, "passive": 0},
                    "glow": B(1 if t["glow"] else 0),
                    "string_id": t["name"],
                }
            else:
                d["icon"] = item(t["icon"])
            write(root / f"reward_tables/{t['name']}.snbt", d)
            self.lang[f"reward_table.{d['id']}.title"] = t["title"]

    @staticmethod
    def table_entry(table, n, row):
        it, count, weight, *bonus = row
        stack = book(*it[1:]) if isinstance(it, tuple) and it[0] == "book" else (
            it if isinstance(it, dict) else item(it))
        r = {"id": qid(f"table:{table}:{n}"), "item": stack}
        if count != 1:
            r["count"] = count
        if bonus:
            r["random_bonus"] = bonus[0]
        if weight != 1:
            r["weight"] = F(weight)
        return r

    # ---- tasks and rewards --------------------------------------------------
    # A quest's tier marker, {"crate": tier}, pays out from the chapter's theme when it has
    # one: (reward type on the theme, general table rolled as well).
    PAYOUTS = {
        "kindling": ("random", None),
        "hearth": ("loot", None),
        "lantern": ("loot", "lantern"),
        "ember": ("choice", "ember"),
    }

    def reward(self, qkey, n, r, theme=None):
        """One reward entry from a chapter file, as a list of FTB rewards."""
        if "crate" in r:
            kind, extra = self.PAYOUTS[r["crate"]] if theme else ("loot", None)
            rolls = [(kind, theme or r["crate"])] + ([("loot", extra)] if extra else [])
            out = []
            for c in range(r.get("count", 1)):
                for k, (kind, table) in enumerate(rolls):
                    # The first keeps the id the crate item had, so a claimed reward stays claimed.
                    key = f"{qkey}:reward:{n}" + (f":{c}:{k}" if c or k else "")
                    out.append({"id": qid(key), "type": kind, "table_id": table_ref(table)})
            return out
        d = {"id": qid(f"{qkey}:reward:{n}")}
        if "xp" in r:
            d.update(type="xp", xp=r["xp"])
        elif "xp_levels" in r:
            d.update(type="xp_levels", xp_levels=r["xp_levels"])
        elif "crate_item" in r:
            # A crate to open later: the Bounty Board's pay.
            d.update(type="item", item=crate(r["crate_item"]))
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
        return [d]

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
        lines:    several tracks stacked top to bottom, each centred on x = 0 and with no
                  dependency on the others. A line is one of:
                  {"spine": [...], "branches": {...}}  laid out as above;
                  {"flow": [...], "branches": {...}}   like a spine, but a stage may be a list
                      of keys, stacked in one column: a fan out from the stage before and a
                      fan in to the stage after (two lists of the same length pair up);
                  {"rows": [...], "per_row": n}        keys in wrapped rows with no dependencies,
                      for catalogs that need no order.
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
                if "rows" in line:
                    lpos, ldeps = Book.rows_layout(line["rows"], line.get("per_row", 10)), {}
                else:
                    stages = line.get("flow") or line["spine"]
                    lpos, ldeps = Book.flow_layout(stages, line.get("branches", {}))
                xs = [x for x, _ in lpos.values()]
                ys = [y for _, y in lpos.values()]
                dx = -(min(xs) + max(xs)) / 2
                shift = top - min(ys)
                pos.update({k: (x + dx, y + shift) for k, (x, y) in lpos.items()})
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
            xs = [x for x, _ in pos.values()]
            y = min(y for _, y in pos.values()) - LINE_GAP
            x0 = (min(xs) + max(xs)) / 2 - (len(lay["info"]) - 1) * SPINE_DX / 2
            for i, k in enumerate(lay["info"]):
                pos[k] = (x0 + i * SPINE_DX, y)
        return pos, deps

    @staticmethod
    def flow_layout(stages, branches):
        """Stages left to right; a list stage stacks its keys in one column, centred on the line."""
        pos, deps, prev = {}, {}, []
        for i, stage in enumerate(stages):
            keys = stage if isinstance(stage, list) else [stage]
            for j, k in enumerate(keys):
                pos[k] = (i * SPINE_DX, (j - (len(keys) - 1) / 2) * BRANCH_DY)
                if len(prev) == len(keys) > 1:
                    deps[k] = [prev[j]]
                elif prev:
                    deps[k] = list(prev)
            prev = keys
        for root, arms in branches.items():
            x, y0 = pos[root]
            for direction, sign in (("up", -1), ("down", 1)):
                last = root
                for j, k in enumerate(arms.get(direction, []), 1):
                    pos[k] = (x, y0 + sign * j * BRANCH_DY)
                    deps[k] = [last]
                    last = k
        return pos, deps

    @staticmethod
    def rows_layout(keys, per_row):
        """Wrapped rows with no dependencies; a short last row is centred under the others."""
        pos = {}
        for i, k in enumerate(keys):
            r, c = divmod(i, per_row)
            n = min(per_row, len(keys) - r * per_row)
            pos[k] = ((c - (n - 1) / 2) * GRID_DX, r * GRID_DY)
        return pos

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
                "rewards": [d for n, r in enumerate(q.get("rewards", []))
                            for d in self.reward(qkey, n, r, ch.get("theme"))],
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
            # No group puts a chapter above all the groups, in order.
            "group": qid(f"group:{ch['group']}") if ch.get("group") else "",
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
