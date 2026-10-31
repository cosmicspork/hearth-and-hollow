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
    "subtitle": "Industry on a grand scale",
    "icon": "oritech:basic_generator_block",
    "theme": "oritech",
    # The machine ladder and the core ladder carry the order. Generators, addons and odds and
    # ends need none, so they sit in blocks; the laser and the frame machines fan out briefly.
    "layout": {
        "lines": [
            {"flow": ["start", "generator", "pulverizer", "furnace", "foundry", "assembler", "centrifuge", "fragment",
                      "atomic_forge"]},
            {"flow": ["cores", "core_2", "core_3", "core_4", "core_5", "core_6", "finale"]},
            {"rows": ["lava_gen", "steam_engine", "boiler", "fuel_gen", "bio_gen", "biomass", "solar", "reactor",
                      "adamant", "components", "cooler", "prometheum", "accelerator"],
             "per_row": 7},
            {"rows": ["addons", "extender", "fluid_addon", "yield_addon", "capacitor_addon", "acceptor_addon",
                      "processing_addon", "proxy_addon", "redstone_addon", "burst_addon", "cap_extender",
                      "ultimate_addon", "splicer", "combi_addon"],
             "per_row": 7},
            {"flow": ["laser", "fluxite", "drill"]},
            {"flow": ["frame", ["destroyer", "placer", "fertilizer"]]},
            {"rows": ["designator", "hunter_addon", "silk_addon", "enchanter", "spawner", "quarry_addon",
                      "crop_filter", "treefeller"]},
        ],
    },
    "quests": [
        {
            "key": "start", "title": "Oritech",
            "shape": "hexagon", "size": 1.5, "icon": "oritech:basic_generator_block",
            "desc": [
                "Oritech is industry on a grand scale: multiblock machines, lasers, oil refineries, and a drill that pulls ore up from below the bedrock forever.",
                "",
                "It runs on &enickel&r. Here nickel comes from AllTheOres veins, and the ore boulders you'll find on the surface often have some showing.",
                "",
                "Bring copper, iron, coal and redstone too.",
                "",
                "Oritech's own manual, the &eOracle Index&r, has a page for nearly every block: hover an Oritech item and hold &eAlt&r. Its key is unbound here; set &eOpen Oracle Index&r under Options, Controls, Key Binds if you want one.",
            ],
            "tasks": [{"tag": "c:ingots/nickel", "title": "Nickel Ingot", "icon": "alltheores:nickel_ingot",
                       "count": 8}],
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
        side("adamant", "Adamant", {"tag": "c:ingots/adamant", "title": "Adamant Ingot", "icon": "oritech:adamant_ingot",
                                    "count": 4}, [
            "A diamond and a nickel ingot in the Foundry make &eAdamant&r. The Assembler, the hand drill and the better machine cores all ask for it.",
            "",
            "The Foundry's other alloys are worth knowing: iron and coal dust for steel, gold and redstone for electrum, nickel and fluxite for energite.",
        ], icon="oritech:adamant_ingot"),
        side("components", "Nuts and Bolts", {"any": ["oritech:motor", "oritech:magnetic_coil", "oritech:processing_unit"],
                                              "title": "A motor, coil or processing unit", "icon": "oritech:motor"}, [
            "Most Oritech machines are built from a few parts: &eMagnetic Coils&r from nickel and steel, &eMotors&r from coils and steel, and later &eProcessing Units&r from plastic, carbon fibre, electrum and redstone.",
            "",
            "Keep a stack of each. You'll use them everywhere.",
        ], icon="oritech:motor"),
        side("cooler", "Industrial Chiller", item("oritech:cooler_block"), [
            "The &eIndustrial Chiller&r turns water into ice, lava into obsidian and steam into snow. Reactors that cool with absorbers need its ice.",
            "",
            "It needs one machine core, and it works better somewhere cold.",
        ]),
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
        {
            "key": "drill", "title": "Endless Ore", "shape": "hexagon",
            "desc": [
                "The &eBedrock Extractor&r sits over resource nodes and mines them forever. It scans the 3x3 area beneath it, up to three blocks down, and picks one spot at random each cycle, so center it over as many nodes as you can.",
                "",
                "It needs 26 machine cores, and it only takes power from &eEnderic Lasers&r. Each ore costs about 20,000 RF.",
                "",
                "Right-click it to see which nodes it can reach.",
                "",
                "Finding nodes: now and then a heap of deepslate studded with ore sits on the surface. That &eore boulder&r marks resource nodes in the bedrock right below it. Common boulders sit over copper, iron, nickel and coal; rarer ones over diamond, gold, emerald, uranium and platinum. Press &eShift+B&r to drop a waypoint.",
            ],
            "tasks": [{"item": "oritech:deep_drill_block"}],
            "rewards": [{"xp": 25}, {"crate": "lantern"}],
        },
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
        side("placer", "Placer", item("oritech:placer_block"), [
            "The &ePlacer&r puts blocks from its inventory onto the layer below its frame. It plants seeds in farmland and saplings in dirt, and skips spots where the item won't go.",
        ]),
        side("fertilizer", "Fertilizer", item("oritech:fertilizer_block"), [
            "The &eFertilizer&r waters the farmland below its frame and speeds up whatever grows there, like weak bone meal.",
            "",
            "Give it Mineral Slurry instead of water and the effect gets much stronger.",
        ]),
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
        side("quarry_addon", "Quarry Addon", item("oritech:quarry_addon"), [
            "Widens what a Destroyer or Enderic Laser can reach, so one machine clears far more without moving.",
        ]),
        side("crop_filter", "Crop Filter Addon", item("oritech:crop_filter_addon"), [
            "Makes a Destroyer or Enderic Laser skip crops that aren't ripe yet. On a laser with a Hunter Addon, it filters animals too.",
        ]),
        side("treefeller", "Tree Cutter", item("oritech:treefeller_block"), [
            "Set a &eTree Cutter&r in front of a tree and it takes the whole thing down, leaves and all, and keeps the saplings and fruit that drop.",
            "",
            "Pair it with a Placer for a tree farm that runs itself.",
        ]),
    ],
}
