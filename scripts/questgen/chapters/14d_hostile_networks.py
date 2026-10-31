def model(path):
    return {"hostilenetworks:data_model": f"hostilenetworks:{path}"}


WORLDS = {"overworld": "Overworld", "nether": "Nether", "end": "Ender"}

# Every data model that loads in this pack: (path, mob, sim cost in FE a tick, what it fabricates).
# Left out: the bat (its model needs Reliquary), the block models (switched off in
# config/hostilenetworks.cfg), and the Twilight Forest, Thermal and Ars Nouveau mobs, whose mods
# aren't in the pack.
MODELS = {
    "overworld": [
        ("zombie", "Zombie", 128, "Rotten flesh, iron, carrots and potatoes."),
        ("skeleton", "Skeleton", 128, "Arrows, bones and the odd skull."),
        ("creeper", "Creeper", 128, "Gunpowder by the stack, and creeper heads."),
        ("spider", "Spider", 128, "String, spider eyes and cobwebs."),
        ("slime", "Slime", 128, "Slimeballs and slime blocks."),
        ("drowned", "Drowned", 128, "Rotten flesh and copper."),
        ("phantom", "Phantom", 128, "Phantom membrane, without the sleepless nights."),
        ("witch", "Witch", 256, "Redstone, glowstone, sugar, spider eyes and bottles: a brewer's shopping list."),
        ("breeze", "Breeze", 256, "Breeze rods, for wind charges and the mace."),
        ("guardian", "Guardian", 256, "Prismarine crystals and fish."),
        ("vindicator", "Vindicator", 512, "Emeralds, and an iron axe now and then."),
        ("evoker", "Evoker", 1024, "Totems of Undying and emeralds."),
        ("elder_guardian", "Elder Guardian", 1024, "Wet sponges, prismarine and a lot of fish."),
        ("iron_golem", "Iron Golem", 1024, "Iron ingots and poppies."),
        ("chicken", "Chicken", 64, "Raw chicken and feathers."),
        ("cow", "Cow", 64, "Raw beef and leather."),
        ("mooshroom", "Mooshroom", 64, "Beef, leather and both kinds of mushroom."),
        ("pig", "Pig", 64, "Raw porkchops."),
        ("sheep", "Sheep", 64, "Wool in every color, mutton and bezoars."),
        ("rabbit", "Rabbit", 64, "Rabbit hide, meat and rabbit's feet."),
        ("polar_bear", "Polar Bear", 64, "Fish and polar bear gall bladders."),
        ("snow_golem", "Snow Golem", 64, "Snowballs."),
        ("cod", "Cod", 32, "Cod, roe and bone meal."),
        ("squid", "Squid", 32, "Ink sacs and calamari."),
        ("glow_squid", "Glow Squid", 32, "Glow ink sacs and glowing calamari."),
    ],
    "nether": [
        ("blaze", "Blaze", 256, "Blaze rods, with no fortress to find."),
        ("ghast", "Ghast", 256, "Ghast tears, the hardest drop in the Nether to collect by hand, and gunpowder."),
        ("magma_cube", "Magma Cube", 256, "Magma cream."),
        ("hoglin", "Hoglin", 256, "Porkchops and leather."),
        ("zombified_piglin", "Zombified Piglin", 256, "Rotten flesh and gold ingots."),
        ("wither_skeleton", "Wither Skeleton", 768, "Wither skeleton skulls, skull fragments, bones and coal."),
    ],
    "end": [
        ("enderman", "Enderman", 512, "Ender pearls by the stack, and an End Crystal."),
        ("shulker", "Shulker", 512, "Shulker shells for every shulker box you'll ever want, and end rods."),
        ("wither", "Wither", 2560, "A nether star, every time."),
        ("warden", "Warden", 2560, "Echo shards, a warden tendril and sculk catalysts."),
        ("ender_dragon", "Ender Dragon", 4096, "Dragon's breath, and a dragon egg of your very own."),
        ("artifacts/mimic", "Mimic", 2560, "Any artifact a Mimic can drop. Pick the one you want on the fabricator's screen."),
        ("allthemodium/piglich", "Piglich", 16384, "Piglich Hearts, four at a time, for the Allthemodium alloys."),
    ],
}


def _a(word):
    return "an" if word[0] in "AEIOU" else "a"


def _reward(cost):
    if cost >= 1024:
        return [{"xp": 25}, {"crate": "lantern"}]
    if cost >= 256:
        return [{"xp": 15}, {"crate": "hearth"}]
    return [{"xp": 10}, {"crate": "kindling"}]


def model_quest(world, path, mob, cost, makes):
    return {
        "key": f"model_{path.split('/')[-1]}", "title": f"{mob} Model", "optional": True,
        "icon": "hostilenetworks:data_model", "icon_components": model(path),
        "desc": [
            makes,
            "",
            f"Right-click {_a(mob)} {mob} with a &eModel Framework&r to attune one. Simulating it costs {cost:,} FE a tick, and every run makes a &eGeneralized {WORLDS[world]} Prediction&r as well.",
        ],
        "tasks": [{"item": "hostilenetworks:data_model", "components": model(path), "title": f"{mob} Data Model",
                   "icon": "hostilenetworks:blank_data_model"}],
        "rewards": _reward(cost),
    }


def _per_row(n):
    rows = -(-n // 9)
    return -(-n // rows)


CHAPTER = {
    "file": "hostile_networks",
    "group": "hum",
    "title": "Hostile Neural Networks",
    "subtitle": "Teach a model a mob, then farm it without the fight",
    "icon": "hostilenetworks:sim_chamber",
    "layout": {"lines": [
        {"flow": ["learner", "sim", "fabricator", "data_center"],
         "branches": {"sim": {"up": ["matrix"], "down": ["wither_prediction"]}}},
        {"rows": ["pred_overworld", "pred_nether", "pred_end"]},
    ] + [
        {"rows": [f"model_{p.split('/')[-1]}" for p, *_ in MODELS[w]], "per_row": _per_row(len(MODELS[w]))}
        for w in WORLDS
    ]},
    "quests": [
        {
            "key": "learner", "shape": "hexagon", "size": 1.5, "title": "Deep Learner",
            "desc": [
                "Hostile Neural Networks grows mob drops from simulations instead of seeds.",
                "",
                "Craft a &eDeep Learner&r and a &eModel Framework&r. Right-click a mob with the framework to attune it, put the model in the learner, and wear the learner in its Curios slot. &eShift+U&r opens it.",
                "",
                "Then go fight. Every kill of that mob teaches the model a little more.",
            ],
            "tasks": [{"item": "hostilenetworks:deep_learner"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "matrix", "title": "Prediction Matrix",
            "desc": [
                "Every simulation uses up one &ePrediction Matrix&r, so the chamber needs a steady supply. Make them in bulk.",
            ],
            "tasks": [{"item": "hostilenetworks:prediction_matrix", "count": 16}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}],
        },
        {
            "key": "sim", "title": "Train a Model",
            "desc": [
                "Put a trained model and a &ePrediction Matrix&r in a powered &eSimulation Chamber&r and it fights the battle for you, producing that mob's &ePrediction&r. A &eLoot Fabricator&r turns predictions into real drops.",
                "",
                "New models are Faulty, and a Faulty model can't be simulated. Get a few kills in first. After that, the chamber's Training Mode can level a model up for you, at the cost of making nothing while it does.",
            ],
            "tasks": [{"item": "hostilenetworks:sim_chamber"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "wither_prediction", "title": "A Wither in a Box", "shape": "hexagon",
            "icon": "hostilenetworks:prediction", "icon_components": model("wither"),
            "desc": [
                "Right-click the Wither with a Model Framework (carefully), then train the model past Faulty with a few more Wither fights. Simulating it costs 2,560 FE a tick, so have power to spare.",
                "",
                "A &eWither Prediction&r is one of the pieces of the &eAllthemodium Alloy Paxel&r. The paxel quest gives it back once you've crafted the paxel.",
            ],
            "tasks": [{"item": "hostilenetworks:prediction", "components": model("wither"), "title": "Wither Prediction"}],
            "rewards": [{"xp": 50}, {"crate": "ember"}],
        },
        {
            "key": "fabricator", "title": "Loot Fabricator",
            "desc": [
                "The &eLoot Fabricator&r turns Predictions into the real thing. Pick which of the mob's drops you want on its screen.",
                "",
                "A &eFabrication Directive&r copies one fabricator's choices onto another.",
            ],
            "tasks": [{"item": "hostilenetworks:loot_fabricator"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "data_center", "title": "The Data Center", "shape": "hexagon",
            "desc": [
                "The top of the line. A &eData Center&r runs up to twenty-five Self Aware models at once, all feeding one output.",
                "",
                "It needs a hollow 7x7x7 shell: an obsidian floor, black stained glass walls and ceiling, and the controller set into the bottom of a wall, facing out. &eData Center IO Ports&r can stand in for any wall or ceiling block to move power, models and items.",
            ],
            "tasks": [{"item": "hostilenetworks:data_center"}],
            "rewards": [{"xp": 25}, {"crate": "lantern"}],
        },
    ] + [
        {
            "key": f"pred_{w}", "title": f"Generalized {name} Prediction", "optional": True,
            "desc": [
                f"Many models turn out a &eGeneralized {name} Prediction&r with every simulation, on top of their own. Each model's quest says which kind it makes.",
                "",
                {
                    "overworld": "They craft into everyday drops: bones, gunpowder, rotten flesh, iron and more. Four of them around netherrack make a Nether one.",
                    "nether": "They craft into blaze rods, ghast tears, gold, nether wart and soul sand. Four of them around end stone make an Ender one.",
                    "end": "They craft into ender pearls, end stone and chorus fruit.",
                }[w],
            ],
            "tasks": [{"item": f"hostilenetworks:{w}_prediction"}],
            "rewards": [{"xp": 15}, {"crate": "hearth"}],
        }
        for w, name in WORLDS.items()
    ] + [model_quest(w, *m) for w in WORLDS for m in MODELS[w]],
}
