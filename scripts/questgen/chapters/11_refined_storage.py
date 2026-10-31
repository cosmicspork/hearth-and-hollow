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

CHAPTER = {
    "file": "refined_storage",
    "group": "hum",
    "title": "Refined Storage",
    "subtitle": "One network for everything: disks, grids and wireless access",
    "icon": "refinedstorage:controller",
    # The network fans out from the processors to the controller, the item and fluid disk ladders
    # climb side by side, and the wireless grids meet in the Universal Grid. The bigger disks and
    # other odds and ends need no order.
    "layout": {
        "lines": [
            {"flow": ["rs_start", ["proc_basic", "proc_improved", "processors"], "controller", ["drive", "grid"],
                      ["portable_grid", "crafting_grid"]]},
            {"flow": [["disk_4k", "fluid_disk"], ["disk_16k", "fluid_256b"], ["disk_64k", "fluid_1024b"],
                      ["big_disks", "fluid_4096b"], ["disk_infinite", "fluid_infinite"]]},
            {"rows": ["cable", "wrench", "storage_block", "housing", "adv_housing", "withering"]
                     + [d[0] for d in BIG_ITEM_DISKS] + [d[0] for d in BIG_FLUID_DISKS]
                     + ["chemicals", "chem_big", "energy", "wireless_upgrades"],
             "per_row": 10},
            {"flow": ["wireless", ["wireless_crafting", "wireless_monitor"], "universal"],
             "branches": {"wireless": {"up": ["range"], "down": ["interdim"]}}},
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
                "Either mod's disk counts for these quests, and they upgrade the same way.",
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
            "key": "fluid_infinite", "title": "A Bottomless Tank",
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
    ],
}
