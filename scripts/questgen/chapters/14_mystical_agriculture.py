GEAR = ["sword", "pickaxe", "axe", "shovel", "hoe", "sickle", "scythe", "bow", "crossbow", "shears", "fishing_rod",
        "helmet", "chestplate", "leggings", "boots"]
ESSENCE_TIERS = ["inferium", "prudentium", "tertium", "imperium", "supremium"]


def gear(tier):
    return [f"mysticalagriculture:{tier}_{g}" for g in GEAR]


_ROMAN = ["i", "ii", "iii", "iv", "v"]
# Augments, a quest per family: (key, title, augment ids, what it does).
AUGMENTS = [
    (n, t, [f"mysticalagriculture:{n}_{r}_augment" for r in _ROMAN[:tiers]], d)
    for n, t, tiers, d in [
        ("absorption", "Absorption", 5, "Extra golden hearts that soak up damage."),
        ("health_boost", "Health Boost", 5, "More hearts, plain and simple."),
        ("strength", "Strength", 3, "Hit harder."),
        ("attack_aoe", "Attack Area", 3, "Your swings catch whatever's standing around the target too."),
        ("speed", "Speed", 3, "Walk and run faster."),
        ("jump_boost", "Jump Boost", 3, "Jump higher."),
        ("haste", "Haste", 3, "Mine and dig faster."),
        ("mining_aoe", "Mining Area", 4, "Break a wider patch of blocks with each swing."),
        ("pathing_aoe", "Pathing Area", 4, "Turn a wide patch of grass into path at once."),
        ("tilling_aoe", "Tilling Area", 4, "Till a wide patch of farmland at once."),
        ("luck", "Luck", 3, "Better rolls on loot and fishing."),
    ]
] + [
    (n, t, [f"mysticalagriculture:{n}_augment"], d)
    for n, t, d in [
        ("flight", "Flight", "Fly, as in creative mode. The best one there is."),
        ("night_vision", "Night Vision", "See in the dark, with no torches."),
        ("no_fall_damage", "No Fall Damage", "Land from any height, unhurt."),
        ("slow_falling", "Slow Falling", "Drift down gently instead of falling."),
        ("step_assist", "Step Assist", "Walk up full blocks as if they were slabs."),
        ("water_breathing", "Water Breathing", "Stay under water as long as you like."),
    ]
] + [
    ("resistance", "Resistance", [f"mysticalagriculture:{r}_resistance_augment" for r in (
        "blindness", "fire", "hunger", "mining_fatigue", "nausea", "poison", "slowness", "weakness", "wither")],
     "Shrug off one bad effect: blindness, fire, hunger, mining fatigue, nausea, poison, slowness, weakness or wither."),
]


def augment_quest(key, title, ids, does):
    tiers = f" It comes in {len(ids)} tiers." if len(ids) > 1 and key != "resistance" else ""
    return {
        "key": f"aug_{key}", "title": f"{title} Augment{'s' if len(ids) > 1 else ''}", "optional": True,
        "icon": ids[0],
        "desc": [does + tiers, "", "Look it up with &eR&r to see what it takes and which gear it fits."],
        "tasks": [{"any": ids, "title": f"Any {title} augment", "icon": ids[0]}] if len(ids) > 1 else [{"item": ids[0]}],
        "rewards": [{"xp": 10}, {"crate": "hearth"}],
    }


CHAPTER = {
    "file": "mystical_agriculture",
    "group": "hum",
    "title": "Mystical Agriculture",
    "subtitle": "Grow your resources instead of mining them",
    "icon": "mysticalagriculture:inferium_seeds",
    "theme": "grower",
    "layout": {"lines": [
        {"spine": ["start", "seeds", "altar", "crystal", "prudentium", "tertium", "imperium", "supremium", "finale"],
         "branches": {
             "start": {"up": ["prosperity"]},
             "seeds": {"down": ["farmland"]},
             "altar": {"up": ["soul_dagger"], "down": ["resource_seed"]},
             "supremium": {"down": ["master_crystal"]},
         }},
        {"spine": ["gear_inferium", "gear_prudentium", "gear_tertium", "gear_imperium", "gear_supremium"],
         "branches": {"gear_inferium": {"down": ["sickle"]}}},
        {"flow": [["cognizant", "awakening"], "awakened", "awakened_gear"]},
        {"rows": ["tinkering"] + [f"aug_{a[0]}" for a in AUGMENTS] + ["paxel", "apple"], "per_row": 11},
        {"rows": ["frame", "furnace", "reprocessor", "soul_extractor", "harvester", "enchanter", "machine_upgrade"]},
        {"flow": [["withering_soul", "dragon_scale"], ["star_crux", "egg_crux"]],
         "branches": {"withering_soul": {"up": ["witherproof"]}}},
    ]},
    "quests": [
        {
            "key": "start", "title": "Mystical Agriculture",
            "shape": "hexagon", "size": 1.5, "icon": "mysticalagriculture:inferium_essence",
            "desc": [
                "Why mine iron when you can grow it? Mystical Agriculture has seeds that grow real resources. This chapter climbs the essence ladder, and &eA Seed for Everything&r has a quest for every seed.",
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
                "They grow on any farmland, but do best on Essence Farmland, just below.",
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
                "Four Supremium around an Infusion Crystal make &eInsanium Essence&r, the very top of the ladder. The last row of seeds needs it, and so do the cruxes below.",
                "",
                "It's also a piece of the &eAllthemodium Alloy Paxel&r. The paxel quest gives it back once you've crafted the paxel.",
            ],
            "tasks": [{"item": "mysticalagradditions:insanium_essence"}],
            "rewards": [{"xp": 50}, {"crate": "ember"}, {"item": "mysticalagradditions:insanium_farmland", "count": 4}],
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
    ] + [augment_quest(*a) for a in AUGMENTS] + [
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
                "Make a few. Every machine in this row takes one.",
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
    ],
}
