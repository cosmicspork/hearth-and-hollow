TIERS = {
    "odd": ("Odd Job", [{"xp": 10}, {"crate_item": "kindling"}]),
    "commission": ("Commission", [{"xp": 10}, {"crate_item": "hearth"}]),
    "grand": ("Grand Bounty", [{"xp": 25}, {"crate_item": "ember"}]),
}


def bounty(tier, key, title, desc, task):
    subtitle, rewards = TIERS[tier]
    return {"key": key, "title": title, "subtitle": subtitle, "repeat": True,
            "desc": desc, "tasks": [task], "rewards": [dict(r) for r in rewards]}


ODD_JOBS = [
    bounty("odd", "o_logs", "Firewood", ["Winter's coming somewhere. Any logs will do."],
           {"tag": "minecraft:logs", "count": 64, "title": "64 logs, any kind", "icon": "minecraft:oak_log"}),
    bounty("odd", "o_bread", "Baker's Order", ["The village feast needs bread, and plenty of it."],
           {"item": "minecraft:bread", "count": 32}),
    bounty("odd", "o_zombies", "Night Watch", ["Thin out the shamblers around the farms."],
           {"kill": "minecraft:zombie", "count": 10}),
    bounty("odd", "o_cobble", "Quarry Run", ["A stack of cobblestone for the new road."],
           {"item": "minecraft:cobblestone", "count": 64}),
    bounty("odd", "o_wool", "Shearing Day", ["Any color. The weavers aren't fussy."],
           {"tag": "minecraft:wool", "count": 32, "title": "32 wool, any color", "icon": "minecraft:white_wool"}),
    bounty("odd", "o_skeletons", "Bone Collector", ["Somebody has to keep the archers in check."],
           {"kill": "minecraft:skeleton", "count": 10}),
    bounty("odd", "o_spiders", "Cobweb Duty", ["Clear the spiders out of the barn rafters."],
           {"kill": "minecraft:spider", "count": 8}),
    bounty("odd", "o_iron", "Smelter's Due", ["Iron for hinges, buckets and a hundred small repairs."],
           {"item": "minecraft:iron_ingot", "count": 32}),
    bounty("odd", "o_crops", "Harvest Help", ["Any crop at all, from wheat to whatever Croptopia grows."],
           {"tag": "c:crops", "count": 64, "title": "64 crops, any kind", "icon": "minecraft:wheat"}),
    bounty("odd", "o_meat", "Hot Supper", ["Cooked beef, pork, chicken or mutton for the work crews."],
           {"tag": "c:foods/cooked_meat", "count": 16, "title": "16 cooked meat, any kind",
            "icon": "minecraft:cooked_beef"}),
    bounty("odd", "o_creepers", "Creeper Control", ["Before they get to the garden."],
           {"kill": "minecraft:creeper", "count": 8}),
    bounty("odd", "o_fish", "Fresh Catch", ["Cooked fish of any kind, for the Friday fish fry."],
           {"tag": "c:foods/cooked_fish", "count": 16, "title": "16 cooked fish, any kind",
            "icon": "minecraft:cooked_cod"}),
]

COMMISSIONS = [
    bounty("commission", "c_steel", "Steel Order", ["Sixteen steel ingots for a new bridge."],
           {"tag": "c:ingots/steel", "count": 16, "title": "16 Steel Ingots", "icon": "alltheores:steel_ingot"}),
    bounty("commission", "c_meals", "Catering Job",
           ["Proper Croptopia meals for a wedding: pizzas, pies, stews and the like."],
           {"tag": "croptopia:advancements_food_big", "count": 32, "title": "32 Croptopia meals, any kind",
            "icon": "croptopia:supreme_pizza"}),
    bounty("commission", "c_blazes", "Blaze Hunt", ["The fortress has gotten crowded again."],
           {"kill": "minecraft:blaze", "count": 8}),
    bounty("commission", "c_processors", "Processor Batch",
           ["Refined Storage processors: Basic, Improved or Advanced. A mix is fine."],
           {"any": ["refinedstorage:basic_processor", "refinedstorage:improved_processor",
                    "refinedstorage:advanced_processor"],
            "count": 8, "title": "8 processors, any grade", "icon": "refinedstorage:advanced_processor"}),
    bounty("commission", "c_wither_skeletons", "Skull Duty", ["Ten wither skeletons. Skulls are yours to keep."],
           {"kill": "minecraft:wither_skeleton", "count": 10}),
    bounty("commission", "c_endermen", "Ender Harvest", ["Don't look them in the eye. Well, until you have to."],
           {"kill": "minecraft:enderman", "count": 12}),
    bounty("commission", "c_osmium", "Osmium Order", ["Thirty-two osmium ingots for the machine shop."],
           {"tag": "c:ingots/osmium", "count": 32, "title": "32 Osmium Ingots", "icon": "alltheores:osmium_ingot"}),
    bounty("commission", "c_diamonds", "Diamond Order", ["Eight diamonds, no questions asked."],
           {"item": "minecraft:diamond", "count": 8}),
    bounty("commission", "c_quartz", "Quartz Delivery", ["A stack of nether quartz for the glassworks."],
           {"item": "minecraft:quartz", "count": 64}),
    bounty("commission", "c_ghasts", "Quiet the Wailing", ["Three ghasts. Mind the fireballs."],
           {"kill": "minecraft:ghast", "count": 3}),
    bounty("commission", "c_guardians", "Monument Work", ["Clear the guardians from an ocean monument."],
           {"kill": "minecraft:guardian", "count": 10}),
    bounty("commission", "c_circuits", "Circuit Order", ["Eight Basic Control Circuits for somebody's new factory."],
           {"item": "mekanism:basic_control_circuit", "count": 8}),
]

GRAND = [
    bounty("grand", "g_wither", "The Wither", ["Summon it, beat it, keep the star."],
           {"kill": "minecraft:wither", "count": 1}),
    bounty("grand", "g_warden", "The Warden", ["Wake it on purpose this time."],
           {"kill": "minecraft:warden", "count": 1}),
    bounty("grand", "g_dragon", "The Dragon, Again", ["Respawn the dragon with four End Crystals and do it all over again."],
           {"kill": "minecraft:ender_dragon", "count": 1}),
    bounty("grand", "g_allthemodium", "Allthemodium Shipment", ["Four Allthemodium Ingots, straight from the deep."],
           {"tag": "c:ingots/allthemodium", "count": 4, "title": "4 Allthemodium Ingots",
            "icon": "allthemodium:allthemodium_ingot"}),
    bounty("grand", "g_diamond_blocks", "Diamond Hoard", ["Sixteen blocks of diamond for the vault."],
           {"item": "minecraft:diamond_block", "count": 16}),
    bounty("grand", "g_mountain", "The Mountain", ["One Cobblestone 3x: that's 729 cobblestone, compressed three times."],
           {"item": "allthecompressed:cobblestone_3x", "count": 1}),
]

BOARD = {
    "key": "board", "title": "The Bounty Board", "shape": "gear", "size": 2.0, "wide": True,
    "desc": [
        "Every job on this board can be done again and again, as often as you like.",
        "",
        "Deliveries take the items when you hand them in, so open the quest and click the task to turn them over. Don't hand over anything you still need. Hunts only count kills.",
        "",
        "Three tiers: &7Odd Jobs&r pay a Kindling crate, &aCommissions&r a Hearth crate, and &6Grand Bounties&r an Ember crate.",
    ],
    "tasks": [{"check": "Got it"}],
    "rewards": [],
}

CHAPTER = {
    "file": "bounty_board",
    "title": "Bounty Board",
    "subtitle": "Repeatable deliveries and hunts, in three tiers",
    "icon": "minecraft:bell",
    "layout": {"grid": [["board"], [q["key"] for q in ODD_JOBS], [q["key"] for q in COMMISSIONS],
                        [q["key"] for q in GRAND]]},
    "quests": [BOARD] + ODD_JOBS + COMMISSIONS + GRAND,
}
