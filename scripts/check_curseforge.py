"""Check docs/curseforge.md: every word in the summary must also appear in the description.

usage: python3 scripts/check_curseforge.py [docs/curseforge.md]
"""
import re
import sys
from pathlib import Path


def section(text, name):
    m = re.search(rf"^## {name}\n(.*?)(?=^## |\Z)", text, re.S | re.M)
    if not m:
        sys.exit(f"check_curseforge: no '## {name}' section")
    return m.group(1)


def words(text):
    return {w.lower() for w in re.findall(r"[A-Za-z0-9][A-Za-z0-9'&-]*", text)}


path = Path(sys.argv[1] if sys.argv[1:] else Path(__file__).parents[1] / "docs/curseforge.md")
text = path.read_text()
missing = sorted(words(section(text, "Summary")) - words(section(text, "Description")))
if missing:
    sys.exit(f"check_curseforge: summary words not in the description: {', '.join(missing)}")
print("check_curseforge: summary ok")
