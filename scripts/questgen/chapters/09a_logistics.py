OAK = {"sophisticatedstorage:wood_type": "oak"}

def side(key, title, desc, task, crate="hearth", icon=None, **extra):
    """An optional catalog quest: one variant of a mod's kit, with a line or two about it."""
    q = {"key": key, "title": title, "optional": True, "desc": desc, "tasks": [task],
         "rewards": [{"xp": 10}, {"crate": crate}]}
    if icon:
        q["icon"] = icon
    q.update(extra)
    return q


def tiers(*ids):
    return list(ids)


PIPEZ = [
    side("pz_fluid", "Fluid Pipes", [
        "&eFluid Pipes&r work like item pipes: wrench the side touching a tank to pull from it, and the fluid flows to whatever the pipe touches.",
    ], {"item": "pipez:fluid_pipe"}, crate="kindling", optional=False),
    side("pz_energy", "Energy Pipes", [
        "&eEnergy Pipes&r carry FE from generators to machines, the same way.",
    ], {"item": "pipez:energy_pipe"}, crate="kindling", optional=False),
    side("pz_gas", "Gas Pipes", [
        "&eGas Pipes&r move Mekanism's gases. They need Infused Alloy, so they come a little later.",
    ], {"item": "pipez:gas_pipe"}),
    side("pz_improved", "Improved Pipe Upgrade", [
        "Gold and redstone around a Basic upgrade. Moves more, more often.",
    ], {"item": "pipez:improved_upgrade"}, optional=False),
    side("pz_advanced", "Advanced Pipe Upgrade", [
        "Diamonds and redstone blocks around an Improved upgrade, and faster again.",
    ], {"item": "pipez:advanced_upgrade"}, optional=False),
    side("pz_ultimate", "Ultimate Pipe Upgrade", [
        "Netherite ingots and redstone blocks around an Advanced upgrade. The fastest pipes you can make.",
    ], {"item": "pipez:ultimate_upgrade"}, optional=False),
    side("pz_filter_tool", "Send It There", [
        "A filter in an upgrade can name a destination. Click a block with the &eFilter Destination Tool&r, then add it to a filter, and matching items go only there.",
    ], {"item": "pipez:filter_destination_tool"}),
]

ROUTERS = [
    side("mr_speed", "Speed Upgrade", [
        "A &eSpeed Upgrade&r makes the router tick more often. Stack a few for a router that keeps up with a busy machine.",
    ], {"item": "modularrouters:speed_upgrade"}),
    side("mr_stack", "Stack Upgrade", [
        "A &eStack Upgrade&r moves more items each time the router ticks.",
    ], {"item": "modularrouters:stack_upgrade"}),
    side("mr_filter", "Smarter Filters", [
        "Module filters take items, but also filter items: a &eTag Filter&r, a &eMod Filter&r, a &eRegex Filter&r for registry names, an &eInspection Filter&r, and a &eBulk Item Filter&r for long lists.",
    ], {"any": tiers("modularrouters:tag_filter", "modularrouters:mod_filter", "modularrouters:regex_filter",
                     "modularrouters:inspection_filter", "modularrouters:bulk_item_filter"),
        "title": "Any filter item", "icon": "modularrouters:tag_filter"}),
    side("mr_sender2", "Sender Module Mk2", [
        "The &eSender Module Mk2&r sends items to any inventory nearby, with no line of sight needed. Most routers end up with one.",
    ], {"item": "modularrouters:sender_module_2"}, optional=False),
    side("mr_fluid", "Fluid Module", [
        "With a bucket or tank item in its buffer, a router with a &eFluid Module&r moves fluids to and from the block it faces. The Mk2 reaches any block nearby.",
    ], {"any": tiers("modularrouters:fluid_module", "modularrouters:fluid_module_2"),
        "title": "A fluid module", "icon": "modularrouters:fluid_module"}),
    side("mr_distributor", "Share It Out", [
        "A &eDistributor Module&r spreads items across several inventories: round robin, random, nearest first or furthest first.",
    ], {"item": "modularrouters:distributor_module"}),
    side("mr_xp", "Bottled Experience", [
        "Fit an &eXP Vacuum Augment&r to a Vacuum Module and it collects experience orbs instead of items, as Bottles o' Enchanting.",
    ], {"item": "modularrouters:xp_vacuum_augment"}),
    side("mr_breaker", "Breaker Module", [
        "A &eBreaker Module&r breaks the block in front of the router and keeps it. Pair it with a sender for a tiny automatic quarry face.",
    ], {"item": "modularrouters:breaker_module"}, optional=False),
    side("mr_placer", "Placer Module", [
        "The &ePlacer Module&r puts a block from the router's buffer in front of it. Handy for replanting, or for setting blocks where a machine expects them.",
    ], {"item": "modularrouters:placer_module"}),
    side("mr_dropper", "Dropper Module", [
        "The &eDropper Module&r drops items from the buffer onto the ground in front of the router.",
    ], {"item": "modularrouters:dropper_module"}),
    side("mr_flinger", "Flinger Module", [
        "The &eFlinger Module&r throws items, a long way if you like. Set the speed and angle in its menu, and aim for a hopper.",
    ], {"item": "modularrouters:flinger_module"}),
    side("mr_extruder", "Extruder Module", [
        "An &eExtruder Module Mk1&r places a line of blocks from the buffer when the router gets a redstone signal, and pulls them back when it stops. Instant doors and bridges.",
    ], {"item": "modularrouters:extruder_module_1"}, optional=False),
    side("mr_extruder2", "Extruder Module Mk2", [
        "The Mk2 extrudes copies of blocks from a pattern instead of real ones, so a hidden door can look like any wall.",
    ], {"item": "modularrouters:extruder_module_2"}),
    side("mr_activator", "Activator Module", [
        "An &eActivator Module&r right-clicks blocks and mobs with whatever is in the buffer, like a player would. Shear sheep, milk cows, fill bottles.",
    ], {"item": "modularrouters:activator_module"}, optional=False),
    side("mr_player", "Player Module", [
        "The &ePlayer Module&r moves items between the router and your own inventory, remotely. Armor slots included.",
    ], {"item": "modularrouters:player_module"}),
    side("mr_detector", "Detector Module", [
        "A &eDetector Module&r gives off a redstone signal when the item in the buffer matches its filter.",
    ], {"item": "modularrouters:detector_module"}),
    side("mr_sender3", "Sender Module Mk3", [
        "The Mk3 sends items to an inventory anywhere, even in another dimension. Mining Dimension output, straight home.",
    ], {"item": "modularrouters:sender_module_3"}, shape="hexagon", optional=False,
        rewards=[{"xp": 25}, {"crate": "hearth"}]),
    side("mr_puller2", "Puller Module Mk2", [
        "The Mk2 pulls from an inventory in range instead of the one it touches. Sneak and right-click the inventory with the module to set it.",
    ], {"item": "modularrouters:puller_module_2"}),
    side("mr_void", "Void Module", [
        "A &eVoid Module&r deletes what's in the router's buffer, filtered or not. A tidy end for overflow.",
    ], {"item": "modularrouters:void_module"}),
    side("mr_energy", "Routers Carry Power Too", [
        "With &eEnergy Upgrades&r a router holds FE. An &eEnergy Output Module&r passes it to the block in front, and an &eEnergy Distributor Module&r shares it out to several.",
    ], {"any": tiers("modularrouters:energy_output_module", "modularrouters:energy_distributor_module"),
        "title": "An energy output or distributor module", "icon": "modularrouters:energy_output_module"}),
    side("mr_augments", "Fine Tuning", [
        "&eAugments&r fit inside a module and change how it works: more range or less, bigger stacks, redstone control, and more. Each module lists the ones it takes.",
    ], {"any": tiers("modularrouters:range_up_augment", "modularrouters:range_down_augment",
                     "modularrouters:stack_augment", "modularrouters:regulator_augment",
                     "modularrouters:redstone_augment", "modularrouters:pushing_augment"),
        "title": "Any augment", "icon": "modularrouters:range_up_augment"}),
    side("mr_camo", "Hide the Machinery", [
        "A &eCamouflage Upgrade&r makes the router look like any block you set in it, so it disappears into the wall.",
    ], {"item": "modularrouters:camouflage_upgrade"}),
]

ODDS = [
    side("cs_more", "More Sticks", [
        "The &eStonecutter&r, &eLoom&r, &eSmithing Table&r, &eAnvil&r, &eGrindstone&r and &eCartography Table&r all come on sticks too.",
    ], {"any": tiers("crafting_on_a_stick:stonecutter", "crafting_on_a_stick:loom", "crafting_on_a_stick:smithing_table",
                     "crafting_on_a_stick:anvil", "crafting_on_a_stick:grindstone", "crafting_on_a_stick:cartography_table"),
        "title": "Any other workstation on a stick", "icon": "crafting_on_a_stick:stonecutter"}, crate="kindling"),
    side("ic_advanced", "Advanced Item Collector", [
        "The &eAdvanced Item Collector&r reaches a little farther, and has a filter so it only picks up what you want.",
    ], {"item": "itemcollectors:advanced_collector"}),
    side("tc_liquid", "Liquid Trash Can", [
        "Voids fluids and gases, with a filter for up to nine fluids.",
    ], {"item": "trashcans:liquid_trash_can"}, optional=False),
    side("tc_energy", "Energy Trash Can", [
        "Voids energy. It can also cap how fast it takes it, which makes it a handy limiter.",
    ], {"item": "trashcans:energy_trash_can"}, optional=False),
    side("tc_ultimate", "Ultimate Trash Can", [
        "Items, fluids and energy, all in one can. It's made from one of each of the other three.",
    ], {"item": "trashcans:ultimate_trash_can"}, shape="hexagon", optional=False,
        rewards=[{"xp": 25}, {"crate": "lantern"}]),
]

CHAPTER = {
    "file": "logistics",
    "group": "hum",
    "title": "Logistics",
    "subtitle": "Pipes that carry, routers that sort, cans that swallow",
    "icon": "pipez:item_pipe",
    # Pipez fans out from the first pipe to the Universal Pipe, routers climb their two Mk
    # ladders side by side, and the trash cans meet in the Ultimate one. Modules that need no
    # order sit in a block with no lines.
    "layout": {
        "lines": [
            {"flow": ["pipes", ["pz_fluid", "pz_energy"], "universal"],
             "branches": {"pipes": {"up": ["pz_filter_tool"], "down": ["pz_gas"]}}},
            {"flow": ["pipe_speed", "pz_improved", "pz_advanced", "pz_ultimate"]},
            {"flow": ["router", ["mr_sender2", "mr_extruder"], ["mr_sender3", "mr_extruder2"]]},
            {"rows": ["vacuum", "mr_puller2", "mr_fluid", "mr_distributor", "mr_breaker", "mr_placer", "mr_dropper",
                      "mr_flinger", "mr_activator", "mr_player", "mr_detector", "mr_void", "mr_energy", "mr_xp",
                      "mr_speed", "mr_stack", "mr_filter", "mr_augments", "mr_camo"],
             "per_row": 10},
            {"flow": [["trash", "tc_liquid", "tc_energy"], "tc_ultimate"]},
            {"rows": ["stick", "cs_more", "collector", "ic_advanced", "extractor"]},
        ],
    },
    "quests": [
        {
            "key": "pipes", "title": "Pipe a Furnace Array",
            "shape": "hexagon", "size": 1.5,
            "desc": [
                "&eItem Pipes&r connect to anything with an inventory. Right-click where a pipe meets a chest with the &ePipe Wrench&r, and that side starts pulling items out.",
                "",
                "Pipes push into whichever face they touch. Run one along the tops of a row of furnaces for ore, one along the sides for fuel, and pull the bottoms into an output chest.",
                "",
                "Now you can fill one chest and walk away. The rest of this chapter is about moving things: pipes, routers, and somewhere for the leftovers to go.",
            ],
            "tasks": [{"item": "pipez:item_pipe", "count": 16}, {"item": "pipez:wrench"}],
            "rewards": [{"xp": 25}, {"crate": "lantern"}, {"item": "pipez:item_pipe", "count": 16}],
        },
        {
            "key": "universal", "title": "One Pipe for Everything", "shape": "hexagon",
            "desc": [
                "The &eUniversal Pipe&r carries items, fluids and energy in one line, which keeps a busy wall tidy.",
                "",
                "Two each of the item, energy and fluid pipes, with iron and a block of redstone, make six.",
            ],
            "tasks": [{"item": "pipez:universal_pipe"}],
            "rewards": [{"xp": 25}, {"crate": "lantern"}],
        },
        {
            "key": "pipe_speed", "title": "Faster Pipes", "icon": "pipez:basic_upgrade",
            "desc": [
                "A bare pipe is slow. Right-click the pulling end of a pipe to open it, and slot in an upgrade.",
                "",
                "Upgrades move more at once and more often. Better ones also unlock filters, redstone control and how items are shared out, such as round robin across all your furnaces.",
                "",
                "They go Basic, Improved, Advanced and Ultimate, each built around the one before.",
            ],
            "tasks": [{"any": ["pipez:basic_upgrade", "pipez:improved_upgrade", "pipez:advanced_upgrade",
                               "pipez:ultimate_upgrade"],
                       "title": "Any pipe upgrade", "icon": "pipez:basic_upgrade"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "router", "title": "Route It",
            "shape": "hexagon",
            "desc": [
                "A &eModular Router&r is a tiny block with one slot of buffer and room for modules. Each module does one job.",
                "",
                "A &ePuller Module&r takes items from the inventory beside it. A &eSender Module&r ships them to an inventory in a straight line; the Mk2 doesn't need line of sight.",
                "",
                "Hover a module and press &eCtrl+C&r to set its direction and filter.",
            ],
            "tasks": [{"item": "modularrouters:modular_router"}, {"item": "modularrouters:puller_module_1"}],
            "rewards": [{"xp": 25}, {"crate": "lantern"}, {"item": "modularrouters:blank_module", "count": 4}],
        },
        {
            "key": "vacuum", "title": "Vacuum Module", "optional": True,
            "desc": [
                "The &eVacuum Module&r sucks nearby items off the ground into the router.",
                "",
                "Pair it with a Sender Module and items go straight to storage. Add an &eXP Vacuum Augment&r and it gathers experience orbs instead, turning them into Bottles o' Enchanting.",
            ],
            "tasks": [{"item": "modularrouters:vacuum_module"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "trash", "title": "Take Out the Trash",
            "desc": [
                "Every automated setup makes something you don't want. A &eTrash Can&r deletes it.",
                "",
                "The &eItem Trash Can&r has a filter for up to nine items, so it only eats what you tell it to.",
                "",
                "Pipe your overflow into one and nothing backs up.",
            ],
            "tasks": [{"item": "trashcans:item_trash_can"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "stick", "title": "A Workbench in Your Pocket",
            "desc": [
                "A crafting table on a stick. Right-click it to craft wherever you stand.",
                "",
                "Better yet, tuck it into its Curios slot and press &eShift+E&r to open it without digging through your bags. Anything you leave in the grid is still there next time.",
            ],
            "tasks": [{"item": "crafting_on_a_stick:crafting_table"}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}],
        },
        {
            "key": "collector", "title": "Tidy Up the Floor", "optional": True,
            "desc": [
                "An &eItem Collector&r picks up items lying around it and puts them in the inventory it's attached to.",
                "",
                "Put one on a chest next to your mob farm or under a tree farm and stop chasing drops. You can widen or shrink its range in its menu.",
            ],
            "tasks": [{"any": ["itemcollectors:basic_collector", "itemcollectors:advanced_collector"],
                       "title": "Any item collector", "icon": "itemcollectors:basic_collector"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "extractor", "title": "Stone from Nowhere", "optional": True,
            "desc": [
                "XyCraft's &eExtractor&r pulls items out of the world. Point it at a stone block with water and lava touching it, and it makes copies of that stone, slowly, with no power.",
                "",
                "It keeps what it makes, so pipe the stone out into a chest.",
                "",
                "Cobblestone, andesite, granite and more each have their own setup. Press &eU&r on the Extractor to see them all.",
            ],
            "tasks": [{"item": "xycraft_machines:extractor"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
    ] + PIPEZ + ROUTERS + ODDS,
}
