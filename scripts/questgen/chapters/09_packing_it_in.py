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
    ], {"item": "sophisticatedstorage:stack_upgrade_tier_1"}, optional=False),
    side("ss_stack_2", "Stack Upgrade Tier 2", [
        "Built from a Tier 1 upgrade, and each slot holds more again. There's a Tier 1 Plus in between if you want a cheaper step.",
    ], {"item": "sophisticatedstorage:stack_upgrade_tier_2"}, optional=False),
    side("ss_stack_3", "Stack Upgrade Tier 3", [
        "Tier 3 holds a lot. Conversion recipes turn the tier you have into a better one, so nothing goes to waste.",
    ], {"item": "sophisticatedstorage:stack_upgrade_tier_3"}, optional=False),
    side("ss_stack_4", "Stack Upgrade Tier 4", [
        "Deeper again. By now one chest can swallow a whole mining trip.",
    ], {"item": "sophisticatedstorage:stack_upgrade_tier_4"}, optional=False),
    side("ss_stack_5", "Stack Upgrade Tier 5", [
        "The deepest slots Sophisticated Storage makes. Put one in a netherite barrel and see how far it goes.",
    ], {"item": "sophisticatedstorage:stack_upgrade_tier_5"}, shape="hexagon", optional=False,
        rewards=[{"xp": 25}, {"crate": "lantern"}]),
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
    side("ss_filter", "Only What Belongs", [
        "A &eFilter Upgrade&r sets what pipes and hoppers may put into the chest, or take out of it. Keep the ore chest for ore.",
    ], {"any": tiers("sophisticatedstorage:filter_upgrade", "sophisticatedstorage:advanced_filter_upgrade"),
        "title": "A filter upgrade", "icon": "sophisticatedstorage:filter_upgrade"}),
    side("ss_jukebox", "A Chest with a Tune", [
        "Put music discs in a chest with a &eJukebox Upgrade&r and it plays them. The advanced one holds several and plays them in turn.",
    ], {"any": tiers("sophisticatedstorage:jukebox_upgrade", "sophisticatedstorage:advanced_jukebox_upgrade"),
        "title": "A jukebox upgrade", "icon": "sophisticatedstorage:jukebox_upgrade"}),
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
    side("bp_stack_starter", "Stack Upgrade Starter Tier", [
        "A backpack &eStack Upgrade&r lets each slot hold more than a stack. The Starter Tier is the cheap first step.",
    ], {"item": "sophisticatedbackpacks:stack_upgrade_starter_tier"}, optional=False),
    side("bp_stack_1", "Stack Upgrade Tier 1", [
        "More per slot again. Each tier is built from the one before, and conversion recipes skip a step if you have the materials.",
    ], {"item": "sophisticatedbackpacks:stack_upgrade_tier_1"}, optional=False),
    side("bp_stack_2", "Stack Upgrade Tier 2", [
        "A backpack that carries a small warehouse.",
    ], {"item": "sophisticatedbackpacks:stack_upgrade_tier_2"}, optional=False),
    side("bp_stack_3", "Stack Upgrade Tier 3", [
        "Deeper still. Pair it with a magnet and the mining trips get long.",
    ], {"item": "sophisticatedbackpacks:stack_upgrade_tier_3"}, optional=False),
    side("bp_stack_4", "Stack Upgrade Tier 4", [
        "The deepest backpack slots there are.",
    ], {"item": "sophisticatedbackpacks:stack_upgrade_tier_4"}, shape="hexagon", optional=False,
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
    side("bp_smelting", "A Furnace on Your Back", [
        "The &eSmelting Upgrade&r adds a furnace in a tab on the backpack. Blasting and smoking ones too, and auto versions that smelt as items come in.",
    ], {"any": tiers("sophisticatedbackpacks:smelting_upgrade", "sophisticatedbackpacks:auto_smelting_upgrade",
                     "sophisticatedbackpacks:blasting_upgrade", "sophisticatedbackpacks:auto_blasting_upgrade",
                     "sophisticatedbackpacks:smoking_upgrade", "sophisticatedbackpacks:auto_smoking_upgrade"),
        "title": "A smelting, blasting or smoking upgrade", "icon": "sophisticatedbackpacks:smelting_upgrade"}),
    side("bp_workshop", "A Workshop in a Bag", [
        "The &eStonecutter&r, &eAnvil&r and &eSmithing&r upgrades each add their workstation as a tab on the backpack.",
    ], {"any": tiers("sophisticatedbackpacks:stonecutter_upgrade", "sophisticatedbackpacks:anvil_upgrade",
                     "sophisticatedbackpacks:smithing_upgrade"),
        "title": "A stonecutter, anvil or smithing upgrade", "icon": "sophisticatedbackpacks:anvil_upgrade"}),
    side("bp_compacting", "Squeeze It In", [
        "A &eCompacting Upgrade&r turns nuggets into ingots and ingots into blocks as you pick them up.",
    ], {"any": tiers("sophisticatedbackpacks:compacting_upgrade", "sophisticatedbackpacks:advanced_compacting_upgrade"),
        "title": "A compacting upgrade", "icon": "sophisticatedbackpacks:compacting_upgrade"}),
    side("bp_filter", "Keep It Tidy", [
        "A &eFilter Upgrade&r sets what may go into the backpack or come out of it when it's placed and piped.",
    ], {"any": tiers("sophisticatedbackpacks:filter_upgrade", "sophisticatedbackpacks:advanced_filter_upgrade"),
        "title": "A filter upgrade", "icon": "sophisticatedbackpacks:filter_upgrade"}),
]

CHAPTER = {
    "file": "packing_it_in",
    "group": "hum",
    "title": "Packing It In",
    "subtitle": "Chests and backpacks that grow with you",
    "icon": "minecraft:chest",
    "theme": "packer",
    # Each tier ladder runs beside its stack upgrade ladder; everything that just fits in a
    # slot sits in a block of its own with no lines, since it needs no order.
    "layout": {
        "lines": [
            {"flow": [["start", "ss_stack"], ["tier", "ss_stack_2"], ["ss_gold", "ss_stack_3"],
                      ["packed", "ss_stack_4"], ["ss_netherite", "ss_stack_5"]]},
            {"flow": ["controller", ["link", "ss_io"]]},
            {"rows": ["upgrades", "ss_hopper", "ss_magnet", "ss_compacting", "ss_smelting", "ss_void", "ss_crafting",
                      "ss_filter", "ss_jukebox", "tape", "motion", "ss_shulker", "ss_limited", "ss_paint"],
             "per_row": 7},
            {"flow": [["bp_bigger", "bp_stack_starter"], ["bp_iron", "bp_stack_1"], ["bp_gold", "bp_stack_2"],
                      ["bp_diamond", "bp_stack_3"], ["bp_netherite", "bp_stack_4"]]},
            {"rows": ["bp_base", "bp_magnet", "bp_feeding", "bp_crafting", "bp_tool_swapper", "bp_refill",
                      "bp_deposit", "bp_void", "bp_tank", "bp_smelting", "bp_workshop", "bp_compacting", "bp_filter",
                      "bp_jukebox", "bp_inception", "bp_mob_catcher", "bp_everlasting"],
             "per_row": 9},
        ],
    },
    "quests": [
        {
            "key": "start", "title": "Packing It In",
            "shape": "hexagon", "size": 1.5, "icon": "sophisticatedstorage:chest", "icon_components": OAK,
            "desc": [
                "Sooner or later every base turns into a maze of chests. This chapter is about taming the pile: chests and backpacks that grow with you. Moving things between them is in &eLogistics&r.",
                "",
                "Start with a Sophisticated &echest&r or &ebarrel&r: planks around a lever. It holds as much as a vanilla chest, plus a slot for an upgrade.",
                "",
                "Already have chests full of stuff? Right-click a placed vanilla chest with a &eBasic Tier Upgrade&r and it becomes a Sophisticated one, with everything still inside.",
                "",
                "Some clicks that save clicking: &eShift&r and drag moves a whole row of items, &eCtrl&r-click moves one, &eSpace&r-click moves everything, and &eMiddle-click&r sorts.",
            ],
            "tasks": [{"any": ["sophisticatedstorage:chest", "sophisticatedstorage:barrel"],
                       "title": "A Sophisticated chest or barrel", "icon": "sophisticatedstorage:chest",
                       "icon_components": OAK}],
            "rewards": [{"xp": 10}, {"crate": "kindling", "count": 2}],
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
                "Any upgrade at all finishes this one. The others around it are the ones worth having, in any order.",
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
    ] + STORAGE + CHEST_UPGRADES + BACKPACKS,
}
