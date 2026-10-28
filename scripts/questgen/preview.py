"""ASCII preview of chapter layouts: o quest, O first/finale, digits mark 2+ deps.

usage: python3 preview.py [file stem ...]
"""
import sys
from gen import Book, load_chapters

for ch in load_chapters():
    if sys.argv[1:] and ch["file"] not in sys.argv[1:]:
        continue
    pos, deps = Book.layout(ch)
    big = {q["key"] for q in ch["quests"] if q.get("size", 1) >= 1.5}
    xs = [p[0] for p in pos.values()]; ys = [p[1] for p in pos.values()]
    W = int(round((max(xs) - min(xs)) * 2.5)) + 2; H = int(round(max(ys) - min(ys))) + 2
    grid = [[" "] * W for _ in range(H)]
    for k, (x, y) in pos.items():
        c = "O" if k in big else (str(len(deps[k])) if len(deps.get(k, [])) > 1 else "o")
        grid[int(round(y - min(ys)))][int(round((x - min(xs)) * 2.5))] = c
    print(f"== {ch['title']} ({len(pos)})")
    print("\n".join("".join(r).rstrip() for r in grid))
    print()
