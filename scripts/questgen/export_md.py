"""Export every chapter's quest text to one Markdown file for review.

usage: python3 export_md.py OUT.md
"""
import re
import sys
from pathlib import Path

import content
from gen import load_chapters

NAMES = {}
for line in (Path(__file__).parent / "index/items.tsv").read_text().splitlines():
    i, name, _ = (line.split("\t") + ["", ""])[:3]
    NAMES[i] = name


def md(s):
    """FTB formatting codes to Markdown: highlighted spans become bold, other codes drop."""
    s = re.sub(r"&[0-9a-f]([^&]*?)&r", r"**\1**", s)
    return re.sub(r"&[0-9a-fk-or]", "", s)


def name(i):
    return f"{NAMES.get(i) or i}"


def task(t):
    n = f" x{t['count']}" if t.get("count", 1) != 1 else ""
    if "check" in t:
        return f"Checkmark: \"{t['check']}\""
    if "item" in t:
        return f"{t.get('title') or name(t['item'])}{n}"
    if "tag" in t:
        return f"{t.get('title')} (tag `{t['tag']}`){n}"
    if "any" in t:
        return f"{t.get('title')} (any of {len(t['any'])}){n}"
    if "filter" in t:
        return f"{t.get('title')}{n}"
    if "kill" in t:
        return f"Kill {t.get('title') or t['kill']}{n}"
    for k in ("structure", "biome", "dimension", "advancement", "stat"):
        if k in t:
            return f"{k.title()}: {t.get('title') or t[k]}" + (f" ({t['value']})" if k == "stat" and t.get("value", 1) != 1 else "")
    return str(t)


def reward(r):
    n = f" x{r['count']}" if r.get("count", 1) != 1 else ""
    if "xp" in r:
        return f"{r['xp']} XP"
    if "xp_levels" in r:
        return f"{r['xp_levels']} levels"
    if "crate" in r:
        return f"{r['crate'].title()} crate{n}"
    if "book" in r:
        return f"Book: {r['book'].split(':')[1].replace('_', ' ')} {r.get('level', 1)}"
    if "item" in r:
        return f"{name(r['item'])}{n}"
    if "command" in r:
        return "Chat announcement"
    return str(r)


def main():
    out = ["# Hearth & Hollow quest book", ""]
    chapters = load_chapters()
    total = sum(len(c["quests"]) for c in chapters)
    out += [f"{len(chapters)} chapters, {total} quests. Highlighted words in game show as **bold** here.", ""]
    groups = {g["key"]: g["title"] for g in content.GROUPS}
    for n, ch in enumerate(chapters, 1):
        out += [f"## {n}. {ch['title']}", ""]
        meta = f"*{groups[ch['group']]}*"
        if ch.get("subtitle"):
            meta += f" · {md(ch['subtitle'])}"
        out += [meta, ""]
        for q in ch["quests"]:
            flags = []
            if q.get("optional"):
                flags.append("optional")
            if q.get("repeat"):
                flags.append("repeatable")
            out += [f"### {md(q['title'])}" + (f" ({', '.join(flags)})" if flags else ""), ""]
            if q.get("subtitle"):
                out += [f"*{md(q['subtitle'])}*", ""]
            para = []
            for line in q["desc"]:
                if line == "":
                    if para:
                        out += ["  \n".join(para), ""]
                        para = []
                else:
                    para.append(md(line))
            if para:
                out += ["  \n".join(para), ""]
            out += ["- **Tasks:** " + "; ".join(task(t) for t in q["tasks"])]
            if q.get("rewards"):
                out += ["- **Rewards:** " + ", ".join(reward(r) for r in q["rewards"])]
            out += [""]
    Path(sys.argv[1]).write_text("\n".join(out))
    print(f"wrote {sys.argv[1]}: {total} quests")


if __name__ == "__main__":
    main()
