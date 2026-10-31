_COLORS = ["white", "orange", "magenta", "light_blue", "yellow", "lime", "pink", "gray", "light_gray", "cyan",
           "purple", "blue", "brown", "green", "red", "black"]
_HOPPER_POTS = (["botanypots:terracotta_hopper_botany_pot"]
                + [f"botanypots:{c}_{m}_hopper_botany_pot" for c in _COLORS
                   for m in ("terracotta", "glazed_terracotta", "concrete")]
                + [f"botanypots:{b}_hopper_botany_pot" for b in
                   ("bricks", "stone_bricks", "mossy_stone_bricks", "deepslate_bricks", "tuff_bricks", "mud_bricks",
                    "prismarine_bricks", "nether_bricks", "red_nether_bricks", "polished_blackstone_bricks",
                    "end_stone_bricks", "quartz_bricks")])

CHAPTER = {
    "file": "green_thumb",
    "group": "hum",
    "title": "Green Thumb",
    "subtitle": "Grow your resources, then let the farm run itself",
    "icon": "mysticalagriculture:inferium_seeds",
    "layout": {
        "spine": ["start", "seeds", "altar", "crystal", "prudentium", "tertium", "imperium", "supremium", "finale"],
        "branches": {
            "start": {"up": ["prosperity"]},
            "seeds": {"up": ["farmland"], "down": ["watering"]},
            "altar": {"down": ["resource_seed"]},
            "prudentium": {"up": ["pot", "hopper_pot"], "down": ["accelerator"]},
            "tertium": {"up": ["pylon"], "down": ["trees"]},
            "imperium": {"up": ["soul_dagger"], "down": ["masher", "absorption"]},
            "supremium": {"up": ["learner", "sim"], "down": ["master_crystal"]},
            "finale": {"up": ["metal_seeds"]},
        },
    },
    "quests": [
        {
            "key": "start", "title": "Green Thumb",
            "shape": "hexagon", "size": 1.5, "icon": "mysticalagriculture:inferium_essence",
            "desc": [
                "Why mine iron when you can grow it? Mystical Agriculture has seeds that grow real resources, and the rest of this chapter gets the farm running by itself.",
                "",
                "It all starts with &eInferium Essence&r. Grass and mobs don't drop it in this pack, so dig for it: &eInferium Ore&r is common underground in the Overworld, from about Y 64 down to Y -32, and each one drops two to four essence. Fortune helps.",
                "",
                "The Nether and the End have Inferium Ore of their own, too.",
            ],
            "tasks": [{"item": "mysticalagriculture:inferium_essence", "count": 16}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}],
        },
        {
            "key": "prosperity", "title": "Prosperity Shards",
            "desc": [
                "&eProsperity Ore&r sits a little deeper than Inferium, from about Y 24 down to Y -60, and drops &eProsperity Shards&r.",
                "",
                "Shards go into Infusion Crystals and into the seed base that every resource seed is built on, so keep a healthy pile.",
            ],
            "tasks": [{"item": "mysticalagriculture:prosperity_shard", "count": 8}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}],
        },
        {
            "key": "seeds", "title": "Plant an Inferium Seed",
            "desc": [
                "Eight Inferium Essence around a Wheat Seed make &eInferium Seeds&r, which grow more Inferium Essence. Once a few are in the ground, you'll never need to dig for it again.",
                "",
                "They grow on any farmland, but do best on Essence Farmland, just above.",
            ],
            "tasks": [{"item": "mysticalagriculture:inferium_seeds"}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}],
        },
        {
            "key": "farmland", "title": "Essence Farmland",
            "desc": [
                "Right-click Farmland with an essence to turn it into &eEssence Farmland&r of that tier, or craft it from Farmland and the essence.",
                "",
                "Inferium Seeds yield more essence on higher tier farmland. In a Botany Pot, Mystical crops need farmland of their own tier or better to grow at all.",
            ],
            "tasks": [{"item": "mysticalagriculture:inferium_farmland", "count": 4}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}],
        },
        {
            "key": "watering", "title": "Watering Can", "optional": True,
            "desc": [
                "Right-click your crops with a &eWatering Can&r and they grow faster.",
                "",
                "Upgraded with essence, a can reaches further and grows things quicker. &eShift+right-click&r into the air with an upgraded can to have it water on its own.",
            ],
            "tasks": [{"item": "mysticalagriculture:watering_can"}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}],
        },
        {
            "key": "altar", "title": "The Infusion Altar",
            "desc": [
                "Resource seeds are made on an &eInfusion Altar&r with eight &eInfusion Pedestals&r around it. Place the altar first and it shows you where the pedestals go.",
                "",
                "Put the seed base on the altar and the ingredients on the pedestals, then right-click the altar with a &eWand&r, or give it a redstone signal.",
            ],
            "tasks": [{"item": "mysticalagriculture:infusion_altar"},
                      {"item": "mysticalagriculture:infusion_pedestal", "count": 8}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}],
        },
        {
            "key": "resource_seed", "title": "Your First Resource Seed",
            "desc": [
                "A resource seed grows the real thing: stone, coal, iron, diamond and many more. Each one is a seed base on the altar, with four of the material and four essences on the pedestals.",
                "",
                "Better materials need better essence. Look any seed up in JEI with &eR&r to see what it takes, and start with whatever you use the most of.",
            ],
            "tasks": [{"any": ["mysticalagriculture:stone_seeds", "mysticalagriculture:dirt_seeds",
                               "mysticalagriculture:wood_seeds", "mysticalagriculture:water_seeds",
                               "mysticalagriculture:air_seeds", "mysticalagriculture:earth_seeds",
                               "mysticalagriculture:fire_seeds", "mysticalagriculture:ice_seeds",
                               "mysticalagriculture:nature_seeds", "mysticalagriculture:coal_seeds",
                               "mysticalagriculture:copper_seeds", "mysticalagriculture:nether_seeds",
                               "mysticalagriculture:iron_seeds", "mysticalagriculture:zombie_seeds",
                               "mysticalagriculture:gold_seeds", "mysticalagriculture:diamond_seeds"],
                       "title": "Any resource seed", "icon": "mysticalagriculture:iron_seeds"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "crystal", "title": "Infusion Crystal",
            "desc": [
                "A diamond, four Prosperity Shards and four Inferium Essence make an &eInfusion Crystal&r.",
                "",
                "Four essences of one tier around the crystal make one essence of the next tier up. The crystal comes back each time with one use fewer, and it's good for a thousand.",
            ],
            "tasks": [{"item": "mysticalagriculture:infusion_crystal"}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}],
        },
        {
            "key": "prudentium", "title": "Prudentium", "shape": "hexagon",
            "desc": [
                "Four Inferium around your crystal make &ePrudentium Essence&r, the second of five tiers.",
                "",
                "Each tier opens up more resource seeds, better farmland and faster growth accelerators. Every step up costs four of the step below, so a big inferium field pays off.",
            ],
            "tasks": [{"item": "mysticalagriculture:prudentium_essence", "count": 4}],
            "rewards": [{"xp": 25}, {"crate": "lantern"}, {"item": "mysticalagriculture:prosperity_seed_base", "count": 2}],
        },
        {
            "key": "pot", "title": "A Garden in a Pot",
            "desc": [
                "A &eBotany Pot&r grows a crop on a single block. Give it soil and a seed and it grows right there, with no farmland to trample and no field to fence in.",
                "",
                "Mystical seeds need Essence Farmland as their soil, of their own tier or better. Essence Farmland makes them grow a little faster, too.",
            ],
            "tasks": [{"tag": "botanypots:botany_pots", "title": "Any Botany Pot",
                       "icon": "botanypots:terracotta_botany_pot"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "hopper_pot", "title": "A Row of Pots",
            "desc": [
                "A &eHopper Botany Pot&r harvests its own crop and passes it down into a chest or hopper underneath.",
                "",
                "Line a few up over a row of hoppers feeding one chest, and your essence piles up while you're off doing something else.",
            ],
            "tasks": [{"any": _HOPPER_POTS, "title": "Four Hopper Botany Pots, any kind",
                       "icon": "botanypots:terracotta_hopper_botany_pot", "count": 4}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "accelerator", "title": "Growth Accelerator",
            "desc": [
                "A &eGrowth Accelerator&r goes under your farmland and speeds up the crop above it.",
                "",
                "Stack several, of any tier, as long as the crop is within their range. The tooltip shows each one's range.",
            ],
            "tasks": [{"any": ["mysticalagriculture:inferium_growth_accelerator",
                               "mysticalagriculture:prudentium_growth_accelerator",
                               "mysticalagriculture:tertium_growth_accelerator",
                               "mysticalagriculture:imperium_growth_accelerator",
                               "mysticalagriculture:supremium_growth_accelerator",
                               "mysticalagriculture:awakened_supremium_growth_accelerator"],
                       "title": "Any Growth Accelerator", "icon": "mysticalagriculture:inferium_growth_accelerator"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "tertium", "title": "Tertium", "shape": "hexagon",
            "desc": [
                "Four Prudentium make &eTertium Essence&r, tier three. Every tier opens up seeds for more valuable materials.",
                "",
                "A field of resource crops occasionally drops &eFertilized Essence&r, which works like bone meal on Mystical crops. Save it for the slow ones.",
            ],
            "tasks": [{"item": "mysticalagriculture:tertium_essence", "count": 4}],
            "rewards": [{"xp": 25}, {"crate": "lantern"}, {"item": "mysticalagriculture:prudentium_essence", "count": 16}],
        },
        {
            "key": "pylon", "title": "Harvester Pylon",
            "desc": [
                "Prefer a proper field to pots? The &eHarvester Pylon&r harvests ripe crops in a square around it, from 3x3 up to 9x9, and puts them in a chest on top.",
                "",
                "Set it in the water block of your farm or level with the crops. It needs a hoe inside, which loses a point of durability with each harvest, so Unbreaking is a good friend here.",
            ],
            "tasks": [{"item": "pylons:harvester_pylon"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "trees", "title": "Trees in a Pot", "optional": True,
            "desc": [
                "With Botany Trees, saplings grow in Botany Pots too. An oak sapling in a pot of dirt gives logs, leaves, apples and the odd sapling, with no tree to chop and no leaves to clear.",
                "",
                "Put one in a Hopper Botany Pot and you have a wood supply the size of a block.",
            ],
            "tasks": [{"check": "Got it"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "imperium", "title": "Imperium", "shape": "hexagon",
            "desc": [
                "Four Tertium make &eImperium Essence&r, tier four.",
                "",
                "Your farm is getting big. A Harvester Pylon or a wall of Hopper Botany Pots will save your wrists.",
            ],
            "tasks": [{"item": "mysticalagriculture:imperium_essence", "count": 4}],
            "rewards": [{"xp": 25}, {"crate": "lantern"}, {"item": "mysticalagriculture:tertium_essence", "count": 16}],
        },
        {
            "key": "soul_dagger", "title": "Mob Seeds",
            "desc": [
                "Seeds for mob drops, like zombie or skeleton seeds, need a &eSoul Jar&r full of that mob's souls.",
                "",
                "Carry an empty Soul Jar and kill the mob with a &eSoulium Dagger&r to fill it. Soulium Ore hides in Soulstone veins in the Nether.",
                "",
                "A Soul Extractor can fill jars from spare mob drops too, though more slowly.",
            ],
            "tasks": [{"item": "mysticalagriculture:soulium_dagger"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "masher", "title": "Mob Masher", "optional": True,
            "desc": [
                "Some drops are easier to farm the old way. The &eMob Masher&r is a mob grinder you can fit with upgrades for Sharpness, Looting, Fire Aspect and more. Its kills count as player kills.",
                "",
                "For a steady supply of monsters, &eDreadful Dirt&r spawns them in the dark. Keep it out of the daylight, or it catches fire.",
            ],
            "tasks": [{"item": "mob_grinding_utils:saw"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "absorption", "title": "Absorption Hopper", "optional": True,
            "desc": [
                "The &eAbsorption Hopper&r vacuums up items and experience orbs in a 7x7x7 area around it.",
                "",
                "It can push out of any side you choose, into chests for items and tanks for experience. Radius upgrades make the area bigger.",
            ],
            "tasks": [{"item": "mob_grinding_utils:absorption_hopper"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "supremium", "title": "Supremium", "shape": "hexagon",
            "desc": [
                "Four Imperium make &eSupremium Essence&r, the top tier in Mystical Agriculture itself. The seeds for the most precious materials need it.",
                "",
                "One more step remains, from Mystical Agradditions. That's the finale.",
            ],
            "tasks": [{"item": "mysticalagriculture:supremium_essence", "count": 4}],
            "rewards": [{"xp": 25}, {"crate": "lantern"}, {"item": "mysticalagriculture:imperium_essence", "count": 8}],
        },
        {
            "key": "master_crystal", "title": "Master Infusion Crystal",
            "desc": [
                "The &eMaster Infusion Crystal&r never wears out. It's made from a Supremium Gemstone, Supremium Essence and Prosperity Shards.",
                "",
                "Once you have one, your old crystals can retire.",
            ],
            "tasks": [{"item": "mysticalagriculture:master_infusion_crystal"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "learner", "title": "Deep Learner",
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
            "key": "finale", "title": "Insanium",
            "shape": "hexagon", "size": 1.5, "icon": "mysticalagradditions:insanium_essence",
            "desc": [
                "Four Supremium around an Infusion Crystal make &eInsanium Essence&r, the very top of the ladder.",
                "",
                "For the &eWither Prediction&r, right-click the Wither with a Model Framework (carefully), then train the model past Faulty with several Wither fights. Simulating it costs 2,560 FE a tick, so have power to spare.",
                "",
                "Both are pieces of the &eAllthemodium Alloy Paxel&r, the pack's capstone. The paxel quest gives them back once you've crafted the paxel.",
            ],
            "tasks": [
                {"item": "mysticalagradditions:insanium_essence"},
                {"item": "hostilenetworks:prediction", "components": {"hostilenetworks:data_model": "hostilenetworks:wither"}},
            ],
            "rewards": [{"xp": 50}, {"crate": "ember"}, {"item": "mysticalagradditions:insanium_farmland", "count": 4}],
        },
        {
            "key": "metal_seeds", "title": "Metal in the Soil", "optional": True,
            "desc": [
                "Insanium Essence opens up seeds for the three endgame metals: &eAllthemodium&r, &eVibranium&r and &eUnobtainium Seeds&r, made on the Infusion Altar from their ingots.",
                "",
                "Each one is picky about its soil: it only grows with a block of the same metal under its farmland.",
                "",
                "Eight essence in a ring make one ingot. Slow, but it never runs out.",
            ],
            "tasks": [{"any": ["mysticalagriculture:allthemodium_seeds", "mysticalagriculture:vibranium_seeds",
                               "mysticalagriculture:unobtainium_seeds"],
                       "title": "Any Allthemodium metal seed", "icon": "mysticalagriculture:allthemodium_seeds"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
    ],
}
