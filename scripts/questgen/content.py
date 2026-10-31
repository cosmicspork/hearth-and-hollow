"""Quest book content: chapter groups, crate tables and chapters."""

GROUPS = [
    {"key": "settled", "title": "Getting Settled"},
    {"key": "world", "title": "Out in the World"},
    {"key": "hum", "title": "Making It Hum"},
    {"key": "long", "title": "The Long Road"},
]

# rewards: (item id | ("book", enchantment, level), count, weight)
TABLES = [
    {
        "name": "kindling", "title": "&7Kindling Crate", "color": 0xA89A88, "glow": False, "rolls": 2,
        "rewards": [
            ("minecraft:bread", 8, 1),
            ("minecraft:baked_potato", 8, 1),
            ("minecraft:cooked_beef", 6, 1),
            ("minecraft:torch", 16, 1),
            ("minecraft:coal", 8, 1),
            ("minecraft:copper_ingot", 12, 1),
            ("minecraft:oak_sapling", 4, 0.6),
            ("minecraft:birch_sapling", 4, 0.6),
            ("minecraft:cherry_sapling", 2, 0.4),
            ("minecraft:white_wool", 6, 0.8),
            ("minecraft:lantern", 4, 0.6),
            ("minecraft:candle", 4, 0.6),
            ("minecraft:flower_pot", 4, 0.4),
            ("minecraft:leather", 6, 0.6),
            ("minecraft:ender_pearl", 2, 0.4),
        ],
    },
    {
        "name": "hearth", "title": "&aHearth Crate", "color": 0x6FA84F, "glow": False, "rolls": 2,
        "rewards": [
            ("minecraft:diamond", 2, 0.6),
            ("minecraft:gold_ingot", 6, 1),
            ("minecraft:redstone", 16, 1),
            ("minecraft:lapis_lazuli", 16, 0.8),
            ("minecraft:ender_pearl", 4, 0.8),
            ("minecraft:emerald", 4, 0.8),
            ("minecraft:amethyst_shard", 8, 0.6),
            ("alltheores:steel_ingot", 4, 0.8),
            ("mysticalagriculture:inferium_essence", 16, 1),
            ("mysticalagriculture:prosperity_shard", 8, 0.8),
            ("sophisticatedbackpacks:upgrade_base", 2, 0.8),
            ("mekanism:basic_control_circuit", 2, 0.6),
            ("powah:dielectric_paste", 16, 0.8),
        ],
    },
    {
        "name": "lantern", "title": "&dLantern Crate", "color": 0xB06FD0, "glow": True, "rolls": 2,
        "rewards": [
            ("allthemodium:allthemodium_nugget", 4, 1),
            ("allthemodium:vibranium_nugget", 2, 0.5),
            ("minecraft:diamond", 6, 1),
            ("minecraft:netherite_scrap", 2, 0.5),
            ("minecraft:golden_apple", 2, 0.8),
            ("minecraft:name_tag", 1, 0.5),
            ("mysticalagriculture:iron_seeds", 1, 0.6),
            ("mysticalagriculture:gold_seeds", 1, 0.4),
            (("book", "minecraft:mending", 1), 1, 0.5),
            (("book", "minecraft:unbreaking", 3), 1, 0.8),
            (("book", "minecraft:efficiency", 4), 1, 0.8),
            (("book", "minecraft:fortune", 2), 1, 0.6),
            (("book", "minecraft:looting", 2), 1, 0.6),
            (("book", "minecraft:protection", 3), 1, 0.8),
        ],
    },
    {
        "name": "ember", "title": "&6Ember Crate", "color": 0xE0882A, "glow": True, "rolls": 2,
        "rewards": [
            ("allthemodium:allthemodium_ingot", 2, 1),
            ("allthemodium:vibranium_ingot", 1, 0.6),
            ("allthemodium:unobtainium_ingot", 1, 0.3),
            ("minecraft:netherite_ingot", 1, 0.6),
            ("minecraft:nether_star", 1, 0.4),
            ("minecraft:enchanted_golden_apple", 1, 0.4),
            ("minecraft:totem_of_undying", 1, 0.5),
            ("minecraft:diamond_block", 1, 0.8),
        ],
    },
]
