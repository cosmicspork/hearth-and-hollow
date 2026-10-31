_COLORS = ["white", "orange", "magenta", "light_blue", "yellow", "lime", "pink", "gray", "light_gray", "cyan",
           "purple", "blue", "brown", "green", "red", "black"]
_HOPPER_POTS = (["botanypots:terracotta_hopper_botany_pot"]
                + [f"botanypots:{c}_{m}_hopper_botany_pot" for c in _COLORS
                   for m in ("terracotta", "glazed_terracotta", "concrete")]
                + [f"botanypots:{b}_hopper_botany_pot" for b in
                   ("bricks", "stone_bricks", "mossy_stone_bricks", "deepslate_bricks", "tuff_bricks", "mud_bricks",
                    "prismarine_bricks", "nether_bricks", "red_nether_bricks", "polished_blackstone_bricks",
                    "end_stone_bricks", "quartz_bricks")])

CHAPTER = {
    "file": "green_thumb",
    "group": "hum",
    "title": "Green Thumb",
    "subtitle": "Pots, pylons and faster crops",
    "icon": "botanypots:terracotta_botany_pot",
    "layout": {"lines": [
        {"flow": ["pot", "hopper_pot"]},
        {"rows": ["watering", "accelerator", "fertilizer"]},
        {"rows": ["pylon", "infusion_pylon", "interdiction_pylon", "expulsion_pylon", "protection_pylon"]},
    ]},
    "quests": [
        {
            "key": "pot", "shape": "hexagon", "size": 1.5, "title": "A Garden in a Pot",
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
                "",
                "Saplings grow in pots too. An oak sapling in a pot of dirt gives logs, leaves, apples and the odd sapling, so a Hopper Botany Pot makes a wood supply the size of a block.",
            ],
            "tasks": [{"any": _HOPPER_POTS, "title": "Four Hopper Botany Pots, any kind",
                       "icon": "botanypots:terracotta_hopper_botany_pot", "count": 4}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
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
    ],
}
