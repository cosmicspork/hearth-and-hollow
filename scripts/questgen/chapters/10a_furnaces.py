def side(key, title, desc, task, crate="hearth", icon=None, **extra):
    """An optional catalog quest: one variant of a mod's kit, with a line or two about it."""
    q = {"key": key, "title": title, "optional": True, "desc": desc, "tasks": [task],
         "rewards": [{"xp": 10}, {"crate": crate}]}
    if icon:
        q["icon"] = icon
    q.update(extra)
    return q


def furnace(key, name, title, desc, upgrades, crate="hearth", **extra):
    """An Iron Furnaces tier: the furnace, or an upgrade kit that turns a placed one into it."""
    item = f"ironfurnaces:{name}_furnace"
    return side(key, title, desc,
                {"any": [item] + [f"ironfurnaces:{u}" for u in upgrades],
                 "title": f"{title}, or the upgrade to one", "icon": item},
                crate=crate, icon=item, **extra)


FURNACES = [
    furnace("if_silver", "silver", "Silver Furnace", ["Another road to gold. Built around a copper or iron furnace."],
            ["upgrade_silver", "upgrade_silver2"]),
    furnace("if_gold", "gold", "Golden Furnace", ["Faster again. Built around an iron or silver furnace."],
            ["upgrade_gold", "upgrade_gold2"], optional=False),
    furnace("if_diamond", "diamond", "Diamond Furnace", ["Built around a golden furnace. From here it branches: emerald or crystal, then obsidian."],
            ["upgrade_diamond"], optional=False),
    furnace("if_emerald", "emerald", "Emerald Furnace", ["A faster step up from diamond."], ["upgrade_emerald"]),
    furnace("if_crystal", "crystal", "Crystal Furnace", [
        "Glass and an eye of ender around a diamond furnace. Emerald and crystal both lead on to obsidian.",
    ], ["upgrade_crystal"]),
    furnace("if_obsidian", "obsidian", "Obsidian Furnace", ["From an emerald or crystal furnace."],
            ["upgrade_obsidian", "upgrade_obsidian2"], optional=False),
    furnace("if_netherite", "netherite", "Netherite Furnace", ["The fastest of the vanilla metals."], ["upgrade_netherite"],
            optional=False),
    furnace("if_allthemodium", "allthemodium", "Allthemodium Furnace", ["Past netherite, the furnaces follow the allthemodium metals."],
            ["upgrade_allthemodium"], optional=False),
    furnace("if_vibranium", "vibranium", "Vibranium Furnace", ["Faster again."], ["upgrade_vibranium"], optional=False),
    furnace("if_unobtainium", "unobtainium", "Unobtainium Furnace", ["The last of the metal furnaces."],
            ["upgrade_unobtainium"], optional=False, shape="hexagon", rewards=[{"xp": 25}, {"crate": "hearth"}]),
    side("if_rainbow", "The Rainbow Furnace", [
        "The showpiece. One each of the copper, iron, silver, gold, diamond, emerald, crystal and obsidian furnaces make eight &eRainbow Plating&r.",
        "",
        "Wrap the plating around a &eRainbow Core&r, made from netherite furnaces and stained glass in every color of the rainbow.",
    ], {"item": "ironfurnaces:million_furnace"}, icon="ironfurnaces:million_furnace",
        rewards=[{"xp": 25}, {"crate": "lantern"}]),
    side("if_heater", "Heat Without Fuel", [
        "Feed FE to a &eWireless Heat Transmitter&r, and place a &eWireless Heat Receiver&r in it to bind them.",
        "",
        "Then put the receiver in a furnace's fuel slot, and the furnace runs on that power. Iron tier and up.",
    ], {"any": ["ironfurnaces:heater", "ironfurnaces:item_heater"], "title": "A wireless heat transmitter or receiver",
        "icon": "ironfurnaces:heater"}, icon="ironfurnaces:heater"),
    side("aug_speed", "Augment: Speed", ["Halves the cook time for every recipe, but burns fuel twice as fast."],
         {"item": "ironfurnaces:augment_speed"}),
    side("aug_fuel", "Augment: Fuel Efficiency", ["Fuel heats the furnace twice as much, but cooking is a quarter slower."],
         {"item": "ironfurnaces:augment_fuel"}),
    side("aug_blasting", "Augment: Blasting", ["The furnace only does blasting recipes, like a blast furnace."],
         {"item": "ironfurnaces:augment_blasting"}),
    side("aug_smoking", "Augment: Smoking", ["The furnace only does smoking recipes, like a smoker. Good for a kitchen."],
         {"item": "ironfurnaces:augment_smoking"}),
    side("aug_factory", "Augment: Factory", ["Turns the furnace into a factory that runs on power instead of fuel."],
         {"item": "ironfurnaces:augment_factory"}),
]

CHAPTER = {
    "file": "furnaces",
    "group": "hum",
    "title": "Faster Furnaces",
    "subtitle": "From iron to unobtainium, upgraded in place",
    "icon": "ironfurnaces:iron_furnace",
    # One ladder of furnace tiers, with the side roads above and below it, and the augments,
    # which fit any furnace, in a row of their own.
    "layout": {
        "lines": [
            {"spine": ["iron_furnace", "if_gold", "if_diamond", "if_obsidian", "if_netherite", "if_allthemodium",
                       "if_vibranium", "if_unobtainium"],
             "branches": {
                 "iron_furnace": {"up": ["if_silver"]},
                 "if_diamond": {"up": ["if_emerald"], "down": ["if_crystal"]},
                 "if_netherite": {"up": ["if_rainbow"]},
             }},
            {"rows": ["aug_speed", "aug_fuel", "aug_blasting", "aug_smoking", "aug_factory", "gen_augment", "if_heater"]},
        ],
    },
    "quests": [
        {
            "key": "iron_furnace", "title": "Iron Furnaces", "shape": "hexagon", "size": 1.5,
            "desc": [
                "Eight iron ingots around a furnace make an &eIron Furnace&r, which smelts faster than the stone one. Copper ingots make a &eCopper Furnace&r, a smaller step up.",
                "",
                "Already built a row of vanilla furnaces? Sneak and right-click one with a &eStone to Iron Furnace Upgrade&r and it changes on the spot. Every tier on this line works that way.",
                "",
                "Every furnace in the pack runs a little lighter on your computer, too.",
            ],
            "tasks": [{"any": ["ironfurnaces:iron_furnace", "ironfurnaces:copper_furnace", "ironfurnaces:upgrade_iron",
                               "ironfurnaces:upgrade_copper", "ironfurnaces:upgrade_iron2"],
                       "title": "A copper or iron furnace, or the upgrade to one", "icon": "ironfurnaces:iron_furnace"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "gen_augment", "title": "A Furnace That Makes Power", "optional": True,
            "desc": [
                "Iron Furnaces take augments. Right-click a furnace with an augment to fit it.",
                "",
                "The &eGenerator&r augment turns the furnace's heat into power, though it can't smelt any more. Better furnaces make more.",
            ],
            "tasks": [{"item": "ironfurnaces:augment_generator"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
    ] + FURNACES,
}
