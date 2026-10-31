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


STORAGE = [
    side("ss_gold", "Gold Tier", [
        "Gold chests and barrels hold more again, with another upgrade slot. Upgrade in place or craft one around an iron chest.",
    ], {"any": tiers("sophisticatedstorage:gold_chest", "sophisticatedstorage:gold_barrel",
                     "sophisticatedstorage:basic_to_gold_tier_upgrade", "sophisticatedstorage:copper_to_gold_tier_upgrade",
                     "sophisticatedstorage:iron_to_gold_tier_upgrade"),
        "title": "A gold chest or barrel, or the upgrade to one", "icon": "sophisticatedstorage:gold_chest"},
        icon="sophisticatedstorage:gold_chest", optional=False),
    side("ss_netherite", "Netherite Tier", [
        "The biggest chests and barrels there are, with the most upgrade slots.",
    ], {"any": tiers("sophisticatedstorage:netherite_chest", "sophisticatedstorage:netherite_barrel",
                     "sophisticatedstorage:basic_to_netherite_tier_upgrade",
                     "sophisticatedstorage:copper_to_netherite_tier_upgrade",
                     "sophisticatedstorage:iron_to_netherite_tier_upgrade",
                     "sophisticatedstorage:gold_to_netherite_tier_upgrade",
                     "sophisticatedstorage:diamond_to_netherite_tier_upgrade"),
        "title": "A netherite chest or barrel, or the upgrade to one", "icon": "sophisticatedstorage:netherite_chest"},
        icon="sophisticatedstorage:netherite_chest"),
    side("ss_shulker", "A Shulker Box That Grows", [
        "A Sophisticated &eShulker Box&r keeps everything inside when you break it, and takes tiers and upgrades like the chests do.",
        "",
        "Got vanilla shulker boxes already? Craft one into its Sophisticated version.",
    ], {"any": tiers("sophisticatedstorage:shulker_box", "sophisticatedstorage:copper_shulker_box",
                     "sophisticatedstorage:iron_shulker_box", "sophisticatedstorage:gold_shulker_box",
                     "sophisticatedstorage:diamond_shulker_box", "sophisticatedstorage:netherite_shulker_box"),
        "title": "Any Sophisticated shulker box", "icon": "sophisticatedstorage:shulker_box"},
        icon="sophisticatedstorage:shulker_box"),
    side("ss_limited", "Fewer Slots, Bigger Ones", [
        "A &eLimited Barrel&r trades slots for size: from one slot (I) up to four (IV), and each slot holds many stacks of one item.",
        "",
        "Perfect for the cobblestone, the dirt and everything else you have far too much of.",
    ], {"any": tiers("sophisticatedstorage:limited_barrel_1", "sophisticatedstorage:limited_barrel_2",
                     "sophisticatedstorage:limited_barrel_3", "sophisticatedstorage:limited_barrel_4"),
        "title": "Any limited barrel", "icon": "sophisticatedstorage:limited_barrel_1"},
        icon="sophisticatedstorage:limited_barrel_1"),
    side("ss_paint", "Dress It Up", [
        "The &eDecoration Table&r gives chests and barrels the look of other materials, with a main and an accent color.",
        "",
        "The &ePaintbrush&r applies a design to storage that's already placed, so you don't have to empty it first.",
    ], {"any": tiers("sophisticatedstorage:decoration_table", "sophisticatedstorage:paintbrush"),
        "title": "A Decoration Table or a Paintbrush", "icon": "sophisticatedstorage:paintbrush"},
        icon="sophisticatedstorage:paintbrush"),
    side("ss_io", "In and Out", [
        "Pipes can go into any chest in a controller's wall, but an &eStorage Input&r, &eStorage Output&r or &eStorage I/O&r block makes a tidy spot for them.",
        "",
        "Place one in the wall: input lets you pipe items in, output lets you pipe them out, and I/O does both.",
    ], {"any": tiers("sophisticatedstorage:storage_input", "sophisticatedstorage:storage_output",
                     "sophisticatedstorage:storage_io"),
        "title": "A storage input, output or I/O", "icon": "sophisticatedstorage:storage_io"},
        icon="sophisticatedstorage:storage_io"),
]

CHEST_UPGRADES = [
    side("ss_hopper", "Built-in Hopper", [
        "The &eHopper Upgrade&r pulls items from the block above the chest and pushes them into the block below. The advanced one works on any side, faster.",
    ], {"any": tiers("sophisticatedstorage:hopper_upgrade", "sophisticatedstorage:advanced_hopper_upgrade"),
        "title": "A hopper upgrade", "icon": "sophisticatedstorage:hopper_upgrade"}),
    side("ss_magnet", "A Chest That Reaches", [
        "A chest with a &eMagnet Upgrade&r pulls in items lying around it. Set it under a tree farm and the saplings come home on their own.",
    ], {"any": tiers("sophisticatedstorage:magnet_upgrade", "sophisticatedstorage:advanced_magnet_upgrade",
                     "sophisticatedstorage:pickup_upgrade", "sophisticatedstorage:advanced_pickup_upgrade"),
        "title": "A magnet or pickup upgrade", "icon": "sophisticatedstorage:magnet_upgrade"}),
    side("ss_stack", "Deeper Slots", [
        "A &eStack Upgrade&r lets each slot hold more than a stack. Tier 1 doubles it, and every tier after holds more again.",
        "",
        "Upgrade slots are few, so it's usually the first thing worth putting in a chest.",
    ], {"item": "sophisticatedstorage:stack_upgrade_tier_1"}),
    side("ss_stack_high", "Deeper Still", [
        "Tiers 3, 4 and 5 hold a lot. Conversion recipes turn the tier you have into a better one, so nothing goes to waste.",
    ], {"any": tiers("sophisticatedstorage:stack_upgrade_tier_3", "sophisticatedstorage:stack_upgrade_tier_4",
                     "sophisticatedstorage:stack_upgrade_tier_5"),
        "title": "A Tier 3 stack upgrade or better", "icon": "sophisticatedstorage:stack_upgrade_tier_3"}),
    side("ss_compacting", "Pack It Down", [
        "A &eCompacting Upgrade&r squeezes items into their compressed forms as they come in: nuggets into ingots, ingots into blocks.",
    ], {"any": tiers("sophisticatedstorage:compacting_upgrade", "sophisticatedstorage:advanced_compacting_upgrade"),
        "title": "A compacting upgrade", "icon": "sophisticatedstorage:compacting_upgrade"}),
    side("ss_smelting", "A Furnace in a Tab", [
        "The &eSmelting Upgrade&r adds a furnace to the chest, in a tab down the side. There are blasting and smoking ones too.",
    ], {"any": tiers("sophisticatedstorage:smelting_upgrade", "sophisticatedstorage:auto_smelting_upgrade",
                     "sophisticatedstorage:blasting_upgrade", "sophisticatedstorage:auto_blasting_upgrade",
                     "sophisticatedstorage:smoking_upgrade", "sophisticatedstorage:auto_smoking_upgrade"),
        "title": "A smelting, blasting or smoking upgrade", "icon": "sophisticatedstorage:smelting_upgrade"}),
    side("ss_void", "Into the Void", [
        "The &eVoid Upgrade&r deletes whatever you put in its filter as it arrives. Pipe in a quarry's output and keep only what you want.",
    ], {"any": tiers("sophisticatedstorage:void_upgrade", "sophisticatedstorage:advanced_void_upgrade"),
        "title": "A void upgrade", "icon": "sophisticatedstorage:void_upgrade"}),
    side("ss_crafting", "Craft from the Chest", [
        "A &eCrafting Upgrade&r puts a crafting table in a tab on the chest. The &eStonecutter Upgrade&r adds a stonecutter the same way.",
    ], {"any": tiers("sophisticatedstorage:crafting_upgrade", "sophisticatedstorage:stonecutter_upgrade"),
        "title": "A crafting or stonecutter upgrade", "icon": "sophisticatedstorage:crafting_upgrade"}),
]

BACKPACKS = [
    side("bp_iron", "Iron Backpack", [
        "Iron ingots around a copper backpack. More room, and another upgrade slot.",
    ], {"any": tiers("sophisticatedbackpacks:iron_backpack", "sophisticatedbackpacks:gold_backpack",
                     "sophisticatedbackpacks:diamond_backpack", "sophisticatedbackpacks:netherite_backpack"),
        "title": "An iron backpack or better", "icon": "sophisticatedbackpacks:iron_backpack"},
        icon="sophisticatedbackpacks:iron_backpack", optional=False),
    side("bp_gold", "Gold Backpack", [
        "Gold around iron. Bigger again.",
    ], {"any": tiers("sophisticatedbackpacks:gold_backpack", "sophisticatedbackpacks:diamond_backpack",
                     "sophisticatedbackpacks:netherite_backpack"),
        "title": "A gold backpack or better", "icon": "sophisticatedbackpacks:gold_backpack"},
        icon="sophisticatedbackpacks:gold_backpack", optional=False),
    side("bp_diamond", "Diamond Backpack", [
        "Diamonds around gold. Bigger again, and it goes everywhere you do.",
    ], {"any": tiers("sophisticatedbackpacks:diamond_backpack", "sophisticatedbackpacks:netherite_backpack"),
        "title": "A diamond backpack or better", "icon": "sophisticatedbackpacks:diamond_backpack"},
        icon="sophisticatedbackpacks:diamond_backpack", optional=False),
    side("bp_netherite", "Netherite Backpack", [
        "The last tier is made on a smithing table: a netherite upgrade template, your diamond backpack and a netherite ingot.",
    ], {"item": "sophisticatedbackpacks:netherite_backpack"},
        icon="sophisticatedbackpacks:netherite_backpack", shape="hexagon",
        rewards=[{"xp": 25}, {"crate": "lantern"}]),
    side("bp_crafting", "Craft on the Go", [
        "The &eCrafting Upgrade&r adds a crafting table to the backpack, in a tab down its side.",
    ], {"item": "sophisticatedbackpacks:crafting_upgrade"}),
    side("bp_tool_swapper", "The Right Tool", [
        "With a &eTool Swapper Upgrade&r, hitting a block or a mob swaps the best tool from your backpack into your hand.",
    ], {"any": tiers("sophisticatedbackpacks:tool_swapper_upgrade", "sophisticatedbackpacks:advanced_tool_swapper_upgrade"),
        "title": "A tool swapper upgrade", "icon": "sophisticatedbackpacks:tool_swapper_upgrade"}),
    side("bp_refill", "Never Run Out", [
        "The &eRefill Upgrade&r keeps a stack of what you choose topped up in your inventory, from the backpack. Torches, food, building blocks.",
    ], {"any": tiers("sophisticatedbackpacks:refill_upgrade", "sophisticatedbackpacks:advanced_refill_upgrade"),
        "title": "A refill upgrade", "icon": "sophisticatedbackpacks:refill_upgrade"}),
    side("bp_deposit", "Empty Your Pockets", [
        "A &eDeposit Upgrade&r unloads the backpack into a chest when you sneak and right-click the chest. A &eRestock Upgrade&r does the reverse.",
    ], {"any": tiers("sophisticatedbackpacks:deposit_upgrade", "sophisticatedbackpacks:advanced_deposit_upgrade",
                     "sophisticatedbackpacks:restock_upgrade", "sophisticatedbackpacks:advanced_restock_upgrade"),
        "title": "A deposit or restock upgrade", "icon": "sophisticatedbackpacks:deposit_upgrade"}),
    side("bp_void", "Leave It Behind", [
        "A backpack &eVoid Upgrade&r deletes the items in its filter as you pick them up. Goodbye, cobblestone.",
    ], {"any": tiers("sophisticatedbackpacks:void_upgrade", "sophisticatedbackpacks:advanced_void_upgrade"),
        "title": "A void upgrade", "icon": "sophisticatedbackpacks:void_upgrade"}),
    side("bp_tank", "A Bucket That Never Ends", [
        "The &eTank Upgrade&r swaps part of the backpack's space for fluid storage. Add a &ePump Upgrade&r and it fills and empties itself.",
    ], {"item": "sophisticatedbackpacks:tank_upgrade"}),
    side("bp_jukebox", "Bring the Music", [
        "A &eJukebox Upgrade&r plays music discs from your backpack while you walk. The advanced one holds a whole playlist.",
    ], {"any": tiers("sophisticatedbackpacks:jukebox_upgrade", "sophisticatedbackpacks:advanced_jukebox_upgrade"),
        "title": "A jukebox upgrade", "icon": "sophisticatedbackpacks:jukebox_upgrade"}),
    side("bp_inception", "Backpacks in Backpacks", [
        "The &eInception Upgrade&r lets you put backpacks inside your backpack, and their upgrades keep working.",
    ], {"item": "sophisticatedbackpacks:inception_upgrade"}),
    side("bp_mob_catcher", "Pocket Zoo", [
        "Sneak and right-click an animal with a &eMob Catcher Upgrade&r fitted, and it goes into a backpack slot. The advanced one catches monsters too.",
    ], {"any": tiers("sophisticatedbackpacks:mob_catcher_upgrade", "sophisticatedbackpacks:advanced_mob_catcher_upgrade"),
        "title": "A mob catcher upgrade", "icon": "sophisticatedbackpacks:mob_catcher_upgrade"}),
    side("bp_everlasting", "Forever Yours", [
        "With an &eEverlasting Upgrade&r your backpack can't be destroyed. Dropped, it never despawns and never falls into the void.",
    ], {"item": "sophisticatedbackpacks:everlasting_upgrade"}),
]

PIPEZ = [
    side("pz_fluid", "Fluid Pipes", [
        "&eFluid Pipes&r work like item pipes: wrench the side touching a tank to pull from it, and the fluid flows to whatever the pipe touches.",
    ], {"item": "pipez:fluid_pipe"}, crate="kindling"),
    side("pz_energy", "Energy Pipes", [
        "&eEnergy Pipes&r carry FE from generators to machines, the same way.",
    ], {"item": "pipez:energy_pipe"}, crate="kindling"),
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
    ], {"item": "trashcans:liquid_trash_can"}),
    side("tc_energy", "Energy Trash Can", [
        "Voids energy. It can also cap how fast it takes it, which makes it a handy limiter.",
    ], {"item": "trashcans:energy_trash_can"}),
    side("tc_ultimate", "Ultimate Trash Can", [
        "Items, fluids and energy, all in one can.",
    ], {"item": "trashcans:ultimate_trash_can"}),
]

CHAPTER = {
    "file": "packing_it_in",
    "group": "hum",
    "title": "Packing It In",
    "subtitle": "Chests that grow, pipes that carry, routers that sort",
    "icon": "minecraft:chest",
    # Five tracks you can follow at once, one per mod or job, plus the odds and ends.
    "layout": {
        "info": ["essentials"],
        "lines": [
            # Sophisticated Storage: the chests themselves.
            {"spine": ["start", "tier", "ss_gold", "controller", "packed", "ss_netherite"],
             "branches": {
                 "start": {"up": ["tape"], "down": ["motion"]},
                 "tier": {"up": ["ss_shulker"], "down": ["ss_limited"]},
                 "ss_gold": {"up": ["ss_paint"]},
                 "controller": {"up": ["link"], "down": ["ss_io"]},
             }},
            # What goes in a chest's upgrade slots.
            {"spine": ["upgrades", "ss_hopper", "ss_stack", "ss_compacting", "ss_smelting", "ss_void",
                       "ss_crafting"],
             "branches": {
                 "ss_hopper": {"up": ["ss_magnet"]},
                 "ss_stack": {"up": ["ss_stack_high"]},
             }},
            # Sophisticated Backpacks: each tier, with its upgrades above and below it.
            {"spine": ["bp_base", "bp_bigger", "bp_iron", "bp_gold", "bp_diamond", "bp_netherite"],
             "branches": {
                 "bp_base": {"up": ["bp_magnet", "bp_feeding"], "down": ["bp_crafting"]},
                 "bp_bigger": {"up": ["bp_tool_swapper"], "down": ["bp_refill"]},
                 "bp_iron": {"up": ["bp_deposit"], "down": ["bp_void"]},
                 "bp_gold": {"up": ["bp_tank"], "down": ["bp_jukebox"]},
                 "bp_diamond": {"up": ["bp_inception"], "down": ["bp_mob_catcher"]},
                 "bp_netherite": {"up": ["bp_everlasting"]},
             }},
            # Pipez: each pipe, and each upgrade tier.
            {"spine": ["pipes", "pipe_speed", "pz_improved", "pz_advanced", "pz_ultimate"],
             "branches": {
                 "pipes": {"up": ["pz_fluid"], "down": ["pz_energy"]},
                 "pipe_speed": {"up": ["universal"], "down": ["pz_gas"]},
                 "pz_improved": {"up": ["pz_filter_tool"]},
             }},
            # Modular Routers: the modules worth knowing.
            {"spine": ["router", "mr_sender2", "vacuum", "mr_breaker", "mr_extruder", "mr_activator", "mr_sender3"],
             "branches": {
                 "router": {"up": ["mr_speed", "mr_stack"], "down": ["mr_filter"]},
                 "mr_sender2": {"up": ["mr_fluid"], "down": ["mr_distributor"]},
                 "vacuum": {"up": ["mr_xp"]},
                 "mr_breaker": {"up": ["mr_placer"], "down": ["mr_dropper", "mr_flinger"]},
                 "mr_extruder": {"up": ["mr_extruder2"]},
                 "mr_activator": {"up": ["mr_player"], "down": ["mr_detector"]},
             }},
            # Odds and ends.
            {"spine": ["stick", "collector", "trash", "extractor"],
             "branches": {
                 "stick": {"up": ["cs_more"]},
                 "collector": {"up": ["ic_advanced"]},
                 "trash": {"up": ["tc_liquid", "tc_energy"], "down": ["tc_ultimate"]},
             }},
        ],
    },
    "quests": [
        {
            "key": "start", "title": "Packing It In",
            "shape": "hexagon", "size": 1.5, "icon": "sophisticatedstorage:chest", "icon_components": OAK,
            "desc": [
                "Sooner or later every base turns into a maze of chests. This chapter is about taming the pile: chests that grow with you, pipes that carry, and small machines that sort things while you're out.",
                "",
                "Start with a Sophisticated &echest&r or &ebarrel&r: planks around a lever. It holds as much as a vanilla chest, plus a slot for an upgrade.",
                "",
                "Already have chests full of stuff? Right-click a placed vanilla chest with a &eBasic Tier Upgrade&r and it becomes a Sophisticated one, with everything still inside.",
            ],
            "tasks": [{"any": ["sophisticatedstorage:chest", "sophisticatedstorage:barrel"],
                       "title": "A Sophisticated chest or barrel", "icon": "sophisticatedstorage:chest",
                       "icon_components": OAK}],
            "rewards": [{"xp": 10}, {"crate": "kindling", "count": 2}],
        },
        {
            "key": "stick", "title": "A Workbench in Your Pocket", "shape": "hexagon",
            "desc": [
                "A crafting table on a stick. Right-click it to craft wherever you stand.",
                "",
                "Better yet, tuck it into its Curios slot and press &eShift+E&r to open it without digging through your bags. Anything you leave in the grid is still there next time.",
                "",
                "This line is for the small helpers that don't belong to any one mod.",
            ],
            "tasks": [{"item": "crafting_on_a_stick:crafting_table"}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}],
        },
        {
            "key": "essentials", "title": "Inventory Tricks", "shape": "gear", "wide": True,
            "desc": [
                "A few clicks that save a lot of clicking:",
                "",
                "&eShift&r and drag over items to move them all across",
                "&eCtrl&r-click to move just one",
                "&eShift+Ctrl&r-click to move every stack of that item",
                "&eSpace&r-click to move everything in that inventory",
                "&eMiddle-click&r to sort",
                "",
                "When a tool breaks or a stack of blocks runs out, the next one from your inventory slides into your hand.",
            ],
            "tasks": [{"check": "Got it"}],
        },
        {
            "key": "tier", "title": "Upgrade in Place",
            "icon": "sophisticatedstorage:basic_to_iron_tier_upgrade",
            "desc": [
                "A full chest doesn't need emptying to get bigger. Right-click a placed one with a tier upgrade, such as &eBasic to Iron Tier Upgrade&r, and it grows on the spot with everything still inside. A double chest takes two.",
                "",
                "You can also craft the next tier directly: a Sophisticated chest ringed with copper ingots becomes a Copper Chest.",
                "",
                "Copper, iron, gold, diamond, netherite. Each step adds room, and most add another upgrade slot.",
            ],
            "tasks": [{"any": ["sophisticatedstorage:basic_to_copper_tier_upgrade",
                               "sophisticatedstorage:basic_to_iron_tier_upgrade",
                               "sophisticatedstorage:copper_to_iron_tier_upgrade",
                               "sophisticatedstorage:copper_chest", "sophisticatedstorage:iron_chest",
                               "sophisticatedstorage:copper_barrel", "sophisticatedstorage:iron_barrel"],
                       "title": "A tier upgrade, or a copper or iron chest",
                       "icon": "sophisticatedstorage:basic_to_iron_tier_upgrade"}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}],
        },
        {
            "key": "tape", "title": "Moving Day",
            "desc": [
                "&ePacking Tape&r is a slimeball and a sheet of paper. Use it on a Sophisticated chest or barrel, then break it: it drops as one item with everything still packed inside.",
                "",
                "Try to break a stuffed chest without tape and the game stops you, so you don't spray hundreds of items across the floor. Sneak if you really mean it.",
            ],
            "tasks": [{"item": "sophisticatedstorage:packing_tape"}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}],
        },
        {
            "key": "motion", "title": "Storage on the Move", "optional": True,
            "icon": "sophisticatedstorage:iron_chest",
            "desc": [
                "Craft any Sophisticated chest, barrel or shulker box together with a minecart or a boat, and it rides along.",
                "",
                "A storage minecart is handy at the end of a long rail line, and a storage boat makes a fine floating pantry for river trips.",
            ],
            "tasks": [{"any": ["sophisticatedstorageinmotion:storage_minecart", "sophisticatedstorageinmotion:storage_boat"],
                       "title": "A storage minecart or boat", "icon": "minecraft:chest_minecart"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "upgrades", "title": "Chests with Talents", "shape": "hexagon",
            "desc": [
                "Sophisticated chests and barrels have upgrade slots, just like your backpack. Start with an &eUpgrade Base&r: planks and iron.",
                "",
                "Any upgrade at all finishes this one. The rest of the line goes through the ones worth having, one at a time.",
            ],
            "tasks": [{"tag": "sophisticatedstorage:upgrade", "title": "Any storage upgrade",
                       "icon": "sophisticatedstorage:hopper_upgrade"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "bp_base", "title": "Backpack Upgrades", "shape": "hexagon",
            "desc": [
                "Your backpack has upgrade slots down its side. Every upgrade starts from an &eUpgrade Base&r: string, iron and leather.",
                "",
                "Many chest upgrades also craft straight into their backpack twin, so a spare from your chests isn't wasted.",
                "",
                "This line follows the backpack up through its tiers, with the upgrades worth having above and below each one.",
            ],
            "tasks": [{"item": "sophisticatedbackpacks:upgrade_base"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "bp_magnet", "title": "Pull It In",
            "desc": [
                "A &ePickup Upgrade&r scoops items into your backpack as you walk over them.",
                "",
                "Craft it into a &eMagnet Upgrade&r and the backpack pulls them in from a few blocks away. Mining, farming and mob fights get a lot less fiddly.",
                "",
                "Both have filters, so you can leave the cobblestone on the ground.",
            ],
            "tasks": [{"item": "sophisticatedbackpacks:magnet_upgrade"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "bp_feeding", "title": "Packed Lunch", "optional": True,
            "desc": [
                "The &eFeeding Upgrade&r feeds you from the food in your backpack when you get hungry.",
                "",
                "Pack something filling and stop worrying about the hunger bar on long digs. It takes a golden apple, a golden carrot and a glistering melon slice, so it's a treat to make.",
            ],
            "tasks": [{"item": "sophisticatedbackpacks:feeding_upgrade"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "bp_bigger", "title": "A Bigger Backpack",
            "icon": "sophisticatedbackpacks:copper_backpack",
            "desc": [
                "Surround your backpack with copper ingots and it becomes a &eCopper Backpack&r, contents and upgrades included.",
                "",
                "Bigger packs have more slots and more room for upgrades. Each tier after this one is built around the one before.",
            ],
            "tasks": [{"any": ["sophisticatedbackpacks:copper_backpack", "sophisticatedbackpacks:iron_backpack",
                               "sophisticatedbackpacks:gold_backpack", "sophisticatedbackpacks:diamond_backpack",
                               "sophisticatedbackpacks:netherite_backpack"],
                       "title": "A copper backpack or better", "icon": "sophisticatedbackpacks:copper_backpack"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "pipes", "title": "Pipe a Furnace Array",
            "shape": "hexagon",
            "desc": [
                "&eItem Pipes&r connect to anything with an inventory. Right-click where a pipe meets a chest with the &ePipe Wrench&r, and that side starts pulling items out.",
                "",
                "Pipes push into whichever face they touch. Run one along the tops of a row of furnaces for ore, one along the sides for fuel, and pull the bottoms into an output chest.",
                "",
                "Now you can fill one chest and walk away.",
            ],
            "tasks": [{"item": "pipez:item_pipe", "count": 16}, {"item": "pipez:wrench"}],
            "rewards": [{"xp": 25}, {"crate": "lantern"}, {"item": "pipez:item_pipe", "count": 16}],
        },
        {
            "key": "universal", "title": "One Pipe for Everything", "optional": True,
            "desc": [
                "The &eUniversal Pipe&r carries items, fluids and energy in one line, which keeps a busy wall tidy.",
                "",
                "Two each of the item, energy and fluid pipes, with iron and a block of redstone, make six.",
            ],
            "tasks": [{"item": "pipez:universal_pipe"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
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
            "key": "trash", "title": "Take Out the Trash", "optional": True,
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
        {
            "key": "controller", "title": "One Chest to Rule Them",
            "shape": "hexagon",
            "desc": [
                "Build a wall of Sophisticated chests and barrels touching each other, then add a &eStorage Controller&r touching the wall.",
                "",
                "The whole wall now acts as one. Pipe items into the controller and they spread across every chest in the group; pull from it and you can reach them all.",
                "",
                "It's not a full storage network, but it ends a lot of chest-hunting. A gap in the wall? &eStorage Connectors&r bridge it.",
            ],
            "tasks": [{"item": "sophisticatedstorage:controller"}],
            "rewards": [{"xp": 25}, {"crate": "lantern"}, {"item": "sophisticatedstorage:oak_storage_connector", "count": 4}],
        },
        {
            "key": "link", "title": "Storage Link", "optional": True,
            "desc": [
                "Got a second group of chests across the room? Put a &eStorage Link&r against it.",
                "",
                "Link it to your controller with the &eStorage Tool&r and both groups answer to the same controller.",
            ],
            "tasks": [{"item": "sophisticatedstorage:storage_link"}, {"item": "sophisticatedstorage:storage_tool"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "packed", "title": "A Place for Everything",
            "shape": "hexagon", "size": 1.5, "icon": "sophisticatedstorage:diamond_chest",
            "desc": [
                "A diamond chest, fully upgraded, fed by pipes and kept tidy by routers. That's a storeroom.",
                "",
                "When the chests start to feel small again, &eRefined Storage&r turns the whole thing into one searchable network.",
            ],
            "tasks": [{"any": ["sophisticatedstorage:diamond_chest", "sophisticatedstorage:diamond_barrel",
                               "sophisticatedstorage:basic_to_diamond_tier_upgrade",
                               "sophisticatedstorage:copper_to_diamond_tier_upgrade",
                               "sophisticatedstorage:iron_to_diamond_tier_upgrade",
                               "sophisticatedstorage:gold_to_diamond_tier_upgrade",
                               "sophisticatedstorage:netherite_chest", "sophisticatedstorage:netherite_barrel"],
                       "title": "A diamond chest or barrel, or the upgrade to one", "icon": "sophisticatedstorage:diamond_chest"}],
            "rewards": [{"xp": 50}, {"crate": "ember"}, {"item": "sophisticatedstorage:stack_upgrade_tier_2"}],
        },
    ] + STORAGE + CHEST_UPGRADES + BACKPACKS + PIPEZ + ROUTERS + ODDS,
}
