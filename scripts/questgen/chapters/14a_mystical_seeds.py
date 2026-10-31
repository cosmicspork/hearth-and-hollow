# Every resource and mob seed the pack can make, by the tier of essence its recipe takes. Each is
# (crop, what goes on the pedestals). Left out on purpose: ruby, sapphire, peridot and iridium,
# whose ores don't generate here, and the blizz, blitz and basalz seeds, whose mobs aren't in the pack.
SEED_TIERS = [
    ("inferium", "Inferium", "kindling", [
        ("air", "Air Agglomeratio"), ("earth", "Earth Agglomeratio"), ("water", "Water Agglomeratio"),
        ("fire", "Fire Agglomeratio"), ("stone", "Stone"), ("dirt", "Dirt"), ("wood", "Logs, any kind"),
        ("ice", "Ice"), ("deepslate", "Deepslate"),
    ]),
    ("prudentium", "Prudentium", "kindling", [
        ("nature", "Nature Agglomeratio"), ("dye", "Dye Agglomeratio"), ("nether", "Nether Agglomeratio"),
        ("coal", "Coal"), ("coral", "Coral Agglomeratio"), ("honey", "Honey Agglomeratio"),
        ("amethyst", "Amethyst Shards"), ("silicon", "Silicon"), ("sulfur", "Sulfur"),
        ("aluminum", "Aluminum Ingots"), ("mystical_flower", "Mystical Flower Agglomeratio"),
        ("pig", "pig"), ("chicken", "chicken"), ("cow", "cow"), ("sheep", "sheep"), ("squid", "squid"),
        ("fish", "fish"), ("slime", "slime"), ("turtle", "turtle"), ("armadillo", "armadillo"),
    ]),
    ("tertium", "Tertium", "hearth", [
        ("iron", "Iron Ingots"), ("copper", "Copper Ingots"), ("nether_quartz", "Nether Quartz"),
        ("glowstone", "Glowstone Dust"), ("redstone", "Redstone"), ("obsidian", "Obsidian"),
        ("prismarine", "Prismarine Agglomeratio"), ("sculk", "Sculk"), ("tin", "Tin Ingots"),
        ("bronze", "Bronze Ingots"), ("zinc", "Zinc Ingots"), ("brass", "Brass Ingots"),
        ("silver", "Silver Ingots"), ("lead", "Lead Ingots"), ("quartz_enriched_iron", "Quartz Enriched Iron"),
        ("zombie", "zombie"), ("skeleton", "skeleton"), ("creeper", "creeper"), ("spider", "spider"),
        ("phantom", "phantom"), ("rabbit", "rabbit"),
    ]),
    ("imperium", "Imperium", "hearth", [
        ("gold", "Gold Ingots"), ("lapis_lazuli", "Lapis Lazuli"), ("end", "End Agglomeratio"),
        ("experience", "Experience Capsules"), ("steel", "Steel Ingots"), ("nickel", "Nickel Ingots"),
        ("constantan", "Constantan Ingots"), ("electrum", "Electrum Ingots"), ("invar", "Invar Ingots"),
        ("uranium", "Uranium Ingots"), ("soulium", "Soulium Dust"), ("signalum", "Signalum Ingots"),
        ("lumium", "Lumium Ingots"), ("osmium", "Osmium Ingots"), ("fluorite", "Fluorite"),
        ("refined_glowstone", "Refined Glowstone Ingots"), ("refined_obsidian", "Refined Obsidian Ingots"),
        ("energized_steel", "Energized Steel"), ("blazing_crystal", "Blazing Crystals"),
        ("breeze", "breeze"), ("blaze", "blaze"), ("ghast", "ghast"), ("enderman", "enderman"),
    ]),
    ("supremium", "Supremium", "hearth", [
        ("diamond", "Diamonds"), ("emerald", "Emeralds"), ("netherite", "Netherite Ingots"),
        ("platinum", "Platinum Ingots"), ("enderium", "Enderium Ingots"), ("niotic_crystal", "Niotic Crystals"),
        ("spirited_crystal", "Spirited Crystals"), ("uraninite", "Uraninite"),
        ("wither_skeleton", "wither skeleton"),
    ]),
    ("insanium", "Insanium", "hearth", [
        ("nether_star", "Nether Stars"), ("dragon_egg", "Dragon Scales"), ("nitro_crystal", "Nitro Crystals"),
    ]),
]
MOBS = {"pig", "chicken", "cow", "sheep", "squid", "fish", "slime", "turtle", "armadillo", "zombie", "skeleton",
        "creeper", "spider", "phantom", "rabbit", "breeze", "blaze", "ghast", "enderman", "wither_skeleton"}
ELEMENTS = {"air", "earth", "water", "fire"}
# The top-tier seeds only grow with their crux block under the farmland.
CRUXES = {"nether_star": "Nether Star Crux", "dragon_egg": "Dragon Egg Crux", "nitro_crystal": "Nitro Crystal Crux"}


def _title(crop):
    return " ".join(w.capitalize() for w in crop.split("_"))


def seed_quest(crop, material, essence, crate):
    name = _title(crop)
    if crop in MOBS:
        recipe = (f"Made on the Infusion Altar: a Soulium Seed Base in the middle, with four Soul Jars full of "
                  f"{material} souls and four {essence} Essence on the pedestals.")
    else:
        recipe = (f"Made on the Infusion Altar: a Prosperity Seed Base in the middle, with four {material} and "
                  f"four {essence} Essence on the pedestals.")
    if crop in ELEMENTS:
        grows = f"Grows &e{name} Essence&r, one of the four elemental essences the Awakening Altar needs."
    else:
        grows = f"Grows &e{name} Essence&r, which crafts back into the real thing."
    desc = [grows, "", recipe]
    if crop in CRUXES:
        desc += ["", f"It only grows with a &e{CRUXES[crop]}&r under its farmland."]
    return {
        "key": f"seed_{crop}", "title": f"{name} Seeds", "optional": True,
        "desc": desc,
        "tasks": [{"item": f"mysticalagriculture:{crop}_seeds"}],
        "rewards": [{"xp": 10}, {"crate": crate}],
    }


SEED_QUESTS = [seed_quest(c, m, e, crate) for _, e, crate, seeds in SEED_TIERS for c, m in seeds]


def _per_row(n):
    rows = -(-n // 12)
    return -(-n // rows)


_TIER_ROWS = [[f"seed_{c}" for c, _ in seeds] + (["metal_seeds"] if tier == "insanium" else [])
              for tier, _, _, seeds in SEED_TIERS]

CHAPTER = {
    "file": "mystical_seeds",
    "group": "hum",
    "title": "A Seed for Everything",
    "subtitle": "Every resource and mob seed, a row for each tier of essence",
    "icon": "mysticalagriculture:iron_seeds",
    "theme": "grower",
    "layout": {"lines": [{"rows": keys, "per_row": _per_row(len(keys))} for keys in _TIER_ROWS]},
    "quests": SEED_QUESTS + [
        {
            "key": "metal_seeds", "title": "Metal in the Soil", "optional": True,
            "desc": [
                "Insanium Essence opens up seeds for the three endgame metals: &eAllthemodium&r, &eVibranium&r and &eUnobtainium Seeds&r, made on the Infusion Altar from their ingots.",
                "",
                "Each one is picky about its soil: it only grows with a block of the same metal under its farmland.",
                "",
                "Eight essence in a ring make one ingot. Slow, but it never runs out.",
            ],
            "tasks": [{"any": ["mysticalagriculture:allthemodium_seeds", "mysticalagriculture:vibranium_seeds",
                               "mysticalagriculture:unobtainium_seeds"],
                       "title": "Any Allthemodium metal seed", "icon": "mysticalagriculture:allthemodium_seeds"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
    ],
}
