def side(key, title, task, lines, icon=None, optional=True, crate="kindling"):
    """A short catalog quest: one machine, addon or tool, optional by default."""
    q = {"key": key, "title": title, "desc": lines, "tasks": [task], "rewards": [{"xp": 10}, {"crate": crate}]}
    if optional:
        q["optional"] = True
    if icon:
        q["icon"] = icon
    return q


def item(i, count=1):
    return {"item": i, "count": count} if count > 1 else {"item": i}


CHAPTER = {
    "file": "oritech_kit",
    "group": "hum",
    "title": "Oritech Kit",
    "subtitle": "Oil, pipes, exo suits and augments",
    "icon": "oritech:exo_chestplate",
    # Oil runs to the refinery and splits; the jetpack and the exo suit meet in the exo jetpack.
    # Tools, pipes and storage need no order, so they sit in blocks.
    "layout": {
        "lines": [
            {"flow": ["oil", "pump", "refinery", ["plastic", "turbofuel"]],
             "branches": {"refinery": {"up": ["refinery_module"]}}},
            {"flow": [["jetpack", "exo_armor"], "exo_jetpack"],
             "branches": {"jetpack": {"up": ["elytra_jetpack"]}}},
            {"flow": ["augment", ["quantum_station", "arcane_station"]]},
            {"rows": ["hand_drill", "chainsaw", "charger", "portable_laser", "electric_mace", "prom_tools"]},
            {"rows": ["item_pipe", "fluid_pipe", "energy_pipe", "wrench", "item_filter", "booster", "ducts",
                      "superconductor", "power_pole", "drone_port", "energy_storage", "big_storage", "tank"],
             "per_row": 7},
        ],
    },
    "quests": [
        {
            "key": "oil", "title": "Black Gold", "shape": "hexagon", "size": 1.5,
            "desc": [
                "Oil springs gush up out of the ground, and they're much more common in deserts.",
                "",
                "Fill a bucket, or set a &ePump&r over the spring. It lowers a pipe until it finds the oil, then drains the whole pool into its tank.",
                "",
                "Crude oil burns in a &eFuel Generator&r as it is, but it's worth far more refined.",
            ],
            "tasks": [{"item": "oritech:still_oil_bucket"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        side("pump", "The Pump", item("oritech:pump_block"), [
            "Place a &ePump&r over any liquid and it lowers a trunk until it finds it, then drains the whole body, up to a hundred thousand blocks of it.",
            "",
            "It costs power for every block it takes. Oil, lava or water, it doesn't mind.",
        ], optional=False, crate="hearth"),
        {
            "key": "refinery", "title": "The Refinery",
            "desc": [
                "The &eRefinery&r splits crude oil into &eheavy oil&r, &enaphtha&r and &esulfuric acid&r. It needs nine machine cores.",
                "",
                "Out of the box only the first output works. Stack &eRefinery Chamber Modules&r on top to open the other two.",
                "",
                "Heavy oil refines again into diesel. Refined fuels give a Fuel Generator much more power per bucket than crude.",
            ],
            "tasks": [{"item": "oritech:refinery_block"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        side("refinery_module", "Refinery Chamber Module", item("oritech:refinery_module_block"), [
            "The Refinery is built from three of these, and up to two more stacked on top give it extra outputs. Pull those fluids from the modules, not the base.",
        ]),
        side("plastic", "Plastic", {"tag": "c:plates/plastic", "title": "Plastic Sheet", "icon": "oritech:plastic_sheet",
                                    "count": 8}, [
            "Sand in a Centrifuge with a Fluid Addon and naphtha makes &ePolymer Resin&r, and resin smelts into &ePlastic&r.",
            "",
            "No oil yet? Packed wheat spun with water makes raw biopolymer, and spun again it makes plastic too.",
        ], icon="oritech:plastic_sheet", optional=False, crate="hearth"),
        side("turbofuel", "Turbofuel", item("oritech:still_fuel_bucket"), [
            "Diesel and fluxite in a Centrifuge with a Fluid Addon make &eTurbofuel&r. It burns longest of anything a Fuel Generator takes, and it's what makes jetpacks fly fastest.",
        ], crate="hearth"),
        side("jetpack", "Jetpack", item("oritech:jetpack"), [
            "Oritech's &eJetpack&r runs on power or on turbofuel, and it's faster on fuel. Fill its tank at an Equipment Charger.",
            "",
            "It's steel, gunpowder, leather and an Advanced Battery.",
        ], optional=False, crate="hearth"),
        side("exo_armor", "The Exo Suit", {"any": ["oritech:exo_helmet", "oritech:exo_chestplate", "oritech:exo_leggings",
                                                   "oritech:exo_boots"],
                                           "title": "Any piece of the Exo Suit", "icon": "oritech:exo_chestplate"}, [
            "Each piece of the &eExo Suit&r does one thing: the helmet gives night vision, the chestplate charges your powered gear, the leggings make you faster, and the boots stop all fall damage.",
        ], icon="oritech:exo_chestplate", optional=False, crate="hearth"),
        side("exo_jetpack", "Exo Jetpack", item("oritech:exo_jetpack"), [
            "A jetpack and an Exo Chestplate fused with ion thrusters and a tank: much more power, much more speed, and it still charges your gear.",
        ], crate="hearth"),
        side("elytra_jetpack", "Wings and Thrust", item("oritech:jetpack_elytra"), [
            "A jetpack built into an elytra. Its engine only fires while you're already gliding, so jump, spread your wings, then hold jump.",
        ]),
        {
            "key": "augment", "title": "Better Than Flesh",
            "desc": [
                "The &eCybernetic Augmentation Center&r researches and installs permanent upgrades to your body: more health, more armor, faster mining, longer reach, and stranger things further up the tree.",
                "",
                "It needs ten machine cores, plus at least one &eCybernetic Research Station&r with three cores of its own. Walk into the center to open its research screen.",
                "",
                "Research takes materials and a great deal of power, so build it near your best generators.",
                "",
                "When a research finishes, install it from the center's screen for a one-time fee. Hold &eCtrl+G&r for the augment wheel, to switch any installed augment on or off. Removing one doesn't refund the fee.",
            ],
            "tasks": [{"item": "oritech:augment_application_block"}, {"item": "oritech:simple_augment_station"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        side("quantum_station", "Quantum Research Station", item("oritech:advanced_augment_station"), [
            "A second kind of research station, with three cores of its own. It unlocks the high-tier augments: stronger health and armor, far reach, hyper mining and more.",
            "",
            "The center has three station slots, so plan your layout.",
        ]),
        side("arcane_station", "Arcane Research Station", item("oritech:arcane_augment_station"), [
            "The strangest augments need this one: flight, a cloak, ore vision, a way home through a portal, and more.",
        ]),
        side("hand_drill", "Hand Drill", item("oritech:hand_drill"), [
            "The &eHand Drill&r is a pickaxe and a shovel in one, runs on power instead of durability, and never breaks.",
            "",
            "Each block costs power according to how hard it is, so keep it charged.",
        ], optional=False, crate="hearth"),
        side("chainsaw", "Chainsaw", item("oritech:chainsaw"), [
            "An axe that never breaks, and a sword in a pinch. Like the drill, it runs on power.",
        ]),
        side("charger", "Equipment Charger", item("oritech:charger_block"), [
            "The &eEquipment Charger&r tops up powered tools and armor quickly, and fills the fuel tanks of jetpacks.",
        ]),
        side("portable_laser", "Portable Laser", item("oritech:portable_laser"), [
            "A laser you carry. One mode mines blocks from far away. The other makes things explode. &eShift+right-click&r switches between them.",
        ]),
        side("electric_mace", "Electric Mace", item("oritech:electric_mace"), [
            "A mace that calls down lightning when it hits. Like any mace, it hits harder the further you fall first.",
        ]),
        side("prom_tools", "Tools That Never Break", {"any": ["oritech:promethium_pickaxe", "oritech:promethium_axe"],
                                                      "title": "A Prometheum Pickaxe or Battleaxe",
                                                      "icon": "oritech:promethium_pickaxe"}, [
            "Prometheum tools have no durability at all. The &ePickaxe&r switches between area mining and Silk Touch, and the &eBattleaxe&r fells a whole tree if you sneak while you chop.",
        ], icon="oritech:promethium_pickaxe", crate="hearth"),
        {
            "key": "item_pipe", "title": "Pipes", "shape": "hexagon",
            "desc": [
                "Oritech's &eItem Pipes&r are planks and nickel. They move eight items every quarter second from any inventory you set them to pull from.",
                "",
                "Right-click where a pipe meets a machine to make that end pull items out.",
            ],
            "tasks": [{"item": "oritech:item_pipe", "count": 8}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        side("fluid_pipe", "Fluid Pipes", item("oritech:fluid_pipe", 8), [
            "Half a bucket every three ticks. Toggle an end to extract, just like item pipes.",
        ]),
        side("energy_pipe", "Energy Pipes", item("oritech:energy_pipe", 8), [
            "Carry up to 10,000 RF a tick. Oritech power is pushed: generators and storage send it out, and pipes never pull.",
        ]),
        side("wrench", "Pipe Wrench", item("oritech:wrench"), [
            "The &ePipe Wrench&r turns pipe connections on and off, and sneak-right-click picks a pipe up instantly.",
            "",
            "It also lets you zipline along the cables between Power Poles.",
        ]),
        side("item_filter", "Item Filter", item("oritech:item_filter_block"), [
            "Place an &eItem Filter&r against an inventory and it only lets matching items through. It doesn't pull on its own, so pipe items into it.",
        ]),
        side("booster", "Pipe Booster", item("oritech:pipe_booster_block"), [
            "Point a powered &ePipe Booster&r at an extracting pipe and it pulls a full stack every tick, or up to 50 buckets of fluid.",
        ]),
        side("ducts", "Pipe Ducts", {"any": ["oritech:item_pipe_duct_block", "oritech:fluid_pipe_duct_block",
                                             "oritech:energy_pipe_duct_block", "oritech:superconductor_duct_block"],
                                     "title": "Any Pipe Duct", "icon": "oritech:item_pipe_duct_block"}, [
            "A &ePipe Duct&r is a pipe wrapped in plating and stone, for runs that should look like part of the wall. Ducts only join other pipes, not machines, so end each run with an ordinary pipe.",
        ], icon="oritech:item_pipe_duct_block"),
        side("superconductor", "Superconductor", item("oritech:superconductor", 8), [
            "Moves over four million RF a tick. It won't join ordinary energy pipes, so run it as its own line.",
        ], crate="hearth"),
        side("power_pole", "Power Lines", item("oritech:power_pole_block"), [
            "&ePower Poles&r send power across long distances. Link two with a Target Designator: sneak-click the first, then the second.",
            "",
            "One pole can link to as many others as you like.",
        ]),
        side("drone_port", "Drone Port", item("oritech:drone_port_block"), [
            "Two &eDrone Ports&r at least 50 blocks apart, linked with a Target Designator, fly items between them. Add a Fluid Addon to carry liquids too.",
            "",
            "Both ends need to be chunk-loaded.",
        ], crate="hearth"),
        side("energy_storage", "Portable Energy Storage", item("oritech:small_storage_block"), [
            "A million RF in a block that keeps its charge when you pick it up. A redstone signal stops it sending power.",
        ]),
        side("big_storage", "Large Energy Storage", item("oritech:large_storage_block"), [
            "Twenty million RF, with room for addons to make it bigger. It needs three machine cores and only sends power out of its red marker.",
        ]),
        side("tank", "Portable Tank", item("oritech:small_tank_block"), [
            "Holds 256 buckets and keeps them when you break it. Stack tanks and the fluid flows down into the lower ones.",
        ]),
    ],
}
