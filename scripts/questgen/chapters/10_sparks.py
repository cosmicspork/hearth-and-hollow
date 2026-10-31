POWAH_TIERS = ["starter", "basic", "hardened", "blazing", "niotic", "spirited", "nitro"]


def side(key, title, desc, task, crate="hearth", icon=None, **extra):
    """An optional catalog quest: one variant of a mod's kit, with a line or two about it."""
    q = {"key": key, "title": title, "optional": True, "desc": desc, "tasks": [task],
         "rewards": [{"xp": 10}, {"crate": crate}]}
    if icon:
        q["icon"] = icon
    q.update(extra)
    return q


def gg(key, name, desc, upgrades, crate="hearth", **extra):
    """A Generator Galore tier: the generator itself, or the upgrade that turns a placed one into it."""
    gen = f"generatorgalore:{name}_generator"
    return side(key, f"{name.capitalize()} Generator", desc,
                {"any": [gen] + [f"generatorgalore:{u}_upgrade" for u in upgrades],
                 "title": f"A {name} generator, or the upgrade to one", "icon": gen},
                crate=crate, icon=gen, **extra)


def furnace(key, name, title, desc, upgrades, crate="hearth", **extra):
    """An Iron Furnaces tier: the furnace, or an upgrade kit that turns a placed one into it."""
    item = f"ironfurnaces:{name}_furnace"
    return side(key, title, desc,
                {"any": [item] + [f"ironfurnaces:{u}" for u in upgrades],
                 "title": f"{title}, or the upgrade to one", "icon": item},
                crate=crate, icon=item, **extra)


def powah(key, title, desc, kind, crate="hearth", **extra):
    """A Powah machine in any of its seven tiers."""
    first = f"powah:{kind}_starter"
    return side(key, title, desc,
                {"any": [f"powah:{kind}_{t}" for t in POWAH_TIERS], "title": f"Any {title.lower()}", "icon": first},
                crate=crate, icon=first, **extra)


def rod(tier, desc):
    item = f"powah:energizing_rod_{tier}"
    return side(f"p_rod_{tier}", f"{tier.capitalize()} Energizing Rod", desc, {"item": item})


GENERATORS = [
    gg("gg_gold", "gold", ["Gold generators make 32 FE/t, and burn their fuel a little slower than iron ones."],
       ["iron_to_gold"], optional=False),
    gg("gg_diamond", "diamond", ["64 FE/t, and thriftier with fuel again. Diamond is where the line branches out."],
       ["gold_to_diamond"], optional=False),
    gg("gg_emerald", "emerald", ["An emerald generator makes 256 FE/t from ordinary furnace fuel."], ["diamond_to_emerald"]),
    gg("gg_obsidian", "obsidian", [
        "128 FE/t, and the root of three odd ones: magmatic, ender and enchantment generators all grow from it.",
    ], ["diamond_to_obsidian"], optional=False),
    gg("gg_netherite", "netherite", ["256 FE/t, and it holds a lot more power than the emerald one."], ["diamond_to_netherite"]),
    gg("gg_netherstar", "netherstar", [
        "Burns &enether stars&r for 4,092 FE/t. Wither farm, meet power plant.",
    ], ["netherite_to_netherstar"], rewards=[{"xp": 25}, {"crate": "lantern"}]),
    gg("gg_honey", "honey", ["Drinks honey and makes 64 FE/t. A beehive full of bees is a power station."],
       ["culinary_to_honey"]),
    gg("gg_potion", "potion", ["Burns potions. A use for the ones you were never going to drink."], ["culinary_to_potion"]),
    gg("gg_magmatic", "magmatic", ["Drinks lava for 40 FE/t. Pipe it from a Nether lake and it never stops."],
       ["obsidian_to_magmatic"]),
    gg("gg_enchantment", "enchantment", ["Burns enchanted books. Every unwanted Bane of Arthropods finally pays its way."],
       ["obsidian_to_enchantment"]),
    gg("gg_ender", "ender", ["Burns ender pearls for 96 FE/t, or eyes of ender, which last twice as long at 80."],
       ["obsidian_to_ender"], optional=False),
    gg("gg_halitosis", "halitosis", [
        "Burns the Ender Dragon's breath, bottled, for 128 FE/t. Each bottle lasts a long time.",
    ], ["ender_to_halitosis"], optional=False, shape="hexagon", rewards=[{"xp": 25}, {"crate": "hearth"}]),
    side("gg_8x", "Eight in One", [
        "Eight generators of a kind around an &eecho shard&r press into one &e8x generator&r. Saves a lot of floor space.",
    ], {"any": [f"generatorgalore:{g}_generator_8x" for g in (
        "copper", "iron", "gold", "diamond", "emerald", "obsidian", "netherite", "netherstar", "culinary",
        "honey", "potion", "magmatic", "enchantment", "ender", "halitosis")],
        "title": "Any 8x generator", "icon": "generatorgalore:iron_generator_8x"},
        icon="generatorgalore:iron_generator_8x"),
    side("gg_64x", "Sixty-Four in One", [
        "And eight of those around a &econduit&r make a &e64x generator&r.",
    ], {"any": [f"generatorgalore:{g}_generator_64x" for g in (
        "copper", "iron", "gold", "diamond", "emerald", "obsidian", "netherite", "netherstar", "culinary",
        "honey", "potion", "magmatic", "enchantment", "ender", "halitosis")],
        "title": "Any 64x generator", "icon": "generatorgalore:iron_generator_64x"},
        icon="generatorgalore:iron_generator_64x"),
]

FURNACES = [
    furnace("if_silver", "silver", "Silver Furnace", ["Another road to gold. Built around a copper or iron furnace."],
            ["upgrade_silver", "upgrade_silver2"]),
    furnace("if_gold", "gold", "Golden Furnace", ["Faster again. Built around an iron or silver furnace."],
            ["upgrade_gold", "upgrade_gold2"], optional=False),
    furnace("if_diamond", "diamond", "Diamond Furnace", ["Built around a golden furnace. From here the line splits."],
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

POWAH = [
    powah("p_battery", "Battery", [
        "A &eBattery&r charges the gear in your inventory while you carry it. Shift-click one into an Ender Cell to grow its channel.",
    ], "battery"),
    powah("p_hopper", "Energy Hopper", [
        "An &eEnergy Hopper&r charges the items inside the chest or other inventory it touches. Drop your tools in overnight.",
    ], "energy_hopper"),
    powah("p_discharger", "Energy Discharger", [
        "The reverse: an &eEnergy Discharger&r drains power out of charged items and holds it, for cables to carry off.",
    ], "energy_discharger"),
    powah("p_magmator", "Magmator", [
        "A &eMagmator&r burns hot fluids like lava for power. Better tiers burn faster and make more.",
    ], "magmator"),
    powah("p_furnator", "Furnator", [
        "The &eFurnator&r burns coal, wood and other furnace fuel. Better tiers burn faster and make more from each piece.",
    ], "furnator"),
    powah("p_solar", "Solar Panel", [
        "A &eSolar Panel&r makes power in daylight. Anything blocking the sky above it stops it.",
        "",
        "A &eLens of Ender&r fitted to a panel lets it see through blocks, so you can bury it under a floor.",
    ], "solar_panel"),
    powah("p_transmitter", "Player Transmitter", [
        "A &ePlayer Transmitter&r charges your gear wherever you are in the same dimension, armor and off hand included.",
        "",
        "It takes a &eBinding Card&r: right-click it to bind it to yourself, then slot it in. A Dimensional Binding Card works from anywhere.",
    ], "player_transmitter"),
    powah("p_ender_cell", "Ender Cell", [
        "An &eEnder Cell&r stores power in a channel of your own Ender Network. Every cell on that channel shares it, wherever it is in the world.",
    ], "ender_cell"),
    powah("p_ender_gate", "Ender Gate", [
        "An &eEnder Gate&r moves power between the block it touches and your Ender Network. Unlike a cell, it can't add capacity.",
    ], "ender_gate"),
    rod("hardened", ["A hardened capacitor around a basic rod. Faster again."]),
    rod("blazing", ["The blazing tier's rod. Swap a few in and watch the orb speed up."]),
    rod("niotic", ["Niotic rods move power into the orb faster still."]),
    rod("spirited", ["Spirited rods. By now a single orb can keep a whole base supplied."]),
    rod("nitro", ["The fastest rods there are."]),
    side("nitro", "Nitro Crystal", [
        "The top tier. A nether star, two redstone blocks and a block of blazing crystal, energized, come out as sixteen &eNitro Crystals&r.",
        "",
        "It takes 20 million FE, so a ring of good rods earns its keep here.",
    ], {"item": "powah:crystal_nitro"}, subtitle="Nitro tier", shape="hexagon", optional=False,
        rewards=[{"xp": 25}, {"crate": "lantern"}]),
]

FLUX = [
    side("flux_herculean", "Herculean Flux Storage", ["16 million FE for the network."],
         {"item": "fluxnetworks:herculean_flux_storage"}),
    side("flux_gargantuan", "Gargantuan Flux Storage", ["128 million FE. That's a lot of jetpack."],
         {"item": "fluxnetworks:gargantuan_flux_storage"}),
]

CHARGING = [
    side("wc_advanced_player", "Advanced Player Charger", [
        "The advanced &eWireless Player Charger&r reaches farther and charges faster.",
    ], {"item": "wirelesschargers:advanced_wireless_player_charger"}),
    side("wc_block", "Wireless Block Charger", [
        "A &eWireless Block Charger&r powers the machines around it, no cables needed.",
    ], {"item": "wirelesschargers:basic_wireless_block_charger"}),
    side("wc_advanced_block", "Advanced Block Charger", [
        "The advanced block charger covers a bigger area, faster.",
    ], {"item": "wirelesschargers:advanced_wireless_block_charger"}),
]

CHAPTER = {
    "file": "sparks",
    "group": "hum",
    "title": "Sparks",
    "subtitle": "From a coal generator to a reactor, carried anywhere",
    "icon": "powah:energizing_orb",
    # One line per mod, so a furnace upgrade never waits on a flux network.
    "layout": {
        "lines": [
            # Generator Galore: each generator, upgraded in place from the one before.
            {"spine": ["start", "gg_upgrade", "gg_gold", "gg_diamond", "gg_obsidian", "gg_ender", "gg_halitosis"],
             "branches": {
                 "start": {"up": ["gg_8x", "gg_64x"]},
                 "gg_gold": {"up": ["gg_other", "gg_honey"], "down": ["gg_potion"]},
                 "gg_diamond": {"up": ["gg_emerald"], "down": ["gg_netherite", "gg_netherstar"]},
                 "gg_obsidian": {"up": ["gg_magmatic"], "down": ["gg_enchantment"]},
             }},
            # Iron Furnaces: each tier, with the augments hung off the tiers that suit them.
            {"spine": ["iron_furnace", "if_gold", "if_diamond", "if_obsidian", "if_netherite", "if_allthemodium",
                       "if_vibranium", "if_unobtainium"],
             "branches": {
                 "iron_furnace": {"up": ["if_silver"]},
                 "if_gold": {"up": ["aug_speed", "aug_fuel"], "down": ["aug_blasting", "aug_smoking"]},
                 "if_diamond": {"up": ["if_emerald"], "down": ["if_crystal"]},
                 "if_obsidian": {"up": ["gen_augment"], "down": ["aug_factory"]},
                 "if_netherite": {"up": ["if_rainbow"], "down": ["if_heater"]},
             }},
            # Powah: a tier ladder. Each tier's rod sits above it, and the machines it opens up below.
            {"spine": ["cables", "cell", "orb", "steel", "blazing", "niotic", "spirited", "nitro", "reactor"],
             "branches": {
                 "cables": {"up": ["wrench"]},
                 "cell": {"up": ["p_battery"], "down": ["p_hopper", "p_discharger"]},
                 "orb": {"up": ["rods_basic"], "down": ["thermo", "p_magmator"]},
                 "steel": {"up": ["p_rod_hardened"], "down": ["p_furnator", "p_solar"]},
                 "blazing": {"up": ["p_rod_blazing"], "down": ["p_transmitter"]},
                 "niotic": {"up": ["p_rod_niotic"], "down": ["p_ender_cell", "p_ender_gate"]},
                 "spirited": {"up": ["p_rod_spirited"]},
                 "nitro": {"up": ["p_rod_nitro"]},
             }},
            # Flux Networks.
            {"spine": ["flux_dust", "flux_link", "flux_controller", "flux_storage", "flux_herculean",
                       "flux_gargantuan"]},
            # Charging your gear.
            {"spine": ["charging_station", "charger", "wc_advanced_player"],
             "branches": {"charger": {"down": ["wc_block", "wc_advanced_block"]}}},
        ],
    },
    "quests": [
        {
            "key": "start", "title": "Sparks",
            "shape": "hexagon", "size": 1.5, "icon": "generatorgalore:copper_generator",
            "desc": [
                "Machines want power, measured in FE. Every bit of it starts with a generator.",
                "",
                "The &eCopper Generator&r burns coal and other furnace fuel. Powah's &eFurnator&r does the same job.",
                "",
                "Feed it, connect it to a machine, and you've got a spark. This chapter has a line each for Generator Galore, Iron Furnaces, Powah, Flux Networks and charging your gear.",
            ],
            "tasks": [{"any": ["generatorgalore:copper_generator", "powah:furnator_starter"],
                       "title": "A Copper Generator or a Furnator", "icon": "generatorgalore:copper_generator"}],
            "rewards": [{"xp": 10}, {"crate": "kindling", "count": 2}, {"item": "minecraft:coal", "count": 32}],
        },
        {
            "key": "gg_upgrade", "title": "Turn It Up",
            "icon": "generatorgalore:iron_generator",
            "desc": [
                "No need to tear out your generator to get a better one. Right-click a placed one with an upgrade, such as &eCopper to Iron Upgrade&r, and it changes on the spot.",
                "",
                "An &eIron Generator&r makes 16 FE/t, twice the copper one. Each tier on this line climbs from there.",
            ],
            "tasks": [{"any": ["generatorgalore:iron_generator", "generatorgalore:copper_to_iron_upgrade"],
                       "title": "An iron generator, or the upgrade to one", "icon": "generatorgalore:iron_generator"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "gg_other", "title": "Odd Fuels", "optional": True,
            "icon": "generatorgalore:culinary_generator",
            "desc": [
                "Generator Galore has generators for things other than coal. The first is the &eCulinary Generator&r: it eats food.",
                "",
                "It's a Gold Generator with a cake, crops, eggs and redstone around it, or a Gold to Culinary Upgrade on a placed one. Honey and potion generators grow from it.",
            ],
            "tasks": [{"any": ["generatorgalore:culinary_generator", "generatorgalore:gold_to_culinary_upgrade"],
                       "title": "A culinary generator, or the upgrade to one", "icon": "generatorgalore:culinary_generator"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "cables", "title": "Carry the Current", "shape": "hexagon",
            "desc": [
                "Power needs a road. Powah's &eEnergy Cables&r carry it from generators to machines.",
                "",
                "Nearly every Powah recipe starts with &eDielectric Paste&r: three coal, two clay balls and a bucket of lava make a big batch.",
                "",
                "Pipez &eEnergy Pipes&r work too, if you'd rather match your item pipes.",
                "",
                "This line climbs Powah's tiers: starter, basic, hardened, blazing, niotic, spirited and nitro. Each tier's rod sits above it and the machines it opens up below.",
            ],
            "tasks": [{"any": ["powah:energy_cable_starter", "pipez:energy_pipe"], "count": 8,
                       "title": "8 energy cables or pipes", "icon": "powah:energy_cable_starter"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}, {"item": "powah:dielectric_paste", "count": 16}],
        },
        {
            "key": "wrench", "title": "Powah Wrench", "optional": True,
            "desc": [
                "The &eWrench&r has three modes.",
                "",
                "&eConfig&r changes which way a cable sends power. &eLink&r ties blocks together, like an Energizing Orb and its rods. &eRotate&r turns blocks to face the way you want.",
                "",
                "You won't need it often, but when you do, nothing else will do.",
            ],
            "tasks": [{"item": "powah:wrench"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "cell", "title": "Store It Up",
            "desc": [
                "Generators make power whether or not you're using it. An &eEnergy Cell&r saves the extra for later.",
                "",
                "Put one between your generators and machines. It fills up overnight and covers the busy moments when everything runs at once.",
                "",
                "Higher tiers hold more, and you can build each tier out of cells from the one before.",
                "",
                "Shift-click a cell into an &eEnder Cell&r's screen and it adds its capacity to that Ender Network channel.",
            ],
            "tasks": [{"item": "powah:energy_cell_starter"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "charging_station", "title": "Power to the Gadgets", "shape": "hexagon",
            "desc": [
                "Gadgets run on FE. If you don't have a power setup yet, the &eCharging Station&r is the easy way.",
                "",
                "Feed it furnace fuel, like coal, and put a gadget in to charge. Coal blocks burn longest.",
                "",
                "Later on, any machine or cell that charges items will top up a gadget too.",
            ],
            "tasks": [{"item": "charginggadgets:charging_station"}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}, {"item": "minecraft:coal_block", "count": 8}],
        },
        {
            "key": "charger", "title": "Charge on the Go",
            "desc": [
                "A &eWireless Player Charger&r tops up the powered gear of anyone standing near it: tools, armor, jetpacks, anything that holds FE.",
                "",
                "Put one by your front door, feed it power, and never think about batteries again.",
            ],
            "tasks": [{"any": ["wirelesschargers:basic_wireless_player_charger",
                               "wirelesschargers:advanced_wireless_player_charger"],
                       "title": "A wireless player charger", "icon": "wirelesschargers:basic_wireless_player_charger"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "iron_furnace", "title": "Iron Furnaces", "shape": "hexagon",
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
        {
            "key": "orb", "title": "The Energizing Orb",
            "shape": "hexagon",
            "desc": [
                "An &eEnergizing Orb&r does nothing alone. Place &eEnergizing Rods&r within four blocks of it, set them on cables so they get power, and right-click your ingredients into the orb. More rods, and better ones, means faster crafting.",
                "",
                "The orb itself needs no power. Right-click it with an empty hand to take things back out.",
                "",
                "Most of Powah's better parts are made here. Press &eU&r on the orb to see what it can make.",
            ],
            "tasks": [{"item": "powah:energizing_orb"}, {"item": "powah:energizing_rod_starter"}],
            "rewards": [{"xp": 25}, {"crate": "lantern"}, {"item": "powah:energizing_rod_starter", "count": 2}],
        },
        {
            "key": "rods_basic", "title": "Better Rods",
            "desc": [
                "Each rod tier passes power to the orb faster, so a few good rods beat a ring of starter ones.",
                "",
                "Craft a &eBasic Energizing Rod&r from a starter rod, then keep climbing as you make better crystals.",
            ],
            "tasks": [{"item": "powah:energizing_rod_basic"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "thermo", "title": "Hot and Cold", "optional": True, "icon": "powah:thermo_generator_starter",
            "desc": [
                "A &eThermo Generator&r sits on top of something hot, like lava, and makes power as long as you give it a coolant such as water.",
                "",
                "No fuel to shovel. Pipe water in and it hums along on its own. Every Powah generator comes in all seven tiers, and any tier counts here.",
            ],
            "tasks": [{"any": ["powah:thermo_generator_starter", "powah:thermo_generator_basic",
                               "powah:thermo_generator_hardened", "powah:thermo_generator_blazing",
                               "powah:thermo_generator_niotic", "powah:thermo_generator_spirited",
                               "powah:thermo_generator_nitro"],
                       "title": "Any thermo generator", "icon": "powah:thermo_generator_starter"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "steel", "title": "Energized Steel", "subtitle": "Hardened tier",
            "desc": [
                "Your first energizing recipe: an iron ingot and a gold ingot in the orb come out as two &eEnergized Steel&r.",
                "",
                "Wrapped around a large basic capacitor, it makes a &eHardened Capacitor&r: the key to Powah's hardened tier.",
            ],
            "tasks": [{"item": "powah:steel_energized", "count": 8}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "blazing", "title": "Blazing Crystal", "subtitle": "Blazing tier",
            "shape": "hexagon",
            "desc": [
                "A blaze rod, or four blaze powder, energized into a &eBlazing Crystal&r.",
                "",
                "It's the key to Powah's blazing tier: stronger generators, cells, cables and rods. Each crystal after this one unlocks the next tier the same way.",
            ],
            "tasks": [{"item": "powah:crystal_blazing"}],
            "rewards": [{"xp": 25}, {"crate": "lantern"}, {"item": "powah:energy_cable_basic", "count": 12}],
        },
        {
            "key": "niotic", "title": "Niotic Crystal", "subtitle": "Niotic tier",
            "desc": [
                "A diamond, energized. Takes a good deal more power than a blazing crystal, so it's a fair test of your rods.",
                "",
                "Niotic parts make the tier after blazing.",
            ],
            "tasks": [{"item": "powah:crystal_niotic"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "spirited", "title": "Spirited Crystal", "subtitle": "Spirited tier",
            "desc": [
                "An emerald, energized, and hungrier still.",
                "",
                "Spirited parts make the tier after niotic.",
            ],
            "tasks": [{"item": "powah:crystal_spirited"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "flux_dust", "title": "Flux Dust", "shape": "hexagon",
            "desc": [
                "Flux Networks starts in an odd place: the bottom of the world.",
                "",
                "Set a block of obsidian on top of bedrock, drop some redstone on it, and left-click the obsidian. The redstone gets crushed into &eFlux Dust&r.",
                "",
                "Bring plenty of redstone. You'll want a lot of dust.",
            ],
            "tasks": [{"item": "fluxnetworks:flux_dust", "count": 16}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "flux_link", "title": "Link Two Bases",
            "shape": "hexagon",
            "desc": [
                "A &eFlux Plug&r takes power from whatever it touches. A &eFlux Point&r gives power to whatever it touches. Put both on the same network, and power jumps between them however far apart they are.",
                "",
                "Right-click a flux block to make a network or pick one. You can have up to five.",
                "",
                "Flux can't keep chunks loaded here, so force-load both ends with the claim map (&eM&r, then &eShift&r-drag).",
            ],
            "tasks": [{"item": "fluxnetworks:flux_plug"}, {"item": "fluxnetworks:flux_point"}],
            "rewards": [{"xp": 25}, {"crate": "lantern"}, {"item": "fluxnetworks:flux_dust", "count": 32}],
        },
        {
            "key": "flux_storage", "title": "A Battery for the Network", "optional": True,
            "desc": [
                "&eFlux Storage&r holds power for the whole network and evens out the peaks.",
                "",
                "The &eBasic Flux Storage&r holds 2 million FE.",
            ],
            "tasks": [{"item": "fluxnetworks:basic_flux_storage"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "flux_controller", "title": "Charge from Anywhere",
            "desc": [
                "A &eFlux Controller&r turns on wireless charging for its network: the powered gear of the players on that network gets topped up from it.",
                "",
                "Pair it with a big flux storage and your jetpack never runs dry.",
            ],
            "tasks": [{"item": "fluxnetworks:flux_controller"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "reactor", "title": "Reactor",
            "shape": "hexagon", "size": 1.5,
            "desc": [
                "Powah's &eReactor&r is a big generator built from 36 reactor blocks. Hold all of them and place one where there's open room, 3 blocks across and 4 tall: the reactor builds itself.",
                "",
                "It runs on &eUraninite&r. Energize uranium ingots in the orb to make it, both for the blocks and for fuel.",
                "",
                "Wire it into a flux network and your whole world has power. Higher tiers of reactor make much more.",
            ],
            "tasks": [{"item": "powah:reactor_starter", "count": 36}],
            "rewards": [{"xp": 50}, {"crate": "ember"}, {"item": "powah:energizing_rod_hardened", "count": 2}],
        },
    ] + GENERATORS + FURNACES + POWAH + FLUX + CHARGING,
}
