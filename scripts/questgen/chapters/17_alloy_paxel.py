VA = "allthemodium:vibranium_allthemodium_alloy_ingot"
UA = "allthemodium:unobtainium_allthemodium_alloy_ingot"
UV = "allthemodium:unobtainium_vibranium_alloy_ingot"
WITHER = {"hostilenetworks:data_model": "hostilenetworks:wither"}

# Jonn's Trophies stores an item trophy as custom data naming the item it shows.
PAXEL_TROPHY = {"minecraft:custom_data": {
    "TrophyType": "item",
    "TrophyItem": {"id": "allthemodium:alloy_paxel", "count": 1},
    "BaseBlock": "minecraft:smooth_stone_slab",
    "Spin": True,
    "Subject": "item.allthemodium.alloy_paxel",
}}

CHAPTER = {
    "file": "alloy_paxel",
    "group": "long",
    "title": "The Alloy Paxel",
    "subtitle": "The capstone: one tool, every road",
    "icon": "allthemodium:alloy_paxel",
    # A funnel: the three alloys fan out from the hearts and meet again at the tools.
    # The tech pieces come in from the side, since they're gathered in parallel.
    "layout": {
        "free": {
            "road": (0, 0), "hearts": (0, 1.75),
            "va": (-2.25, 3.5), "ua": (0, 3.5), "uv": (2.25, 3.5),
            "tools": (0, 5.25), "paxel": (0, 7.25), "pieces": (3.25, 7.25), "copy": (0, 9.25),
        },
        "deps": {
            "hearts": ["road"], "va": ["hearts"], "ua": ["hearts"], "uv": ["hearts"],
            "tools": ["va", "ua", "uv"], "paxel": ["tools", "pieces"], "copy": ["paxel"],
        },
    },
    "quests": [
        {
            "key": "road", "title": "The Alloy Paxel", "shape": "hexagon", "size": 1.5, "wide": True,
            "desc": [
                "The Allthemodium Alloy Paxel is a pickaxe, axe and shovel in one, forged from the three endgame metals and a finished piece of everything else you've built.",
                "",
                "It's a long road, and that's the point:",
                "",
                "&e1.&r Piglich Hearts, to bind the metals",
                "&e2.&r Three alloy ingots, from the Energizing Orb",
                "&e3.&r Four alloy tools, on an Advanced Crafting Table",
                "&e4.&r One piece from each tech chapter",
                "&e5.&r The paxel, on an Elite Crafting Table",
                "",
                "Every recipe is in JEI. Press &eU&r on an alloy ingot to see where it goes.",
            ],
            "tasks": [{"check": "Show me the way"}],
            "rewards": [],
        },
        {
            "key": "hearts", "title": "Heart of a Lich",
            "desc": [
                "Alloys won't hold without something to bind them. A &ePiglich Heart&r does it.",
                "",
                "Piglichs guard the &eAncient Pyramids&r in the soul sand valleys of the Other. Each one drops a heart. Bring friends.",
                "",
                "Once you've met one, a Hostile Networks model can learn them, and every Piglich prediction fabricates four hearts. The tools and the paxel take eighteen hearts between them, so the model pays for itself.",
            ],
            "tasks": [{"item": "allthemodium:piglich_heart", "count": 4}],
            "rewards": [{"xp": 25}, {"crate": "lantern"}],
        },
        {
            "key": "va", "title": "Vibranium Meets Allthemodium",
            "desc": [
                "Right-click two &eAllthemodium Ingots&r, two &eVibranium Ingots&r and a &ePiglich Heart&r into an Energizing Orb. It takes 2,000,000 FE and gives you two alloy ingots.",
                "",
                "That's a lot of power through one orb. More rods, and better ones, fill it faster.",
            ],
            "tasks": [{"item": VA}],
            "rewards": [{"xp": 25}, {"crate": "hearth", "count": 2}],
        },
        {
            "key": "ua", "title": "Unobtainium Meets Allthemodium",
            "desc": [
                "Two &eUnobtainium Ingots&r, two &eAllthemodium Ingots&r and a Piglich Heart, into the orb again. This one wants 5,000,000 FE.",
            ],
            "tasks": [{"item": UA}],
            "rewards": [{"xp": 25}, {"crate": "hearth", "count": 2}],
        },
        {
            "key": "uv", "title": "Unobtainium Meets Vibranium",
            "desc": [
                "The hardest of the three: two &eUnobtainium Ingots&r, two &eVibranium Ingots&r and a Piglich Heart, for 10,000,000 FE.",
                "",
                "If your power grid has been coasting, this is where you'll find out.",
            ],
            "tasks": [{"item": UV}],
            "rewards": [{"xp": 25}, {"crate": "lantern"}],
        },
        {
            "key": "tools", "title": "Four Alloy Tools", "shape": "hexagon",
            "icon": "allthemodium:alloy_pick", "wide": True,
            "desc": [
                "Each alloy tool upgrades its unobtainium counterpart. On an &eAdvanced Crafting Table&r, surround an Unobtainium pickaxe, axe, shovel or sword with alloy ingots and Unobtainium Rods.",
                "",
                "They're the best tools in the pack in their own right, so use them while you work toward the paxel. It needs all four.",
            ],
            "tasks": [
                {"item": "allthemodium:alloy_pick"},
                {"item": "allthemodium:alloy_axe"},
                {"item": "allthemodium:alloy_shovel"},
                {"item": "allthemodium:alloy_sword"},
            ],
            "rewards": [{"xp": 50}, {"crate": "ember"}],
        },
        {
            "key": "pieces", "title": "A Piece of Everything", "shape": "hexagon",
            "icon": "mekanism:ultimate_control_circuit", "wide": True,
            "desc": [
                "The paxel takes one finished piece from each tech chapter. Each one is near the end of its chapter. You'll get them all back when you craft the paxel.",
                "",
                "&eMekanism:&r an Ultimate Control Circuit",
                "&eOritech:&r an Ultimate Machine Core",
                "&eRefined Storage:&r a 64K Storage Disk",
                "&eGreen Thumb:&r Insanium Essence and a Wither Prediction",
                "",
                "The recipe takes four Insanium Essence, so grow a few more.",
            ],
            "tasks": [
                {"item": "mekanism:ultimate_control_circuit"},
                {"item": "oritech:machine_core_7"},
                {"item": "refinedstorage:64k_storage_disk"},
                {"item": "mysticalagradditions:insanium_essence", "count": 4},
                {"item": "hostilenetworks:prediction", "components": WITHER, "title": "Wither Prediction"},
            ],
            "rewards": [{"xp": 50}, {"crate": "ember"}],
        },
        {
            "key": "paxel", "title": "The Allthemodium Alloy Paxel", "shape": "hexagon", "size": 2.0,
            "icon": "allthemodium:alloy_paxel",
            "desc": [
                "Bring it all to an &eElite Crafting Table&r: the four alloy tools, a ring of alloy ingots, four Insanium Essence and the five tech pieces.",
                "",
                "One tool for every block, made from everything you've built along the way. Well done.",
                "",
                "The tech pieces come back to you as rewards, so your bases don't go short.",
            ],
            "tasks": [{"item": "allthemodium:alloy_paxel"}],
            "rewards": [
                {"xp_levels": 30},
                {"crate": "ember", "count": 3},
                {"item": "trophymanager:trophy", "components": PAXEL_TROPHY},
                # The tech pieces the recipe used, given back.
                {"item": "mekanism:ultimate_control_circuit"},
                {"item": "oritech:machine_core_7"},
                {"item": "refinedstorage:64k_storage_disk"},
                {"item": "mysticalagradditions:insanium_essence", "count": 4},
                {"item": "hostilenetworks:prediction", "components": WITHER},
                {"command": '/tellraw @a ["",{"text":"{p}","color":"gold"},{"text":" has forged the Allthemodium Alloy Paxel!","color":"yellow"}]'},
            ],
        },
        {
            "key": "copy", "title": "One for a Friend", "optional": True,
            "desc": [
                "Once you have a paxel, you can make more without the tech pieces. Put yours in the middle of a crafting table with eight blocks of alloy around it: Vibranium-Allthemodium and Unobtainium-Vibranium on the corners, two of each, and Unobtainium-Allthemodium on the four sides.",
                "",
                "Your paxel stays in the grid, so you end up with two. Pass one on, or keep a spare.",
            ],
            "tasks": [{"item": "allthemodium:alloy_paxel", "count": 2}],
            "rewards": [{"xp": 25}, {"crate": "lantern"}],
        },
    ],
}
