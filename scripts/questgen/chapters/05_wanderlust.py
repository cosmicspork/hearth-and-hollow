TEN_BIOMES = [
    ("sakura_grove", "terralith:sakura_grove", "Sakura Grove", "minecraft:cherry_sapling",
     "Cherry trees in full bloom, and pink petals drifting over everything."),
    ("lavender_forest", "terralith:lavender_forest", "Lavender Forest", "minecraft:allium",
     "Purple as far as you can see. Bring a friend to show it to."),
    ("moonlight_grove", "terralith:moonlight_grove", "Moonlight Grove", "minecraft:white_tulip",
     "Pale flowers under tall trees. It's at its best after dark."),
    ("birch_taiga", "terralith:birch_taiga", "Birch Taiga", "minecraft:birch_sapling",
     "White birch among the spruce, cool and quiet."),
    ("shrubland", "terralith:shrubland", "Shrubland", "minecraft:dead_bush",
     "Dry scrub and low bushes. Not much shade, but a long view."),
    ("steppe", "terralith:steppe", "Steppe", "minecraft:short_grass",
     "Wide, open grassland that goes on and on. Good riding country."),
    ("highlands", "terralith:highlands", "Highlands", "minecraft:stone",
     "Rolling high ground of grass and bare stone. Climb a ridge and look around."),
    ("orchid_swamp", "terralith:orchid_swamp", "Orchid Swamp", "minecraft:blue_orchid",
     "A swamp that someone decorated, full of blue orchids."),
    ("lush_desert", "terralith:lush_desert", "Lush Desert", "minecraft:cactus",
     "Sand, but with grass and green scrub in it. Easier on the feet than a plain desert."),
    ("alpine_grove", "terralith:alpine_grove", "Alpine Grove", "minecraft:spruce_sapling",
     "Spruce on cold mountain slopes. Bring a paraglider for the way down."),
]


def biome_quest(key, biome, title, icon, line):
    return {
        "key": f"biome_{key}", "title": title, "icon": icon,
        "desc": [line, "", "Your &eNature's Compass&r can find it."],
        "tasks": [{"biome": biome, "title": f"Visit a {title}", "icon": icon}],
        "rewards": [{"xp": 10}, {"crate": "kindling"}],
    }


CHAPTER = {
    "file": "wanderlust",
    "group": "world",
    "title": "Wanderlust",
    "subtitle": "Strange biomes, sky islands, old towns and older ruins",
    "icon": "paraglider:paraglider",
    # A grid: the world hands these out in whatever order you wander into them.
    "layout": {"grid": [
        ["arrive"],
        ["wanderlust", "lootr", "glider", "orbs", "goddess", "horned"],
        [f"biome_{b[0]}" for b in TEN_BIOMES[:5]],
        [f"biome_{b[0]}" for b in TEN_BIOMES[5:]],
        ["skylands", "biomes", "volcano"],
        ["villages", "rs_villages", "tavern", "fortified", "waystones", "sharestone"],
        ["ruins", "towers", "sky", "witch_tower", "witch_hut", "temple"],
        ["traveler"],
    ]},
    # Shown here as well as in Monsters & Mettle, either side of the row of things to do on the road.
    "links": [
        {"quest": "monsters_and_mettle:affix", "pos": (-6.125, 1.75)},
        {"quest": "monsters_and_mettle:pearl", "pos": (6.125, 1.75)},
    ],
    "quests": [
        {
            "key": "arrive", "title": "Wanderlust", "shape": "hexagon", "size": 1.5, "icon": "minecraft:grass_block",
            "desc": [
                "The world out there is bigger and stranger than you'd think. Terralith reshapes the land into dozens of new biomes, islands float overhead, and towns, towers and ruins wait to be found.",
                "",
                "Nothing in this chapter has to be done in order. Each row is one kind of discovery, and they tick off as you stumble on them.",
                "",
                "Chests out here, and the monsters guarding them, carry gear with bonus stats. The two quests either side of the next row are from &eMonsters & Mettle&r, the chapter for all of that.",
                "",
                "Here's a &espyglass&r for scouting the horizon.",
            ],
            "tasks": [{"dimension": "minecraft:overworld", "title": "Set foot in the Overworld"}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}, {"item": "minecraft:spyglass"}],
        },
        {
            "key": "wanderlust", "title": "Which Way?", "shape": "hexagon", "icon": "naturescompass:naturescompass",
            "desc": [
                "Craft a &eNature's Compass&r: a compass ringed with saplings and logs. Open it, pick a biome and press &eStart Search&r. The needle points the way and the screen shows the coordinates.",
                "",
                "It won't teleport you. The walk is the point.",
            ],
            "tasks": [{"item": "naturescompass:naturescompass"}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}],
        },
        {
            "key": "lootr", "title": "Everyone's Share",
            "desc": [
                "Chests in dungeons, villages and ruins are &eLoot Chests&r here. Everyone who opens one gets their own fresh loot, so you never find a chest a friend already emptied.",
                "",
                "Barrels, minecarts with chests and decorated pots work the same way.",
            ],
            "tasks": [{"advancement": "lootr:1chest"}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}],
        },
        {
            "key": "glider", "title": "Off the Edge",
            "desc": [
                "A &eParaglider&r is a few sticks and some leather, and it changes how you see a mountain.",
                "",
                "Hold it in your hand and step off something tall, and you'll glide instead of falling. Gliding uses stamina, shown by the wheel on screen. Land before it runs out.",
                "",
                "Running and swimming don't use stamina in this pack. Only gliding does.",
                "",
                "Glide over a lit &eCampfire&r and the rising warm air lifts you up, though it costs stamina too.",
            ],
            "tasks": [{"item": "paraglider:paraglider"}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}],
        },
        {
            "key": "biomes", "title": "Ten Corners of the World", "shape": "hexagon", "wide": True,
            "icon": "minecraft:filled_map",
            "desc": [
                "Terralith has cherry groves, lavender fields, orchid swamps, deserts with grass in them, and far more.",
                "",
                "Visit all ten. Each one ticks off its own quest in the rows above too. Your Nature's Compass finds any of them, and &eSearch for Next&r skips to another one if the first is too far.",
                "",
                "Keep an eye out on the way: villages, ruins and waystones turn up where you least expect them. Take this &eExplorer's Compass&r for the structures you'll want to find next.",
            ],
            "tasks": [{"biome": b, "title": t, "icon": i} for _, b, t, i, _ in TEN_BIOMES],
            "rewards": [{"xp": 25}, {"crate": "lantern"}, {"item": "explorerscompass:explorerscompass"}],
        },
        {
            "key": "skylands", "title": "Above the Clouds", "optional": True,
            "desc": [
                "Somewhere out there, whole biomes of land float high above the ground: Terralith's &eSkylands&r, in spring, summer, autumn and winter colors.",
                "",
                "Let the Nature's Compass find one. Bring blocks to climb up, and a paraglider for the way down.",
            ],
            "tasks": [{"biome": "#terralith:skylands", "title": "Any Skylands biome", "icon": "minecraft:feather"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "volcano", "title": "Hot Ground", "optional": True,
            "desc": [
                "Terralith's volcanoes rise out of the land like nothing else in the world.",
                "",
                "Find a Volcanic Peak or Crater, climb to the rim and look in. Then glide down the side.",
            ],
            "tasks": [{"biome": "#terralith:volcanic", "title": "Any volcanic biome", "icon": "minecraft:basalt"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "villages", "title": "Every Town Is Different",
            "desc": [
                "Villages here come in far more shapes than the usual. Towns and Towers builds them to suit the land, plus special towns in Tudor, Swedish, Iberian and Mediterranean styles. ChoiceTheorem's Overhauled Village adds villages for nearly every biome, some of them walled.",
                "",
                "Visit one of each. Most villages have a waystone, and a village is a fine place to trade for what you can't find.",
            ],
            "tasks": [
                {"structure": "#towns_and_towers:town", "title": "A Towns and Towers village", "icon": "minecraft:bell"},
                {"structure": "#ctov:village", "title": "An Overhauled Village", "icon": "minecraft:emerald"},
            ],
            "rewards": [{"xp": 10}, {"crate": "hearth"}, {"item": "minecraft:emerald", "count": 8}],
        },
        {
            "key": "rs_villages", "title": "Off the Usual Map", "optional": True,
            "desc": [
                "Repurposed Structures puts villages where vanilla never would: in badlands, bamboo jungles, birch and dark forests, cherry groves, mountains, swamps and mushroom islands.",
                "",
                "Even the Nether has a couple, if you're feeling brave.",
            ],
            "tasks": [{"structure": "#repurposed_structures:collections/villages", "title": "A Repurposed Structures village",
                       "icon": "minecraft:cherry_planks"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "tavern", "title": "A Roadside Tavern", "optional": True,
            "desc": [
                "Out on the plains and in the forests, Explorify scatters small places to stop: taverns, farmsteads, campsites, watchtowers and supply caches.",
                "",
                "Find a tavern. A warm room on a long road is worth something.",
            ],
            "tasks": [{"structure": "explorify:tavern", "title": "An Explorify tavern", "icon": "minecraft:barrel"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}, {"item": "minecraft:cooked_beef", "count": 8}],
        },
        {
            "key": "fortified", "title": "Behind the Walls", "optional": True,
            "desc": [
                "Terralith builds its own walled villages, including one for the desert.",
                "",
                "Safe places to spend a night on the road, as long as the gates hold.",
            ],
            "tasks": [{"structure": "#terralith:fortified_villages", "title": "A fortified village",
                       "icon": "minecraft:cobblestone_wall"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "waystones", "title": "Stones in the Wild",
            "desc": [
                "You already know waystones live in villages. They also stand alone out in the countryside, in a style that matches the land around them.",
                "",
                "Activate five. The more you have, the less walking home.",
                "",
                "Here's a &eWarp Stone&r. Hold right-click with it, anywhere, and you can travel to any waystone you've activated.",
            ],
            "tasks": [{"stat": "waystones:waystone_activated", "value": 5, "title": "Activate 5 waystones",
                       "icon": "waystones:waystone"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}, {"item": "waystones:warp_stone"}],
        },
        {
            "key": "sharestone", "title": "Matching Pairs", "optional": True,
            "desc": [
                "A &eSharestone&r links only to other sharestones of the same color. Put a pair of red ones at your base and your mine, and you have a private line between them.",
                "",
                "Each one takes a Warp Stone to make, so plan your colors before you craft.",
            ],
            "tasks": [{"tag": "waystones:sharestones", "title": "Any sharestone", "icon": "waystones:red_sharestone"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "ruins", "title": "Old Stones",
            "desc": [
                "People lived out here once. Structory leaves their traces: abandoned camps and chapels, an old manor, firetowers, graveyards, and ruins both above and below ground.",
                "",
                "Most have a chest or two. Some have company.",
            ],
            "tasks": [{"structure": "#structory:all_structory_structures", "title": "Any Structory ruin",
                       "icon": "minecraft:mossy_cobblestone"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "towers", "title": "Lookouts and Lighthouses", "optional": True,
            "desc": [
                "Structory Towers adds tall things to climb: lighthouses, lookouts and outposts, a great toadstool and a few stranger ones.",
                "",
                "The view from the top is free. So is the jump, with a paraglider.",
            ],
            "tasks": [{"structure": "#structory_towers:any_tower", "title": "Any Structory tower",
                       "icon": "minecraft:spyglass"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "sky", "title": "Land on a Sky Island", "shape": "hexagon", "icon": "minecraft:grass_block",
            "desc": [
                "Look up. Moog's Soaring Structures floats islands high over the land: castle ruins, little houses, ponds, groves of trees, even a volcano.",
                "",
                "This quest wants the &eCalcite House&r. Search for it in your Explorer's Compass, then build your way up and step onto it. Your paraglider is the easy way down.",
            ],
            "tasks": [{"structure": "mss:calcite_house", "title": "Stand on the Calcite House island",
                       "icon": "minecraft:calcite"}],
            "rewards": [{"xp": 25}, {"crate": "lantern"}, {"item": "minecraft:scaffolding", "count": 32}],
        },
        {
            "key": "witch_tower", "title": "The Witch's Tower",
            "desc": [
                "Deep in forests, jungles and taiga stands a lonely tower. Somebody lived here, and they didn't like visitors.",
                "",
                "Watch for traps and the monster spawner inside. There's a brewing stand, chests worth opening, and a bed. Spend the night in it, if you dare.",
                "",
                "It's rare. The Explorer's Compass knows it as the Witch Tower.",
            ],
            "tasks": [{"structure": "formationsoverworld:witch_tower", "title": "Find a Witch Tower",
                       "icon": "minecraft:brewing_stand"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "witch_hut", "title": "Swamp Cottage", "optional": True,
            "desc": [
                "The witch who lives in the swamp has had a renovation. YUNG's Better Witch Huts are bigger and stranger than the old shack on stilts.",
                "",
                "There's usually a witch at home, and a cat.",
            ],
            "tasks": [{"structure": "betterwitchhuts:witch_hut", "title": "A witch hut", "icon": "minecraft:cauldron"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "temple", "title": "The Pharaoh's Curse", "optional": True,
            "desc": [
                "Desert temples here are deep tombs, and the curse is real: you get &cMining Fatigue&r inside until the temple is cleared, so digging is slow going.",
                "",
                "Find the Pharaoh at its heart and put him to rest. The curse lifts with him.",
            ],
            "tasks": [{"advancement": "betterdeserttemples:temple_clear"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "orbs", "title": "Spirit Orbs",
            "desc": [
                "Strange glowing &eSpirit Orbs&r turn up in old chests: buried treasure, ocean ruins, woodland mansions, ancient cities and bastions.",
                "",
                "Every monster spawner you break drops one, and trial chamber rewards include them too.",
                "",
                "Collect four, then bring them to the Goddess.",
            ],
            "tasks": [{"item": "paraglider:spirit_orb", "count": 4}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "goddess", "title": "Pray to the Goddess", "shape": "hexagon", "icon": "paraglider:goddess_statue",
            "desc": [
                "A &eGoddess Statue&r stands in some villages, and now and then on its own out on the plains. Bring her four Spirit Orbs and she'll trade them for a gift:",
                "",
                "A &cHeart Container&r gives you one more heart, up to 20 extra.",
                "A &eStamina Vessel&r grows your stamina wheel for longer flights, up to 10 of them.",
                "",
                "Winning a raid, or beating the Wither or the Ender Dragon, gives you a Heart Container as well.",
            ],
            "tasks": [{"advancement": "paraglider:pray_to_the_goddess"}],
            "rewards": [{"xp": 25}, {"crate": "lantern"}],
        },
        {
            "key": "horned", "title": "The Horned Statue", "optional": True,
            "desc": [
                "Underground, in the Nether and in some villages, you may find a darker statue with horns. It's the goddess's opposite, and it deals in the same goods.",
                "",
                "Give it a Heart Container or Stamina Vessel and it pays you in emeralds and an &eEssence&r. Bring it an Essence and some emeralds, and it gives one back.",
                "",
                "Wish you'd picked stamina over hearts? This is how you change your mind. This quest wants one of the underground statues.",
            ],
            "tasks": [{"structure": "paraglider:underground_horned_statue", "title": "Find a Horned Statue underground",
                       "icon": "paraglider:horned_statue"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
    ] + [biome_quest(*b) for b in TEN_BIOMES] + [
        {
            "key": "traveler", "title": "Seasoned Traveler", "shape": "hexagon", "size": 1.5,
            "icon": "explorerscompass:explorerscompass",
            "desc": [
                "Fifty chests opened, from villages to tombs to islands in the sky. You've seen more of this world than most.",
                "",
                "There's always another horizon. Keep your compass handy and your waystones close.",
            ],
            "tasks": [{"advancement": "lootr:50loot"}],
            "rewards": [{"xp": 50}, {"crate": "ember"}, {"item": "waystones:warp_stone"}],
        },
    ],
}
