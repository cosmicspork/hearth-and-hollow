"""Index every item, tag, entity, structure, biome and advancement in the pack.

usage: python3 build_index.py MODS_DIR VANILLA_JAR OUT_DIR

Writes tab-separated files that quest authors grep to check an id exists:
  items.tsv          id <tab> English name <tab> mod jar
  item_tags.txt      #ns:path, one per line (includes c: and neoforge-merged tags)
  entities.tsv       id <tab> English name
  entity_tags.txt
  structures.txt, structure_tags.txt, biomes.txt, biome_tags.txt, advancements.txt
"""
import json
import re
import sys
import zipfile
from pathlib import Path

mods, vanilla, out = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
out.mkdir(parents=True, exist_ok=True)

items, names, ents = {}, {}, {}
sets = {k: set() for k in ("item_tags", "entity_tags", "structures", "structure_tags",
                           "biomes", "biome_tags", "advancements", "dimensions")}

pats = {
    "model": re.compile(r"^assets/([a-z0-9_.-]+)/models/item/([a-z0-9_/.-]+)\.json$"),
    "lang": re.compile(r"^assets/([a-z0-9_.-]+)/lang/en_us\.json$"),
    "item_tags": re.compile(r"^data/([a-z0-9_.-]+)/tags/items?/([a-z0-9_/.-]+)\.json$"),
    "entity_tags": re.compile(r"^data/([a-z0-9_.-]+)/tags/entity_types?/([a-z0-9_/.-]+)\.json$"),
    "structures": re.compile(r"^data/([a-z0-9_.-]+)/worldgen/structure/([a-z0-9_/.-]+)\.json$"),
    "structure_tags": re.compile(r"^data/([a-z0-9_.-]+)/tags/worldgen/structure/([a-z0-9_/.-]+)\.json$"),
    "biomes": re.compile(r"^data/([a-z0-9_.-]+)/worldgen/biome/([a-z0-9_/.-]+)\.json$"),
    "biome_tags": re.compile(r"^data/([a-z0-9_.-]+)/tags/worldgen/biome/([a-z0-9_/.-]+)\.json$"),
    "dimensions": re.compile(r"^data/([a-z0-9_.-]+)/dimension/([a-z0-9_/.-]+)\.json$"),
    "advancements": re.compile(r"^data/([a-z0-9_.-]+)/advancements?/([a-z0-9_/.-]+)\.json$"),
}

jars = [vanilla] + sorted(mods.glob("*.jar"))
for jar in jars:
    try:
        z = zipfile.ZipFile(jar)
    except zipfile.BadZipFile:
        continue
    for n in z.namelist():
        m = pats["model"].match(n)
        if m:
            items.setdefault(f"{m[1]}:{m[2]}", jar.name)
            continue
        m = pats["lang"].match(n)
        if m:
            try:
                lang = json.loads(z.read(n).decode("utf-8", "replace"))
            except ValueError:
                continue
            for k, v in lang.items():
                p = k.split(".")
                if len(p) == 3 and p[0] in ("item", "block"):
                    names.setdefault(f"{p[1]}:{p[2]}", v)
                elif len(p) == 3 and p[0] == "entity":
                    ents.setdefault(f"{p[1]}:{p[2]}", v)
            continue
        for key, pat in pats.items():
            if key in ("model", "lang"):
                continue
            m = pat.match(n)
            if m:
                prefix = "#" if key.endswith("_tags") else ""
                sets[key].add(f"{prefix}{m[1]}:{m[2]}")
                break

# Mystical Customization registers the pack's own crops at startup from config, so no jar lists them.
for crop in sorted((Path(__file__).resolve().parents[2] / "config/mysticalcustomization/crops").glob("*.json")):
    name = json.loads(crop.read_text())["name"]
    for kind in ("seeds", "essence"):
        items.setdefault(f"mysticalagriculture:{crop.stem}_{kind}", crop.name)
        names.setdefault(f"mysticalagriculture:{crop.stem}_{kind}", f"{name} {kind.title()}")

with open(out / "items.tsv", "w") as f:
    for i in sorted(items):
        f.write(f"{i}\t{names.get(i, '')}\t{items[i]}\n")
with open(out / "entities.tsv", "w") as f:
    for e in sorted(ents):
        f.write(f"{e}\t{ents[e]}\n")
for key, s in sets.items():
    (out / f"{key}.txt").write_text("\n".join(sorted(s)) + "\n")
print(f"{len(items)} items, {len(ents)} entities, " + ", ".join(f"{len(s)} {k}" for k, s in sets.items()))
