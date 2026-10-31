def trophy(entity, subject):
    """A Jonn's Trophies mob trophy, as one drops when the mob dies."""
    return {"minecraft:custom_data": {"TrophyType": "entity", "TrophyEntity": {"entityType": entity},
                                      "Subject": subject}}


def item_trophy(item, subject):
    return {"minecraft:custom_data": {"TrophyType": "item", "TrophyItem": {"id": item, "count": 1},
                                      "BaseBlock": "minecraft:smooth_stone_slab", "Spin": True, "Subject": subject}}


def fish(*names):
    return [{"item": f"aquaculture:{n}"} for n in names]


def dishes(*ids):
    return [{"item": i} for i in ids]


def biomes(*entries):
    return [{"biome": b, "title": t, "icon": i} for b, t, i in entries]


PAGES = {
    "cookbook": "The Cookbook",
    "angler": "The Angler's Log",
    "field_notes": "Field Notes",
    "trophies": "The Trophy Wall",
}


def page(key):
    """A page of the Almanac: each page's finale gives one, and the capstone asks for all four.
    Only a quest reward can carry this custom data, so a page can't be crafted or faked."""
    return {
        "minecraft:custom_name": '{"text":"Almanac Page: %s","color":"gold","italic":false}' % PAGES[key],
        "minecraft:custom_data": {"AlmanacPage": key},
        "minecraft:enchantment_glint_override": True,
    }


def boss(entity, title, icon):
    return [{"kill": entity, "title": title, "icon": icon}]


def boss_trophy(entity, subject):
    """The boss's own trophy as a reward. Trophies that drop carry their pose as custom data, and
    FTB Quests compares custom data whole, so a quest can't ask for one; it hands one out instead."""
    return {"item": "trophymanager:trophy", "components": trophy(entity, subject)}


# Four pages, one row each, every row ending in a column of finales that meets at the capstone.
ROWS = [
    ["breakfast", "soups", "bakery", "far_afield", "parlor", "jams", "feasts", "food_150", "food_200", "star_cake"],
    ["rivers", "cold_water", "open_sea", "dry_country", "jungle_water", "swamp", "mushroom", "bounty"],
    ["caves", "cold_country", "warm_places", "wonders", "skylands", "end"],
    ["elder", "warden", "wither", "piglich", "dragon"],
]
FINAL_X = 2.0 * (max(len(r) for r in ROWS) - 1)
ROW_Y = [-3.0, -1.0, 1.0, 3.0]
FREE = {k: (FINAL_X - 2.0 * (len(row) - 1 - i), y) for row, y in zip(ROWS, ROW_Y) for i, k in enumerate(row)}
FREE["almanac"] = (0.0, 2.0)
FREE["complete"] = (FINAL_X + 3.0, 0.0)
DEPS = {k: [row[i - 1]] for row in ROWS for i, k in enumerate(row) if i}
DEPS["complete"] = [row[-1] for row in ROWS]

CHAPTER = {
    "file": "almanac",
    "title": "The Almanac",
    "subtitle": "Every fish, every feast, every far-off place",
    "icon": "minecraft:writable_book",
    "layout": {"free": FREE, "deps": DEPS},
    "quests": [
        {
            "key": "almanac", "title": "The Almanac", "shape": "hexagon", "size": 1.5,
            "desc": [
                "Not every long road runs through a reactor. This one runs through rivers, kitchens, far-off biomes and the occasional boss fight.",
                "",
                "The Almanac has four pages: a &ecookbook&r, an &eangler's log&r, &efield notes&r and a &etrophy wall&r. Finish all four and the book is complete.",
                "",
                "The last quest on each page gives you a glowing &6Almanac Page&r. Bring all four to the end of the book.",
                "",
                "None of it is needed for anything else. Take your time, and bring friends: it goes faster with a fisher, a cook and an explorer.",
            ],
            "tasks": [{"check": "Open the book"}],
            "rewards": [],
        },

        # ---- the cookbook ---------------------------------------------------
        {
            "key": "breakfast", "title": "Farmhouse Breakfast", "wide": True, "icon": "croptopia:the_big_breakfast",
            "desc": [
                "Start the cookbook the way you start the day.",
                "",
                "Croptopia's dishes mostly come together in a crafting grid with a utensil or two. Press &eR&r on any of these to see what it takes.",
            ],
            "tasks": dishes("croptopia:the_big_breakfast", "farmersdelight:bacon_and_eggs", "croptopia:cinnamon_roll",
                            "croptopia:oatmeal", "croptopia:toast_with_jam", "croptopia:scones"),
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "soups", "title": "Soup Night", "wide": True, "icon": "farmersdelight:vegetable_soup",
            "desc": [
                "A pot on the stove and whatever the garden gave you today.",
                "",
                "Farmer's Delight soups simmer in the &eCooking Pot&r. Croptopia's come together in the crafting grid.",
            ],
            "tasks": dishes("farmersdelight:chicken_soup", "farmersdelight:vegetable_soup", "farmersdelight:onion_soup",
                            "croptopia:leek_soup", "croptopia:borscht", "croptopia:potato_soup"),
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "bakery", "title": "The Bakery", "wide": True, "icon": "croptopia:cherry_pie",
            "desc": [
                "Flour, sugar, butter, and a lot of patience.",
                "",
                "Some of these need fruit from trees you may not have planted yet. The Market sells the saplings.",
            ],
            "tasks": dishes("croptopia:cherry_pie", "croptopia:banana_nut_bread", "croptopia:doughnut",
                            "croptopia:macaron", "farmersdelight:sweet_berry_cheesecake",
                            "culturaldelights:lemon_muffin"),
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "far_afield", "title": "From Far Afield", "wide": True, "icon": "culturaldelights:spicy_curry",
            "desc": [
                "Dishes from a long way off, made from crops you've found growing wild.",
                "",
                "Corn, eggplant and cucumbers come from Cultural Delights; rice grows wild near water.",
            ],
            "tasks": dishes("culturaldelights:spicy_curry", "culturaldelights:chicken_taco",
                            "culturaldelights:eggplant_burger", "culturaldelights:elote", "croptopia:sushi",
                            "croptopia:tamales"),
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "parlor", "title": "The Ice Cream Parlor", "wide": True, "icon": "croptopia:strawberry_ice_cream",
            "desc": [
                "Six scoops, six flavors. Some of them grow on trees in places you'll need to go looking for.",
                "",
                "A good excuse for a trip somewhere warm.",
            ],
            "tasks": dishes("croptopia:vanilla_ice_cream", "croptopia:strawberry_ice_cream",
                            "croptopia:chocolate_ice_cream", "croptopia:mango_ice_cream",
                            "croptopia:pecan_ice_cream", "croptopia:kiwi_sorbet"),
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "jams", "title": "The Jam Shelf", "wide": True, "icon": "croptopia:strawberry_jam",
            "desc": [
                "A jar of every berry and stone fruit you can find, lined up on a shelf.",
                "",
                "Berry bushes grow wild in their own biomes. Break one for the berries, then craft them into seeds to grow your own.",
            ],
            "tasks": dishes("croptopia:apricot_jam", "croptopia:blackberry_jam", "croptopia:blueberry_jam",
                            "croptopia:cherry_jam", "croptopia:elderberry_jam", "croptopia:grape_jam",
                            "croptopia:peach_jam", "croptopia:raspberry_jam", "croptopia:strawberry_jam"),
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "feasts", "title": "A Table for Everyone", "wide": True,
            "icon": "farmersdelight:honey_glazed_ham_block",
            "desc": [
                "Every feast there is. Set them out on one long table and invite the whole server.",
                "",
                "Each one only has to be in your inventory once. After that, set it out and let everyone help themselves.",
            ],
            "tasks": dishes("farmersdelight:roast_chicken_block", "farmersdelight:honey_glazed_ham_block",
                            "farmersdelight:shepherds_pie_block", "farmersdelight:stuffed_pumpkin_block",
                            "farmersdelight:rice_roll_medley_block", "farmersdelight:gleaming_salad_block",
                            "culturaldelights:eggplant_parmesan_block"),
            "rewards": [{"xp": 25}, {"crate": "lantern"}],
        },
        {
            "key": "food_150", "title": "A Hundred and Fifty Flavors", "icon": "solcarrot:food_book",
            "desc": [
                "Eat &e150 different foods&r for another &c3 hearts&r.",
                "",
                "The cookbook pages above are a good place to find ones you haven't tried.",
                "",
                "Click the checkmark once your Food Book shows 150.",
            ],
            "tasks": [{"check": "I've eaten 150 foods"}],
            "rewards": [{"xp": 10}, {"crate": "lantern"}],
        },
        {
            "key": "food_200", "title": "Two Hundred Flavors", "icon": "solcarrot:food_book",
            "desc": [
                "Eat &e200 different foods&r. That's &c3 more hearts&r.",
                "",
                "There are milestones past this one, all the way to 500, if you're the sort who has to see the end of a list.",
                "",
                "Click the checkmark once your Food Book shows 200.",
            ],
            "tasks": [{"check": "I've eaten 200 foods"}],
            "rewards": [{"xp": 10}, {"crate": "lantern"}],
        },
        {
            "key": "star_cake", "title": "A Cake Fit for a Star", "shape": "hexagon", "size": 1.5,
            "desc": [
                "The last page of the cookbook: a &eNether Star Cake&r.",
                "",
                "Yes, it takes a Nether Star. Yes, you can eat it. Whether you should is between you and your Food Book.",
                "",
                "Here's a trophy of it to keep, whatever you decide.",
            ],
            "tasks": [{"item": "croptopia:nether_star_cake"}],
            "rewards": [{"xp": 25}, {"crate": "lantern"},
                        {"item": "trophymanager:trophy",
                         "components": item_trophy("croptopia:nether_star_cake", "item.croptopia.nether_star_cake")},
                        {"item": "minecraft:paper", "components": page("cookbook")}],
        },

        # ---- the angler's log -----------------------------------------------
        {
            "key": "rivers", "title": "Rivers and Lakes", "wide": True, "icon": "aquaculture:smallmouth_bass",
            "desc": [
                "Every fish in the Angler's Log, starting close to home.",
                "",
                "These live in rivers and lakes in ordinary country: forests, plains and hills. A few of them skip the warm biomes, and a few skip the snowy ones.",
                "",
                "Each one only needs to be in your inventory once. Release them afterward if you like.",
            ],
            "tasks": fish("smallmouth_bass", "bluegill", "brown_trout", "carp", "catfish", "gar", "minnow",
                          "muskellunge", "perch"),
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "cold_water", "title": "Cold Water", "wide": True, "icon": "aquaculture:atlantic_cod",
            "desc": [
                "Bundle up. These fish only bite along cold coasts and in cold seas.",
                "",
                "Rainbow trout and pink salmon also turn up in cold rivers.",
            ],
            "tasks": fish("atlantic_cod", "blackfish", "pacific_halibut", "pink_salmon", "pollock", "rainbow_trout"),
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "open_sea", "title": "The Open Sea", "wide": True, "icon": "aquaculture:tuna",
            "desc": [
                "Fish from a boat, or off a beach.",
                "",
                "Halibut and herring prefer seas that aren't too warm. Tuna, grouper and jellyfish turn up in any ocean.",
            ],
            "tasks": fish("atlantic_halibut", "atlantic_herring", "jellyfish", "red_grouper", "tuna"),
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "dry_country", "title": "Rivers in Dry Country", "wide": True, "icon": "aquaculture:bayad",
            "desc": [
                "Deserts, savannas and badlands look dry, but find water there and these four are waiting in it.",
            ],
            "tasks": fish("bayad", "boulti", "capitaine", "synodontis"),
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "jungle_water", "title": "Jungle Water", "wide": True, "icon": "aquaculture:arapaima",
            "desc": [
                "Jungle rivers hold the biggest catch in the log, the &eArapaima&r, and the toothiest, the &cPiranha&r.",
                "",
                "Arrau turtles come up on the line here too.",
            ],
            "tasks": fish("arapaima", "arrau_turtle", "piranha", "tambaqui"),
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "swamp", "title": "Swamp Fishing", "icon": "aquaculture:box_turtle",
            "desc": [
                "The swamp's catch isn't pretty, but it counts.",
                "",
                "A leech makes decent bait, if you can bring yourself to use it.",
            ],
            "tasks": fish("leech", "box_turtle"),
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "mushroom", "title": "Mushroom Island", "icon": "aquaculture:red_shrooma",
            "desc": [
                "The rarest water in the world surrounds the mushroom fields, and the &eShroomas&r live nowhere else.",
                "",
                "Mushroom islands are far out at sea. A Nature's Compass will point the way.",
            ],
            "tasks": fish("red_shrooma", "brown_shrooma"),
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "bounty", "title": "Neptune's Bounty", "shape": "hexagon", "size": 1.5,
            "icon": "aquaculture:neptunes_bounty",
            "desc": [
                "Every so often the line comes up heavy with treasure instead of a fish. The best of it is &eNeptune's Bounty&r, a chest full of a sea god's loot.",
                "",
                "Better rods and the right hooks help. After that it's patience, and a comfortable chair.",
                "",
                "Here's a tuna for the wall. It won't spoil.",
            ],
            "tasks": [{"item": "aquaculture:neptunes_bounty"}],
            "rewards": [{"xp": 25}, {"crate": "lantern"},
                        {"item": "trophymanager:trophy", "components": trophy("aquaculture:tuna", "entity.aquaculture.tuna")},
                        {"item": "minecraft:paper", "components": page("angler")}],
        },

        # ---- field notes ----------------------------------------------------
        {
            "key": "caves", "title": "Under the Hills", "wide": True, "icon": "minecraft:moss_block",
            "desc": [
                "The world underground has biomes of its own. Each of these is a whole cave system, not just a room.",
                "",
                "Stand anywhere inside one and it counts. Mantle and thermal caves sit deep; bring fire resistance.",
            ],
            "tasks": biomes(
                ("minecraft:lush_caves", "Lush Caves", "minecraft:moss_block"),
                ("minecraft:dripstone_caves", "Dripstone Caves", "minecraft:pointed_dripstone"),
                ("terralith:cave/fungal_caves", "Fungal Caves", "minecraft:red_mushroom"),
                ("terralith:cave/frostfire_caves", "Frostfire Caves", "minecraft:blue_ice"),
                ("terralith:cave/underground_jungle", "Underground Jungle", "minecraft:jungle_leaves"),
                ("terralith:cave/thermal_caves", "Thermal Caves", "minecraft:magma_block"),
            ),
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "cold_country", "title": "Cold Country", "wide": True, "icon": "minecraft:snow_block",
            "desc": [
                "Pack a warm coat. These are the most beautiful cold places in the world.",
            ],
            "tasks": biomes(
                ("terralith:siberian_taiga", "Siberian Taiga", "minecraft:spruce_sapling"),
                ("terralith:snowy_maple_forest", "Snowy Maple Forest", "minecraft:snow_block"),
                ("terralith:snowy_cherry_grove", "Snowy Cherry Grove", "minecraft:cherry_leaves"),
                ("terralith:ice_marsh", "Ice Marsh", "minecraft:ice"),
                ("terralith:frozen_cliffs", "Frozen Cliffs", "minecraft:packed_ice"),
                ("minecraft:ice_spikes", "Ice Spikes", "minecraft:blue_ice"),
            ),
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "warm_places", "title": "Warm Places", "wide": True, "icon": "minecraft:red_sand",
            "desc": [
                "Somewhere to thaw out afterward. Oases count double in the heart, if not in the book.",
            ],
            "tasks": biomes(
                ("terralith:desert_oasis", "Desert Oasis", "minecraft:lily_pad"),
                ("terralith:red_oasis", "Red Oasis", "minecraft:red_sand"),
                ("terralith:tropical_jungle", "Tropical Jungle", "minecraft:cocoa_beans"),
                ("terralith:painted_mountains", "Painted Mountains", "minecraft:orange_terracotta"),
                ("terralith:warped_mesa", "Warped Mesa", "minecraft:warped_nylium"),
                ("terralith:ashen_savanna", "Ashen Savanna", "minecraft:acacia_sapling"),
            ),
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "wonders", "title": "Wonders of the World", "wide": True, "icon": "minecraft:amethyst_cluster",
            "desc": [
                "The places worth a screenshot. Some are rare enough that you may need a Nature's Compass to find them.",
            ],
            "tasks": biomes(
                ("terralith:yellowstone", "Yellowstone", "minecraft:yellow_terracotta"),
                ("terralith:bryce_canyon", "Bryce Canyon", "minecraft:terracotta"),
                ("terralith:amethyst_canyon", "Amethyst Canyon", "minecraft:amethyst_cluster"),
                ("terralith:mirage_isles", "Mirage Isles", "minecraft:white_terracotta"),
                ("terralith:glacial_chasm", "Glacial Chasm", "minecraft:packed_ice"),
                ("minecraft:mushroom_fields", "Mushroom Fields", "minecraft:mycelium"),
            ),
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "skylands", "title": "Four Seasons in the Sky", "wide": True, "icon": "minecraft:feather",
            "desc": [
                "The Skylands come in four seasons. Find all of them.",
                "",
                "A paraglider and a good updraft will get you between islands. Falling will get you down.",
            ],
            "tasks": biomes(
                ("terralith:skylands_spring", "Skylands in Spring", "minecraft:pink_tulip"),
                ("terralith:skylands_summer", "Skylands in Summer", "minecraft:sunflower"),
                ("terralith:skylands_autumn", "Skylands in Autumn", "minecraft:orange_tulip"),
                ("terralith:skylands_winter", "Skylands in Winter", "minecraft:snowball"),
            ),
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "end", "title": "Beyond the Dragon", "shape": "hexagon", "size": 1.5, "wide": True,
            "icon": "minecraft:end_stone",
            "desc": [
                "The last page of the field notes is the strangest place in the world.",
                "",
                "Past the dragon's island, the outer End has its own lands: crystal peaks, shadowlands and the empty void barrens.",
                "",
                "Here's a globe for the study, and a map to go with it.",
            ],
            "tasks": biomes(
                ("nullscape:crystal_peaks", "Crystal Peaks", "minecraft:amethyst_block"),
                ("nullscape:shadowlands", "Shadowlands", "minecraft:obsidian"),
                ("nullscape:void_barrens", "Void Barrens", "minecraft:end_stone"),
            ),
            "rewards": [{"xp": 25}, {"crate": "lantern"}, {"item": "supplementaries:globe"},
                        {"item": "cluttered:antique_map"}, {"item": "minecraft:paper", "components": page("field_notes")}],
        },

        # ---- the trophy wall ------------------------------------------------
        {
            "key": "elder", "title": "Something from the Deep", "icon": "minecraft:prismarine_shard",
            "desc": [
                "Every boss in the world belongs on the wall. Defeat each one and this page gives you its &eTrophy&r to mount.",
                "",
                "Start with an &eElder Guardian&r, deep in an ocean monument. They'll tire you out before you see them: bring milk for the fatigue.",
            ],
            "tasks": boss("minecraft:elder_guardian", "Defeat an Elder Guardian", "minecraft:prismarine_shard"),
            "rewards": [{"xp": 10}, {"crate": "hearth"},
                        boss_trophy("minecraft:elder_guardian", "entity.minecraft.elder_guardian")],
        },
        {
            "key": "warden", "title": "Quiet, Please", "icon": "minecraft:sculk_shrieker",
            "desc": [
                "The &eWarden&r is blind, but it can hear you breathe.",
                "",
                "Sneak, throw snowballs to distract it, and don't fight it in a corridor. Plenty of people never do fight it, and that's allowed.",
            ],
            "tasks": boss("minecraft:warden", "Defeat a Warden", "minecraft:sculk_shrieker"),
            "rewards": [{"xp": 10}, {"crate": "lantern"}, boss_trophy("minecraft:warden", "entity.minecraft.warden")],
        },
        {
            "key": "wither", "title": "Three Heads Are Worse Than One", "icon": "minecraft:wither_skeleton_skull",
            "desc": [
                "Summon the &eWither&r somewhere you don't mind losing. It breaks almost everything.",
                "",
                "Its Nether Star bakes into a certain cake, if you're working on the cookbook.",
            ],
            "tasks": boss("minecraft:wither", "Defeat the Wither", "minecraft:wither_skeleton_skull"),
            "rewards": [{"xp": 10}, {"crate": "lantern"}, boss_trophy("minecraft:wither", "entity.minecraft.wither")],
        },
        {
            "key": "piglich", "title": "A Lich in Gold", "icon": "allthemodium:piglich_heart",
            "desc": [
                "The &ePiglich&r guards the Ancient Pyramids in the soul sand valleys of the Other.",
                "",
                "You'll be fighting a few of these for their hearts if you're after the Alloy Paxel. One of them goes on the wall.",
            ],
            "tasks": boss("allthemodium:piglich", "Defeat a Piglich", "allthemodium:piglich_heart"),
            "rewards": [{"xp": 10}, {"crate": "lantern"}, boss_trophy("allthemodium:piglich", "entity.allthemodium.piglich")],
        },
        {
            "key": "dragon", "title": "The Trophy Wall", "shape": "hexagon", "size": 1.5, "icon": "minecraft:dragon_egg",
            "desc": [
                "Last on the wall: the &eEnder Dragon&r.",
                "",
                "Already beaten it once? Respawn it with four End Crystals on the exit portal. It's a good afternoon out with friends.",
                "",
                "Here's its trophy, and a dragon's head to hang beside it.",
            ],
            "tasks": boss("minecraft:ender_dragon", "Defeat the Ender Dragon", "minecraft:dragon_egg"),
            "rewards": [{"xp": 25}, {"crate": "lantern"},
                        boss_trophy("minecraft:ender_dragon", "entity.minecraft.ender_dragon"),
                        {"item": "minecraft:dragon_head"},
                        {"item": "minecraft:paper", "components": page("trophies")}],
        },

        # ---- the end of the book --------------------------------------------
        {
            "key": "complete", "title": "The Almanac, Complete", "shape": "hexagon", "size": 2.0,
            "icon": "minecraft:writable_book",
            "desc": [
                "Every page filled: the cookbook, the angler's log, the field notes and the trophy wall.",
                "",
                "There's nothing left to unlock. That was never really the point.",
                "",
                "Bring the four &6Almanac Pages&r together, and the whole server will hear about it.",
            ],
            "tasks": [{"item": "minecraft:paper", "components": page(k), "title": f"Almanac Page: {t}",
                       "icon": "minecraft:paper", "icon_components": page(k)} for k, t in PAGES.items()],
            "rewards": [
                {"xp_levels": 30},
                {"crate": "ember", "count": 2},
                {"item": "trophymanager:trophy", "components": item_trophy("minecraft:writable_book", "item.minecraft.writable_book")},
                {"command": '/tellraw @a ["",{"text":"{p}","color":"gold"},{"text":" has completed the Almanac!","color":"yellow"}]'},
            ],
        },
    ],
}
