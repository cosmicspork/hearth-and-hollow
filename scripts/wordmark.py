"""Draw the Hearth & Hollow wordmark as an SVG: Minecraft-style block letters with a pixel texture
per word, a bevel, a 3D extrusion and a black outline.

usage: wordmark.py OUT.svg [--layout stacked|line]
"""
import argparse, random

# 7 rows tall, vertical strokes two cells wide.
GLYPHS = {
    "H": ["XX..XX", "XX..XX", "XX..XX", "XXXXXX", "XX..XX", "XX..XX", "XX..XX"],
    "E": ["XXXXXX", "XXXXXX", "XX....", "XXXXX.", "XX....", "XXXXXX", "XXXXXX"],
    "A": [".XXXX.", "XXXXXX", "XX..XX", "XX..XX", "XXXXXX", "XX..XX", "XX..XX"],
    "R": ["XXXXX.", "XXXXXX", "XX..XX", "XXXXX.", "XX.XX.", "XX..XX", "XX..XX"],
    "T": ["XXXXXX", "XXXXXX", "..XX..", "..XX..", "..XX..", "..XX..", "..XX.."],
    "O": [".XXXX.", "XXXXXX", "XX..XX", "XX..XX", "XX..XX", "XXXXXX", ".XXXX."],
    "L": ["XX....", "XX....", "XX....", "XX....", "XX....", "XXXXXX", "XXXXXX"],
    "W": ["XX...XX", "XX...XX", "XX...XX", "XX.X.XX", "XXXXXXX", "XXX.XXX", "XX...XX"],
    "M": ["XX...XX", "XXX.XXX", "XXXXXXX", "XX.X.XX", "XX...XX", "XX...XX", "XX...XX"],
    "D": ["XXXXX.", "XXXXXX", "XX..XX", "XX..XX", "XX..XX", "XXXXXX", "XXXXX."],
    "P": ["XXXXX.", "XXXXXX", "XX..XX", "XXXXXX", "XXXXX.", "XX....", "XX...."],
    "C": [".XXXXX", "XXXXXX", "XX....", "XX....", "XX....", "XXXXXX", ".XXXXX"],
    "K": ["XX..XX", "XX.XX.", "XXXX..", "XXX...", "XXXX..", "XX.XX.", "XX..XX"],
    "&": [".XXX...", "XX.XX..", "XX.XX..", ".XXX.XX", "XX.XXX.", "XX..XX.", ".XXX.XX"],
    " ": ["...", "...", "...", "...", "...", "...", "..."],
}

# Each word gets a block texture: face palette, ore-like specks, and an extrusion color.
TEXTURES = {
    "ember": dict(face=["#b5523c", "#a8472f", "#c55c3a", "#d56b3b", "#9c3f2f"], speck=["#ffc861", "#f2a23b"], speck_p=0.025, side="#5c2219"),
    "gold": dict(face=["#ffd27a", "#f6c45c", "#ffe08a", "#eab04a"], speck=[], speck_p=0, side="#8a5a1c"),
    "deepslate": dict(face=["#625e72", "#58556a", "#6d6980", "#4f4c60"], speck=["#f2a23b", "#b88be8", "#6ad7d2"], speck_p=0.06, side="#25232f"),
    "planks": dict(face=["#c99a5c", "#bd8e52", "#d4a96a"], speck=[], speck_p=0, side="#5e4224", seam="#8f6a3c"),
}

TEX = 4         # texture pixels per glyph cell, per side
OUTLINE = 0.25  # outline width, in cells
DEPTH = 6       # extrusion length, in texture pixels


def text_cells(words, cell):
    """Glyph cells for one line, left-aligned at 0,0, and the line's width."""
    cells, x = [], 0
    for text, tex in words:
        for ch in text:
            g = GLYPHS[ch]
            filled = lambda r, c: 0 <= r < len(g) and 0 <= c < len(g[0]) and g[r][c] == "X"
            for r, row in enumerate(g):
                for c, v in enumerate(row):
                    if v == "X":
                        cells.append(dict(x=(x + c) * cell, y=r * cell, s=cell, tex=tex,
                                          up=filled(r - 1, c), down=filled(r + 1, c),
                                          left=filled(r, c - 1), right=filled(r, c + 1)))
            x += len(g[0]) + 1
    return cells, (x - 1) * cell


def shade(hex_color, f):
    r, g, b = (int(hex_color[i:i + 2], 16) for i in (1, 3, 5))
    m = lambda v: max(0, min(255, round(v * f if f < 1 else v + (255 - v) * (f - 1))))
    return f"#{m(r):02x}{m(g):02x}{m(b):02x}"


def draw(cells, rng, out):
    """Outline, extrusion, then faces, so a later group sits on top of an earlier one."""
    for c in cells:
        u, o = c["s"] / TEX, OUTLINE * c["s"]
        for k in range(DEPTH + 1):
            out.append(f'<rect x="{c["x"] + round(k * 0.35) * u - o:.1f}" y="{c["y"] + k * u - o:.1f}" width="{c["s"] + 2 * o:.1f}" height="{c["s"] + 2 * o:.1f}" fill="#120d14"/>')
    for k in range(DEPTH, 0, -1):
        for c in cells:
            u = c["s"] / TEX
            side = TEXTURES[c["tex"]]["side"]
            fill = shade(side, 0.7) if k > DEPTH // 2 else side
            out.append(f'<rect x="{c["x"] + round(k * 0.35) * u:.1f}" y="{c["y"] + k * u:.1f}" width="{c["s"]:.1f}" height="{c["s"]:.1f}" fill="{fill}"/>')
    for c in cells:
        t, u = TEXTURES[c["tex"]], c["s"] / TEX
        speck = bool(t["speck"]) and rng.random() < t["speck_p"] * TEX
        sr, sc = rng.randrange(TEX - 1), rng.randrange(TEX - 1)
        scol = rng.choice(t["speck"]) if t["speck"] else None
        for r in range(TEX):
            for q in range(TEX):
                col = rng.choice(t["face"])
                if "seam" in t and r == TEX - 1:
                    col = t["seam"]
                if speck and r in (sr, sr + 1) and q in (sc, sc + 1) and rng.random() < 0.8:
                    col = scol
                # Bevel: light on exposed top and left edges, dark on bottom and right.
                if (r == 0 and not c["up"]) or (q == 0 and not c["left"]):
                    col = shade(col, 1.3)
                elif (r == TEX - 1 and not c["down"]) or (q == TEX - 1 and not c["right"]):
                    col = shade(col, 0.75)
                out.append(f'<rect x="{c["x"] + q * u:.1f}" y="{c["y"] + r * u:.1f}" width="{u + 0.3:.1f}" height="{u + 0.3:.1f}" fill="{col}"/>')


def place(cells, dx, dy):
    for c in cells:
        c["x"] += dx
        c["y"] += dy
    return cells


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("--layout", choices=["stacked", "line"], default="stacked")
    args = ap.parse_args()
    rng = random.Random(11)
    big, small = 32, 20
    groups = []
    if args.layout == "stacked":
        # HEARTH over HOLLOW, a gold & across the seam between them, MODPACK below.
        hearth, wh = text_cells([("HEARTH", "ember")], big)
        hollow, wo = text_cells([("HOLLOW", "deepslate")], big)
        width = max(wh, wo)
        gap = big * 3
        place(hearth, (width - wh) / 2, 0)
        place(hollow, (width - wo) / 2, big * 7 + gap)
        amp, wa = text_cells([("&", "gold")], small * 1.2)
        place(amp, (width - wa) / 2, big * 7 + gap / 2 - small * 1.2 * 3.5)
        modpack, wm = text_cells([("MODPACK", "planks")], small)
        place(modpack, (width - wm) / 2, big * 14 + gap + big * 2.2)
        groups = [hearth, hollow, modpack, amp]
    else:
        line, width = text_cells([("HEARTH", "ember"), (" ", "ember"), ("&", "gold"), (" ", "ember"), ("HOLLOW", "deepslate")], big)
        modpack, wm = text_cells([("MODPACK", "planks")], small * 1.4)
        place(modpack, (width - wm) / 2, big * 7 + big * 1.9)
        groups = [line, modpack]
    pad = big * 1.2
    cells = [c for g in groups for c in g]
    for c in cells:
        c["x"] += pad
        c["y"] += pad
    W = width + 2 * pad + big
    H = max(c["y"] + c["s"] for c in cells) + pad + big
    out = []
    for g in groups:
        draw(g, rng, out)
    with open(args.out, "w") as f:
        f.write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.0f} {H:.0f}" width="{W:.0f}" height="{H:.0f}" shape-rendering="crispEdges">\n'
                '<title>Hearth &amp; Hollow Modpack</title>\n' + "\n".join(out) + "\n</svg>\n")


if __name__ == "__main__":
    main()
