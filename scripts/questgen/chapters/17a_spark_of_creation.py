SPARK = "hearthandhollow:spark_of_creation"

# The singularities Extended Crafting is set up with in config/extendedcrafting/singularities.
# The Ultimate Singularity takes one of each, so this list must match that folder.
SINGULARITIES = [
    ("iron", "Iron"), ("gold", "Gold"), ("copper", "Copper"), ("coal", "Coal"), ("redstone", "Redstone"),
    ("lapis_lazuli", "Lapis Lazuli"), ("glowstone", "Glowstone"), ("diamond", "Diamond"), ("emerald", "Emerald"),
    ("tin", "Tin"), ("lead", "Lead"), ("silver", "Silver"), ("nickel", "Nickel"), ("aluminum", "Aluminum"),
    ("platinum", "Platinum"), ("bronze", "Bronze"), ("steel", "Steel"), ("electrum", "Electrum"), ("invar", "Invar"),
]
ALLOYS = {"bronze", "steel", "electrum", "invar"}


def singularity(key, name):
    sid = {"extendedcrafting:singularity_id": f"extendedcrafting:{key}"}
    source = (f"{name} is an alloy. Press &eR&r on the ingot to see what makes it." if key in ALLOYS
              else "A Mystical Agriculture farm makes short work of it.")
    return {
        "key": f"sing_{key}", "title": f"{name} Singularity", "optional": True,
        "icon": "extendedcrafting:singularity", "icon_components": sid,
        "desc": [f"5,000 {name} in the Quantum Compressor.", "", source],
        "tasks": [{"item": "extendedcrafting:singularity", "components": sid, "title": f"{name} Singularity",
                   "icon": "extendedcrafting:singularity"}],
        "rewards": [{"xp": 25}, {"crate": "lantern"}],
    }


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
    "file": "spark_of_creation",
    "group": "long",
    "title": "The Spark of Creation",
    "subtitle": "A little of everything, crushed into one spark, and creative items from it",
    "icon": SPARK,
    "layout": {
        "lines": [
            {"flow": ["ultimate_table", "compressor"]},
            {"rows": [f"sing_{k}" for k, _ in SINGULARITIES], "per_row": 10},
            {"flow": ["ultimate_singularity", "ultimate_ingot", "spark"]},
            {"rows": ["creative_cube", "creative_jetpack", "creative_chem_tank", "creative_fluid_tank", "creative_bin",
                      "creative_cell", "creative_controller", "creative_grid", "creative_battery"], "per_row": 9},
        ],
    },
    # The Spark also takes an Antimatter Pellet from Mekanism Reactors.
    "links": [{"quest": "mekanism_reactors:antimatter", "pos": (4.5, 6.75)}],
    "quests": [
        {
            "key": "ultimate_table", "title": "The Biggest Table", "shape": "hexagon", "size": 1.5,
            "icon": "extendedcrafting:ultimate_table",
            "desc": [
                "The &eUltimate Crafting Table&r is 9x9: two Elite tables, a block of emerald and Ultimate Components.",
                "",
                "Everything in this chapter is made on one. The tables before it are in &eAllthemodium Ascent&r.",
            ],
            "tasks": [{"item": "extendedcrafting:ultimate_table"}],
            "rewards": [{"xp": 25}, {"crate": "lantern"}],
        },
        {
            "key": "compressor", "title": "Quantum Compression", "shape": "hexagon",
            "icon": "extendedcrafting:compressor",
            "desc": [
                "The &eQuantum Compressor&r crushes 5,000 of one material into a &eSingularity&r, using 5,000,000 FE to do it.",
                "",
                "It needs an &eUltimate Catalyst&r in its catalyst slot, and it keeps it.",
                "",
                "There are nineteen singularities to make. They'll take a while, so set up farms and let the compressor chew.",
            ],
            "tasks": [{"item": "extendedcrafting:compressor"}, {"item": "extendedcrafting:ultimate_catalyst"}],
            "rewards": [{"xp": 25}, {"crate": "lantern"}],
        },
        *[singularity(k, n) for k, n in SINGULARITIES],
        {
            "key": "ultimate_singularity", "title": "A Little of Everything", "shape": "hexagon",
            "icon": "extendedcrafting:ultimate_singularity",
            "desc": [
                "One of every singularity, on the Ultimate Crafting Table, makes the &eUltimate Singularity&r.",
                "",
                "Press &eR&r on it to see the full set.",
            ],
            "tasks": [{"item": "extendedcrafting:ultimate_singularity"}],
            "rewards": [{"xp": 50}, {"crate": "ember"}],
        },
        {
            "key": "ultimate_ingot", "title": "The Ultimate Ingot", "shape": "hexagon",
            "icon": "extendedcrafting:the_ultimate_ingot",
            "desc": [
                "Set the Ultimate Singularity in the middle of the Ultimate Crafting Table, ring it with twelve &eCrystaltine Ingots&r, and put a &eBlock of Black Iron&r in each corner of the ring.",
                "",
                "Out comes &eThe Ultimate Ingot&r. Hold on to it.",
            ],
            "tasks": [{"item": "extendedcrafting:the_ultimate_ingot"}],
            "rewards": [{"xp": 50}, {"crate": "ember"}],
        },
        {
            "key": "spark", "title": "Break the Universe", "shape": "hexagon", "size": 2.0, "wide": True, "icon": SPARK,
            "desc": [
                "A little of everything in one ingot, and a pellet of antimatter from &eMekanism Reactors&r. That's enough to tear a hole in the world.",
                "",
                "On the Ultimate Crafting Table: The Ultimate Ingot in the middle, the &eAntimatter Pellet&r above it, Crystaltine around them, Atomic Alloy on the diagonals, Ultimate Control Circuits in the middle of each edge and Nether Stars in the corners. Press &eR&r on the Spark for the exact layout.",
                "",
                "The Spark is a catalyst. It never gets used up, and with the best of each tech line it makes &dcreative&r items: endless power, an endless jetpack, tanks and bins that never run dry.",
            ],
            "tasks": [{"item": SPARK}],
            "rewards": [{"xp_levels": 30}, {"crate": "ember", "count": 3},
                        {"command": '/tellraw @a ["",{"text":"{p}","color":"gold"},{"text":" has made a Spark of Creation!","color":"light_purple"}]'}],
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
