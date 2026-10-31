SPARK = "hearthandhollow:spark_of_creation"


def creative(key, title, item, line, components=None):
    task = {"item": item}
    if components:
        task["components"] = components
    return {
        "key": key, "title": title, "optional": True, "icon": item,
        "desc": [line],
        "tasks": [task],
        "rewards": [{"xp": 25}, {"crate": "ember"}],
    }


CHAPTER = {
    "file": "mekanism_reactors",
    "group": "long",
    "title": "Mekanism Reactors",
    "subtitle": "Fission, fusion, antimatter, and enough power to break the universe",
    "icon": "mekanismgenerators:fission_reactor_casing",
    "layout": {
        "info": ["safety"],
        "lines": [
            {"flow": ["yellowcake", "centrifuge", "fission_casing", "fuel_assembly", "fission"]},
            {"flow": ["turbine_casing", "rotor", "coils", "condenser"]},
            {"flow": ["sna", "polonium", "sps", "antimatter", "nucleosynthesizer"]},
            {"flow": ["laser", ["amplifier", "hohlraum"], "fusion"]},
            {"rows": ["hazmat", "waste_barrel", "boiler", "plutonium", "exp_pig", "exp_creeper", "exp_mooshroom",
                      "exp_villager"]},
            {"rows": ["spark", "creative_cube", "creative_jetpack", "creative_chem_tank", "creative_fluid_tank",
                      "creative_bin", "creative_cell", "creative_controller", "creative_grid", "creative_battery"]},
        ],
    },
    "quests": [
        {
            "key": "safety", "title": "Read This First", "shape": "gear",
            "desc": [
                "Reactors make more power than anything else in the pack, and they can go very wrong.",
                "",
                "Nuclear waste is &cradioactive&r. Never dump it into the air: keep it in tanks or a Radioactive Waste Barrel, and wear a Hazmat Suit near anything that leaks.",
                "",
                "Every multiblock here is shown layer by layer in JEI, thanks to Just Enough Mekanism Multiblocks. Look up the casing or the controller before you build.",
            ],
            "tasks": [{"check": "Understood"}],
        },
        {
            "key": "yellowcake", "title": "Look, Don't Eat", "shape": "hexagon", "size": 1.5,
            "icon": "mekanism:yellow_cake_uranium",
            "desc": [
                "Fission starts with uranium. Run it through an Enrichment Chamber for &eYellow Cake Uranium&r.",
                "",
                "From there the chemistry gets long: the cake becomes uranium oxide, then uranium hexafluoride with hydrofluoric acid, and finally &efissile fuel&r. JEI walks you through each step.",
            ],
            "tasks": [{"item": "mekanism:yellow_cake_uranium", "count": 8}],
            "rewards": [{"xp": 10}, {"crate": "lantern"}],
        },
        {
            "key": "centrifuge", "title": "Spin It Really Fast",
            "desc": [
                "The &eIsotopic Centrifuge&r spins uranium hexafluoride into fissile fuel.",
                "",
                "It also turns nuclear waste into plutonium later on, so you'll want two.",
            ],
            "tasks": [{"item": "mekanism:isotopic_centrifuge"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "fission_casing", "title": "Lead-Lined",
            "desc": [
                "A &eFission Reactor&r is a hollow box of &eFission Reactor Casing&r, with Reactor Glass where you want to look in.",
                "",
                "Start small. A reactor can be as little as a few blocks across, and a small one is far easier to keep cool.",
            ],
            "tasks": [{"item": "mekanismgenerators:fission_reactor_casing", "count": 16},
                      {"item": "mekanismgenerators:reactor_glass", "count": 4}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "fuel_assembly", "title": "Fuel Rods",
            "desc": [
                "Inside the reactor go columns of &eFission Fuel Assemblies&r, each topped with a &eControl Rod Assembly&r.",
                "",
                "More assemblies burn more fuel and make more heat. Leave room around them for coolant.",
            ],
            "tasks": [{"item": "mekanismgenerators:fission_fuel_assembly", "count": 2},
                      {"item": "mekanismgenerators:control_rod_assembly"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "fission", "title": "Critical", "shape": "hexagon", "icon": "mekanismgenerators:fission_reactor_port",
            "desc": [
                "&eFission Reactor Ports&r move fuel and coolant in and waste and steam out. A &eLogic Adapter&r lets redstone watch the reactor and switch it off.",
                "",
                "Set a Logic Adapter to trip when the reactor is damaged, and wire it so the reactor stops. Start the burn rate low and raise it slowly while you watch the heat.",
                "",
                "Cooled with water, it makes steam. The turbine on the next line turns that steam into power.",
            ],
            "tasks": [{"item": "mekanismgenerators:fission_reactor_port", "count": 2},
                      {"item": "mekanismgenerators:fission_reactor_logic_adapter"}],
            "rewards": [{"xp": 25}, {"crate": "ember"}],
        },
        {
            "key": "hazmat", "title": "Dress for It", "optional": True, "icon": "mekanism:hazmat_mask",
            "desc": [
                "A full &eHazmat Suit&r keeps radiation off you. A &eGeiger Counter&r tells you how much is around, and a &eDosimeter&r how much you've taken.",
            ],
            "tasks": [{"item": "mekanism:hazmat_mask"}, {"item": "mekanism:hazmat_gown"},
                      {"item": "mekanism:hazmat_pants"}, {"item": "mekanism:hazmat_boots"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}, {"item": "mekanism:geiger_counter"}],
        },
        {
            "key": "waste_barrel", "title": "Somewhere to Put It", "optional": True,
            "desc": [
                "A &eRadioactive Waste Barrel&r holds waste and slowly makes it safe. It's the place for anything you can't use.",
                "",
                "Most waste is worth more than that, though: it's where polonium and plutonium come from.",
            ],
            "tasks": [{"item": "mekanism:radioactive_waste_barrel"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "turbine_casing", "title": "The Industrial Turbine", "shape": "hexagon",
            "icon": "mekanismgenerators:turbine_casing",
            "desc": [
                "An &eIndustrial Turbine&r turns steam into a great deal of power. It's a tall box of &eTurbine Casing&r, with &eTurbine Valves&r for steam in and power out, and &eTurbine Vents&r to let the steam go.",
                "",
                "Look it up in JEI: the size of the box sets how much it can do.",
            ],
            "tasks": [{"item": "mekanismgenerators:turbine_casing", "count": 16},
                      {"item": "mekanismgenerators:turbine_valve", "count": 2},
                      {"item": "mekanismgenerators:turbine_vent", "count": 4}],
            "rewards": [{"xp": 10}, {"crate": "lantern"}],
        },
        {
            "key": "rotor", "title": "Blades and Rotors",
            "desc": [
                "Down the middle goes a column of &eTurbine Rotors&r, each holding &eTurbine Blades&r. Steam pushes on the blades and spins the rotor.",
            ],
            "tasks": [{"item": "mekanismgenerators:turbine_rotor", "count": 2},
                      {"item": "mekanismgenerators:turbine_blade", "count": 4}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "coils", "title": "Spinning Into Power",
            "desc": [
                "A &eRotational Complex&r sits on the top rotor, with &ePressure Dispersers&r filling the rest of that layer. &eElectromagnetic Coils&r above it turn the spin into power.",
            ],
            "tasks": [{"item": "mekanismgenerators:rotational_complex"}, {"item": "mekanism:pressure_disperser", "count": 8},
                      {"item": "mekanismgenerators:electromagnetic_coil", "count": 2}],
            "rewards": [{"xp": 25}, {"crate": "lantern"}],
        },
        {
            "key": "condenser", "title": "Water Back", "optional": True,
            "desc": [
                "&eSaturating Condensers&r above the rotational complex turn spent steam back into water, which you can pipe straight back into the reactor.",
            ],
            "tasks": [{"item": "mekanismgenerators:saturating_condenser", "count": 4}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "boiler", "title": "The Thermoelectric Boiler", "optional": True, "icon": "mekanism:boiler_casing",
            "desc": [
                "A &eThermoelectric Boiler&r makes steam from heat: from a fission reactor cooled with sodium, or from Resistive Heaters.",
                "",
                "It's Boiler Casing and Boiler Valves around &eSuperheating Elements&r and a layer of Pressure Dispersers.",
            ],
            "tasks": [{"item": "mekanism:boiler_casing", "count": 16}, {"item": "mekanism:boiler_valve", "count": 2},
                      {"item": "mekanism:superheating_element", "count": 2}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "sna", "title": "Sunlight, Weaponized", "shape": "hexagon",
            "icon": "mekanism:solar_neutron_activator",
            "desc": [
                "The &eSolar Neutron Activator&r uses the sun to transmute chemicals. It only works under open sky in daylight.",
                "",
                "Feed it nuclear waste and it makes &epolonium&r. Feed it lithium and it makes tritium, for fusion.",
            ],
            "tasks": [{"advancement": "mekanism:sna"}],
            "rewards": [{"xp": 10}, {"crate": "lantern"}],
        },
        {
            "key": "polonium", "title": "Polonium, Not Plutonium",
            "desc": [
                "A &ePressurized Reaction Chamber&r turns polonium, water and fluorite into &ePolonium Pellets&r.",
                "",
                "The MekaSuit, the Meka-Tool, the Modification Station and the SPS all need them.",
            ],
            "tasks": [{"item": "mekanism:pellet_polonium", "count": 4}],
            "rewards": [{"xp": 25}, {"crate": "lantern"}],
        },
        {
            "key": "plutonium", "title": "Plutonium, Not Polonium", "optional": True,
            "desc": [
                "The other road for waste: an Isotopic Centrifuge makes &eplutonium&r, and a PRC turns that into &ePlutonium Pellets&r.",
                "",
                "JEI shows where they go. Some of the heaviest machinery in Mekanism wants them.",
            ],
            "tasks": [{"item": "mekanism:pellet_plutonium"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "sps", "title": "Supercritical Phase Shifter", "shape": "hexagon", "icon": "mekanism:sps_casing",
            "desc": [
                "The &eSPS&r turns polonium into &eantimatter&r. It's a big box of SPS Casing with SPS Ports, and &eSupercharged Coils&r on the ports to feed it power.",
                "",
                "And what power. Each drop of antimatter costs a vast amount of polonium and energy. This is where the Induction Matrix and the reactors earn their keep.",
            ],
            "tasks": [{"item": "mekanism:sps_casing", "count": 16}, {"item": "mekanism:sps_port", "count": 2},
                      {"item": "mekanism:supercharged_coil", "count": 2}],
            "rewards": [{"xp": 25}, {"crate": "ember"}],
        },
        {
            "key": "exp_pig", "title": "A Smarter Pig?", "optional": True, "icon": "minecraft:carrot",
            "desc": ["The SPS does strange things to animals that get too close. Try it on a pig. Don't expect much."],
            "tasks": [{"advancement": "mekanism:sps_experiment_pig"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "exp_creeper", "title": "Supercharged", "optional": True, "icon": "minecraft:creeper_head",
            "desc": ["Now try a creeper. Stand well back."],
            "tasks": [{"advancement": "mekanism:sps_experiment_creeper"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "exp_mooshroom", "title": "A Different Shade", "optional": True, "icon": "minecraft:red_mushroom",
            "desc": ["A mooshroom, perhaps. Its color might not survive the trip."],
            "tasks": [{"advancement": "mekanism:sps_experiment_mooshroom"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "exp_villager", "title": "Villain Origin Story", "optional": True, "icon": "minecraft:emerald",
            "desc": ["And a villager. Something tells you this won't end well for the village."],
            "tasks": [{"advancement": "mekanism:sps_experiment_villager"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "antimatter", "title": "Impossible Material",
            "desc": [
                "A Chemical Crystallizer packs antimatter into an &eAntimatter Pellet&r.",
                "",
                "Each pellet is a whole bucket of the stuff. Hold it carefully.",
            ],
            "tasks": [{"item": "mekanism:pellet_antimatter"}],
            "rewards": [{"xp": 25}, {"crate": "ember"}],
        },
        {
            "key": "nucleosynthesizer", "title": "Alchemy, With Science", "optional": True,
            "icon": "mekanism:antiprotonic_nucleosynthesizer",
            "desc": [
                "The &eAntiprotonic Nucleosynthesizer&r uses a little antimatter and a lot of power to turn one thing into another: coal into diamond, diamond into emerald, an egg into a dragon egg.",
                "",
                "JEI lists everything it knows.",
            ],
            "tasks": [{"item": "mekanism:antiprotonic_nucleosynthesizer"}],
            "rewards": [{"xp": 10}, {"crate": "lantern"}],
        },
        {
            "key": "laser", "title": "Lasers", "shape": "hexagon", "icon": "mekanism:laser",
            "desc": [
                "Fusion needs a spark to get going, and that spark is a laser. A &eLaser&r fires a beam that breaks blocks, and hurts anything in the way.",
                "",
                "Never stand in front of one.",
            ],
            "tasks": [{"item": "mekanism:laser"}],
            "rewards": [{"xp": 10}, {"crate": "lantern"}],
        },
        {
            "key": "amplifier", "title": "Store the Beam",
            "desc": [
                "A &eLaser Amplifier&r collects energy from lasers aimed into it and fires it all out in one big pulse. That pulse is what lights a fusion reactor.",
            ],
            "tasks": [{"item": "mekanism:laser_amplifier"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "hohlraum", "title": "Fusion Fuel",
            "desc": [
                "Fusion burns &edeuterium&r and &etritium&r. Deuterium comes from heavy water in an Electrolytic Separator. Tritium comes from lithium in the Solar Neutron Activator.",
                "",
                "A &eHohlraum&r filled with mixed D-T fuel goes into the reactor controller for ignition.",
            ],
            "tasks": [{"item": "mekanismgenerators:hohlraum"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "fusion", "title": "A Star in a Box", "shape": "hexagon", "icon": "mekanismgenerators:fusion_reactor_controller",
            "desc": [
                "The &eFusion Reactor&r is a ring of Reactor Frame around a &eFusion Reactor Controller&r, with Reactor Ports to feed it and a &eLaser Focus Matrix&r for the amplifier to fire into.",
                "",
                "Once it's lit and fed, it runs as long as the fuel lasts, and it doesn't make waste.",
            ],
            "tasks": [{"item": "mekanismgenerators:fusion_reactor_controller"},
                      {"item": "mekanismgenerators:fusion_reactor_frame", "count": 16},
                      {"item": "mekanismgenerators:fusion_reactor_port", "count": 2},
                      {"item": "mekanismgenerators:laser_focus_matrix"}],
            "rewards": [{"xp": 50}, {"crate": "ember"}],
        },
        {
            "key": "spark", "title": "Break the Universe", "shape": "hexagon", "size": 2.0, "wide": True, "icon": SPARK,
            "desc": [
                "Fission, fusion, an Induction Matrix full to bursting, and a whole pellet of antimatter. You've made enough power to tear a hole in the world.",
                "",
                "Put it to use. An Antimatter Pellet, two Nether Stars, Ultimate Control Circuits and Atomic Alloy make a &eSpark of Creation&r.",
                "",
                "The Spark is a catalyst. It never gets used up, and with the best of each tech line it makes &dcreative&r items: an endless battery, an endless jetpack, tanks and bins that never run dry. Press &eU&r on the Spark to see them all.",
            ],
            "tasks": [{"item": SPARK}],
            "rewards": [{"xp": 50}, {"crate": "ember", "count": 2}],
        },
        creative("creative_cube", "Endless Power", "mekanism:creative_energy_cube",
                 "Four Ultimate Energy Cubes and four Ultimate Induction Cells around the Spark make a Creative Energy Cube, full and bottomless."),
        creative("creative_jetpack", "Fly Forever", "ironjetpacks:jetpack",
                 "An Unobtainium Jetpack with Ultimate Induction Cells and Atomic Alloy becomes a Creative Jetpack. It never needs charging.",
                 {"ironjetpacks:jetpack_id": "ironjetpacks:creative"}),
        creative("creative_chem_tank", "A Bottomless Tank", "mekanism:creative_chemical_tank",
                 "Ultimate Chemical Tanks and Atomic Alloy make a Creative Chemical Tank. Fill it once with any chemical and it never empties."),
        creative("creative_fluid_tank", "An Endless Well", "mekanism:creative_fluid_tank",
                 "Ultimate Fluid Tanks and Atomic Alloy make a Creative Fluid Tank. Fill it once with any fluid and it never empties."),
        creative("creative_bin", "A Bin That Gives", "mekanism:creative_bin",
                 "Ultimate Bins and Atomic Alloy make a Creative Bin. Put one item in, and it hands out that item forever."),
        creative("creative_cell", "Powah, Unlimited", "powah:energy_cell_creative",
                 "Four Nitro Energy Cells and four Nitro Crystals make a Creative Energy Cell."),
        creative("creative_controller", "A Network for Free", "refinedstorage:creative_controller",
                 "Refined Storage Controllers and Ultimate Induction Providers make a Creative Controller: a network that never needs power."),
        creative("creative_grid", "Everything, Everywhere", "universalgrid:creative_wireless_universal_grid",
                 "Wireless Universal Grids and Ultimate Induction Cells make a Creative Wireless Universal Grid that never runs flat."),
        creative("creative_battery", "A Gadget That Never Tires", "mininggadgets:upgrade_battery_creative",
                 "Tier 3 Battery Upgrades and Ultimate Induction Cells make a Creative Battery for the Mining Gadget."),
    ],
}
