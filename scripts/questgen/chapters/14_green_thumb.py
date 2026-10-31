_COLORS = ["white", "orange", "magenta", "light_blue", "yellow", "lime", "pink", "gray", "light_gray", "cyan",
           "purple", "blue", "brown", "green", "red", "black"]
_HOPPER_POTS = (["botanypots:terracotta_hopper_botany_pot"]
                + [f"botanypots:{c}_{m}_hopper_botany_pot" for c in _COLORS
                   for m in ("terracotta", "glazed_terracotta", "concrete")]
                + [f"botanypots:{b}_hopper_botany_pot" for b in
                   ("bricks", "stone_bricks", "mossy_stone_bricks", "deepslate_bricks", "tuff_bricks", "mud_bricks",
                    "prismarine_bricks", "nether_bricks", "red_nether_bricks", "polished_blackstone_bricks",
                    "end_stone_bricks", "quartz_bricks")])

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

GEAR = ["sword", "pickaxe", "axe", "shovel", "hoe", "sickle", "scythe", "bow", "crossbow", "shears", "fishing_rod",
        "helmet", "chestplate", "leggings", "boots"]


def gear(tier):
    return [f"mysticalagriculture:{tier}_{g}" for g in GEAR]


AUGMENTS = [f"mysticalagriculture:{a}_augment" for a in (
    "absorption_i", "absorption_ii", "absorption_iii", "absorption_iv", "absorption_v", "attack_aoe_i",
    "attack_aoe_ii", "attack_aoe_iii", "blindness_resistance", "fire_resistance", "flight", "haste_i", "haste_ii",
    "haste_iii", "health_boost_i", "health_boost_ii", "health_boost_iii", "health_boost_iv", "health_boost_v",
    "hunger_resistance", "jump_boost_i", "jump_boost_ii", "jump_boost_iii", "luck_i", "luck_ii", "luck_iii",
    "mining_aoe_i", "mining_aoe_ii", "mining_aoe_iii", "mining_aoe_iv", "mining_fatigue_resistance",
    "nausea_resistance", "night_vision", "no_fall_damage", "pathing_aoe_i", "pathing_aoe_ii", "pathing_aoe_iii",
    "pathing_aoe_iv", "poison_resistance", "slow_falling", "slowness_resistance", "speed_i", "speed_ii",
    "speed_iii", "step_assist", "strength_i", "strength_ii", "strength_iii", "tilling_aoe_i", "tilling_aoe_ii",
    "tilling_aoe_iii", "tilling_aoe_iv", "water_breathing", "weakness_resistance", "wither_resistance")]
ESSENCE_TIERS = ["inferium", "prudentium", "tertium", "imperium", "supremium"]
SAW_UPGRADES = [f"mob_grinding_utils:saw_upgrade_{u}" for u in
                ("sharpness", "looting", "fire", "smite", "arthropod", "beheading")]


def model(mob):
    return {"hostilenetworks:data_model": f"hostilenetworks:{mob}"}


# Lines stacked top to bottom, with the seeds as rows of their own: they need no order, so they
# have no lines. Placed by hand because the chapter mixes both.
_pos, _deps, _y = {}, {}, [0.0]


def _line(spine, branches=None):
    branches = branches or {}
    up = max([len(a.get("up", [])) for a in branches.values()] + [0])
    down = max([len(a.get("down", [])) for a in branches.values()] + [0])
    y0 = _y[0] + up * 1.5
    for i, k in enumerate(spine):
        _pos[k] = (i * 2.0, y0)
        if i:
            _deps[k] = [spine[i - 1]]
    for root, arms in branches.items():
        x = _pos[root][0]
        for direction, sign in (("up", -1), ("down", 1)):
            prev = root
            for j, k in enumerate(arms.get(direction, []), 1):
                _pos[k] = (x, y0 + sign * j * 1.5)
                _deps[k] = [prev]
                prev = k
    _y[0] = y0 + down * 1.5 + 2.5


def _rows(keys, per_row=12):
    for i, k in enumerate(keys):
        if i and i % per_row == 0:
            _y[0] += 1.75
        _pos[k] = ((i % per_row) * 1.75, _y[0])
    _y[0] += 1.75 + 0.75


_line(["start", "seeds", "altar", "crystal", "prudentium", "tertium", "imperium", "supremium", "finale"], {
    "start": {"up": ["prosperity"]},
    "seeds": {"up": ["farmland"], "down": ["watering"]},
    "altar": {"down": ["resource_seed", "soul_dagger"]},
    "prudentium": {"down": ["accelerator"]},
    "supremium": {"down": ["master_crystal"]},
})
for _, _, _, seeds in SEED_TIERS:
    _rows([f"seed_{c}" for c, _ in seeds] + (["metal_seeds"] if seeds is SEED_TIERS[-1][3] else []))
_y[0] += 1.75
_line(["gear_inferium", "gear_prudentium", "gear_tertium", "gear_imperium", "gear_supremium", "awakening",
       "awakened", "awakened_gear"], {
    "gear_inferium": {"up": ["sickle"]},
    "gear_tertium": {"up": ["tinkering", "augment"]},
    "gear_supremium": {"down": ["cognizant"]},
})
_line(["frame", "furnace", "reprocessor", "soul_extractor", "harvester", "enchanter"], {
    "furnace": {"up": ["machine_upgrade"]},
    "harvester": {"up": ["fertilizer"]},
})
_line(["paxel", "apple", "withering_soul", "star_crux", "dragon_scale", "egg_crux"], {
    "withering_soul": {"up": ["witherproof"]},
})
_line(["pot", "hopper_pot", "trees"])
_line(["pylon", "infusion_pylon", "interdiction_pylon", "expulsion_pylon", "protection_pylon"])
_line(["masher", "absorption", "xp_tank", "solidifier", "spawner"], {
    "masher": {"up": ["masher_upgrade"], "down": ["dreadful"]},
    "absorption": {"up": ["fan"]},
    "xp_tank": {"up": ["xp_tap"]},
})
_line(["learner", "sim", "fabricator", "data_center"])
_rows(["model_blaze", "model_enderman", "model_ghast", "model_shulker", "model_diamond_ore"])

CHAPTER = {
    "file": "green_thumb",
    "group": "hum",
    "title": "Green Thumb",
    "subtitle": "Grow your resources, then let the farm run itself",
    "icon": "mysticalagriculture:inferium_seeds",
    "layout": {"free": _pos, "deps": _deps},
    "quests": [
        {
            "key": "start", "title": "Green Thumb",
            "shape": "hexagon", "size": 1.5, "icon": "mysticalagriculture:inferium_essence",
            "desc": [
                "Why mine iron when you can grow it? Mystical Agriculture has seeds that grow real resources, and the rest of this chapter gets the farm running by itself.",
                "",
                "It all starts with &eInferium Essence&r. Grass and mobs don't drop it in this pack, so dig for it: &eInferium Ore&r is common underground in the Overworld, from about Y 64 down to Y -32, and each one drops two to four essence. Fortune helps.",
                "",
                "The Nether and the End have Inferium Ore of their own, too.",
            ],
            "tasks": [{"item": "mysticalagriculture:inferium_essence", "count": 16}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}],
        },
        {
            "key": "prosperity", "title": "Prosperity Shards",
            "desc": [
                "&eProsperity Ore&r sits a little deeper than Inferium, from about Y 24 down to Y -60, and drops &eProsperity Shards&r.",
                "",
                "Shards go into Infusion Crystals and into the seed base that every resource seed is built on, so keep a healthy pile.",
            ],
            "tasks": [{"item": "mysticalagriculture:prosperity_shard", "count": 8}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}],
        },
        {
            "key": "seeds", "title": "Plant an Inferium Seed",
            "desc": [
                "Eight Inferium Essence around a Wheat Seed make &eInferium Seeds&r, which grow more Inferium Essence. Once a few are in the ground, you'll never need to dig for it again.",
                "",
                "They grow on any farmland, but do best on Essence Farmland, just above.",
            ],
            "tasks": [{"item": "mysticalagriculture:inferium_seeds"}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}],
        },
        {
            "key": "farmland", "title": "Essence Farmland",
            "desc": [
                "Right-click Farmland with an essence to turn it into &eEssence Farmland&r of that tier, or craft it from Farmland and the essence.",
                "",
                "Inferium Seeds yield more essence on higher tier farmland. In a Botany Pot, Mystical crops need farmland of their own tier or better to grow at all.",
            ],
            "tasks": [{"item": "mysticalagriculture:inferium_farmland", "count": 4}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}],
        },
        {
            "key": "watering", "title": "Watering Can", "optional": True,
            "desc": [
                "Right-click your crops with a &eWatering Can&r and they grow faster.",
                "",
                "Upgraded with essence, a can reaches further and grows things quicker. &eShift+right-click&r into the air with an upgraded can to have it water on its own.",
            ],
            "tasks": [{"item": "mysticalagriculture:watering_can"}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}],
        },
        {
            "key": "altar", "title": "The Infusion Altar",
            "desc": [
                "Resource seeds are made on an &eInfusion Altar&r with eight &eInfusion Pedestals&r around it. Place the altar first and it shows you where the pedestals go.",
                "",
                "Put the seed base on the altar and the ingredients on the pedestals, then right-click the altar with a &eWand&r, or give it a redstone signal.",
            ],
            "tasks": [{"item": "mysticalagriculture:infusion_altar"},
                      {"item": "mysticalagriculture:infusion_pedestal", "count": 8}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}],
        },
        {
            "key": "resource_seed", "title": "Your First Resource Seed",
            "desc": [
                "A resource seed grows the real thing: stone, coal, iron, diamond and many more. Each one is a seed base on the altar, with four of the material and four essences on the pedestals.",
                "",
                "Better materials need better essence. Look any seed up in JEI with &eR&r to see what it takes, and start with whatever you use the most of.",
            ],
            "tasks": [{"any": ["mysticalagriculture:stone_seeds", "mysticalagriculture:dirt_seeds",
                               "mysticalagriculture:wood_seeds", "mysticalagriculture:water_seeds",
                               "mysticalagriculture:air_seeds", "mysticalagriculture:earth_seeds",
                               "mysticalagriculture:fire_seeds", "mysticalagriculture:ice_seeds",
                               "mysticalagriculture:nature_seeds", "mysticalagriculture:coal_seeds",
                               "mysticalagriculture:copper_seeds", "mysticalagriculture:nether_seeds",
                               "mysticalagriculture:iron_seeds", "mysticalagriculture:zombie_seeds",
                               "mysticalagriculture:gold_seeds", "mysticalagriculture:diamond_seeds"],
                       "title": "Any resource seed", "icon": "mysticalagriculture:iron_seeds"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "soul_dagger", "title": "Mob Seeds",
            "desc": [
                "Seeds for mob drops, like zombie or skeleton seeds, need a &eSoul Jar&r full of that mob's souls.",
                "",
                "Carry an empty Soul Jar and kill the mob with a &eSoulium Dagger&r to fill it. Soulium Ore hides in Soulstone veins in the Nether.",
                "",
                "A Soul Extractor can fill jars from spare mob drops too, though more slowly.",
            ],
            "tasks": [{"item": "mysticalagriculture:soulium_dagger"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "crystal", "title": "Infusion Crystal",
            "desc": [
                "A diamond, four Prosperity Shards and four Inferium Essence make an &eInfusion Crystal&r.",
                "",
                "Four essences of one tier around the crystal make one essence of the next tier up. The crystal comes back each time with one use fewer, and it's good for a thousand.",
            ],
            "tasks": [{"item": "mysticalagriculture:infusion_crystal"}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}],
        },
        {
            "key": "prudentium", "title": "Prudentium", "shape": "hexagon",
            "desc": [
                "Four Inferium around your crystal make &ePrudentium Essence&r, the second of five tiers.",
                "",
                "Each tier opens up more resource seeds, better farmland and faster growth accelerators. Every step up costs four of the step below, so a big inferium field pays off.",
            ],
            "tasks": [{"item": "mysticalagriculture:prudentium_essence", "count": 4}],
            "rewards": [{"xp": 25}, {"crate": "lantern"}, {"item": "mysticalagriculture:prosperity_seed_base", "count": 2}],
        },
        {
            "key": "accelerator", "title": "Growth Accelerator",
            "desc": [
                "A &eGrowth Accelerator&r goes under your farmland and speeds up the crop above it.",
                "",
                "Stack several, of any tier, as long as the crop is within their range. The tooltip shows each one's range.",
            ],
            "tasks": [{"any": ["mysticalagriculture:inferium_growth_accelerator",
                               "mysticalagriculture:prudentium_growth_accelerator",
                               "mysticalagriculture:tertium_growth_accelerator",
                               "mysticalagriculture:imperium_growth_accelerator",
                               "mysticalagriculture:supremium_growth_accelerator",
                               "mysticalagriculture:awakened_supremium_growth_accelerator"],
                       "title": "Any Growth Accelerator", "icon": "mysticalagriculture:inferium_growth_accelerator"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "tertium", "title": "Tertium", "shape": "hexagon",
            "desc": [
                "Four Prudentium make &eTertium Essence&r, tier three. Every tier opens up seeds for more valuable materials.",
                "",
                "A field of resource crops occasionally drops &eFertilized Essence&r, which works like bone meal on Mystical crops. Save it for the slow ones.",
            ],
            "tasks": [{"item": "mysticalagriculture:tertium_essence", "count": 4}],
            "rewards": [{"xp": 25}, {"crate": "lantern"}, {"item": "mysticalagriculture:prudentium_essence", "count": 16}],
        },
        {
            "key": "imperium", "title": "Imperium", "shape": "hexagon",
            "desc": [
                "Four Tertium make &eImperium Essence&r, tier four.",
                "",
                "Your farm is getting big. A Harvester Pylon or a wall of Hopper Botany Pots will save your wrists.",
            ],
            "tasks": [{"item": "mysticalagriculture:imperium_essence", "count": 4}],
            "rewards": [{"xp": 25}, {"crate": "lantern"}, {"item": "mysticalagriculture:tertium_essence", "count": 16}],
        },
        {
            "key": "supremium", "title": "Supremium", "shape": "hexagon",
            "desc": [
                "Four Imperium make &eSupremium Essence&r, the top tier in Mystical Agriculture itself. The seeds for the most precious materials need it.",
                "",
                "One more step remains, from Mystical Agradditions. That's the end of this line.",
            ],
            "tasks": [{"item": "mysticalagriculture:supremium_essence", "count": 4}],
            "rewards": [{"xp": 25}, {"crate": "lantern"}, {"item": "mysticalagriculture:imperium_essence", "count": 8}],
        },
        {
            "key": "master_crystal", "title": "Master Infusion Crystal",
            "desc": [
                "The &eMaster Infusion Crystal&r never wears out. It's made from a Supremium Gemstone, Supremium Essence and Prosperity Shards.",
                "",
                "Once you have one, your old crystals can retire.",
            ],
            "tasks": [{"item": "mysticalagriculture:master_infusion_crystal"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "finale", "title": "Insanium",
            "shape": "hexagon", "size": 1.5, "icon": "mysticalagradditions:insanium_essence",
            "desc": [
                "Four Supremium around an Infusion Crystal make &eInsanium Essence&r, the very top of the ladder. The last row of seeds needs it.",
                "",
                "For the &eWither Prediction&r, right-click the Wither with a Model Framework (carefully), then train the model past Faulty with several Wither fights. Simulating it costs 2,560 FE a tick, so have power to spare.",
                "",
                "Both are pieces of the &eAllthemodium Alloy Paxel&r, the pack's capstone. The paxel quest gives them back once you've crafted the paxel.",
            ],
            "tasks": [
                {"item": "mysticalagradditions:insanium_essence"},
                {"item": "hostilenetworks:prediction", "components": {"hostilenetworks:data_model": "hostilenetworks:wither"}},
            ],
            "rewards": [{"xp": 50}, {"crate": "ember"}, {"item": "mysticalagradditions:insanium_farmland", "count": 4}],
        },
    ] + SEED_QUESTS + [
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
        {
            "key": "gear_inferium", "shape": "hexagon", "title": "Essence Gear", "icon": "mysticalagriculture:inferium_pickaxe",
            "desc": [
                "Essence tools and armor start from diamond. A diamond tool or armor piece between two &eInferium Ingots&r and two &eInferium Gemstones&r comes out as Inferium gear, enchantments and all.",
                "",
                "An ingot is a Prosperity Ingot and two essence, a gemstone a Prosperity Gemstone and two essence. There's a set of tools, weapons and armor for every tier.",
            ],
            "tasks": [{"any": gear("inferium"), "title": "Any Inferium tool or armor", "icon": "mysticalagriculture:inferium_pickaxe"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "sickle", "title": "Sickles and Scythes", "optional": True,
            "desc": [
                "Two farming tools Mystical Agriculture adds: a &eSickle&r cuts through leaves and plants around you, and a &eScythe&r through a whole patch of crops at once.",
                "",
                "They start at diamond, like the rest, and essence versions reach further.",
            ],
            "tasks": [{"any": ["mysticalagriculture:diamond_sickle", "mysticalagriculture:diamond_scythe"],
                       "title": "A Diamond Sickle or Scythe", "icon": "mysticalagriculture:diamond_sickle"}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}],
        },
    ] + [
        {
            "key": f"gear_{t}", "title": f"{t.capitalize()} Gear", "icon": f"mysticalagriculture:{t}_pickaxe",
            "desc": [
                f"Each tier is built on the one below: an {p.capitalize()} piece between two &e{t.capitalize()} Ingots&r and two &e{t.capitalize()} Gemstones&r.",
                "",
                "Damage and enchantments carry over, so nothing you put into the old piece is lost.",
            ],
            "tasks": [{"any": gear(t), "title": f"Any {t.capitalize()} tool or armor", "icon": f"mysticalagriculture:{t}_pickaxe"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        }
        for p, t in zip(ESSENCE_TIERS, ESSENCE_TIERS[1:])
    ] + [
        {
            "key": "tinkering", "title": "The Tinkering Table",
            "desc": [
                "Essence gear takes &eAugments&r: small upgrades like Speed, Night Vision or a bigger mining area.",
                "",
                "They go in at a &eTinkering Table&r, made from stone and Soulium Dust. Put the gear in, then slot the augments around it.",
            ],
            "tasks": [{"item": "mysticalagriculture:tinkering_table"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "augment", "title": "Augmented",
            "desc": [
                "Augments are made on the Infusion Altar, from an &eUnattuned Augment&r with ingredients and essence around it. Speed I, for example, takes sugar and Prudentium Essence.",
                "",
                "There are dozens: health, strength, step assist, no fall damage, even flight. Look up the Unattuned Augment with &eU&r to see them all.",
            ],
            "tasks": [{"any": AUGMENTS, "title": "Any augment", "icon": "mysticalagriculture:unattuned_augment"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "cognizant", "title": "Cognizant Dust", "icon": "mysticalagriculture:cognizant_dust",
            "desc": [
                "The next step needs &eCognizant Dust&r, and only two monsters have it: the Wither and the Ender Dragon.",
                "",
                "They drop it when killed with an essence weapon carrying &eMystical Enlightenment&r. The Enchanter, just below, can put that enchantment on a sword.",
            ],
            "tasks": [{"item": "mysticalagriculture:cognizant_dust", "count": 4}],
            "rewards": [{"xp": 10}, {"crate": "lantern"}],
        },
        {
            "key": "awakening", "title": "The Awakening Altar",
            "desc": [
                "Supremium can be pushed one step further on an &eAwakening Altar&r. It needs four &eAwakening Pedestals&r for the ingredients and four &eEssence Vessels&r for the essence.",
                "",
                "The vessels hold &eAir&r, &eEarth&r, &eWater&r and &eFire Essence&r, so plant the elemental seeds well ahead of time.",
            ],
            "tasks": [{"item": "mysticalagriculture:awakening_altar"},
                      {"item": "mysticalagriculture:awakening_pedestal", "count": 4},
                      {"item": "mysticalagriculture:essence_vessel", "count": 4}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "awakened", "title": "Awakened Supremium", "icon": "mysticalagriculture:awakened_supremium_essence",
            "desc": [
                "A Supremium Block on the altar, four Cognizant Dust on the pedestals and ten of each elemental essence in the vessels make an &eAwakened Supremium Block&r.",
                "",
                "Break it down for nine &eAwakened Supremium Essence&r. Its ingots and gemstones work like any other tier's.",
            ],
            "tasks": [{"item": "mysticalagriculture:awakened_supremium_essence"}],
            "rewards": [{"xp": 25}, {"crate": "lantern"}],
        },
        {
            "key": "awakened_gear", "title": "Wide Awake", "shape": "hexagon", "icon": "mysticalagriculture:awakened_supremium_pickaxe",
            "desc": [
                "Awakened gear is made on the Awakening Altar too: a Supremium piece, Awakened Supremium ingots and gemstones, and forty of each elemental essence.",
                "",
                "A full set of the armor makes crops grow faster around you as you walk.",
            ],
            "tasks": [{"any": [f"mysticalagriculture:awakened_supremium_{g}" for g in GEAR],
                       "title": "Any Awakened Supremium tool or armor", "icon": "mysticalagriculture:awakened_supremium_pickaxe"}],
            "rewards": [{"xp": 25}, {"crate": "lantern"}],
        },
        {
            "key": "frame", "shape": "hexagon", "title": "Machine Frame", "icon": "mysticalagriculture:machine_frame",
            "desc": [
                "Mystical Agriculture's machines are all built around a &eMachine Frame&r: iron, redstone and stone.",
                "",
                "Make a few. Every machine on this line takes one.",
            ],
            "tasks": [{"item": "mysticalagriculture:machine_frame"}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}],
        },
        {
            "key": "furnace", "title": "An Essence Furnace", "icon": "mysticalagriculture:furnace",
            "desc": [
                "The mod's own &eFurnace&r is two furnaces, iron and Prosperity Ingots around a Machine Frame. It cooks like a furnace, and upgrades make it faster.",
            ],
            "tasks": [{"item": "mysticalagriculture:furnace"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "machine_upgrade", "title": "Machine Upgrades", "optional": True, "icon": "mysticalagriculture:inferium_upgrade",
            "desc": [
                "A &eMachine Upgrade&r goes into any of these machines. Each tier changes its speed, fuel use and fuel capacity, and on the Harvester its area. The tooltip shows by how much.",
                "",
                "Each starts as a Machine Upgrade Base, with essence and ingots of its tier around it.",
            ],
            "tasks": [{"any": [f"mysticalagriculture:{t}_upgrade" for t in ESSENCE_TIERS + ["awakened_supremium"]],
                       "title": "Any Machine Upgrade", "icon": "mysticalagriculture:inferium_upgrade"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "reprocessor", "title": "Seed Reprocessor",
            "desc": [
                "Spare seeds are worth something. The &eSeed Reprocessor&r turns each one into two of its essence.",
            ],
            "tasks": [{"item": "mysticalagriculture:seed_reprocessor"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "soul_extractor", "title": "Soul Extractor",
            "desc": [
                "Mob seeds need Soul Jars full of souls. The &eSoul Extractor&r fills them from mob drops, so a pile of rotten flesh becomes zombie souls.",
                "",
                "Slower than a Soulium Dagger, but you don't have to fight anything.",
            ],
            "tasks": [{"item": "mysticalagriculture:soul_extractor"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "harvester", "title": "The Harvester",
            "desc": [
                "The &eHarvester&r is two Diamond Scythes and Soulium Ingots on a Machine Frame. It harvests ripe crops in an area around it, burning fuel as it goes.",
                "",
                "Upgrades widen the area. Hover over it to see how far it reaches.",
            ],
            "tasks": [{"item": "mysticalagriculture:harvester"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "fertilizer", "title": "Mystical Fertilizer", "optional": True,
            "desc": [
                "Bone meal, Inferium Essence and a diamond make four &eMystical Fertilizer&r. It grows a crop or sapling fully in one go.",
                "",
                "Save it for the slow ones at the top of the ladder.",
            ],
            "tasks": [{"item": "mysticalagriculture:mystical_fertilizer"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "enchanter", "title": "The Enchanter",
            "desc": [
                "No more rolling the dice. The &eEnchanter&r gives you the enchantment you pick, for a set price in materials and &eExperience Essence&r.",
                "",
                "Efficiency, for example, takes redstone and a stack of Experience Essence. Experience Seeds are the ones to plant for it.",
            ],
            "tasks": [{"item": "mysticalagriculture:enchanter"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "paxel", "shape": "hexagon", "title": "One Tool for Everything", "icon": "mysticalagradditions:inferium_paxel",
            "desc": [
                "Mystical Agradditions adds an essence &ePaxel&r for every tier: the axe, pickaxe and shovel of one tier, on two sticks.",
            ],
            "tasks": [{"any": [f"mysticalagradditions:{t}_paxel" for t in ESSENCE_TIERS + ["awakened_supremium"]],
                       "title": "Any essence paxel", "icon": "mysticalagradditions:inferium_paxel"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "apple", "title": "An Apple a Day", "optional": True, "icon": "mysticalagradditions:inferium_apple",
            "desc": [
                "A golden apple ringed with four essence becomes an &eessence apple&r. Eat one for a handful of effects: the tooltip lists them.",
            ],
            "tasks": [{"any": [f"mysticalagradditions:{t}_apple" for t in ESSENCE_TIERS + ["insanium"]],
                       "title": "Any essence apple", "icon": "mysticalagradditions:inferium_apple"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "withering_soul", "title": "Withering Soul",
            "desc": [
                "The Wither drops a &eWithering Soul&r when it dies.",
                "",
                "Three of them make three Wither Skeleton Skulls, enough for the next Wither. Keep two back for the crux.",
            ],
            "tasks": [{"item": "mysticalagradditions:withering_soul"}],
            "rewards": [{"xp": 10}, {"crate": "lantern"}],
        },
        {
            "key": "witherproof", "title": "A Proper Arena", "optional": True,
            "desc": [
                "&eWitherproof Blocks&r, &eBricks&r and &eGlass&r shrug off the Wither's explosions. Build a box out of them and the fight stays in the box.",
            ],
            "tasks": [{"any": ["mysticalagriculture:witherproof_block", "mysticalagriculture:witherproof_bricks",
                               "mysticalagriculture:witherproof_glass"],
                       "title": "Any witherproof block", "icon": "mysticalagriculture:witherproof_bricks"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "star_crux", "title": "Nether Star Crux",
            "desc": [
                "Nether Star Seeds only grow over a &eNether Star Crux&r: two Nether Stars, two Withering Souls, four Insanium Essence and a block of diamond.",
                "",
                "Nine Nether Star Essence make a shard, and three shards a Nether Star.",
            ],
            "tasks": [{"item": "mysticalagradditions:nether_star_crux"}],
            "rewards": [{"xp": 25}, {"crate": "lantern"}],
        },
        {
            "key": "dragon_scale", "title": "Dragon Scales",
            "desc": [
                "The Ender Dragon drops &eDragon Scales&r. You'll want plenty: the Dragon Egg Seed takes four, and so does its crux.",
                "",
                "The dragon comes back if you place four End Crystals on the exit portal.",
            ],
            "tasks": [{"item": "mysticalagradditions:dragon_scale", "count": 4}],
            "rewards": [{"xp": 10}, {"crate": "lantern"}],
        },
        {
            "key": "egg_crux", "title": "Dragon Egg Crux", "shape": "hexagon",
            "desc": [
                "Four Dragon Scales, four Insanium Essence and a block of diamond make a &eDragon Egg Crux&r, the soil the Dragon Egg Seed needs below it.",
                "",
                "Nine Dragon Egg Essence make a chunk, and three chunks a whole Dragon Egg. Your friends will each want one.",
            ],
            "tasks": [{"item": "mysticalagradditions:dragon_egg_crux"}],
            "rewards": [{"xp": 25}, {"crate": "ember"}],
        },
        {
            "key": "pot", "shape": "hexagon", "title": "A Garden in a Pot",
            "desc": [
                "A &eBotany Pot&r grows a crop on a single block. Give it soil and a seed and it grows right there, with no farmland to trample and no field to fence in.",
                "",
                "Mystical seeds need Essence Farmland as their soil, of their own tier or better. Essence Farmland makes them grow a little faster, too.",
            ],
            "tasks": [{"tag": "botanypots:botany_pots", "title": "Any Botany Pot",
                       "icon": "botanypots:terracotta_botany_pot"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "hopper_pot", "title": "A Row of Pots",
            "desc": [
                "A &eHopper Botany Pot&r harvests its own crop and passes it down into a chest or hopper underneath.",
                "",
                "Line a few up over a row of hoppers feeding one chest, and your essence piles up while you're off doing something else.",
            ],
            "tasks": [{"any": _HOPPER_POTS, "title": "Four Hopper Botany Pots, any kind",
                       "icon": "botanypots:terracotta_hopper_botany_pot", "count": 4}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "trees", "title": "Trees in a Pot", "optional": True,
            "desc": [
                "With Botany Trees, saplings grow in Botany Pots too. An oak sapling in a pot of dirt gives logs, leaves, apples and the odd sapling, with no tree to chop and no leaves to clear.",
                "",
                "Put one in a Hopper Botany Pot and you have a wood supply the size of a block.",
            ],
            "tasks": [{"check": "Got it"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "pylon", "shape": "hexagon", "title": "Harvester Pylon",
            "desc": [
                "Prefer a proper field to pots? The &eHarvester Pylon&r harvests ripe crops in a square around it, from 3x3 up to 9x9, and puts them in a chest on top.",
                "",
                "Set it in the water block of your farm or level with the crops. It needs a hoe inside, which loses a point of durability with each harvest, so Unbreaking is a good friend here.",
            ],
            "tasks": [{"item": "pylons:harvester_pylon"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "infusion_pylon", "title": "Infusion Pylon",
            "desc": [
                "The &eInfusion Pylon&r keeps a potion effect on you wherever you are, from &ePotion Filters&r you've charged.",
                "",
                "To charge a filter, have the effect on you and right-click with the filter. It needs an hour of the effect in total before it activates, so drink a few long potions. It also keeps its own chunk loaded while you're online.",
            ],
            "tasks": [{"item": "pylons:infusion_pylon"}, {"item": "pylons:potion_filter"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "interdiction_pylon", "title": "Interdiction Pylon",
            "desc": [
                "No more creepers in the garden. The &eInterdiction Pylon&r stops the mobs you choose from spawning, in a range from one chunk up to 5x5. Pick them with &eMob Filters&r.",
                "",
                "A &eLifeless Filter&r instead stops every natural spawn, over a much bigger area.",
            ],
            "tasks": [{"item": "pylons:interdiction_pylon"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "expulsion_pylon", "title": "Expulsion Pylon", "optional": True,
            "desc": [
                "On a server, the &eExpulsion Pylon&r keeps other players out of your chunks, from one chunk up to 5x5. Let friends in with a &ePlayer Filter&r.",
            ],
            "tasks": [{"item": "pylons:expulsion_pylon"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "protection_pylon", "title": "Protection Pylon", "optional": True,
            "desc": [
                "The &eProtection Pylon&r protects you from yourself: within its range you can't break the blocks or hurt the mobs you've picked with filters.",
                "",
                "Perfect around a pen of animals or a delicate build.",
            ],
            "tasks": [{"item": "pylons:protection_pylon"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "masher", "shape": "hexagon", "title": "Mob Masher",
            "desc": [
                "Some drops are easier to farm the old way. The &eMob Masher&r is a mob grinder you can fit with upgrades for Sharpness, Looting, Fire Aspect and more. Its kills count as player kills.",
                "",
                "For a steady supply of monsters, &eDreadful Dirt&r spawns them in the dark. Keep it out of the daylight, or it catches fire.",
            ],
            "tasks": [{"item": "mob_grinding_utils:saw"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "absorption", "title": "Absorption Hopper", "optional": True,
            "desc": [
                "The &eAbsorption Hopper&r vacuums up items and experience orbs in a 7x7x7 area around it.",
                "",
                "It can push out of any side you choose, into chests for items and tanks for experience. Radius upgrades make the area bigger.",
            ],
            "tasks": [{"item": "mob_grinding_utils:absorption_hopper"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "masher_upgrade", "title": "Sharper Teeth", "optional": True,
            "desc": [
                "&eMob Masher Upgrades&r add Sharpness, Looting, Fire Aspect, Smite, Bane of Arthropods or Beheading to the Masher. Beheading means heads.",
            ],
            "tasks": [{"any": SAW_UPGRADES, "title": "Any Mob Masher Upgrade", "icon": "mob_grinding_utils:saw_upgrade_looting"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "dreadful", "title": "Dirt That Spawns Things", "optional": True,
            "desc": [
                "&eDreadful Dirt&r spawns monsters in the dark, and burns in daylight under open sky. A light level of 5 or more stops it.",
                "",
                "&eDelightful Dirt&r does the opposite: animals, in the light. Neither works in oceans.",
            ],
            "tasks": [{"any": ["mob_grinding_utils:dreadful_dirt", "mob_grinding_utils:delightful_dirt"],
                       "title": "Dreadful or Delightful Dirt", "icon": "mob_grinding_utils:dreadful_dirt"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "fan", "title": "Mob Fan", "optional": True,
            "desc": [
                "A &eMob Fan&r pushes mobs the way it faces, straight into whatever's waiting. Upgrades change how far, wide and high it blows.",
            ],
            "tasks": [{"item": "mob_grinding_utils:fan"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "xp_tank", "title": "Bottled Experience",
            "desc": [
                "Point an Absorption Hopper at a &eSingularity Tank&r and the experience it collects pours in as liquid instead of orbs.",
                "",
                "An &eXP Tap&r on the side of the tank turns it back into orbs when you want it. The &eJumbo Tank&r holds 1024 buckets.",
            ],
            "tasks": [{"any": ["mob_grinding_utils:tank", "mob_grinding_utils:jumbo_tank"],
                       "title": "A Singularity or Jumbo Tank", "icon": "mob_grinding_utils:tank"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "xp_tap", "title": "XP Tap", "optional": True,
            "desc": [
                "Fix an &eXP Tap&r to the side of a tank and it turns the liquid back into orbs. Stand under it and soak it up.",
            ],
            "tasks": [{"item": "mob_grinding_utils:xp_tap"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "solidifier", "title": "XP Jellies",
            "desc": [
                "The &eXP Solidifier&r turns liquid experience into edible &eXP Jellies&r, using a mould. Eat one for its experience, or keep them for the next quest.",
            ],
            "tasks": [{"item": "mob_grinding_utils:xpsolidifier"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "spawner", "title": "Entity Spawner", "shape": "hexagon",
            "desc": [
                "The &eEntity Spawner&r spawns the mob from a spawn egg in its top slot, in a 3x3 area, and eats XP Jellies to do it. Upgrades make the area bigger.",
                "",
                "Put a Mob Masher in front of it and you have a farm for any drop you like.",
            ],
            "tasks": [{"item": "mob_grinding_utils:entity_spawner"}],
            "rewards": [{"xp": 25}, {"crate": "lantern"}],
        },
        {
            "key": "learner", "shape": "hexagon", "title": "Deep Learner",
            "desc": [
                "Hostile Neural Networks grows mob drops from simulations instead of seeds.",
                "",
                "Craft a &eDeep Learner&r and a &eModel Framework&r. Right-click a mob with the framework to attune it, put the model in the learner, and wear the learner in its Curios slot. &eShift+U&r opens it.",
                "",
                "Then go fight. Every kill of that mob teaches the model a little more.",
            ],
            "tasks": [{"item": "hostilenetworks:deep_learner"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "sim", "title": "Train a Model",
            "desc": [
                "Put a trained model and a &ePrediction Matrix&r in a powered &eSimulation Chamber&r and it fights the battle for you, producing that mob's &ePrediction&r. A &eLoot Fabricator&r turns predictions into real drops.",
                "",
                "New models are Faulty, and a Faulty model can't be simulated. Get a few kills in first. After that, the chamber's Training Mode can level a model up for you, at the cost of making nothing while it does.",
            ],
            "tasks": [{"item": "hostilenetworks:sim_chamber"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "fabricator", "title": "Loot Fabricator",
            "desc": [
                "The &eLoot Fabricator&r turns Predictions into the real thing. Pick which of the mob's drops you want on its screen.",
                "",
                "A &eFabrication Directive&r copies one fabricator's choices onto another.",
            ],
            "tasks": [{"item": "hostilenetworks:loot_fabricator"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "data_center", "title": "The Data Center", "shape": "hexagon",
            "desc": [
                "The top of the line. A &eData Center&r runs up to twenty-five Self Aware models at once, all feeding one output.",
                "",
                "It needs a hollow 7x7x7 shell: an obsidian floor, black stained glass walls and ceiling, and the controller set into the bottom of a wall, facing out. &eData Center IO Ports&r can stand in for any wall or ceiling block to move power, models and items.",
            ],
            "tasks": [{"item": "hostilenetworks:data_center"}],
            "rewards": [{"xp": 25}, {"crate": "lantern"}],
        },
    ] + [
        {
            "key": f"model_{k}", "title": t, "optional": True, "icon": "hostilenetworks:data_model", "icon_components": model(m),
            "desc": [d],
            "tasks": [{"item": "hostilenetworks:data_model", "components": model(m), "title": f"{t}", "icon": "hostilenetworks:blank_data_model"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        }
        for k, m, t, d in [
            ("blaze", "blaze", "Blaze Data Model", "Blaze rods without the fortress. Right-click a blaze with a Model Framework to attune it."),
            ("enderman", "enderman", "Enderman Data Model", "Ender pearls by the stack, for every pearl recipe in the pack."),
            ("ghast", "ghast", "Ghast Data Model", "Ghast tears, the hardest drop in the Nether to collect by hand."),
            ("shulker", "shulker", "Shulker Data Model", "Shulker shells for as many shulker boxes as you can fill."),
            ("diamond_ore", "blocks/diamond_ore", "Diamond Ore Data Model", "Not every model is a mob. Right-click diamond ore with a framework, and the model learns from every block you mine."),
        ]

    ],
}
