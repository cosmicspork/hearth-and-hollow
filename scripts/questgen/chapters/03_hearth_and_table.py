COLORS = ["white", "orange", "magenta", "light_blue", "yellow", "lime", "pink", "gray", "light_gray", "cyan",
          "purple", "blue", "brown", "green", "red", "black"]


def kitchen(block, base=True):
    """A Cooking for Blockheads block in its plain form and every dyed color."""
    ids = [f"cookingforblockheads:{block}"] if base else []
    return ids + [f"cookingforblockheads:{c}_{block}" for c in COLORS]


SAPLINGS = [f"croptopia:{f}_sapling" for f in [
    "almond", "apple", "apricot", "avocado", "banana", "cashew", "cherry", "cinnamon", "coconut", "date",
    "dragonfruit", "fig", "grapefruit", "kumquat", "lemon", "lime", "mango", "nectarine", "nutmeg", "orange",
    "peach", "pear", "pecan", "persimmon", "plum", "starfruit", "walnut"]]

TREE_FRUIT = [f"croptopia:{f}" for f in [
    "almond", "apricot", "avocado", "banana", "cashew", "cherry", "coconut", "date", "dragonfruit", "fig",
    "grapefruit", "kumquat", "lemon", "lime", "mango", "nectarine", "orange", "peach", "pear", "pecan",
    "persimmon", "plum", "starfruit", "walnut"]]

CHAPTER = {
    "file": "hearth_and_table",
    "group": "settled",
    "title": "Hearth & Table",
    "subtitle": "Grow it, catch it, cook it, and eat a little of everything",
    "icon": "farmersdelight:cooking_pot",
    # Three tracks fan out from the knife: Farmer's Delight, Cooking for Blockheads and fishing.
    # Gardening and the odd extras need no order, so they sit in rows below.
    "layout": {"lines": [
        {"flow": ["table", ["cutting_board", "recipe_book", "rod"], ["cooking_pot", "kitchen", "big_fish"],
                  ["feast", "pantry", "fish_mount"]],
         "branches": {"cooking_pot": {"up": ["stove"]}, "big_fish": {"down": ["fillet"]}}},
        {"rows": ["wild", "garden", "orchard", "cultural", "straw", "utensils",
                  "compost", "rich_soil", "market", "fertilizer", "trough", "nest",
                  "skillet", "cow_jar", "tackle_box"], "per_row": 5},
    ]},
    "quests": [
        {
            "key": "table", "title": "Hearth & Table",
            "shape": "hexagon", "size": 1.5, "icon": "farmersdelight:flint_knife",
            "desc": [
                "Steak and bread will keep you going. This chapter is about eating well: growing your own food, catching fish, and turning it all into proper meals.",
                "",
                "Start with a &eknife&r. It's a kitchen tool and a weapon, and it gets more out of plants and animals than your bare hands. A flint one is fine for now.",
            ],
            "tasks": [{"any": ["farmersdelight:flint_knife", "farmersdelight:iron_knife", "farmersdelight:golden_knife",
                               "farmersdelight:diamond_knife", "farmersdelight:netherite_knife"],
                       "title": "Any knife", "icon": "farmersdelight:flint_knife"}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}],
        },
        {
            "key": "straw", "title": "Last Straw",
            "desc": [
                "Cut grass, wheat or rice with a knife and you'll collect &eStraw&r.",
                "",
                "Straw makes canvas, straw bales and rope, and it goes into organic compost.",
                "",
                "Knives are good for more than plants: a pig felled with one drops ham.",
            ],
            "tasks": [{"item": "farmersdelight:straw", "count": 8}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}],
        },
        {
            "key": "wild", "title": "Wild Crops",
            "desc": [
                "Cabbages, tomatoes, onions and rice grow wild out in the world, along with wild carrots, potatoes and beets. Break them for seeds and the odd crop to take home.",
                "",
                "When your own crops are ready, just &eright-click&r them. You get the harvest and the crop replants itself. No hoe needed.",
            ],
            "tasks": [{"any": ["farmersdelight:cabbage", "farmersdelight:tomato", "farmersdelight:onion",
                               "farmersdelight:rice"],
                       "title": "Cabbage, tomato, onion or rice", "icon": "farmersdelight:cabbage"}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}, {"item": "farmersdelight:cabbage_seeds", "count": 4},
                        {"item": "farmersdelight:tomato_seeds", "count": 4}],
        },
        {
            "key": "garden", "title": "A Bigger Garden",
            "desc": [
                "Croptopia adds dozens more crops, each growing wild in its own kind of biome: lettuce in one place, garlic or strawberries in another.",
                "",
                "Found one? Put the crop in a crafting grid to turn it into seeds, and start a patch at home.",
            ],
            "tasks": [{"any": ["croptopia:lettuce_seed", "croptopia:garlic_seed", "croptopia:strawberry_seed",
                               "croptopia:corn_seed", "croptopia:tomato_seed", "croptopia:basil_seed",
                               "croptopia:bellpepper_seed", "croptopia:onion_seed", "croptopia:rice_seed",
                               "croptopia:ginger_seed"],
                       "title": "Croptopia seeds", "icon": "croptopia:strawberry_seed"}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}, {"item": "croptopia:lettuce_seed", "count": 4}],
        },
        {
            "key": "orchard", "title": "Plant an Orchard",
            "desc": [
                "Fruit trees grow wild across the world: oranges, peaches, bananas, nuts and plenty more. Their leaves sometimes drop a sapling.",
                "",
                "No luck? Two pieces of fruit and any sapling craft a new one.",
                "",
                "Plant a few and wait. When the fruit is ripe, right-click it to pick it and leave the tree to grow more.",
            ],
            "tasks": [
                {"any": SAPLINGS, "count": 4, "title": "Four fruit tree saplings", "icon": "croptopia:orange_sapling"},
                {"any": TREE_FRUIT, "title": "Fruit from a Croptopia tree", "icon": "croptopia:orange"},
            ],
            "rewards": [{"xp": 10}, {"crate": "kindling"}],
        },
        {
            "key": "market", "title": "Market Day",
            "desc": [
                "Can't find a seed in the wild? Buy it. The &eMarket&r sells seeds and saplings for an emerald each, including Croptopia's fruit trees and the crops from Farmer's Delight and Cultural Delights.",
                "",
                "Here are some emeralds to spend.",
            ],
            "tasks": [{"item": "farmingforblockheads:market"}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}, {"item": "minecraft:emerald", "count": 8}],
        },
        {
            "key": "fertilizer", "title": "Better Dirt", "optional": True,
            "desc": [
                "Use fertilizer on farmland and it stays fertilized.",
                "",
                "&cRed&r makes crops grow faster. &aGreen&r gives a bigger harvest. &eYellow&r stops the soil being trampled.",
                "",
                "Craft them from dye, seeds and a few gold nuggets.",
            ],
            "tasks": [{"any": ["farmingforblockheads:red_fertilizer", "farmingforblockheads:green_fertilizer",
                               "farmingforblockheads:yellow_fertilizer"],
                       "title": "Any fertilizer", "icon": "farmingforblockheads:green_fertilizer"}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}],
        },
        {
            "key": "cutting_board", "title": "The Cutting Board",
            "desc": [
                "Place an item on a &eCutting Board&r, then use it with a knife in hand to chop it up: cabbage into leaves, meat into cuts, a pumpkin into slices.",
                "",
                "Other tools work too. An axe strips logs and gives you tree bark.",
                "",
                "Press &eU&r on the board to see everything it can do.",
            ],
            "tasks": [{"item": "farmersdelight:cutting_board"}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}],
        },
        {
            "key": "compost", "title": "Black Gold",
            "desc": [
                "&eOrganic Compost&r is dirt, straw, rotten flesh and bone meal mixed together. Place it and it slowly turns into rich soil.",
                "",
                "It composts faster with sunlight, water nearby and mushrooms around it.",
            ],
            "tasks": [{"item": "farmersdelight:organic_compost"}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}],
        },
        {
            "key": "rich_soil", "title": "Rich Soil", "optional": True,
            "desc": [
                "&eRich Soil&r gives crops planted in it a chance at a free bone meal boost as they grow. Till it for farmland that keeps the bonus.",
                "",
                "Mushrooms planted on it grow into colonies you can shear for more mushrooms.",
            ],
            "tasks": [{"item": "farmersdelight:rich_soil"}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}],
        },
        {
            "key": "trough", "title": "Feeding Time", "optional": True,
            "desc": [
                "A &eFeeding Trough&r breeds animals for you. Fill it with their food and it feeds any nearby animal that's ready to mate.",
                "",
                "It stops once there are 24 of a kind around, so your pen won't overflow.",
            ],
            "tasks": [{"item": "farmingforblockheads:feeding_trough"}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}],
        },
        {
            "key": "nest", "title": "No More Egg Hunts", "optional": True,
            "desc": [
                "A &eChicken Nest&r collects eggs laid by chickens around it, so you don't have to chase them across the coop.",
                "",
                "Eggs go into a surprising number of recipes. Keep a few chickens.",
            ],
            "tasks": [{"item": "farmingforblockheads:chicken_nest"}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}],
        },
        {
            "key": "cooking_pot", "title": "Something on the Stove",
            "desc": [
                "The &eCooking Pot&r makes soups, stews and proper meals. Set it over heat: a campfire, a stove, fire, a magma block or lava.",
                "",
                "Most meals need a bowl to serve into, so keep some nearby. The pot holds the finished food until you take it.",
                "",
                "Hearty meals grant &eNourishment&r, which keeps your hunger from dropping for a while.",
            ],
            "tasks": [{"item": "farmersdelight:cooking_pot"}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}],
        },
        {
            "key": "stove", "title": "The Stove",
            "desc": [
                "A &eStove&r cooks food set on top of it, like a campfire, and heats a cooking pot or skillet placed on it.",
                "",
                "It's made from a campfire, bricks and iron, and looks right at home in a kitchen.",
            ],
            "tasks": [{"item": "farmersdelight:stove"}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}],
        },
        {
            "key": "skillet", "title": "Cooking on the Go", "optional": True,
            "desc": [
                "A &eSkillet&r is a frying pan you carry. Stand near a heat source, hold the skillet, and put food in your other hand to cook it.",
                "",
                "Sneak to place it as a block, on a stove for instance. It also makes a fine club in a pinch.",
            ],
            "tasks": [{"item": "farmersdelight:skillet"}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}],
        },
        {
            "key": "utensils", "title": "Croptopia's Kitchen",
            "desc": [
                "Many Croptopia recipes call for a utensil in the crafting grid: a &eFrying Pan&r, &eCooking Pot&r, &eKnife&r, &eMortar and Pestle&r or &eAll Purpose Food Press&r.",
                "",
                "They're quick to make. Press &eU&r on one to see the dishes it unlocks.",
            ],
            "tasks": [{"any": ["croptopia:frying_pan", "croptopia:cooking_pot", "croptopia:knife",
                               "croptopia:mortar_and_pestle", "croptopia:food_press"],
                       "title": "Any Croptopia utensil", "icon": "croptopia:frying_pan"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "cultural", "title": "Flavors from Afar", "optional": True,
            "desc": [
                "Cultural Delights brings corn, cucumbers, eggplants and beans, all found growing wild, plus avocado and lemon trees.",
                "",
                "They open up tacos, curries, pickles and a lot more. Plenty of it uses the cooking pot and cutting board you already have, and the mod adds its own Oven for baking and a Vat for aging.",
            ],
            "tasks": [{"any": ["culturaldelights:corn_cob", "culturaldelights:cucumber", "culturaldelights:eggplant",
                               "culturaldelights:white_eggplant", "culturaldelights:beans",
                               "culturaldelights:avocado", "culturaldelights:lemon"],
                       "title": "Corn, cucumber, eggplant, beans, avocado or lemon", "icon": "culturaldelights:corn_cob"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "recipe_book", "title": "Cooking for Blockheads",
            "desc": [
                "Smelt a plain book and you get &eCooking for Blockheads I&r: a recipe book that shows every food you can make with what you're carrying.",
                "",
                "It's also the first step toward a full kitchen. Add a crafting table and two diamonds to make &eCooking for Blockheads II&r, which goes into the Cooking Table.",
            ],
            "tasks": [{"item": "cookingforblockheads:recipe_book"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "kitchen", "title": "The Heart of the Kitchen", "shape": "hexagon",
            "desc": [
                "The &eCooking Table&r is the center of a kitchen. Right-click it to see every food you can make from the ingredients in the kitchen around it, and craft any of them with a click or two.",
                "",
                "Counters, fridges, sinks, ovens and the rest share their contents with it when they touch it or each other. Kitchen Floor connects them across a room.",
                "",
                "Looking for something you haven't eaten yet? Sort the Cooking Table's list by &eEaten&r.",
                "",
                "Here's a toaster to get you started.",
            ],
            "tasks": [{"any": kitchen("cooking_table"), "title": "A Cooking Table",
                       "icon": "cookingforblockheads:cooking_table"}],
            "rewards": [{"xp": 25}, {"crate": "lantern"}, {"item": "cookingforblockheads:toaster"}],
        },
        {
            "key": "pantry", "title": "Stock the Pantry",
            "desc": [
                "Fill out the kitchen. A &eFridge&r and &eKitchen Counters&r store ingredients the Cooking Table can reach. A &eSink&r supplies water to recipes, as much as you need.",
                "",
                "An &eOven&r and a &eTool Rack&r for your knives and pans round it out. Hang cabinets on the wall for even more space.",
            ],
            "tasks": [
                {"any": kitchen("fridge"), "title": "A Fridge", "icon": "cookingforblockheads:white_fridge"},
                {"any": kitchen("counter"), "title": "A Kitchen Counter", "icon": "cookingforblockheads:counter"},
                {"any": kitchen("sink"), "title": "A Sink", "icon": "cookingforblockheads:sink"},
            ],
            "rewards": [{"xp": 10}, {"crate": "hearth"}, {"item": "cookingforblockheads:spice_rack"}],
        },
        {
            "key": "cow_jar", "title": "Cow in a Jar", "optional": True,
            "desc": [
                "A &eMilk Jar&r stores milk for recipes. A Cow in a Jar makes its own.",
                "",
                "Lead a cow over a Milk Jar and drop an anvil on it. Don't ask how it fits.",
            ],
            "tasks": [{"item": "cookingforblockheads:cow_jar"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "rod", "title": "Gone Fishing",
            "desc": [
                "Aquaculture fills the water with real fish: bass and trout in rivers and lakes, tuna and halibut at sea, piranha in the jungle, and plenty more.",
                "",
                "An &eIron Fishing Rod&r is the first rod that takes upgrades. Every kind of water has its own catch, so fish everywhere you go.",
            ],
            "tasks": [{"item": "aquaculture:iron_fishing_rod"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "tackle_box", "title": "The Tackle Box",
            "desc": [
                "Put your rod in a &eTackle Box&r to fit it with a hook, bait, fishing line and a bobber.",
                "",
                "Hooks change how it fishes: a Double Hook can catch two at once, a Light Hook casts farther, and a Note Hook plays a sound when a fish is coming.",
                "",
                "&eWorms&r make good bait. A Worm Farm will raise them for you.",
            ],
            "tasks": [{"item": "aquaculture:tackle_box"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}, {"item": "aquaculture:worm", "count": 16}],
        },
        {
            "key": "big_fish", "title": "One for the Wall",
            "desc": [
                "Land a fish worth bragging about. A tuna, a catfish, an arapaima, a halibut: something that took a while to reel in.",
                "",
                "They're rare, so be patient. Tuna and grouper live in the ocean, arapaima in jungle water, and catfish and muskellunge in rivers and lakes.",
            ],
            "tasks": [{"any": ["aquaculture:tuna", "aquaculture:catfish", "aquaculture:arapaima",
                               "aquaculture:muskellunge", "aquaculture:pacific_halibut",
                               "aquaculture:atlantic_halibut", "aquaculture:red_grouper"],
                       "title": "A big fish", "icon": "aquaculture:tuna"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "fillet", "title": "Fish Fillets",
            "desc": [
                "Put a fish and a &eFillet Knife&r in the crafting grid to cut it into fish fillets.",
                "",
                "Cooked fillets are quick, easy food, and they count for the Food Book like anything else.",
            ],
            "tasks": [{"item": "aquaculture:fish_fillet_raw"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "fish_mount", "title": "Mount Your Catch", "optional": True,
            "desc": [
                "A &eFish Mount&r hangs on the wall and shows off a fish of your choosing. You'll need an Iron Hook to make one.",
                "",
                "Every proper cabin has one over the fireplace.",
            ],
            "tasks": [{"any": ["aquaculture:oak_fish_mount", "aquaculture:spruce_fish_mount",
                               "aquaculture:birch_fish_mount", "aquaculture:jungle_fish_mount",
                               "aquaculture:acacia_fish_mount", "aquaculture:dark_oak_fish_mount"],
                       "title": "Any fish mount", "icon": "aquaculture:oak_fish_mount"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "feast", "title": "A Feast for Friends", "shape": "hexagon",
            "icon": "farmersdelight:roast_chicken_block",
            "desc": [
                "Some dishes are too big for one plate. A &efeast&r is placed on the table, and everyone can help themselves to a serving.",
                "",
                "Roast chicken, honey glazed ham, shepherd's pie, stuffed pumpkin: each one is a new food for the book, and a good excuse to have people over.",
            ],
            "tasks": [{"any": ["farmersdelight:roast_chicken_block", "farmersdelight:honey_glazed_ham_block",
                               "farmersdelight:shepherds_pie_block", "farmersdelight:stuffed_pumpkin_block",
                               "farmersdelight:rice_roll_medley_block", "culturaldelights:eggplant_parmesan_block"],
                       "title": "Any feast", "icon": "farmersdelight:roast_chicken_block"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
    ],
}
