"""Draw chapter layouts as PNGs, to judge balance and spacing without starting the game.

usage: python3 render.py OUT_DIR [file stem ...]   (default: every chapter)

Blue: a quest with a real task. Grey: a checkmark-only quest. Pale: optional.
Gold outline: size 1.5 or more. Dashed squares: links from other chapters.
"""
import math
import sys
from pathlib import Path

from PIL import Image, ImageDraw

from gen import Book, load_chapters

S = 48      # pixels per grid unit
PAD = 2.0   # grid units of margin


def shape(d, x, y, r, kind, fill, outline, width):
    if kind == "hexagon":
        pts = [(x + r * math.cos(math.radians(a)), y + r * math.sin(math.radians(a))) for a in range(30, 390, 60)]
    elif kind == "diamond":
        pts = [(x, y - r), (x + r, y), (x, y + r), (x - r, y)]
    elif kind in ("square", "rsquare"):
        d.rectangle([x - r, y - r, x + r, y + r], fill=fill, outline=outline, width=width)
        return
    elif kind == "gear":
        pts = [(x + (r if i % 2 else r * 0.78) * math.cos(math.radians(i * 22.5)),
                y + (r if i % 2 else r * 0.78) * math.sin(math.radians(i * 22.5))) for i in range(16)]
    else:
        d.ellipse([x - r, y - r, x + r, y + r], fill=fill, outline=outline, width=width)
        return
    d.polygon(pts, fill=fill, outline=outline, width=width)


def render(ch, out):
    pos, deps = Book.layout(ch)
    links = [(l["quest"], l["pos"]) for l in ch.get("links", [])]
    xs = [p[0] for p in pos.values()] + [p[0] for _, p in links]
    ys = [p[1] for p in pos.values()] + [p[1] for _, p in links]
    x0, y0 = min(xs) - PAD, min(ys) - PAD
    w, h = int((max(xs) - x0 + PAD) * S), int((max(ys) - y0 + PAD) * S)
    img = Image.new("RGB", (w, h), (30, 30, 34))
    d = ImageDraw.Draw(img)

    def px(p):
        return ((p[0] - x0) * S, (p[1] - y0) * S)

    for gx in range(math.ceil(x0), math.floor(x0 + w / S) + 1):
        d.line([px((gx, y0)), px((gx, y0 + h / S))], fill=(40, 40, 46))
    for gy in range(math.ceil(y0), math.floor(y0 + h / S) + 1):
        d.line([px((x0, gy)), px((x0 + w / S, gy))], fill=(40, 40, 46))
    for k, ds in deps.items():
        for dk in ds:
            d.line([px(pos[dk]), px(pos[k])], fill=(120, 120, 130), width=2)
    quests = {q["key"]: q for q in ch["quests"]}
    for k, p in pos.items():
        q = quests.get(k, {})
        check = q.get("tasks") and all("check" in t for t in q["tasks"])
        fill = (110, 110, 110) if check else (60, 110, 190)
        if q.get("optional"):
            fill = tuple(int(c * 0.6 + 40) for c in fill)
        size = q.get("size", 1)
        outline = (230, 180, 60) if size >= 1.5 else (20, 20, 20)
        x, y = px(p)
        shape(d, x, y, S * 0.42 * size, q.get("shape", "circle"), fill, outline, 3 if size >= 1.5 else 1)
        d.text((x, y + S * 0.42 * size + 2), k, fill=(220, 220, 220), anchor="mt")
    for target, p in links:
        x, y = px(p)
        r = S * 0.42
        for i in range(8):
            a, b = i / 8, (i + 0.5) / 8
            for (ax, ay), (bx, by) in [((x - r + 2 * r * a, y - r), (x - r + 2 * r * b, y - r)),
                                       ((x - r + 2 * r * a, y + r), (x - r + 2 * r * b, y + r)),
                                       ((x - r, y - r + 2 * r * a), (x - r, y - r + 2 * r * b)),
                                       ((x + r, y - r + 2 * r * a), (x + r, y - r + 2 * r * b))]:
                d.line([(ax, ay), (bx, by)], fill=(200, 160, 220), width=2)
        d.text((x, y + r + 2), target, fill=(200, 160, 220), anchor="mt")
    d.text((8, 8), f"{ch['title']}  {len(pos)} quests  {max(xs) - min(xs):.1f} x {max(ys) - min(ys):.1f}",
           fill=(255, 255, 255))
    img.save(out / f"{ch['file']}.png")


def main():
    out = Path(sys.argv[1])
    out.mkdir(parents=True, exist_ok=True)
    for ch in load_chapters():
        if sys.argv[2:] and ch["file"] not in sys.argv[2:]:
            continue
        render(ch, out)
        print(out / f"{ch['file']}.png")


if __name__ == "__main__":
    main()
