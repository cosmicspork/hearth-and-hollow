MGU = "mob_grinding_utils"


def upgrade(key, item, title, desc):
    return {
        "key": key, "title": title, "optional": True,
        "desc": desc,
        "tasks": [{"item": f"{MGU}:{item}"}],
        "rewards": [{"xp": 10}, {"crate": "kindling"}],
    }


SAW_UPGRADES = [
    ("sharpness", "Sharpness"), ("looting", "Looting"), ("fire", "Fire Aspect"), ("smite", "Smite"),
    ("arthropod", "Bane of Arthropods"), ("beheading", "Beheading"),
]
UPGRADES = [
    upgrade(f"saw_{u}", f"saw_upgrade_{u}", f"Masher: {t}",
            [f"Adds a level of &e{t}&r to the Mob Masher. Stack a few for more."
             + (" Beheading means heads." if u == "beheading" else "")])
    for u, t in SAW_UPGRADES
] + [
    upgrade("fan_distance", "fan_upgrade_speed", "Fan: Distance", ["Pushes mobs one block further, up to ten."]),
    upgrade("fan_width", "fan_upgrade_width", "Fan: Width", ["Makes the Mob Fan's push one block wider, up to three."]),
    upgrade("fan_height", "fan_upgrade_height", "Fan: Height", ["Makes the Mob Fan's push one block taller, up to three."]),
    upgrade("spawner_width", "spawner_upgrade_width", "Spawner: Width", ["Widens the area the Entity Spawner spawns in."]),
    upgrade("spawner_height", "spawner_upgrade_height", "Spawner: Height", ["Raises the area the Entity Spawner spawns in."]),
    upgrade("absorption_upgrade", "absorption_upgrade", "Hopper: Radius", ["Makes the Absorption Hopper reach further."]),
    upgrade("xp_speed", "xp_solidifier_upgrade", "XP Speed",
            ["Speeds up the XP Solidifier, or the Entity Spawner."]),
]

CHAPTER = {
    "file": "mob_grinding",
    "group": "hum",
    "title": "Mob Grinding",
    "subtitle": "A farm for any drop, with the experience bottled",
    "icon": "mob_grinding_utils:saw",
    "layout": {"lines": [
        {"flow": ["masher", ["dreadful", "fan", "conveyor", "absorption"]]},
        {"flow": [["xp_tank", "swab"], ["solidifier", "gm_feed"], "spawner"],
         "branches": {"xp_tank": {"up": ["xp_tap"]}}},
        {"rows": [u["key"] for u in UPGRADES], "per_row": 7},
        {"rows": ["spikes", "inhibitor", "muffler", "tinted_glass"]},
    ]},
    "quests": [
        {
            "key": "masher", "shape": "hexagon", "size": 1.5, "title": "Mob Masher",
            "desc": [
                "Some drops are easier to farm the old way. The &eMob Masher&r is a mob grinder you can fit with upgrades for Sharpness, Looting, Fire Aspect and more. Its kills count as player kills.",
                "",
                "For a steady supply of monsters, &eDreadful Dirt&r spawns them in the dark. Keep it out of the daylight, or it catches fire.",
            ],
            "tasks": [{"item": "mob_grinding_utils:saw"}],
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
            "key": "conveyor", "title": "Entity Conveyor",
            "desc": [
                "An &eEntity Conveyor&r carries mobs and items along in a straight line. Mobs can spawn on it, too, so a floor of them makes a spawning pad that delivers itself.",
            ],
            "tasks": [{"item": "mob_grinding_utils:entity_conveyor"}],
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
            "key": "swab", "title": "Mob Swab",
            "desc": [
                "Wool on a stick makes a &eMob Swab&r. Use it on a mob to collect its 'DNA'.",
                "",
                "A used swab is the start of a spawn egg, two quests on.",
            ],
            "tasks": [{"item": "mob_grinding_utils:mob_swab"}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}],
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
            "key": "gm_feed", "title": "Chicken Feed, Modified",
            "desc": [
                "Seeds, a used Mob Swab and a bucket of liquid experience make &eGM Chicken Feed&r. Feed it to a chicken and it turns that DNA into the mob's spawn egg, for the Entity Spawner.",
                "",
                "The chicken only gets the one go. JEI shows the details.",
            ],
            "tasks": [{"item": "mob_grinding_utils:gm_chicken_feed"}],
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
    ] + UPGRADES + [
        {
            "key": "spikes", "title": "Iron Spikes", "optional": True,
            "desc": [
                "The cheap way to kill mobs. &eIron Spikes&r hurt anything that walks over them and drop its experience.",
                "",
                "Their kills don't count as player kills, though, so some drops never come. The Mob Masher's do.",
            ],
            "tasks": [{"item": "mob_grinding_utils:spikes"}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}],
        },
        {
            "key": "inhibitor", "title": "Ender Inhibitor", "optional": True,
            "desc": [
                "Endermen won't teleport within 8 blocks of an &eEnder Inhibitor&r. Right-click it to switch it off and on.",
            ],
            "tasks": [{"any": ["mob_grinding_utils:ender_inhibitor_on", "mob_grinding_utils:ender_inhibitor_off"],
                       "title": "An Ender Inhibitor", "icon": "mob_grinding_utils:ender_inhibitor_on"}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}],
        },
        {
            "key": "muffler", "title": "Peace and Quiet", "optional": True,
            "desc": [
                "A boss farm is loud. The &eWither Boss Death Muffler&r and &eEnder Dragon Death Muffler&r silence their death sounds nearby. Right-click one to hide the boss bar too.",
            ],
            "tasks": [{"any": ["mob_grinding_utils:wither_muffler", "mob_grinding_utils:dragon_muffler"],
                       "title": "Either Death Muffler", "icon": "mob_grinding_utils:wither_muffler"}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}],
        },
        {
            "key": "tinted_glass", "title": "Dark Glass", "optional": True,
            "desc": [
                "This &eTinted Glass&r keeps light out, so mobs spawn behind it, and it's tough enough to hold a Wither.",
            ],
            "tasks": [{"item": "mob_grinding_utils:tinted_glass"}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}],
        },
    ],
}
