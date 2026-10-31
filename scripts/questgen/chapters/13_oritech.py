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
    "file": "oritech",
    "group": "hum",
    "title": "Oritech",
    "subtitle": "Big machines, lasers, and ore from below the bedrock",
    "icon": "oritech:laser_arm_block",
    # Nine tracks: power, processing, machine cores, addons, lasers and mining, gantries, gear and
    # augments, oil and plastic, and logistics. The first quest of each line is cheap to reach.
    "layout": {
        "lines": [
            {"spine": ["start", "generator", "lava_gen", "steam_engine", "fuel_gen", "bio_gen", "solar", "reactor"],
             "branches": {
                 "start": {"up": ["oracle"]},
                 "steam_engine": {"up": ["boiler"]},
                 "bio_gen": {"up": ["biomass"]},
             }},
            {"spine": ["pulverizer", "furnace", "foundry", "assembler", "centrifuge", "fragment", "atomic_forge"],
             "branches": {
                 "foundry": {"up": ["adamant"]},
                 "assembler": {"up": ["components"]},
                 "centrifuge": {"down": ["cooler"]},
                 "atomic_forge": {"up": ["prometheum"], "down": ["accelerator"]},
             }},
            {"spine": ["cores", "core_2", "core_3", "core_4", "core_5", "core_6", "finale"]},
            {"spine": ["addons", "extender", "processing_addon", "burst_addon", "ultimate_addon", "splicer",
                       "combi_addon"],
             "branches": {
                 "addons": {"up": ["fluid_addon"], "down": ["yield_addon"]},
                 "extender": {"up": ["capacitor_addon"], "down": ["acceptor_addon"]},
                 "processing_addon": {"up": ["proxy_addon"], "down": ["redstone_addon"]},
                 "burst_addon": {"up": ["cap_extender"]},
             }},
            {"spine": ["laser", "fluxite", "boulder", "drill"],
             "branches": {
                 "laser": {"up": ["designator", "hunter_addon"], "down": ["silk_addon"]},
                 "fluxite": {"up": ["enchanter"], "down": ["spawner"]},
             }},
            {"spine": ["frame", "destroyer", "placer", "fertilizer", "treefeller"],
             "branches": {
                 "destroyer": {"up": ["quarry_addon"], "down": ["crop_filter"]},
             }},
            {"spine": ["hand_drill", "chainsaw", "charger", "jetpack", "exo_armor", "exo_jetpack", "augment",
                       "apply", "prom_tools"],
             "branches": {
                 "jetpack": {"up": ["elytra_jetpack"]},
                 "exo_jetpack": {"down": ["portable_laser", "electric_mace"]},
                 "augment": {"up": ["quantum_station", "arcane_station"]},
             }},
            {"spine": ["oil", "pump", "tank", "refinery_module", "refinery", "plastic", "turbofuel"]},
            {"spine": ["item_pipe", "fluid_pipe", "energy_pipe", "item_filter", "booster", "ducts", "superconductor",
                       "power_pole", "drone_port"],
             "branches": {
                 "item_pipe": {"up": ["wrench"]},
                 "energy_pipe": {"down": ["energy_storage", "big_storage"]},
             }},
        ],
    },
    "quests": [
        # ---- power ------------------------------------------------------------
        {
            "key": "start", "title": "Oritech",
            "shape": "hexagon", "size": 1.5, "icon": "oritech:basic_generator_block",
            "desc": [
                "Oritech is industry on a grand scale: multiblock machines, lasers, oil refineries, and a drill that pulls ore up from below the bedrock forever.",
                "",
                "It runs on &enickel&r. Here nickel comes from AllTheOres veins, and the ore boulders you'll find on the surface often have some showing.",
                "",
                "Bring copper, iron, coal and redstone too. Each line in this chapter is a separate track; this top one is power.",
            ],
            "tasks": [{"tag": "c:ingots/nickel", "title": "Nickel Ingot", "icon": "alltheores:nickel_ingot",
                       "count": 8}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "oracle", "title": "Read the Manual", "shape": "gear",
            "desc": [
                "Oritech comes with a full in-game manual, the &eOracle Index&r, with a page for nearly every block and a guide to getting started.",
                "",
                "Hover over an Oritech item and the tooltip tells you to hold &eAlt&r for its documentation.",
                "",
                "The key to open the whole manual is unbound in this pack. If you'd like one, set &eOpen Oracle Index&r under Options, Controls, Key Binds.",
            ],
            "tasks": [{"check": "Got it"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "generator", "title": "Your First Oritech Machine",
            "desc": [
                "The &eBasic Generator&r burns ordinary furnace fuel, like coal, charcoal or wood, and makes 32 RF a tick. That's enough for your first few machines.",
                "",
                "It's cheap and needs no multiblock, so build a second or third rather than waiting for something better.",
            ],
            "tasks": [{"item": "oritech:basic_generator_block"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        side("lava_gen", "Lava Generator", item("oritech:lava_generator_block"), [
            "The &eLava Generator&r burns lava for 64 RF a tick. It's a Basic Generator with electrum, a magnetic coil and plating, and it needs two machine cores.",
            "",
            "A Pump over a lava lake keeps it fed for a very long time.",
        ], crate="hearth"),
        side("steam_engine", "Full Steam", item("oritech:steam_engine_block"), [
            "Put a &eSteam Boiler Addon&r on any generator except the Basic one, feed the addon water, and the generator makes steam instead of RF.",
            "",
            "The &eSteam Engine&r turns that steam back into RF and water. It runs faster the fuller its steam tank, and makes the most per bucket at around seven times its base speed. Engines built in a row chain together: pipe steam into the first one only.",
        ], crate="hearth"),
        side("boiler", "Steam Boiler Addon", item("oritech:steam_boiler_addon"), [
            "Water goes into the addon and steam comes out of it, not the generator itself, so pipe to the addon.",
        ]),
        side("fuel_gen", "Fuel Generator", item("oritech:fuel_generator_block"), [
            "The &eFuel Generator&r burns liquid fuel for 256 RF a tick. Crude oil works, but refined fuels go much further per bucket.",
            "",
            "It only sends power out of the two yellow spots on its front, so run your cables there.",
        ], crate="hearth"),
        side("bio_gen", "Bio Generator", item("oritech:bio_generator_block"), [
            "The &eBio Generator&r makes 64 RF a tick from biomass and other plant matter, so a tree or crop farm can power your base.",
            "",
            "It needs two machine cores, and a Flux Gate in its recipe.",
        ]),
        side("biomass", "Biomass", item("oritech:biomass", 16), [
            "The &ePulverizer&r grinds saplings, crops and plants into &eBiomass&r. It's also what Biosteel is made from.",
            "",
            "You can eat it in a pinch. You won't enjoy it.",
        ]),
        side("solar", "Here Comes the Sun", item("oritech:big_solar_panel_block"), [
            "The &eBig Solar Panel&r is a 3x3 multiblock that unfolds in daylight and folds away at night. It makes 32 RF a tick, more with better machine cores.",
            "",
            "No fuel, no upkeep. Just give it open sky.",
        ]),
        side("reactor", "Splitting Atoms", item("oritech:reactor_controller"), [
            "Oritech's &eNuclear Reactor&r is a multiblock of any size you like: walls, rods, a fuel port over each rod, and a controller to assemble it. It burns uranium or plutonium pellets for huge amounts of power.",
            "",
            "&cIt runs hot.&r Heat pipes, vents and absorbers carry the heat away. Read the manual's reactor pages before you load the fuel.",
        ], crate="hearth"),
        # ---- processing -------------------------------------------------------
        {
            "key": "pulverizer", "title": "Crush It", "shape": "hexagon",
            "desc": [
                "The &ePulverizer&r crushes ore into dust, and dust smelts into more metal than raw ore does. It's slow and simple, and it earns its keep from day one.",
                "",
                "It also grinds plants into &ebiomass&r for generators, and coal into coal dust for carbon parts later on.",
            ],
            "tasks": [{"item": "oritech:pulverizer_block"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "furnace", "title": "Powered Furnace",
            "desc": [
                "The &ePowered Furnace&r smelts twice as fast as a stone furnace and needs no fuel, only power.",
                "",
                "It needs one machine core beside it. Right-click the furnace and the spot lights up.",
            ],
            "tasks": [{"item": "oritech:powered_furnace_block"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "foundry", "title": "The Foundry", "shape": "hexagon",
            "desc": [
                "The &eFoundry&r makes Oritech's alloys: steel, electrum, adamant and more. You can hand-craft the first few, but it costs far more metal than the foundry does.",
                "",
                "It needs three machine cores. The manual's advice is to pair it with your Pulverizer as soon as you can.",
                "",
                "Adamant from the foundry is what you need for the Assembler, next.",
            ],
            "tasks": [{"item": "oritech:foundry_block"}],
            "rewards": [{"xp": 25}, {"crate": "lantern"}, {"item": "alltheores:steel_ingot", "count": 8}],
        },
        side("adamant", "Adamant", {"tag": "c:ingots/adamant", "title": "Adamant Ingot", "icon": "oritech:adamant_ingot",
                                    "count": 4}, [
            "A diamond and a nickel ingot in the Foundry make &eAdamant&r. The Assembler, the hand drill and the better machine cores all ask for it.",
            "",
            "The Foundry's other alloys are worth knowing: iron and coal dust for steel, gold and redstone for electrum, nickel and fluxite for energite.",
        ], icon="oritech:adamant_ingot"),
        {
            "key": "assembler", "title": "The Assembler",
            "desc": [
                "The &eAssembler&r crafts Oritech's components, like motors and magnetic coils, on its own 2x2 grid. Many parts can be made by hand, but the assembler uses far less material.",
                "",
                "The order of the inputs doesn't matter, and Refined Storage autocrafting works with it out of the box.",
            ],
            "tasks": [{"item": "oritech:assembler_block"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        side("components", "Nuts and Bolts", {"any": ["oritech:motor", "oritech:magnetic_coil", "oritech:processing_unit"],
                                              "title": "A motor, coil or processing unit", "icon": "oritech:motor"}, [
            "Most Oritech machines are built from a few parts: &eMagnetic Coils&r from nickel and steel, &eMotors&r from coils and steel, and later &eProcessing Units&r from plastic, carbon fibre, electrum and redstone.",
            "",
            "Keep a stack of each. You'll use them everywhere.",
        ], icon="oritech:motor"),
        {
            "key": "centrifuge", "title": "Spin Cycle",
            "desc": [
                "The &eCentrifuge&r spins ore clumps into dust and coal dust into &eCarbon Fibre Strands&r, which you'll need for better machine cores.",
                "",
                "Attach a &eFluid Addon&r and it handles liquids too. Open the machine once after placing the addon so it notices.",
            ],
            "tasks": [{"item": "oritech:centrifuge_block"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        side("cooler", "Industrial Chiller", item("oritech:cooler_block"), [
            "The &eIndustrial Chiller&r turns water into ice, lava into obsidian and steam into snow. Reactors that cool with absorbers need its ice.",
            "",
            "It needs one machine core, and it works better somewhere cold.",
        ]),
        {
            "key": "fragment", "title": "Fragment Forge",
            "desc": [
                "The &eFragment Forge&r is the big step up for ore. Ore blocks become raw ore, and raw ore becomes a clump and some small clumps, plus small clumps of a second metal as a bonus.",
                "",
                "Nine small clumps make a clump, and the Centrifuge spins clumps into dust.",
                "",
                "It needs seven machine cores. Feed it ore blocks mined with Silk Touch for the best return.",
            ],
            "tasks": [{"item": "oritech:fragment_forge_block"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "atomic_forge", "title": "The Atomic Forge", "shape": "hexagon",
            "desc": [
                "The &eAtomic Forge&r makes Oritech's best parts: computing engines, AI chips, duratium and, at the very end, prometheum.",
                "",
                "It needs eight machine cores, and no cable can power it. Only an &eEnderic Laser&r can, and each recipe charges it up before it finishes, so more lasers mean faster work.",
            ],
            "tasks": [{"item": "oritech:atomic_forge_block"}],
            "rewards": [{"xp": 25}, {"crate": "lantern"}],
        },
        side("prometheum", "Stolen Fire", {"tag": "c:ingots/prometheum", "title": "Prometheum Ingot",
                                           "icon": "oritech:prometheum_ingot"}, [
            "&ePrometheum&r is Oritech's last material: a Heisenberg Compensator and two Overcharged Crystals in the Atomic Forge.",
            "",
            "It makes the Ultimate Machine Core, and tools that never break.",
        ], icon="oritech:prometheum_ingot", crate="hearth"),
        side("accelerator", "Smash Things Together", item("oritech:accelerator_controller"), [
            "The &eParticle Accelerator&r sends an item around a ring of guide rings and motors. Get it up to speed, then send a second one into the ring, and the collision can make something new.",
            "",
            "Tachyon Absorbers around the crash catch the energy it throws off. The manual has the whole recipe list.",
        ], crate="hearth"),
        # ---- machine cores ----------------------------------------------------
        {
            "key": "cores", "title": "Machine Cores", "shape": "hexagon",
            "desc": [
                "Most Oritech machines are multiblocks. Place the machine, then right-click it: the spots that need &emachine cores&r light up for a few seconds.",
                "",
                "Right-click the machine with a core in hand and it places the next one for you, as long as the spot is clear. The &ePrimitive Machine Core&r is just planks around a crafting table.",
                "",
                "Better cores don't make a machine faster. They raise its quality, which decides how many addons it can take.",
            ],
            "tasks": [{"any": ["oritech:machine_core_1", "oritech:machine_core_2", "oritech:machine_core_3"],
                       "title": "Three machine cores, any tier", "icon": "oritech:machine_core_1", "count": 3}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        side("core_2", "Basic Machine Core", item("oritech:machine_core_2"), [
            "Copper around a piece of lapis. The first step up in quality.",
        ]),
        side("core_3", "Improved Machine Core", item("oritech:machine_core_3"), [
            "Carbon Fibre Strands around redstone. Spin coal dust in the Centrifuge for the strands.",
        ]),
        side("core_4", "Advanced Machine Core", item("oritech:machine_core_4"), [
            "Plating around &eEnderic Compound&r, which the Pulverizer grinds out of ender pearls or end stone.",
        ]),
        side("core_5", "Elite Machine Core", item("oritech:machine_core_5"), [
            "Adamant around an &eAdvanced Computing Engine&r from the Atomic Forge.",
        ]),
        side("core_6", "Ultra Machine Core", item("oritech:machine_core_6"), [
            "Duratium around a &eDubious Container&r. One step from the top.",
        ], crate="hearth"),
        {
            "key": "finale", "title": "The Ultimate Core",
            "shape": "hexagon", "size": 1.5, "icon": "oritech:machine_core_7",
            "desc": [
                "The &eUltimate Machine Core&r is Oritech's best: prometheum around a superconductor. It gives a machine the highest quality there is, and with it the most room for addons.",
                "",
                "It's also one of the pieces of the &eAllthemodium Alloy Paxel&r, the pack's capstone. The paxel quest gives it back once you've crafted the paxel.",
                "",
                "Your drills never stop and your lasers never miss. Not bad at all.",
            ],
            "tasks": [{"item": "oritech:machine_core_7"}],
            "rewards": [{"xp": 50}, {"crate": "ember"}, {"item": "oritech:duratium_ingot", "count": 16}],
        },
        # ---- addons -----------------------------------------------------------
        {
            "key": "addons", "title": "Addons", "shape": "hexagon",
            "desc": [
                "&eAddons&r are blocks that attach to a machine at its marked spots. A &eSpeed Addon&r makes it work half again as fast but costs more power, and an &eEfficiency Addon&r cuts its power use by a fifth.",
                "",
                "A connected addon's pink parts turn blue. If yours stays pink, right-click the machine.",
            ],
            "tasks": [{"any": ["oritech:machine_speed_addon", "oritech:machine_efficiency_addon"],
                       "title": "A Speed or Efficiency Addon", "icon": "oritech:machine_speed_addon"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        side("fluid_addon", "Fluid Addon", item("oritech:machine_fluid_addon"), [
            "Lets the Centrifuge work with liquids, and lets a Drone Port carry them.",
        ]),
        side("yield_addon", "Yield Addon", item("oritech:machine_yield_addon"), [
            "Doubles the bonus clumps from a Fragment Forge, and raises what a Destroyer or Enderic Laser gets from the blocks it breaks.",
        ]),
        {
            "key": "extender", "title": "Room for More",
            "desc": [
                "A &eMachine Addon Extender&r attaches like an addon and gives you more addon spots. How many extenders a machine can take depends on its core quality.",
                "",
                "That's where better machine cores pay off.",
            ],
            "tasks": [{"item": "oritech:machine_extender"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        side("capacitor_addon", "Capacitor Addon", item("oritech:machine_capacitor_addon"), [
            "Adds two million RF to a machine's battery and lets it take power in faster. Good for anything that works in bursts.",
        ]),
        side("acceptor_addon", "Acceptor Addon", item("oritech:machine_acceptor_addon"), [
            "Lets you feed power into the addon instead of the machine, which helps when the machine's own sides are crowded.",
        ]),
        side("processing_addon", "Processing Chamber", item("oritech:machine_processing_addon"), [
            "Each &eAuxiliary Processing Chamber&r lets a machine work one more recipe at a time, at the cost of efficiency.",
        ], crate="hearth"),
        side("proxy_addon", "Inventory Proxy Addon", item("oritech:machine_inventory_proxy_addon"), [
            "Gives pipes access to one chosen slot of the machine. Handy for the Assembler, where each input slot wants something different.",
        ]),
        side("redstone_addon", "Control Unit Addon", item("oritech:machine_redstone_addon"), [
            "Adds redstone control and comparator output to a machine. Right-click it to set what it does.",
        ]),
        side("burst_addon", "Burst Addon", item("oritech:machine_burst_addon"), [
            "Runs a processing machine at eight times its speed for a short burst. Push it too long and the machine overheats, so let it cool between runs.",
        ]),
        side("cap_extender", "Power Bank Addon Extender", item("oritech:capacitor_addon_extender"), [
            "An extender with a big battery built in: more addon spots and millions of RF of storage in one block.",
        ]),
        side("ultimate_addon", "Synergy Matrix", item("oritech:machine_ultimate_addon"), [
            "The best speed addon: three quarters faster, for only a little more power. Once you can make these, the Speed Addon retires.",
        ], crate="hearth"),
        side("splicer", "Addon Splicer", item("oritech:shrinker_block"), [
            "The &eAddon Splicer&r squeezes several addons into one block. Attach the addons to it through extenders, fill it with power, and it fuses them into a &eHeart of the Machine&r.",
            "",
            "It needs four machine cores and a lot of RF.",
        ]),
        side("combi_addon", "Heart of the Machine", item("oritech:machine_combi_addon"), [
            "Every bonus you spliced into it, in one addon. The catch: it only works as the first and only addon on a machine.",
        ], crate="hearth"),
        # ---- lasers and mining ------------------------------------------------
        {
            "key": "laser", "title": "Enderic Laser", "shape": "hexagon",
            "desc": [
                "The &eEnderic Laser&r fires a beam up to 128 blocks. Aim it with a &eTarget Designator&r and it mines everything in that line, passing through glass, until something stops it.",
                "",
                "Mined drops go into the laser's own inventory, and anything that doesn't fit is destroyed, so pipe them out.",
                "",
                "Aim it at a machine instead and it charges the machine, ignoring the usual input limit. Your biggest machines need power this way.",
            ],
            "tasks": [{"item": "oritech:laser_arm_block"}],
            "rewards": [{"xp": 25}, {"crate": "lantern"}, {"item": "alltheores:electrum_ingot", "count": 8}],
        },
        side("designator", "Target Designator", item("oritech:target_designator"), [
            "Right-click a block to save its position, then sneak and right-click a machine to give it that target.",
            "",
            "Lasers, Drone Ports and Power Poles all take their orders this way.",
        ], crate="hearth"),
        side("hunter_addon", "Hunter Addon", item("oritech:machine_hunter_addon"), [
            "Turns an Enderic Laser on living things instead of blocks. Each extra Hunter Addon reaches further. A mob farm with no moving parts.",
        ]),
        side("silk_addon", "Silk Touch Addon", item("oritech:machine_silk_touch_addon"), [
            "Destroyers and Enderic Lasers fitted with this pick up blocks whole, ore included. Feed the ore to a Fragment Forge for the best return.",
        ]),
        {
            "key": "fluxite", "title": "Fluxite",
            "desc": [
                "Many of Oritech's stronger machines need &eFluxite&r. Point a laser at amethyst clusters and they come off as fluxite instead.",
                "",
                "Aim one at a &eBudding Amethyst&r and it speeds up the growth without breaking the block, so one geode can keep you supplied.",
            ],
            "tasks": [{"item": "oritech:fluxite", "count": 8}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        side("enchanter", "Pick Your Enchantment", item("oritech:enchanter_block"), [
            "The &eStabilized Enchanter&r lets you choose exactly which enchantment to apply. It runs on power and on souls from &eArcane Catalysts&r within 16 blocks.",
            "",
            "Catalysts collect souls from mobs that die nearby. A laser on a catalyst lets it hold far more of them.",
        ]),
        side("spawner", "Make Your Own Spawner", item("oritech:spawner_controller_block"), [
            "The first mob to walk over a &eSpawner Controller&r decides what it spawns. Build &eSpawner Cages&r beneath it to the size it shows, and feed it souls.",
            "",
            "Choose that first mob with care: changing it means breaking the controller.",
        ]),
        {
            "key": "boulder", "title": "Ore Boulders", "icon": "minecraft:deepslate",
            "desc": [
                "Now and then you'll find a heap of deepslate studded with ore sitting on the surface. That's an &eore boulder&r, and it marks a &eresource node&r in the bedrock directly below.",
                "",
                "Common boulders sit over copper, iron, nickel and coal. Rarer ones sit over diamond, gold, emerald, uranium and platinum. The ores in the boulder hint at which.",
                "",
                "Resource nodes can't be broken and never run out. Press &eShift+B&r to drop a waypoint.",
            ],
            "tasks": [{"check": "Found one"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "drill", "title": "Endless Ore", "shape": "hexagon",
            "desc": [
                "The &eBedrock Extractor&r sits over resource nodes and mines them forever. It scans the 3x3 area beneath it, up to three blocks down, and picks one spot at random each cycle, so center it over as many nodes as you can.",
                "",
                "It needs 26 machine cores, and it only takes power from &eEnderic Lasers&r. Each ore costs about 20,000 RF.",
                "",
                "Right-click it to see which nodes it can reach.",
            ],
            "tasks": [{"item": "oritech:deep_drill_block"}],
            "rewards": [{"xp": 25}, {"crate": "lantern"}],
        },
        # ---- gantries ---------------------------------------------------------
        {
            "key": "frame", "title": "Machine Frames", "shape": "hexagon",
            "desc": [
                "A rectangle of &eMachine Frames&r, up to 64 blocks a side and empty in the middle, is the base for Oritech's gantry machines.",
                "",
                "Attach a Destroyer, Placer or Fertilizer to the frame and it rides along the rails, working on the layer of blocks below.",
            ],
            "tasks": [{"item": "oritech:machine_frame_block", "count": 16}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        side("destroyer", "Destroyer", item("oritech:destroyer_block"), [
            "The &eDestroyer&r breaks the blocks under its frame, one by one. Harder blocks take longer and more power.",
            "",
            "Build it over a field with a Crop Filter Addon and it's a harvester. Build it over stone and it's a quarry.",
        ], crate="hearth"),
        side("quarry_addon", "Quarry Addon", item("oritech:quarry_addon"), [
            "Widens what a Destroyer or Enderic Laser can reach, so one machine clears far more without moving.",
        ]),
        side("crop_filter", "Crop Filter Addon", item("oritech:crop_filter_addon"), [
            "Makes a Destroyer or Enderic Laser skip crops that aren't ripe yet. On a laser with a Hunter Addon, it filters animals too.",
        ]),
        side("placer", "Placer", item("oritech:placer_block"), [
            "The &ePlacer&r puts blocks from its inventory onto the layer below its frame. It plants seeds in farmland and saplings in dirt, and skips spots where the item won't go.",
        ]),
        side("fertilizer", "Fertilizer", item("oritech:fertilizer_block"), [
            "The &eFertilizer&r waters the farmland below its frame and speeds up whatever grows there, like weak bone meal.",
            "",
            "Give it Mineral Slurry instead of water and the effect gets much stronger.",
        ]),
        side("treefeller", "Tree Cutter", item("oritech:treefeller_block"), [
            "Set a &eTree Cutter&r in front of a tree and it takes the whole thing down, leaves and all, and keeps the saplings and fruit that drop.",
            "",
            "Pair it with a Placer for a tree farm that runs itself.",
        ]),
        # ---- gear and augments ------------------------------------------------
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
        side("jetpack", "Jetpack", item("oritech:jetpack"), [
            "Oritech's &eJetpack&r runs on power or on turbofuel, and it's faster on fuel. Fill its tank at an Equipment Charger.",
            "",
            "It's steel, gunpowder, leather and an Advanced Battery.",
        ], optional=False, crate="hearth"),
        side("elytra_jetpack", "Wings and Thrust", item("oritech:jetpack_elytra"), [
            "A jetpack built into an elytra. Its engine only fires while you're already gliding, so jump, spread your wings, then hold jump.",
        ]),
        side("exo_armor", "The Exo Suit", {"any": ["oritech:exo_helmet", "oritech:exo_chestplate", "oritech:exo_leggings",
                                                   "oritech:exo_boots"],
                                           "title": "Any piece of the Exo Suit", "icon": "oritech:exo_chestplate"}, [
            "Each piece of the &eExo Suit&r does one thing: the helmet gives night vision, the chestplate charges your powered gear, the leggings make you faster, and the boots stop all fall damage.",
        ], icon="oritech:exo_chestplate", optional=False, crate="hearth"),
        side("exo_jetpack", "Exo Jetpack", item("oritech:exo_jetpack"), [
            "A jetpack and an Exo Chestplate fused with ion thrusters and a tank: much more power, much more speed, and it still charges your gear.",
        ], crate="hearth"),
        side("portable_laser", "Portable Laser", item("oritech:portable_laser"), [
            "A laser you carry. One mode mines blocks from far away. The other makes things explode. &eShift+right-click&r switches between them.",
        ]),
        side("electric_mace", "Electric Mace", item("oritech:electric_mace"), [
            "A mace that calls down lightning when it hits. Like any mace, it hits harder the further you fall first.",
        ]),
        {
            "key": "augment", "title": "Better Than Flesh",
            "desc": [
                "The &eCybernetic Augmentation Center&r researches and installs permanent upgrades to your body: more health, more armor, faster mining, longer reach, and stranger things further up the tree.",
                "",
                "It needs ten machine cores, plus at least one &eCybernetic Research Station&r with three cores of its own. Walk into the center to open its research screen.",
                "",
                "Research takes materials and a great deal of power, so build it near your best generators.",
            ],
            "tasks": [{"item": "oritech:augment_application_block"}, {"item": "oritech:simple_augment_station"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "apply", "title": "Augmented",
            "desc": [
                "When a research finishes, install it from the center's screen. Installing costs a one-time fee in materials, and the augment stays with you after that, with no upkeep.",
                "",
                "Hold &eCtrl+G&r to open the augment wheel and switch any installed augment on or off. Handy when Night Vision gets a bit much.",
                "",
                "Augments can be removed, but what you paid to install them isn't refunded.",
            ],
            "tasks": [{"check": "Upgraded"}],
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
        side("prom_tools", "Tools That Never Break", {"any": ["oritech:promethium_pickaxe", "oritech:promethium_axe"],
                                                      "title": "A Prometheum Pickaxe or Battleaxe",
                                                      "icon": "oritech:promethium_pickaxe"}, [
            "Prometheum tools have no durability at all. The &ePickaxe&r switches between area mining and Silk Touch, and the &eBattleaxe&r fells a whole tree if you sneak while you chop.",
        ], icon="oritech:promethium_pickaxe", crate="hearth"),
        # ---- oil and plastic --------------------------------------------------
        {
            "key": "oil", "title": "Black Gold", "shape": "hexagon",
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
        side("tank", "Portable Tank", item("oritech:small_tank_block"), [
            "Holds 256 buckets and keeps them when you break it. Stack tanks and the fluid flows down into the lower ones.",
        ]),
        side("refinery_module", "Refinery Chamber Module", item("oritech:refinery_module_block"), [
            "The Refinery is built from three of these, and up to two more stacked on top give it extra outputs. Pull those fluids from the modules, not the base.",
        ]),
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
        side("plastic", "Plastic", {"tag": "c:plates/plastic", "title": "Plastic Sheet", "icon": "oritech:plastic_sheet",
                                    "count": 8}, [
            "Sand in a Centrifuge with a Fluid Addon and naphtha makes &ePolymer Resin&r, and resin smelts into &ePlastic&r.",
            "",
            "No oil yet? Packed wheat spun with water makes raw biopolymer, and spun again it makes plastic too.",
        ], icon="oritech:plastic_sheet", optional=False, crate="hearth"),
        side("turbofuel", "Turbofuel", item("oritech:still_fuel_bucket"), [
            "Diesel and fluxite in a Centrifuge with a Fluid Addon make &eTurbofuel&r. It burns longest of anything a Fuel Generator takes, and it's what makes jetpacks fly fastest.",
        ], crate="hearth"),
        # ---- logistics --------------------------------------------------------
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
        side("wrench", "Pipe Wrench", item("oritech:wrench"), [
            "The &ePipe Wrench&r turns pipe connections on and off, and sneak-right-click picks a pipe up instantly.",
            "",
            "It also lets you zipline along the cables between Power Poles.",
        ]),
        side("fluid_pipe", "Fluid Pipes", item("oritech:fluid_pipe", 8), [
            "Half a bucket every three ticks. Toggle an end to extract, just like item pipes.",
        ]),
        side("energy_pipe", "Energy Pipes", item("oritech:energy_pipe", 8), [
            "Carry up to 10,000 RF a tick. Oritech power is pushed: generators and storage send it out, and pipes never pull.",
        ]),
        side("energy_storage", "Portable Energy Storage", item("oritech:small_storage_block"), [
            "A million RF in a block that keeps its charge when you pick it up. A redstone signal stops it sending power.",
        ]),
        side("big_storage", "Large Energy Storage", item("oritech:large_storage_block"), [
            "Twenty million RF, with room for addons to make it bigger. It needs three machine cores and only sends power out of its red marker.",
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
    ],
}
