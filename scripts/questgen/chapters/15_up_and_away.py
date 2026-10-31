def jetpack(name):
    return {"ironjetpacks:jetpack_id": f"ironjetpacks:{name}"}


WAYSTONES = ["waystones:waystone", "waystones:mossy_waystone", "waystones:sandy_waystone",
             "waystones:blackstone_waystone", "waystones:deepslate_waystone", "waystones:end_stone_waystone",
             "waystones:red_nether_bricks_waystone", "waystones:prismarine_waystone", "waystones:purpur_waystone",
             "waystones:mud_bricks_waystone"]

SHARESTONES = ["waystones:sharestone"] + [f"waystones:{c}_sharestone" for c in (
    "orange", "magenta", "light_blue", "yellow", "lime", "pink", "gray", "light_gray", "cyan",
    "purple", "blue", "brown", "green", "red", "black")]

CHAPTER = {
    "file": "up_and_away",
    "group": "hum",
    "title": "Up & Away",
    "subtitle": "Jetpacks, wings, elevators and a waystone network of your own",
    "icon": "minecraft:feather",
    # Separate ways of getting about, so none waits on the others.
    "layout": {
        "lines": [
            {"spine": ["start", "emerald", "allthemodium", "vibranium", "unobtainium"]},
            {"flow": ["elytra", ["hdpe_elytra", "exo_elytra"]]},
            {"spine": ["waystone", "warp_stone", "bound_scroll"],
             "branches": {"waystone": {"up": ["sharestone"], "down": ["warp_plate"]}}},
            {"rows": ["elevator", "shrink"]},
        ],
    },
    "quests": [
        {
            "key": "start", "title": "Up & Away",
            "shape": "hexagon", "size": 1.5, "icon": "ironjetpacks:jetpack", "icon_components": jetpack("wood"),
            "desc": [
                "Walking is lovely. Flying is faster.",
                "",
                "Your first &eJetpack&r can be made of wood: planks, a leather strap and a few simple parts. Wear it in your chest slot or a Curios slot (&eShift+G&r), then hold jump to lift off.",
                "",
                "A wooden jetpack is slow and drinks its charge quickly, but it gets you onto the roof. Better ones are built around the one before.",
                "",
                "Jetpacks run on FE. Anything that charges items will top one up: a &eWireless Player Charger&r by the door, a Powah &ePlayer Transmitter&r, or a &eFlux Controller&r, all in &eSparks&r. Search \"hover\" in Key Binds for the engine, hover and throttle keys. Hover mode lets you hang in the air while you build.",
            ],
            "tasks": [{"item": "ironjetpacks:jetpack", "title": "Any jetpack"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "elytra", "title": "Wings of the End", "shape": "hexagon", "icon": "minecraft:elytra",
            "desc": [
                "An &eElytra&r hangs in the ship moored beside some &eEnd Cities&r, out on the outer islands. Jump off something high, press jump again, and glide. Fireworks give you a boost in the air.",
                "",
                "No ship in sight? Oritech's &eParticle Accelerator&r collides feathers with a saddle and makes one.",
                "",
                "Hang on to a spare. Refined Storage's &eInterdimensional Wireless Transmitter&r takes one, and so does Oritech's &eBoosted Elytra&r.",
            ],
            "tasks": [{"item": "minecraft:elytra"}],
            "rewards": [{"xp": 25}, {"crate": "lantern"}, {"item": "minecraft:firework_rocket", "count": 32}],
        },
        {
            "key": "hdpe_elytra", "title": "Plastic Wings", "optional": True,
            "desc": [
                "Mekanism's &eHDPE Reinforced Elytra&r is an elytra wrapped in five HDPE sheets and two atomic alloy.",
                "",
                "It flies like any elytra but lasts longer between repairs.",
            ],
            "tasks": [{"item": "mekanism:hdpe_elytra"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "exo_elytra", "title": "Wings With an Engine", "optional": True,
            "desc": [
                "Oritech's &eBoosted Exo Elytra&r builds an elytra into the Exo Jetpack, with processing units and gunpowder.",
                "",
                "Its engine only fires while you're already gliding, so take off the usual way and let it carry you from there.",
            ],
            "tasks": [{"item": "oritech:jetpack_exo_elytra"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "elevator", "title": "Going Up", "shape": "hexagon",
            "icon": "elevatorid:elevator_white",
            "desc": [
                "An &eElevator&r is eight wool around an ender pearl. Stack two or more in a shaft, one above the other, with room to stand on each.",
                "",
                "Stand on one and jump to go up to the next. Sneak to go down. They can be a long way apart, and the colors don't have to match.",
                "",
                "Elevators can also be disguised as other blocks, so the shaft can look like part of the wall.",
            ],
            "tasks": [{"tag": "elevatorid:elevators", "count": 2, "title": "Two elevators",
                       "icon": "elevatorid:elevator_white"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "shrink", "title": "Honey, I Shrunk Me", "optional": True,
            "desc": [
                "The &ePersonal Shrinking Device&r makes you small. Right-click it to pick a size, then sneak and right-click to shrink. Do it again to grow back.",
                "",
                "Small you fits through gaps and under slabs, which is half the fun of building a tiny house inside a big one.",
                "",
                "It runs on FE, a little each time, so charge it like your jetpack. It works on animals too.",
            ],
            "tasks": [{"item": "shrink:shrinking_device"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "waystone", "title": "A Waystone of Your Own", "shape": "hexagon",
            "icon": "waystones:waystone",
            "desc": [
                "The waystones in villages are handy, but they're never quite where you live. Make your own.",
                "",
                "A &eWarp Stone&r takes amethyst shards, ender pearls and an emerald. Set it in stone bricks over a row of obsidian, and you have a &eWaystone&r.",
                "",
                "Put one at home, one at the mine, one at the farm. Traveling between them costs nothing in this pack.",
            ],
            "tasks": [{"any": WAYSTONES, "title": "Any waystone", "icon": "waystones:waystone"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "sharestone", "title": "Sharestones", "optional": True,
            "icon": "waystones:red_sharestone",
            "desc": [
                "A &eSharestone&r is a waystone with a color. It takes you to any other sharestone of the same color.",
                "",
                "Give each part of your world its own color: blue for the coast, green for the farms. Playing with friends? A shared color makes a meeting place everyone can reach.",
            ],
            "tasks": [{"any": SHARESTONES, "title": "Any sharestone", "icon": "waystones:red_sharestone"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "warp_plate", "title": "Warp Plates",
            "desc": [
                "A &eWarp Plate&r links to exactly one other plate. Step on one and you arrive at its partner.",
                "",
                "To pair them, put a &eDormant Shard&r into the first plate. It comes out attuned. Carry the &eAttuned Shard&r to the second plate and slot it in.",
                "",
                "Plates carry animals too, so they're perfect for moving a herd to the new barn.",
            ],
            "tasks": [{"item": "waystones:warp_plate", "count": 2}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "bound_scroll", "title": "A Ticket Home",
            "desc": [
                "A &eBlank Scroll&r is paper, a feather and gold nuggets. Use it on a waystone and it becomes a &eBound Scroll&r that takes you to that waystone.",
                "",
                "Keep a few bound to home in your backpack. A &eWarp Scroll&r lets you pick any waystone you know instead.",
            ],
            "tasks": [{"item": "waystones:bound_scroll"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "warp_stone", "title": "Waystones in Your Pocket",
            "desc": [
                "Keep a &eWarp Stone&r of your own instead of setting it in a waystone. Hold right-click to charge it up, and you can jump to any waystone you know from wherever you're standing.",
                "",
                "It wears out with use, so carry a spare on long trips.",
            ],
            "tasks": [{"item": "waystones:warp_stone"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "emerald", "title": "Faster, Higher",
            "shape": "hexagon", "icon": "ironjetpacks:jetpack", "icon_components": jetpack("emerald"),
            "desc": [
                "Each jetpack is crafted around one from the tier below, and it keeps its charge when you do.",
                "",
                "Stone or copper, then iron, gold, diamond, and finally &eEmerald&r. Along the way, steel, electrum and other metals offer a few alternatives at each step.",
                "",
                "Each tier holds more charge and flies faster. Hover over a jetpack to compare.",
            ],
            "tasks": [{"item": "ironjetpacks:jetpack", "components": jetpack("emerald"), "title": "An Emerald Jetpack"}],
            "rewards": [{"xp": 25}, {"crate": "lantern"},
                        {"item": "ironjetpacks:thruster", "components": jetpack("allthemodium")}],
        },
        {
            "key": "allthemodium", "title": "Above the Clouds",
            "shape": "hexagon", "size": 1.5, "icon": "ironjetpacks:jetpack", "icon_components": jetpack("allthemodium"),
            "desc": [
                "Past emerald, Hearth & Hollow adds jetpacks of its own, made from allthemodium, vibranium and unobtainium.",
                "",
                "The &eAllthemodium Jetpack&r is built around your emerald one. It's tougher, faster and holds more charge.",
                "",
                "With elevators in the walls, waystones on every hill and this on your back, the whole world is a short trip away.",
            ],
            "tasks": [{"item": "ironjetpacks:jetpack", "components": jetpack("allthemodium"),
                       "title": "An Allthemodium Jetpack"}],
            "rewards": [{"xp": 50}, {"crate": "ember"},
                        {"item": "ironjetpacks:thruster", "components": jetpack("vibranium")}],
        },
        {
            "key": "vibranium", "title": "Vibranium Jetpack", "optional": True,
            "icon": "ironjetpacks:jetpack", "icon_components": jetpack("vibranium"),
            "desc": [
                "Built around an Allthemodium Jetpack with vibranium ingots. More armor, more speed, more charge.",
            ],
            "tasks": [{"item": "ironjetpacks:jetpack", "components": jetpack("vibranium"),
                       "title": "A Vibranium Jetpack"}],
            "rewards": [{"xp": 10}, {"crate": "ember"}],
        },
        {
            "key": "unobtainium", "title": "Unobtainium Jetpack", "optional": True,
            "icon": "ironjetpacks:jetpack", "icon_components": jetpack("unobtainium"),
            "desc": [
                "The top of the line, built around a Vibranium Jetpack. The fastest thing in the sky, and the toughest thing to wear on your back.",
            ],
            "tasks": [{"item": "ironjetpacks:jetpack", "components": jetpack("unobtainium"),
                       "title": "An Unobtainium Jetpack"}],
            "rewards": [{"xp": 10}, {"crate": "ember"}],
        },
    ],
}
