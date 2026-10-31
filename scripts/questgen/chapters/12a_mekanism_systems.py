CHAPTER = {
    "file": "mekanism_systems",
    "group": "hum",
    "title": "Mekanism Systems",
    "subtitle": "Power, transport, storage and the gear to go with it",
    "icon": "mekanism:basic_energy_cube",
    "theme": "mekanism",
    # Each transmitter climbs its tiers beside the others; energy storage has its own short
    # ladder. Generators, storage and gear need no order, so they sit in blocks.
    "layout": {
        "lines": [
            {"flow": [["cables", "transporter", "mech_pipe", "tube"], ["ult_cable", "ult_transporter", "ult_pipe",
                                                                       "ult_tube"]]},
            {"flow": ["energy_cube", "induction", "induction_ultimate"],
             "branches": {"energy_cube": {"up": ["ultimate_cube"]}}},
            {"rows": ["heat_gen", "wind", "solar", "adv_solar", "gas_gen", "bio_gen", "chargepad"]},
            {"rows": ["conductor", "sorter", "configurator", "config_card", "bin", "cardboard", "fluid_tank",
                      "chem_tank", "personal_chest", "dynamic_tank", "qio"],
             "per_row": 11},
            {"rows": ["disassembler", "jetpack", "free_runners", "scuba", "portable_teleporter", "meka_tool", "mekasuit",
                      "modules", "teleporter", "module_excavation", "module_vein", "module_gravity", "module_jetpack",
                      "module_magnet", "module_elytra", "robit", "digital_miner", "entangloporter"],
             "per_row": 9},
        ],
    },
    "quests": [
        {
            "key": "energy_cube", "title": "Store the Spare", "shape": "hexagon",
            "desc": [
                "An &eEnergy Cube&r is a battery. It fills up while your generators run and pays it out when they stop.",
                "",
                "Each face can be set to take power in or push it out, and a cube can charge an item you put in it.",
            ],
            "tasks": [{"item": "mekanism:basic_energy_cube"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "ultimate_cube", "title": "A Bigger Battery", "optional": True,
            "desc": [
                "Energy Cubes go from Basic up to Ultimate, each holding far more than the one before. Craft each tier from the one below.",
            ],
            "tasks": [{"item": "mekanism:ultimate_energy_cube"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "induction", "title": "The Induction Matrix", "shape": "hexagon", "wide": True,
            "desc": [
                "For serious storage, build an &eInduction Matrix&r: a hollow box of &eInduction Casing&r with a port or two, filled with &eInduction Cells&r and &eProviders&r.",
                "",
                "Cells set how much it holds. Providers set how fast power moves in and out. Look it up in JEI to see the layout.",
            ],
            "tasks": [{"item": "mekanism:induction_casing", "count": 8}, {"item": "mekanism:induction_port"}, {"item": "mekanism:basic_induction_cell"}, {"item": "mekanism:basic_induction_provider"}],
            "rewards": [{"xp": 25}, {"crate": "lantern"}],
        },
        {
            "key": "induction_ultimate", "title": "Ultimate Cells", "optional": True,
            "desc": [
                "Induction Cells and Providers go up to Ultimate too. A matrix full of Ultimate Cells holds more power than you'll likely ever need.",
                "",
                "Almost: the Reactors chapter asks for a lot.",
            ],
            "tasks": [{"item": "mekanism:ultimate_induction_cell"}, {"item": "mekanism:ultimate_induction_provider"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "heat_gen", "title": "Something to Run It On", "shape": "hexagon",
            "desc": [
                "Mekanism's machines run on power, and the &eHeat Generator&r is the easy first source. It burns lava or anything a furnace would take.",
                "",
                "It's made from iron, copper, planks and one osmium ingot, so you can build it today.",
            ],
            "tasks": [{"item": "mekanismgenerators:heat_generator"}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}],
        },
        {
            "key": "wind", "title": "Catch the Wind",
            "desc": [
                "A &eWind Generator&r needs no fuel at all. It makes more power the higher up it stands, so hilltops and tall towers are worth the climb.",
                "",
                "A row of them along a ridge makes a fine little wind farm.",
            ],
            "tasks": [{"item": "mekanismgenerators:wind_generator"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "solar", "title": "Soak Up the Sun",
            "desc": [
                "&eSolar Generators&r run whenever the sun can see them. Four of them and some Infused Alloy make an &eAdvanced Solar Generator&r, which does the job in one block.",
                "",
                "Pair your solar farm with wind or a Heat Generator so the lights stay on at night.",
            ],
            "tasks": [{"any": ["mekanismgenerators:solar_generator", "mekanismgenerators:advanced_solar_generator"],
                       "title": "Four solar generators, either kind", "icon": "mekanismgenerators:solar_generator",
                       "count": 4}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "adv_solar", "title": "Bigger Panels",
            "desc": [
                "Four Solar Generators and some Infused Alloy make an &eAdvanced Solar Generator&r. It makes far more power than the four did, in one block.",
                "",
                "It still sleeps at night, so keep something else running beside it.",
            ],
            "tasks": [{"item": "mekanismgenerators:advanced_solar_generator"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "gas_gen", "title": "Burning Gas",
            "desc": [
                "The &eGas-Burning Generator&r runs on gases like &ehydrogen&r and ethylene.",
                "",
                "Your Electrolytic Separator makes hydrogen from water, so a separator and this generator side by side turn water into power. It's not free: the separator needs some of that power back.",
            ],
            "tasks": [{"item": "mekanismgenerators:gas_burning_generator"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "bio_gen", "title": "Compost Power",
            "desc": [
                "The &eBio-Generator&r burns &eBio Fuel&r, which the Crusher makes from almost anything that grows: crops, seeds, saplings, leaves, mushrooms, kelp.",
                "",
                "Hook it to a farm and your harvest powers your machines.",
            ],
            "tasks": [{"item": "mekanismgenerators:bio_generator"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}, {"item": "mekanism:block_bio_fuel", "count": 4}],
        },
        {
            "key": "chargepad", "title": "Stand Here", "optional": True,
            "desc": [
                "A &eChargepad&r charges anything powered in your inventory while you stand on it, from any mod: tools, jetpacks, gadgets.",
                "",
                "Put one by the door.",
            ],
            "tasks": [{"item": "mekanism:chargepad"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "cables", "title": "Power Lines", "shape": "hexagon", "size": 1.5,
            "desc": [
                "Steel and redstone make eight &eBasic Universal Cables&r. Run them from your generators to your machines and the power follows.",
                "",
                "Every Mekanism machine has a side configuration tab in its screen. Use it to choose which faces take power, items and chemicals, and which push them out.",
            ],
            "tasks": [{"item": "mekanism:basic_universal_cable", "count": 8}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "transporter", "title": "Moving Items",
            "desc": [
                "A &eLogistical Transporter&r carries items from one inventory to another. You can watch them ride along the pipe.",
                "",
                "Machines push their output into a transporter by themselves if the side config says so.",
            ],
            "tasks": [{"item": "mekanism:basic_logistical_transporter", "count": 8}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "mech_pipe", "title": "Moving Fluids",
            "desc": [
                "&eMechanical Pipes&r carry fluids: water to the washer, lava to the Heat Generator.",
            ],
            "tasks": [{"item": "mekanism:basic_mechanical_pipe", "count": 8}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "tube", "title": "Moving Gases",
            "desc": [
                "&ePressurized Tubes&r carry chemicals: gases, slurries and the rest. Oxygen, hydrogen chloride and sulfuric acid all travel in them.",
            ],
            "tasks": [{"item": "mekanism:basic_pressurized_tube", "count": 8}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "conductor", "title": "Moving Heat", "optional": True,
            "desc": [
                "&eThermodynamic Conductors&r carry heat between blocks that use it, like a Resistive Heater and the Thermal Evaporation Plant.",
            ],
            "tasks": [{"item": "mekanism:basic_thermodynamic_conductor", "count": 4}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "sorter", "title": "Sort It Out",
            "desc": [
                "A &eLogistical Sorter&r sits on a chest and pulls items out by filter, sending each kind down the transporter you choose.",
                "",
                "It's also a part in the Digital Miner.",
            ],
            "tasks": [{"item": "mekanism:logistical_sorter"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "configurator", "title": "The Configurator", "shape": "hexagon",
            "desc": [
                "The &eConfigurator&r is Mekanism's wrench. It can set a machine's sides, empty its tanks, rotate it, or pick it up.",
                "",
                "Hover over it to see its current mode and the key that switches it.",
            ],
            "tasks": [{"item": "mekanism:configurator"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "config_card", "title": "Copy the Settings", "optional": True,
            "desc": [
                "A &eConfiguration Card&r copies a machine's side configuration. Sneak and right-click one machine to copy, then right-click another to paste.",
                "",
                "Set up one factory the way you like and stamp the rest.",
            ],
            "tasks": [{"item": "mekanism:configuration_card"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "bin", "title": "Bins", "shape": "hexagon",
            "desc": [
                "A &eBin&r holds a huge stack of one item. Left-click to take a stack, right-click to put in what you're holding.",
                "",
                "Bins come in tiers, each holding more than the last.",
            ],
            "tasks": [{"item": "mekanism:basic_bin"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "cardboard", "title": "Moving Day, Mekanism Style", "optional": True,
            "desc": [
                "A &eCardboard Box&r picks up a block, contents and all. Sneak and right-click a full chest, carry it anywhere, and put it down again.",
            ],
            "tasks": [{"item": "mekanism:cardboard_box"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "fluid_tank", "title": "Fluid Tanks",
            "desc": [
                "A &eFluid Tank&r holds one fluid and keeps it when you pick the tank up. Stack them for more.",
            ],
            "tasks": [{"item": "mekanism:basic_fluid_tank"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "chem_tank", "title": "Chemical Tanks",
            "desc": [
                "A &eChemical Tank&r does the same for gases and slurries. A full tank of hydrogen in your pocket fills a jetpack anywhere.",
            ],
            "tasks": [{"item": "mekanism:basic_chemical_tank"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "personal_chest", "title": "Personal Storage",
            "desc": [
                "A &ePersonal Chest&r is a 54-slot chest you can open straight from your inventory. A &ePersonal Barrel&r is the same, barrel-shaped.",
                "",
                "It's also the heart of the Robit.",
            ],
            "tasks": [{"any": ["mekanism:personal_chest", "mekanism:personal_barrel"], "title": "A Personal Chest or Barrel", "icon": "mekanism:personal_chest"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "dynamic_tank", "title": "The Dynamic Tank", "optional": True,
            "desc": [
                "A &eDynamic Tank&r is a multiblock box of casing and valves that stores a vast amount of one fluid or chemical. Make it any size you like, within limits.",
                "",
                "JEI shows how to build it.",
            ],
            "tasks": [{"item": "mekanism:dynamic_tank", "count": 8}, {"item": "mekanism:dynamic_valve"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "qio", "title": "Quantum Item Orchestration", "optional": True,
            "desc": [
                "Mekanism has its own storage network, &eQIO&r: a Drive Array full of QIO Drives, reached from a Dashboard anywhere on the same frequency.",
                "",
                "Refined Storage does the same job here, so this is for anyone who'd rather keep it all Mekanism.",
            ],
            "tasks": [{"item": "mekanism:qio_drive_array"}, {"item": "mekanism:qio_dashboard"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "disassembler", "title": "The Atomic Disassembler", "shape": "hexagon",
            "desc": [
                "The &eAtomic Disassembler&r is a powered tool that mines, chops and digs anything. Its modes trade speed for power use.",
                "",
                "It also has a vein mode for ores and logs. Charge it like any other powered tool.",
            ],
            "tasks": [{"item": "mekanism:atomic_disassembler"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "jetpack", "title": "Hydrogen Jetpack",
            "desc": [
                "Mekanism's &eJetpack&r burns hydrogen instead of FE. Fill it from your Electrolytic Separator or a Chemical Tank.",
                "",
                "It has a hover mode too. An &eArmored Jetpack&r adds protection, if you can spare the chest slot.",
            ],
            "tasks": [{"any": ["mekanism:jetpack", "mekanism:jetpack_armored"], "title": "A Jetpack, plain or armored", "icon": "mekanism:jetpack"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "free_runners", "title": "Free Runners",
            "desc": [
                "&eFree Runners&r stop fall damage and let you walk straight up single blocks. They run on power.",
            ],
            "tasks": [{"item": "mekanism:free_runners"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "scuba", "title": "Under the Sea", "optional": True,
            "desc": [
                "A &eScuba Mask&r and a &eScuba Tank&r full of oxygen let you breathe underwater for a good long while.",
            ],
            "tasks": [{"item": "mekanism:scuba_mask"}, {"item": "mekanism:scuba_tank"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "portable_teleporter", "title": "Teleporter in Your Pocket", "optional": True,
            "desc": [
                "A &ePortable Teleporter&r takes you to any Teleporter on a frequency you can use, from anywhere. It runs on power, and longer trips cost more.",
            ],
            "tasks": [{"item": "mekanism:portable_teleporter"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "meka_tool", "title": "The Meka-Tool", "shape": "hexagon",
            "desc": [
                "The &eMeka-Tool&r is the Atomic Disassembler grown up: a pick, axe, shovel, hoe, shears and sword in one, made better with modules.",
                "",
                "It needs Polonium Pellets, so it waits for a fission reactor. See the Reactors chapter.",
            ],
            "tasks": [{"item": "mekanism:meka_tool"}],
            "rewards": [{"xp": 25}, {"crate": "lantern"}],
        },
        {
            "key": "mekasuit", "title": "The MekaSuit", "shape": "hexagon", "wide": True,
            "desc": [
                "The &eMekaSuit&r is armor that runs on power. Each piece is made from its netherite counterpart with HDPE, Polonium and Ultimate Control Circuits.",
                "",
                "On its own it's tough. With modules it flies, breathes underwater, feeds you and keeps the radiation out.",
            ],
            "tasks": [{"item": "mekanism:mekasuit_helmet"}, {"item": "mekanism:mekasuit_bodyarmor"}, {"item": "mekanism:mekasuit_pants"}, {"item": "mekanism:mekasuit_boots"}],
            "rewards": [{"xp": 25}, {"crate": "ember"}],
        },
        {
            "key": "modules", "title": "The Modification Station",
            "desc": [
                "Modules go into the Meka-Tool and MekaSuit at a &eModification Station&r. Every module starts from a &eModule Base&r: HDPE, tin and bronze.",
                "",
                "Put the gear in, then the module. Most modules can be installed several times for a stronger effect.",
            ],
            "tasks": [{"item": "mekanism:modification_station"}, {"item": "mekanism:module_base"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "module_excavation", "title": "Excavation Escalation Unit", "optional": True,
            "desc": [
                "Makes the Meka-Tool dig faster. Install several to stack the effect.",
            ],
            "tasks": [{"item": "mekanism:module_excavation_escalation_unit"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "module_vein", "title": "Vein Mining Unit", "optional": True,
            "desc": [
                "Lets the Meka-Tool break a whole vein of ore, or a whole tree, at once.",
            ],
            "tasks": [{"item": "mekanism:module_vein_mining_unit"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "module_gravity", "title": "Gravitational Modulating Unit", "optional": True,
            "desc": [
                "Real flight, the creative kind, for the MekaSuit's chestplate. It drinks power while you fly.",
            ],
            "tasks": [{"item": "mekanism:module_gravitational_modulating_unit"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "module_jetpack", "title": "Jetpack Unit", "optional": True,
            "desc": [
                "A hydrogen jetpack built into the MekaSuit chestplate.",
            ],
            "tasks": [{"item": "mekanism:module_jetpack_unit"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "module_magnet", "title": "Magnetic Attraction Unit", "optional": True,
            "desc": [
                "Pulls nearby items straight to you.",
            ],
            "tasks": [{"item": "mekanism:module_magnetic_attraction_unit"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "module_elytra", "title": "Elytra Unit", "optional": True,
            "desc": [
                "Glide like you're wearing an elytra, without giving up the chestplate.",
            ],
            "tasks": [{"item": "mekanism:module_elytra_unit"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "teleporter", "title": "The Teleporter", "shape": "hexagon",
            "desc": [
                "A &eTeleporter&r sends you to any other Teleporter on the same frequency. Build it into a frame of &eTeleporter Frames&r and set a frequency in its screen.",
                "",
                "JEI shows the frame. It takes power for every trip, more for longer ones.",
            ],
            "tasks": [{"item": "mekanism:teleporter"}, {"item": "mekanism:teleporter_frame", "count": 9}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "robit", "title": "A Robot Friend",
            "desc": [
                "The &eRobit&r follows you around, picks up items, and has a crafting table, a furnace and an inventory of its own. It goes back to a Chargepad on its own when it runs low.",
                "",
                "It's also the brain of the Digital Miner.",
            ],
            "tasks": [{"item": "mekanism:robit"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "digital_miner", "title": "The Digital Miner",
            "desc": [
                "The &eDigital Miner&r mines whatever blocks you tell it to, in a radius around it, without you lifting a finger. Set filters for the ores you want and leave the stone in place.",
                "",
                "It's hungry for power, and it needs somewhere to put what it finds. A chest or a transporter on top will do.",
            ],
            "tasks": [{"item": "mekanism:digital_miner"}],
            "rewards": [{"xp": 25}, {"crate": "lantern"}],
        },
        {
            "key": "entangloporter", "title": "Quantum Entangloporter", "optional": True,
            "desc": [
                "The &eQuantum Entangloporter&r sends items, fluids, chemicals, heat and power to every other entangloporter on its frequency, even across dimensions.",
            ],
            "tasks": [{"item": "mekanism:quantum_entangloporter"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "ult_cable", "title": "Ultimate Universal Cable",
            "desc": [
                "Every transmitter comes in four tiers. Each one is eight of the tier below around an alloy: infused for advanced, reinforced for elite and atomic for ultimate.",
                "",
                "Each tier moves more power, and faster, so it pays to upgrade the busiest lines first.",
            ],
            "tasks": [{"item": "mekanism:ultimate_universal_cable"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "ult_transporter", "title": "Ultimate Logistical Transporter",
            "desc": [
                "Every transmitter comes in four tiers. Each one is eight of the tier below around an alloy: infused for advanced, reinforced for elite and atomic for ultimate.",
                "",
                "Each tier moves more items, and faster, so it pays to upgrade the busiest lines first.",
            ],
            "tasks": [{"item": "mekanism:ultimate_logistical_transporter"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "ult_pipe", "title": "Ultimate Mechanical Pipe",
            "desc": [
                "Every transmitter comes in four tiers. Each one is eight of the tier below around an alloy: infused for advanced, reinforced for elite and atomic for ultimate.",
                "",
                "Each tier moves more fluids, and faster, so it pays to upgrade the busiest lines first.",
            ],
            "tasks": [{"item": "mekanism:ultimate_mechanical_pipe"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "ult_tube", "title": "Ultimate Pressurized Tube",
            "desc": [
                "Every transmitter comes in four tiers. Each one is eight of the tier below around an alloy: infused for advanced, reinforced for elite and atomic for ultimate.",
                "",
                "Each tier moves more chemicals, and faster, so it pays to upgrade the busiest lines first.",
            ],
            "tasks": [{"item": "mekanism:ultimate_pressurized_tube"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
    ],
}
