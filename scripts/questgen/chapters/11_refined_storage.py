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


# Bigger item disks: ExtraStorage and Extra Disks both make them, and Refined Storage's size tags
# accept either.
BIG_ITEM_DISKS = [
    ("disk_1024k", "1024k Storage Disk", "1024k", "extradisks:1024k_item_storage_disk",
     ["Four times the 256k. Each step up takes three parts of the size below and four Advanced Processors."]),
    ("disk_4096k", "4096k Storage Disk", "4096k", "extradisks:4096k_item_storage_disk",
     ["Four million items on one disk. Most bases never fill one."]),
    ("disk_16384k", "16384k Storage Disk", "16384k", "extradisks:16384k_item_storage_disk",
     ["The largest disk ExtraStorage makes. Extra Disks keeps going."]),
    ("disk_65536k", "65536k Storage Disk", "65536k", "extradisks:65536k_item_storage_disk",
     ["From here on the disks come only from Extra Disks."]),
    ("disk_262144k", "262m Storage Disk", "262144k", "extradisks:262144k_item_storage_disk",
     ["Two hundred and sixty-two million items. At this point it's a matter of pride."]),
    ("disk_1048576k", "1048m Storage Disk", "1048576k", "extradisks:1048576k_item_storage_disk",
     ["The last disk with a number on it. The next one doesn't need one."]),
]

FLUID_DISKS = [
    ("fluid_256b", "256B Fluid Storage Disk", "refinedstorage:256b_fluid_storage_disk",
     ["Each Fluid Storage Part is three parts of the size below, a bucket, a Quartz Enriched Iron and four processors."]),
    ("fluid_1024b", "1024B Fluid Storage Disk", "refinedstorage:1024b_fluid_storage_disk",
     ["A thousand buckets. Enough lava to run a generator for a long while."]),
    ("fluid_4096b", "4096B Fluid Storage Disk", "refinedstorage:4096b_fluid_storage_disk",
     ["The biggest fluid disk Refined Storage makes on its own."]),
]
BIG_FLUID_DISKS = [
    ("fluid_16384b", "16384B Fluid Storage Disk", "16384b", "extradisks:16384b_fluid_storage_disk",
     ["Past 4096 buckets, ExtraStorage and Extra Disks take over, just as they do for items."]),
    ("fluid_65536b", "65536B Fluid Storage Disk", "65536b", "extradisks:65536b_fluid_storage_disk",
     ["Sixty-five thousand buckets: a lake's worth, near enough."]),
    ("fluid_262144b", "262kB Fluid Storage Disk", "262144b", "extradisks:262144b_fluid_storage_disk",
     ["For the refineries and reactors that drink fluid by the thousand buckets."]),
    ("fluid_1048576b", "1048kB Fluid Storage Disk", "1048576b", "extradisks:1048576b_fluid_storage_disk",
     ["A million buckets, and one step short of the end."]),
]

# Cable Tiers devices other than the Importer and Exporter (the line's first quest) and the
# Autocrafter (on the autocrafting line).
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
    "file": "refined_storage",
    "group": "hum",
    "title": "Refined Storage",
    "subtitle": "One network for everything: disks, grids, autocrafting, wireless access and chemicals",
    "icon": "refinedstorage:controller",
    # Eight tracks: the core network, item disks, fluid and other disks, autocrafting, wireless,
    # automation, Cable Tiers and upgrades. Only the first needs doing before the others.
    "layout": {
        "lines": [
            {"spine": ["rs_start", "proc_basic", "proc_improved", "processors", "controller", "drive", "grid",
                       "crafting_grid"],
             "branches": {
                 "rs_start": {"up": ["wrench"]},
                 "controller": {"down": ["cable"]},
                 "drive": {"down": ["portable_grid"]},
             }},
            {"spine": ["disk_4k", "disk_16k", "disk_64k", "big_disks"] + [d[0] for d in BIG_ITEM_DISKS]
                      + ["disk_infinite"],
             "branches": {
                 "disk_4k": {"up": ["housing"], "down": ["storage_block"]},
                 "disk_65536k": {"up": ["adv_housing"]},
                 "disk_infinite": {"up": ["withering"]},
             }},
            {"spine": ["fluid_disk"] + [d[0] for d in FLUID_DISKS] + [d[0] for d in BIG_FLUID_DISKS]
                      + ["fluid_infinite"],
             "branches": {
                 "fluid_disk": {"down": ["chemicals", "energy"]},
                 "fluid_256b": {"down": ["chem_big"]},
             }},
            {"spine": ["pattern", "autocraft", "manager", "extra_crafter", "crafter_gold", "crafter_diamond",
                       "crafter_netherite"],
             "branches": {
                 "autocraft": {"up": ["autocraft_upgrade", "fluid_sub"], "down": ["monitor"]},
                 "extra_crafter": {"up": ["neural"], "down": ["ct_autocrafter"]},
             }},
            {"spine": ["wireless", "range", "wireless_crafting", "wireless_monitor", "universal", "interdim"],
             "branches": {
                 "wireless": {"up": ["wireless_upgrades"]},
             }},
            {"spine": ["io", "external", "constructor", "destructor", "interface", "detector", "disk_interface",
                       "relay"],
             "branches": {
                 "io": {"up": ["advanced_io"]},
                 "detector": {"up": ["storage_monitor"]},
                 "relay": {"up": ["network_link"], "down": ["security"]},
             }},
            {"spine": ["cable_tiers"] + [f"ct_{t[0]}" for t in TIERED] + ["ct_ultra", "ct_mega"]},
            {"spine": ["upgrade", "speed", "stack", "regulator", "silk_touch", "fortune"],
             "branches": {
                 "fortune": {"up": ["fortune_3"]},
             }},
        ],
    },
    "quests": [
        # ---- the core network -------------------------------------------------
        {
            "key": "rs_start", "title": "One Network for Everything",
            "shape": "hexagon", "size": 1.5, "icon": "refinedstorage:controller",
            "desc": [
                "Chests fill up. Then the chests need chests. Refined Storage puts everything you own into one network you can search, sort and craft from.",
                "",
                "Almost every part of it starts with &eQuartz Enriched Iron&r: three iron ingots and a piece of quartz make four.",
                "",
                "The top line builds the network itself. Each line below it is a separate track to follow once it's running.",
            ],
            "tasks": [{"item": "refinedstorage:quartz_enriched_iron", "count": 8}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        ladder("wrench", "The Wrench", {"item": "refinedstorage:wrench"}, [
            "A &eWrench&r rotates Refined Storage blocks. Sneak and use it to dismantle one, ready to move.",
            "",
            "It's Quartz Enriched Iron and a Basic Processor, and it saves a lot of breaking and replacing.",
        ]),
        {
            "key": "proc_basic", "title": "Printed Circuits",
            "desc": [
                "Processors start as a &eProcessor Binding&r, made from string and a slime ball. Add silicon, redstone and an iron ingot for a raw processor, then smelt it into a &eBasic Processor&r.",
                "",
                "&eSilicon&r is just quartz, smelted. One binding recipe makes eight, so string is rarely the problem.",
            ],
            "tasks": [{"item": "refinedstorage:basic_processor"}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}],
        },
        {
            "key": "proc_improved", "title": "Improved Processor",
            "desc": [
                "Swap the iron for a gold ingot and you get an &eImproved Processor&r.",
                "",
                "They go into upgrades, constructors and destructors, and the 16k storage part.",
            ],
            "tasks": [{"item": "refinedstorage:improved_processor"}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}],
        },
        {
            "key": "processors", "title": "Advanced Processor",
            "desc": [
                "A diamond makes the &eAdvanced Processor&r, the one the network's best parts ask for: wireless gear, crafting grids, the 64k part and up.",
                "",
                "Make a handful at a time. You'll be back for more.",
            ],
            "tasks": [{"item": "refinedstorage:advanced_processor"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}, {"item": "refinedstorage:basic_processor", "count": 4}],
        },
        {
            "key": "controller", "title": "The Controller",
            "desc": [
                "The &eController&r is the heart of the network. It takes power from any FE source and shares it with every device on the cables.",
                "",
                "No power, no network, so give it a steady supply before you build out. Every device draws a little, and a Disk Drive draws more for each disk in it.",
                "",
                "A big network that runs short can have more than one Controller.",
            ],
            "tasks": [{"tag": "refinedstorage:controllers", "title": "Any Controller", "icon": "refinedstorage:controller"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "cable", "title": "Run the Cables",
            "desc": [
                "&eCable&r links devices to each other. Six &eQuartz Enriched Copper&r, two glass and a redstone make twelve. The copper works like the iron: three ingots and a quartz.",
                "",
                "Dyed cable only joins cable of the same color or plain gray, so two networks can run side by side without merging.",
            ],
            "tasks": [{"tag": "refinedstorage:cables", "count": 12, "title": "12 Cable", "icon": "refinedstorage:cable"}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}],
        },
        {
            "key": "drive", "title": "Disks and Drives",
            "desc": [
                "A &eDisk Drive&r holds storage disks and adds their space to the network. A &e1k Storage Disk&r holds a thousand items of any kind.",
                "",
                "When you outgrow a disk, craft it with a bigger Storage Part to upgrade it. An empty disk used in your hand gives its part back.",
                "",
                "The second line is the whole disk ladder, from 4k to infinite.",
            ],
            "tasks": [{"item": "refinedstorage:disk_drive"}, {"item": "refinedstorage:1k_storage_disk"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        ladder("portable_grid", "Storage in a Box", {"item": "refinedstorage:portable_grid"}, [
            "A &ePortable Grid&r holds one storage disk and lets you use it with no network at all: two Grids and a Controller in a ring of Quartz Enriched Iron.",
            "",
            "Use it from your inventory, or sneak and place it as a block. It has its own small battery, so charge it now and then.",
        ], crate="hearth"),
        {
            "key": "grid", "title": "The Grid", "shape": "hexagon",
            "desc": [
                "Everything you store, in one window. Connect a &eGrid&r to the network and put things in or take them out from one place.",
                "",
                "The search box has tricks: start with &e@&r to search by mod, &e#&r by tag, or &e$&r by tooltip.",
                "",
                "A &eMachine Casing&r is eight Quartz Enriched Iron around a stone. The two cores are a Basic Processor with glowstone dust or with quartz.",
            ],
            "tasks": [{"tag": "refinedstorage:grids", "title": "Any Grid", "icon": "refinedstorage:grid"}],
            "rewards": [{"xp": 25}, {"crate": "lantern"}, {"item": "refinedstorage:advanced_processor", "count": 2}],
        },
        {
            "key": "crafting_grid", "title": "Craft in Place",
            "desc": [
                "A Grid, an Advanced Processor and a crafting table make a &eCrafting Grid&r: a Grid with a crafting area that pulls ingredients straight from storage.",
                "",
                "JEI's recipe transfer button fills it for you.",
            ],
            "tasks": [{"tag": "refinedstorage:crafting_grids", "title": "Any Crafting Grid",
                       "icon": "refinedstorage:crafting_grid"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        # ---- item disks -------------------------------------------------------
        {
            "key": "disk_4k", "title": "Room to Grow", "shape": "hexagon",
            "desc": [
                "Each Storage Part is three parts of the size below, a redstone, a Quartz Enriched Iron and four processors: Basic for 4k, Improved for 16k and Advanced for 64k.",
                "",
                "Put the part in a Storage Housing for a new disk, or craft it with an old disk to upgrade.",
            ],
            "tasks": [{"item": "refinedstorage:4k_storage_disk"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        ladder("housing", "Storage Housing", {"item": "refinedstorage:storage_housing"}, [
            "An empty &eStorage Housing&r is glass, redstone and Quartz Enriched Iron. Put any Storage Part in one and it becomes a disk.",
            "",
            "Making the housing and the part separately is handy when you keep spare parts around.",
        ]),
        ladder("storage_block", "Storage Blocks", tagged("refinedstorage:storage_blocks/items", "Any item Storage Block",
                                                         "refinedstorage:1k_storage_block"), [
            "No room for a Disk Drive? A Storage Part in a Machine Casing makes a &eStorage Block&r, which holds the same amount and joins the network like any other device.",
            "",
            "Use an empty one in your hand to get the part and the casing back.",
        ], icon="refinedstorage:1k_storage_block"),
        ladder("disk_16k", "16k Storage Disk", {"item": "refinedstorage:16k_storage_disk"}, [
            "Sixteen thousand items. The 16k part takes four Improved Processors.",
        ], optional=False, crate="hearth"),
        ladder("disk_64k", "64k Storage Disk", {"item": "refinedstorage:64k_storage_disk"}, [
            "The biggest disk Refined Storage makes on its own, built with Advanced Processors.",
            "",
            "A 64k disk also goes into the &eAllthemodium Alloy Paxel&r, so keep that in mind for later.",
        ], optional=False, crate="hearth"),
        {
            "key": "big_disks", "title": "Bigger Disks", "shape": "hexagon",
            "desc": [
                "64k not cutting it? Extra Disks and ExtraStorage both go far past it, starting at &e256k&r with parts built from 64k parts and Advanced Processors.",
                "",
                "Either mod's disk counts for the quests on this line, and they upgrade the same way.",
            ],
            "tasks": [{"tag": "refinedstorage:disks/items/256k", "title": "Any 256k Storage Disk",
                       "icon": "extradisks:256k_item_storage_disk"}],
            "rewards": [{"xp": 25}, {"crate": "lantern"}],
        },
    ] + [
        ladder(k, t, tagged(f"refinedstorage:disks/items/{size}", f"Any {t}", icon), lines, icon=icon)
        for k, t, size, icon, lines in BIG_ITEM_DISKS
    ] + [
        ladder("adv_housing", "Advanced Storage Housing", {"item": "extradisks:advanced_storage_housing"}, [
            "Extra Disks also makes an &eAdvanced Storage Housing&r, with Advanced and Improved Processors. Its big parts go into either housing.",
        ]),
        ladder("withering", "Withering Processor", {"item": "extradisks:withering_processor"}, [
            "The infinite part needs &eWithering Processors&r: a Processor Binding with a nether star, silicon and redstone, smelted like any other.",
            "",
            "One nether star per processor, and the part takes four. Time to visit the Wither again.",
        ]),
        {
            "key": "disk_infinite", "title": "Infinite Storage", "shape": "hexagon",
            "icon": "extradisks:infinite_item_storage_disk",
            "desc": [
                "No number on the label because there's no limit. An &eInfinite Storage Disk&r takes everything you'll ever own.",
                "",
                "It's the end of the item ladder. Every other disk you own is now a spare.",
            ],
            "tasks": [tagged("refinedstorage:disks/items/infinite", "Any Infinite Storage Disk",
                             "extradisks:infinite_item_storage_disk")],
            "rewards": [{"xp": 25}, {"crate": "lantern"}],
        },
        # ---- fluids and other resources ---------------------------------------
        {
            "key": "fluid_disk", "title": "Liquid Assets", "shape": "hexagon",
            "desc": [
                "Fluids get disks too. A &e64B Fluid Storage Disk&r holds 64 buckets, and the bigger ones go up from there.",
                "",
                "Stored fluids show up in the Grid right next to your items.",
            ],
            "tasks": [{"item": "refinedstorage:64b_fluid_storage_disk"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
    ] + [
        ladder(k, t, {"item": i}, lines) for k, t, i, lines in FLUID_DISKS
    ] + [
        ladder(k, t, tagged(f"refinedstorage:disks/fluids/{size}", f"Any {t}", icon), lines, icon=icon)
        for k, t, size, icon, lines in BIG_FLUID_DISKS
    ] + [
        {
            "key": "fluid_infinite", "title": "A Bottomless Tank", "optional": True,
            "icon": "extradisks:infinite_fluid_storage_disk",
            "desc": [
                "The &eInfinite Fluid Storage Disk&r holds every bucket there is. Like its item cousin, it needs Withering Processors.",
            ],
            "tasks": [tagged("refinedstorage:disks/fluids/infinite", "Any Infinite Fluid Storage Disk",
                             "extradisks:infinite_fluid_storage_disk")],
            "rewards": [{"xp": 25}, {"crate": "lantern"}],
        },
        {
            "key": "chemicals", "title": "Gas and Slurry",
            "desc": [
                "Mekanism's gases, acids and slurries can live on the network too. &eChemical Storage Disks&r start at 64B, and their parts use osmium where the item parts use iron.",
                "",
                "Extra Disks carries chemical disks all the way up to infinite.",
            ],
            "tasks": [{"tag": "refinedstorage_mekanism_integration:chemical_storage_disks",
                       "title": "Any Chemical Storage Disk",
                       "icon": "refinedstorage_mekanism_integration:64b_chemical_storage_disk"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "energy", "title": "Power in the Bank",
            "desc": [
                "Refined Types adds &eEnergy Storage Disks&r, which hold FE in a Disk Drive like any other resource.",
                "",
                "A &eNetwork Energizer&r, eight copper blocks around an Interface, draws on those disks to keep the network running.",
            ],
            "tasks": [{"tag": "refinedtypes:energy_storage_disks", "title": "Any Energy Storage Disk",
                       "icon": "refinedtypes:64k_energy_storage_disk"},
                      {"item": "refinedtypes:network_energizer"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        ladder("chem_big", "Big Chemical Disks", tagged("refinedstorage:disks/chemical",
                                                         "Any chemical disk from Extra Disks",
                                                         "extradisks:65536b_chemical_storage_disk"), [
            "Past 8192B, Extra Disks takes the chemical ladder up to infinite. Its parts ask for Atomic Alloy along with the usual Advanced Processors.",
        ], icon="extradisks:65536b_chemical_storage_disk"),
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
        # ---- wireless ---------------------------------------------------------
        {
            "key": "wireless", "title": "Storage on the Go", "shape": "hexagon",
            "desc": [
                "A &eWireless Transmitter&r lets a &eWireless Grid&r reach the network from 16 blocks away.",
                "",
                "Use the Wireless Grid on any device in the network to bind it, then open it anywhere in range.",
                "",
                "It runs on a battery, so charge it like any other FE item.",
            ],
            "tasks": [{"item": "refinedstorage:wireless_grid"},
                      {"tag": "refinedstorage:wireless_transmitters", "title": "Any Wireless Transmitter",
                       "icon": "refinedstorage:wireless_transmitter"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "wireless_upgrades", "title": "Upgrades in Your Pocket",
            "desc": [
                "Wireless grids have four upgrade slots.",
                "",
                "&eMagnet&r picks up items within 6 blocks, into your inventory or the network. &eInsert&r sends chosen inventory slots into the network. &eExport&r pulls chosen items out to you. &eBlock Picker&r makes Pick Block fetch from storage. &eEnergy Capacity&r adds to the battery.",
            ],
            "tasks": [{"any": ["rsinsertexportupgrade:magnet_upgrade", "rsinsertexportupgrade:insert_upgrade",
                               "rsinsertexportupgrade:export_upgrade", "rsinsertexportupgrade:block_picker_upgrade",
                               "rsinsertexportupgrade:energy_capacity_upgrade"],
                       "title": "Any wireless upgrade", "icon": "rsinsertexportupgrade:magnet_upgrade"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "range", "title": "A Longer Reach",
            "desc": [
                "Each &eRange Upgrade&r in a Wireless Transmitter adds 8 blocks to its reach. It's an Upgrade with ender pearls.",
                "",
                "Several transmitters work together too, if you'd rather cover a wide base.",
            ],
            "tasks": [{"item": "refinedstorage:range_upgrade"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "wireless_crafting", "title": "Craft Anywhere",
            "desc": [
                "The &eWireless Crafting Grid&r is a Crafting Grid you carry. It's built like the Wireless Grid, around a Crafting Grid instead.",
            ],
            "tasks": [{"item": "refinedstorage_quartz_arsenal:wireless_crafting_grid"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "wireless_monitor", "title": "Keep an Eye on It",
            "desc": [
                "The &eWireless Autocrafting Monitor&r shows your running crafts from anywhere in range: an Autocrafting Monitor with ender pearls and an Advanced Processor.",
                "",
                "With this and the two wireless grids, you have everything the next quest needs.",
            ],
            "tasks": [{"item": "refinedstorage:wireless_autocrafting_monitor"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "universal", "title": "The Universal Grid", "shape": "hexagon",
            "desc": [
                "The &eWireless Universal Grid&r rolls a Wireless Grid, a Wireless Crafting Grid and a Wireless Autocrafting Monitor into one, with a button to switch between them.",
                "",
                "Press &eShift+E&r to open it straight from your inventory.",
                "",
                "Your Curios (&eShift+G&r) have a Refined Storage slot for wireless grids, so it doesn't have to take up a pocket.",
            ],
            "tasks": [{"item": "universalgrid:wireless_universal_grid"}],
            "rewards": [{"xp": 25}, {"crate": "lantern"}, {"item": "refinedstorage:advanced_processor", "count": 4}],
        },
        {
            "key": "interdim", "title": "No Borders", "shape": "hexagon", "size": 1.5,
            "desc": [
                "A Wireless Transmitter stops at the edge of its range and at the edge of the dimension it's in. The &eInterdimensional Wireless Transmitter&r doesn't: infinite range, from any dimension.",
                "",
                "It takes four Wireless Transmitters, four nether stars and an elytra, and it draws more power than an ordinary one.",
                "",
                "One last thing: a &e64k Storage Disk&r is part of the &eAllthemodium Alloy Paxel&r recipe. The paxel quest gives it back once you've crafted it.",
            ],
            "tasks": [{"tag": "interdimensionalwirelesstransmitter:interdimensional_wireless_transmitters",
                       "title": "Interdimensional Wireless Transmitter",
                       "icon": "interdimensionalwirelesstransmitter:interdimensional_wireless_transmitter"}],
            "rewards": [{"xp": 50}, {"crate": "ember"}, {"item": "refinedstorage:advanced_processor", "count": 8}],
        },
        # ---- automation -------------------------------------------------------
        {
            "key": "io", "title": "In and Out", "shape": "hexagon",
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
    ],
}
