def ladder(key, title, task, lines, icon=None, optional=True, crate="kindling"):
    """A short catalog quest: one variant or one rung of a ladder, optional by default."""
    q = {"key": key, "title": title, "desc": lines, "tasks": [task], "rewards": [{"xp": 10}, {"crate": crate}]}
    if optional:
        q["optional"] = True
    if icon:
        q["icon"] = icon
    return q


def tagged(tag, title, icon):
    return {"tag": tag, "title": title, "icon": icon}


# Cable Tiers devices other than the Importer and Exporter (the grade ladder) and the
# Autocrafter (with the other autocrafters).
TIERED = [
    ("constructor", "Constructor", "Tiered Constructors",
     ["A faster Constructor that places blocks more often, with more filter slots."]),
    ("destructor", "Destructor", "Tiered Destructors",
     ["A faster Destructor. Put one in front of a cobblestone generator and watch the numbers climb."]),
    ("disk_interface", "Disk Interface", "Tiered Disk Interfaces",
     ["Empties and fills disks much faster, with more filter slots."]),
    ("interface", "Interface", "Tiered Interfaces",
     ["More slots and a bigger transfer quota, for feeding a hungry machine line."]),
]
CT_KINDS = ["importer", "exporter", "constructor", "destructor", "disk_interface", "interface", "autocrafter"]

CHAPTER = {
    "file": "refined_automation",
    "group": "hum",
    "title": "The Network at Work",
    "subtitle": "Importers and exporters, faster devices, upgrades and autocrafting",
    "icon": "refinedstorage:autocrafter",
    # Two ladders, Cable Tiers grades and autocrafters, with the devices and upgrades that need
    # no order in blocks between them.
    "layout": {
        "lines": [
            {"flow": ["io", "cable_tiers", "ct_ultra", "ct_mega"]},
            {"rows": ["external", "advanced_io", "constructor", "destructor", "interface", "disk_interface", "detector",
                      "storage_monitor", "relay", "network_link", "security"]
                     + [f"ct_{t[0]}" for t in TIERED],
             "per_row": 8},
            {"flow": ["pattern", "autocraft", "extra_crafter", "crafter_gold", "crafter_diamond", "crafter_netherite"],
             "branches": {"autocraft": {"up": ["manager"], "down": ["monitor"]}}},
            {"rows": ["upgrade", "speed", "stack", "regulator", "silk_touch", "fortune", "fortune_3",
                      "autocraft_upgrade", "fluid_sub", "neural", "ct_autocrafter"],
             "per_row": 11},
        ],
    },
    "quests": [
        # ---- automation -------------------------------------------------------
        {
            "key": "io", "title": "In and Out", "shape": "hexagon", "size": 1.5,
            "desc": [
                "An &eImporter&r pulls from whatever it faces into the network. An &eExporter&r pushes the items you choose back out. Between them they can feed furnaces, machines and farms.",
                "",
                "A &eRegulator Upgrade&r in an Exporter keeps a set amount in the target instead of emptying the network into it.",
            ],
            "tasks": [{"tag": "refinedstorage:importers", "title": "Any Importer", "icon": "refinedstorage:importer"},
                      {"tag": "refinedstorage:exporters", "title": "Any Exporter", "icon": "refinedstorage:exporter"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        ladder("advanced_io", "More Filters", {"any": ["extrastorage:advanced_importer", "extrastorage:advanced_exporter"],
                                               "title": "An Advanced Importer or Exporter",
                                               "icon": "extrastorage:advanced_exporter"}, [
            "ExtraStorage's &eAdvanced Importer&r and &eAdvanced Exporter&r are the plain ones with an Improved Processor and redstone torches, and many more filter slots.",
            "",
            "One advanced exporter can stock a whole row of machines.",
        ], icon="extrastorage:advanced_exporter"),
        {
            "key": "external", "title": "Bring Your Chests",
            "desc": [
                "Put an &eExternal Storage&r against a chest, barrel or drawer and its contents show up in the Grid. The network can fill it too.",
                "",
                "It's a gentle way to move in: keep your old storage and hook it up while you build disks.",
            ],
            "tasks": [{"tag": "refinedstorage:external_storages", "title": "Any External Storage",
                       "icon": "refinedstorage:external_storage"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        ladder("constructor", "Put It Down", tagged("refinedstorage:constructors", "Any Constructor",
                                                    "refinedstorage:constructor"), [
            "A &eConstructor&r places blocks from the network into the world in front of it. Set which block in its filter.",
            "",
            "It's built around a &eConstruction Core&r: a Basic Processor with glowstone dust.",
        ], icon="refinedstorage:constructor", crate="hearth"),
        ladder("destructor", "Pick It Up", tagged("refinedstorage:destructors", "Any Destructor",
                                                  "refinedstorage:destructor"), [
            "A &eDestructor&r breaks the block in front of it and sends it into the network. Pair one with a Constructor and the network can move blocks around on its own.",
            "",
            "Silk Touch and Fortune upgrades work in it, just like on a pickaxe.",
        ], icon="refinedstorage:destructor", crate="hearth"),
        ladder("interface", "The Interface", {"item": "refinedstorage:interface"}, [
            "An &eInterface&r combines importing and exporting, with slots in between. Hoppers and pipes put things in to store them, and pull out whatever you've set it to stock.",
        ], crate="hearth"),
        ladder("detector", "Ring a Bell", tagged("refinedstorage:detectors", "Any Detector", "refinedstorage:detector"), [
            "A &eDetector&r gives a redstone signal when the network holds more, less or exactly as much of something as you set.",
            "",
            "Switch a farm off when the stock is full, or a light on when the coal runs low.",
        ], icon="refinedstorage:detector"),
        ladder("storage_monitor", "On Display", {"item": "refinedstorage:storage_monitor"}, [
            "A &eStorage Monitor&r shows how much of one item the network holds, right on its face. Sneak and right-click it to choose the item.",
            "",
            "Left-click takes a stack out, and right-click puts things in. A row of them by the door works like a shop counter.",
        ]),
        ladder("disk_interface", "Disk Interface", tagged("refinedstorage:disk_interfaces", "Any Disk Interface",
                                                          "refinedstorage:disk_interface"), [
            "A &eDisk Interface&r moves resources between the network and the disks you put in it, in either direction.",
            "",
            "Use it to empty an old disk into the network, or to fill a disk with something to carry away.",
        ], icon="refinedstorage:disk_interface"),
        {
            "key": "relay", "title": "Branch Lines",
            "desc": [
                "A &eRelay&r passes the network on to the cables behind it, and redstone can switch it off. Use it to turn a whole wing of the network on or off.",
                "",
                "It can also pass along only some of the network, like its storage or its patterns, which makes a separate branch for a friend's base.",
            ],
            "tasks": [tagged("refinedstorage:relays", "Any Relay", "refinedstorage:relay")],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        ladder("network_link", "No Cables Required", {"item": "refinedstorage:network_transmitter"}, [
            "A &eNetwork Transmitter&r and a &eNetwork Receiver&r carry the network between two places with no cable between them. Pair them with a &eNetwork Card&r bound to the receiver.",
            "",
            "Each one takes a netherite ingot, so they're not cheap. For a base on the other side of the mountain, they're worth it.",
        ]),
        ladder("security", "Who Goes There", tagged("refinedstorage:security_managers", "Any Security Manager",
                                                    "refinedstorage:security_manager"), [
            "Playing with friends? A &eSecurity Manager&r locks the network down: once it's on, nobody can use it until you add a &eSecurity Card&r for them.",
            "",
            "Each card sets what one player may do. A Fallback Security Card covers everyone else.",
        ], icon="refinedstorage:security_manager"),
        # ---- Cable Tiers ------------------------------------------------------
        {
            "key": "cable_tiers", "title": "Faster Hands", "shape": "hexagon",
            "desc": [
                "Cable Tiers makes faster Importers, Exporters, Constructors, Destructors, Disk Interfaces and Interfaces, in three grades: &eElite&r, &eUltra&r and &eMega&r.",
                "",
                "An Elite device is four of the plain one around an Advanced Processor, with iron blocks. Each grade after that is built from four of the one before.",
            ],
            "tasks": [{"any": ["cabletiers:elite_importer", "cabletiers:elite_exporter", "cabletiers:ultra_importer",
                               "cabletiers:ultra_exporter", "cabletiers:mega_importer", "cabletiers:mega_exporter"],
                       "title": "Any tiered Importer or Exporter", "icon": "cabletiers:elite_importer"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
    ] + [
        ladder(f"ct_{kind}", title, {"any": [f"cabletiers:{t}_{kind}" for t in ("elite", "ultra", "mega")],
                                     "title": f"An Elite, Ultra or Mega {name}", "icon": f"cabletiers:elite_{kind}"},
               lines, icon=f"cabletiers:elite_{kind}")
        for kind, name, title, lines in TIERED
    ] + [
        ladder("ct_ultra", "Ultra Grade", {"any": [f"cabletiers:ultra_{k}" for k in CT_KINDS],
                                           "title": "Any Ultra device", "icon": "cabletiers:ultra_importer"}, [
            "&eUltra&r devices are four Elite ones with diamond blocks and an Advanced Processor.",
        ], icon="cabletiers:ultra_importer", crate="hearth"),
        ladder("ct_mega", "Mega Grade", {"any": [f"cabletiers:mega_{k}" for k in CT_KINDS],
                                         "title": "Any Mega device", "icon": "cabletiers:mega_importer"}, [
            "&eMega&r is the top: four Ultra devices, netherite blocks and a &edragon head&r. The heads hang on the prows of End ships.",
        ], icon="cabletiers:mega_importer", crate="hearth"),
        # ---- upgrades ---------------------------------------------------------
        {
            "key": "upgrade", "title": "A Blank Upgrade", "shape": "hexagon",
            "desc": [
                "Every upgrade starts as a plain &eUpgrade&r: Quartz Enriched Iron and glass around an Improved Processor.",
                "",
                "Importers, Exporters, Constructors, Destructors and more have slots for them.",
            ],
            "tasks": [{"item": "refinedstorage:upgrade"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        ladder("speed", "Speed Upgrade", {"item": "refinedstorage:speed_upgrade"}, [
            "Sugar and an Upgrade make a &eSpeed Upgrade&r. The device works more often, and draws a little more power.",
        ]),
        ladder("stack", "Stack Upgrade", {"item": "refinedstorage:stack_upgrade"}, [
            "Speed Upgrades and sugar make a &eStack Upgrade&r: the device handles far more per operation.",
        ]),
        ladder("regulator", "Regulator Upgrade", {"item": "refinedstorage:regulator_upgrade"}, [
            "In an Exporter, a &eRegulator Upgrade&r only exports while the target holds less than you set. In an Importer, it only imports while the target holds more.",
            "",
            "Use the upgrade in your hand to set the amount.",
        ]),
        ladder("silk_touch", "Silk Touch Upgrade", {"item": "refinedstorage:silk_touch_upgrade"}, [
            "An Upgrade with a Silk Touch book makes a &eSilk Touch Upgrade&r. In a Destructor, it picks blocks up whole, like a Silk Touch pickaxe.",
        ]),
        ladder("fortune", "Fortune Upgrade", {"any": ["refinedstorage:fortune_1_upgrade", "refinedstorage:fortune_2_upgrade",
                                                      "refinedstorage:fortune_3_upgrade"],
                                              "title": "Any Fortune Upgrade", "icon": "refinedstorage:fortune_1_upgrade"}, [
            "Fortune books make &eFortune Upgrades&r, one for each level. In a Destructor they work like a Fortune pickaxe.",
        ], icon="refinedstorage:fortune_1_upgrade"),
        ladder("fortune_3", "The Best of Luck", {"item": "refinedstorage:fortune_3_upgrade"}, [
            "A Fortune III book makes the best one. Put it on a Destructor facing an ore block and see what comes out.",
        ], icon="refinedstorage:fortune_3_upgrade"),
    ] + [
        # ---- autocrafting -----------------------------------------------------
        {
            "key": "pattern", "title": "Write It Down", "shape": "hexagon",
            "desc": [
                "Autocrafting starts with &ePatterns&r. Put a blank one in a &ePattern Grid&r, lay out a recipe and encode it.",
                "",
                "Crafting patterns cover anything from a crafting table. Processing patterns are for machines: you list what goes in and what should come back out.",
                "",
                "Fuzzy mode lets a pattern accept alternatives, like any kind of plank.",
            ],
            "tasks": [{"tag": "refinedstorage:pattern_grids", "title": "Any Pattern Grid",
                       "icon": "refinedstorage:pattern_grid"},
                      {"item": "refinedstorage:pattern", "count": 4}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "autocraft", "title": "Autocrafting", "shape": "hexagon",
            "desc": [
                "Put a Pattern in an &eAutocrafter&r and that item shows up in the Grid as craftable, even with none in stock. Ask for any amount and the network works out the rest, sub-recipes included.",
                "",
                "For a processing pattern, face the Autocrafter at the machine that does the work. Autocrafters facing each other form a chain, so one machine can serve many patterns.",
            ],
            "tasks": [{"tag": "refinedstorage:autocrafters", "title": "Any Autocrafter",
                       "icon": "refinedstorage:autocrafter"}],
            "rewards": [{"xp": 25}, {"crate": "lantern"}, {"item": "refinedstorage:quartz_enriched_iron", "count": 16}],
        },
        {
            "key": "autocraft_upgrade", "title": "Never Run Out",
            "desc": [
                "An &eAutocrafting Upgrade&r in an Exporter starts a craft whenever something it should export is missing.",
                "",
                "Pair it with a Regulator Upgrade and a chest of torches, or a machine's input, stays topped up forever.",
            ],
            "tasks": [{"item": "refinedstorage:autocrafting_upgrade"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "fluid_sub", "title": "Buckets Not Included",
            "desc": [
                "Recipes that call for a water or lava bucket normally need a real filled bucket in storage.",
                "",
                "A &eFluid Substitution Pattern&r, a Pattern between two buckets, lets autocrafting use the stored fluid instead.",
            ],
            "tasks": [{"item": "refinedfluidsubstitution:fluid_substitution_pattern"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        ladder("monitor", "Watch It Work", tagged("refinedstorage:autocrafting_monitors", "Any Autocrafting Monitor",
                                                   "refinedstorage:autocrafting_monitor"), [
            "The &eAutocrafting Monitor&r shows every craft the network is working on, and lets you cancel one that's stuck.",
            "",
            "When a big order stalls, look here first.",
        ], icon="refinedstorage:autocrafting_monitor"),
        {
            "key": "manager", "title": "Every Pattern in One Place",
            "desc": [
                "The &eAutocrafter Manager&r lists the patterns in every Autocrafter on the network, with a search box.",
                "",
                "Add and remove patterns from one screen instead of walking from crafter to crafter.",
            ],
            "tasks": [tagged("refinedstorage:autocrafter_managers", "Any Autocrafter Manager",
                             "refinedstorage:autocrafter_manager")],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "extra_crafter", "title": "Bigger Autocrafters", "icon": "extrastorage:iron_crafter",
            "desc": [
                "More patterns than slots? Time to upgrade.",
                "",
                "ExtraStorage's &eIron Autocrafter&r is an Autocrafter with iron and a chest around it, and it holds more patterns and works faster. Each tier after it is built around the one before.",
                "",
                "Hover one and hold Shift to see its slots and speed.",
            ],
            "tasks": [{"item": "extrastorage:iron_crafter"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        ladder("neural", "Neural Processor", {"item": "extrastorage:neural_processor"}, [
            "The better ExtraStorage crafters need a &eNeural Processor&r: raw improved and advanced processors, quartz, obsidian and a crafting table around a Processor Binding, then smelted.",
        ]),
        ladder("crafter_gold", "Gold Autocrafter", {"item": "extrastorage:gold_crafter"}, [
            "An Iron Autocrafter with gold blocks and Neural Processors. More slots, more speed.",
        ]),
        ladder("crafter_diamond", "Diamond Autocrafter", {"item": "extrastorage:diamond_crafter"}, [
            "Diamond blocks this time, around a Gold Autocrafter.",
        ]),
        ladder("crafter_netherite", "Netherite Autocrafter", {"item": "extrastorage:netherite_crafter"}, [
            "The biggest of ExtraStorage's crafters, built around a Diamond one with netherite blocks.",
        ], crate="hearth"),
        ladder("ct_autocrafter", "Tiered Autocrafters", {"any": [f"cabletiers:{t}_autocrafter" for t in ("elite", "ultra", "mega")],
                                                         "title": "An Elite, Ultra or Mega Autocrafter",
                                                         "icon": "cabletiers:elite_autocrafter"}, [
            "Cable Tiers makes Autocrafters too, in Elite, Ultra and Mega. They're faster than a plain one and take more patterns.",
            "",
            "Their menu has an import mode, so a tiered crafter facing a machine can pull back what it made.",
        ], icon="cabletiers:elite_autocrafter"),
    ],
}
