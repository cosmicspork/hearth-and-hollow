GATE = {"gateways:gateway": "gateways:overworldian_nights"}

CHAPTER = {
    "file": "monsters_and_mettle",
    "group": "world",
    "title": "Monsters & Mettle",
    "subtitle": "Better gear, harder fights",
    "icon": "apotheosis:sigil_of_socketing",
    "theme": "hunter",
    "layout": {
        "info": ["mettle"],
        "lines": [
            # World Tiers, with each tier's challenge Gateway above it.
            {"spine": ["affix", "frontier", "ascent", "summit", "pinnacle"],
             "branches": {
                 "frontier": {"up": ["frontier_gate"], "down": ["locals"]},
                 "ascent": {"up": ["ascent_gate"]},
                 "summit": {"up": ["summit_gate"]},
                 "pinnacle": {"up": ["pinnacle_gate", "supremacy"]},
             }},
            # The gear guide: gems and the Apotheosis workbenches.
            {"spine": ["gem", "dust", "salvage", "reforge"],
             "branches": {
                 "dust": {"up": ["cutting"], "down": ["sigil"]},
                 "reforge": {"up": ["hellshelf"], "down": ["disenchant"]},
             }},
            # Trial Chambers, down to the mace.
            {"flow": ["trials", "vault", "heavy_core", "mace"]},
            # Fights and keepsakes that need no order.
            {"rows": ["pearl", "nether_trial", "fragments", "trophy", "dummy"]},
        ],
    },
    "quests": [
        {
            "key": "mettle", "title": "Monsters & Mettle", "shape": "gear",
            "desc": [
                "Out in the world, gear isn't just iron or diamond. A sword can roll with bonus damage, a chestplate with extra health, boots with a burst of speed. Some even carry sockets for gems.",
                "",
                "How strong that loot gets, and how strong the monsters guarding it are, depends on your &eWorld Tier&r. Press &eCtrl+T&r to see them.",
                "",
                "The top line climbs the World Tiers. The middle one is a guide to gems and the workbenches, and the bottom ones are fights worth seeking out. Follow whichever you're in the mood for.",
                "",
                "Harder fights mean the odd death. Your things go into a &eGrave&r where you fell, which only you can open, and the chat tells you where. Items with the &eSoulbound&r enchantment stay with you instead: World Tier Haven gives you a book of it.",
            ],
            "tasks": [{"check": "Show me"}],
        },
        {
            "key": "affix", "title": "World Tier: Haven", "shape": "hexagon", "size": 1.5, "icon": "minecraft:golden_sword",
            "desc": [
                "Watch for gear with a colored name. That's an &eaffix item&r: Common, Uncommon, Rare, Epic or Mythic, each with more bonuses than the last.",
                "",
                "They turn up in chests, and on &eElite&r mobs, the ones with names that hit too hard. Pick up your first one and the &eHaven&r tier is yours.",
                "",
                "Until Haven is active, affix items show as Unidentified. Open the World Tier screen with &eCtrl+T&r to check.",
            ],
            "tasks": [{"advancement": "apotheosis:progression/haven"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}, {"book": "epitaphs:soulbound", "level": 1}],
        },
        {
            "key": "dummy", "title": "Practice Makes Perfect", "optional": True,
            "desc": [
                "A &eTarget Dummy&r shows the damage of every hit and your damage per second, so you can tell whether that new affix really is better. Your gear doesn't wear down hitting it.",
                "",
                "Put a pumpkin on its head and it doubles as a scarecrow: animals keep their distance and monsters won't spawn nearby.",
            ],
            "tasks": [{"item": "dummmmmmy:target_dummy"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "locals", "title": "Locals With Attitude", "optional": True, "icon": "endermanoverhaul:icy_pearl",
            "desc": [
                "Creepers and endermen here dress for the biome they live in, and they don't all fight the same way. Endermen out in the End can throw you somewhere else with a single hit.",
                "",
                "Many endermen drop a pearl of their own. Snowy ones drop the &eIcy Pearl&r, which freezes whatever it hits, a &eBubble Pearl&r flies straight with no drop, and an &eAncient Pearl&r calls a friendly enderman to fight for you.",
            ],
            "tasks": [{"tag": "endermanoverhaul:ender_pearls", "title": "Any special pearl", "icon": "endermanoverhaul:icy_pearl"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "frontier", "title": "Ready for the Frontier", "shape": "hexagon", "icon": "minecraft:iron_chestplate",
            "desc": [
                "Wear an affix item in all four armor slots and hold an affix weapon, and the &eFrontier&r tier unlocks.",
                "",
                "Tiers don't switch on by themselves. Open &eCtrl+T&r, pick Frontier and activate it. Monsters get tougher and loot gets better, and from here on &cApothic Invaders&r start to show up.",
                "",
                "You can switch back to an easier tier any time.",
            ],
            "tasks": [{"advancement": "apotheosis:progression/frontier"}],
            "rewards": [{"xp": 25}, {"crate": "lantern"}, {"book": "minecraft:protection", "level": 3}],
        },
        {
            "key": "gem", "title": "A Gem in the Rough", "shape": "hexagon", "icon": "minecraft:amethyst_shard",
            "desc": [
                "&eGems&r turn up in chest loot and now and then from monsters. Bosses and Invaders drop them more often.",
                "",
                "Each gem has a &ePurity&r, from Cracked up to Perfect, and purity is all that sets its strength. A gem gives a different bonus depending on what you put it in: hover over one to see.",
                "",
                "To socket a gem, put the item and the gem together in a &eSmithing Table&r, or pick the gem up and right-click it onto the item. The item needs an empty socket: Uncommon and better gear often has one.",
                "",
                "This line covers what to do with them, and with the gear you outgrow.",
            ],
            "tasks": [{"item": "apotheosis:gem", "title": "Any gem", "icon": "minecraft:amethyst_shard"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "dust", "title": "Crushed", "icon": "apotheosis:gem_dust",
            "desc": [
                "Got a gem you don't need? Drop it on the ground and drop an &eanvil&r on top. It breaks down into &eGem Dust&r.",
                "",
                "Gem Dust goes into nearly every Apotheosis workbench, so crush your spares rather than tossing them.",
            ],
            "tasks": [{"item": "apotheosis:gem_dust"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "cutting", "title": "Cut and Polish", "optional": True,
            "desc": [
                "The &eGem Cutting Table&r raises a gem's purity. It takes a second gem of the same purity, plus Gem Dust and some salvaged materials.",
                "",
                "The better the gem, the more it costs. JEI shows the exact price for each step.",
            ],
            "tasks": [{"item": "apotheosis:gem_cutting_table"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "sigil", "title": "Make Some Room", "optional": True,
            "desc": [
                "No socket on your favorite sword? A &eSigil of Socketing&r adds one. Combine the item and the sigil in a Smithing Table.",
                "",
                "Sigils can add up to two sockets to an item. Changed your mind about a gem? A &eSigil of Withdrawal&r pops it back out, and you keep both.",
                "",
                "The recipe needs &eGem-Fused Slate&r, which is deepslate around a pinch of Gem Dust.",
            ],
            "tasks": [{"item": "apotheosis:sigil_of_socketing"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "salvage", "title": "Waste Not",
            "desc": [
                "Gear you've outgrown is still worth something. The &eSalvaging Table&r breaks affix items down into &eRarity Materials&r, one kind per rarity.",
                "",
                "Common gear gives Mysterious Scrap Metal, Uncommon gives Timeworn Fabric, Rare gives Luminous Crystal Shards, and up from there.",
                "",
                "Those materials pay for reforging, gem cutting and more.",
            ],
            "tasks": [{"item": "apotheosis:salvaging_table"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "reforge", "title": "Try, Try Again",
            "desc": [
                "Love a sword but hate its affixes? Reforge it.",
                "",
                "The &eSimple Reforging Table&r rerolls an item up to Rare. Put in the item, the Rarity Materials for the rarity you want, and &eSigils of Rebirth&r, then pick one of three outcomes, a bit like enchanting.",
                "",
                "It works on plain gear too, so any good sword can become an affix item.",
            ],
            "tasks": [{"item": "apotheosis:simple_reforging_table"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "hellshelf", "title": "Shelves With Heat", "optional": True,
            "desc": [
                "Enchanting goes deeper here. Every shelf has stats: &eEterna&r sets how high you can enchant, &eQuanta&r makes results swing more, and &eArcana&r brings in rarer enchantments.",
                "",
                "A &eHellshelf&r adds more Eterna and Quanta than a bookshelf. Your World Tier caps how far Eterna can take you, so the best shelves pay off in higher tiers.",
                "",
                "The question mark on the enchanting screen shows exactly what you can roll.",
            ],
            "tasks": [{"item": "apothic_enchanting:hellshelf"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "disenchant", "title": "Take It Back",
            "desc": [
                "Found a great enchantment on a rubbish pickaxe? The &eDis-Enchanting Table&r lifts the enchantments off an item and onto a book, for a little experience.",
                "",
                "The item's anvil cost resets too, which makes it cheap to work on again.",
            ],
            "tasks": [{"item": "disenchanting_table:disenchanting_table"},
                      {"check": "Pulled an enchantment onto a book"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}, {"item": "minecraft:book", "count": 4}],
        },
        {
            "key": "pearl", "title": "A Pearl Full of Trouble", "shape": "hexagon", "icon": "gateways:gate_pearl",
            "desc": [
                "A &eGate Pearl&r opens a Gateway: a portal that sends out waves of monsters, and pays out if you beat them all.",
                "",
                "&eOverworldian Nights&r is a good first one: zombies, skeletons, spiders, creepers and witches, with a pile of dungeon loot at the end.",
                "",
                "Hover over a pearl to see its waves, rewards and rules. Use it on a block in an open space and stand back. A Gateway fails if the timer runs out, a monster wanders too far, or it can't find room to spawn, so fight on flat ground and stay close.",
            ],
            "tasks": [{"item": "gateways:gate_pearl", "components": GATE, "title": "Overworldian Nights Gate Pearl"}],
            "rewards": [{"xp": 25}, {"crate": "lantern"},
                        {"item": "apotheosis:gem", "components": {"apotheosis:gem": "apotheosis:core/ballast",
                                                                  "apotheosis:purity": "flawed"}}],
        },
        {
            "key": "frontier_gate", "title": "Challenge Gates", "optional": True, "icon": "gateways:gate_pearl",
            "desc": [
                "Apotheosis has a challenge Gateway for each World Tier past Haven. The Frontier gate is full of zombies and skeletons in affixed armor.",
                "",
                "Win and it pays in affix gear, gems and Gem Dust. Check JEI for the pearl's recipe.",
            ],
            "tasks": [{"advancement": "apotheosis:gateways/frontier"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            # A trophy draws the mob named in its data, so a bare trophy icon is blank.
            "key": "trophy", "title": "Something for the Mantel", "optional": True, "icon": "trophymanager:trophy",
            "icon_components": {"minecraft:custom_data": {"TrophyType": "entity",
                                                          "TrophyEntity": {"entityType": "minecraft:creeper"},
                                                          "Subject": "entity.minecraft.creeper"}},
            "desc": [
                "Monsters very occasionally drop a &eTrophy&r of themselves. Bosses drop them far more often, and the Ender Dragon always does.",
                "",
                "Place one, then right-click it with an empty hand to change its size, rotation and pose: standing, sitting or flying. Right-click it with any slab to swap the stand it sits on, or with armor to dress it up.",
                "",
                "A wall of trophies makes a fine record of your adventures.",
            ],
            "tasks": [{"item": "trophymanager:trophy"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "trials", "title": "Trial Chambers", "icon": "minecraft:trial_key",
            "desc": [
                "Trial Chambers are copper halls buried underground, full of Trial Spawners and Breezes.",
                "",
                "Beat a spawner's wave and it drops loot, sometimes a &eTrial Key&r. Keys open Vaults, the locked boxes with the best loot in the place.",
                "",
                "Bring blocks to wall off corridors, and a shield for the arrows.",
            ],
            "tasks": [{"structure": "minecraft:trial_chambers", "title": "Find a Trial Chamber", "icon": "minecraft:trial_spawner"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "nether_trial", "title": "Trials, but Hotter", "optional": True, "icon": "minecraft:nether_bricks",
            "desc": [
                "The Nether has trial chambers of its own, buried low beneath the lava sea.",
                "",
                "Their vaults hold diamond gear, a mace now and then, and the odd scrap of netherite. The fights are hotter too.",
            ],
            "tasks": [{"structure": "hellish_trials:nether_trial", "title": "Find a Nether trial", "icon": "minecraft:vault"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "fragments", "title": "Skull Fragments", "optional": True, "icon": "wstweaks:fragment",
            "desc": [
                "In the Nether, every skeleton is a Wither Skeleton, not just the ones in fortresses.",
                "",
                "They drop &eWither Skull Fragments&r. Nine fragments craft a Wither Skeleton Skull, so you'll have three skulls long before your luck would give them to you.",
            ],
            "tasks": [{"item": "wstweaks:fragment", "count": 9}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "heavy_core", "title": "Heavier Than It Looks", "icon": "minecraft:heavy_core",
            "desc": [
                "A &eHeavy Core&r is the rarest thing in a Trial Chamber. Drink an Ominous Bottle, beat the chamber's ominous waves for an &eOminous Trial Key&r, and open an &eOminous Vault&r. Now and then one gives a core.",
                "",
                "If luck won't oblige, Oritech can make one. Forge &eReinforced Deepslate&r in the Atomic Forge from deepslate and two duratium ingots, then collide it with &eDuratium Dust&r in the Particle Accelerator.",
                "",
                "Oritech's &eElectric Mace&r needs a core too.",
            ],
            "tasks": [{"item": "minecraft:heavy_core"}],
            "rewards": [{"xp": 25}, {"crate": "lantern"}, {"item": "minecraft:ominous_bottle"}],
        },
        {
            "key": "mace", "title": "Mind the Drop", "shape": "hexagon", "icon": "minecraft:mace",
            "desc": [
                "A Heavy Core and a &eBreeze Rod&r make a &eMace&r. It hits hard on its own, and much harder when you fall onto your target first: the further the drop, the bigger the smash.",
                "",
                "It's also where the Allthemodium maces start. &eAllthemodium Ascent&r upgrades it three times over.",
            ],
            "tasks": [{"item": "minecraft:mace"}],
            "rewards": [{"xp": 25}, {"crate": "lantern"}, {"item": "minecraft:wind_charge", "count": 16}],
        },
        {
            "key": "vault", "title": "Back for Seconds", "icon": "minecraft:vault",
            "desc": [
                "Normally a Vault only opens once for each player. Not here: use another key on a vault you've already opened and it pays out again.",
                "",
                "So a good chamber is worth coming back to.",
                "",
                "Drink an Ominous Bottle before you go in, and the chamber turns ominous: harder fights, &eOminous Trial Keys&r and better vaults.",
            ],
            "tasks": [{"advancement": "minecraft:adventure/under_lock_and_key"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}, {"item": "minecraft:trial_key", "count": 2}],
        },
        {
            "key": "ascent", "title": "World Tier: Ascent", "shape": "hexagon", "icon": "minecraft:diamond_chestplate",
            "desc": [
                "Wear a full set of &aUncommon&r gear, weapon included, and slay an &cApothic Invader&r. They arrive with a loud noise and a beam of light from the sky, and never in Haven.",
                "",
                "Do both and the &eAscent&r tier is yours. Every Invader drops its own affix item, so it's worth the fight.",
            ],
            "tasks": [{"advancement": "apotheosis:progression/ascent"}],
            "rewards": [{"xp": 25}, {"crate": "lantern"},
                        {"item": "apotheosis:gem", "components": {"apotheosis:gem": "apotheosis:core/splendor",
                                                                  "apotheosis:purity": "normal"}},
                        {"book": "minecraft:unbreaking", "level": 3}],
        },
        {
            "key": "ascent_gate", "title": "The Sunlit Ascent", "optional": True, "icon": "gateways:gate_pearl",
            "desc": [
                "Ascent has a challenge Gateway of its own, tougher than the Frontier's and better paid.",
                "",
                "As before, JEI has the pearl's recipe. Bring your best gear, and some food.",
            ],
            "tasks": [{"advancement": "apotheosis:gateways/ascent"}],
            "rewards": [{"xp": 10}, {"crate": "lantern"}],
        },
        {
            "key": "summit", "title": "World Tier: Summit", "shape": "hexagon", "icon": "minecraft:wither_skeleton_skull",
            "desc": [
                "The &eSummit&r takes a full set of &9Rare&r gear, weapon included, and the &cWither&r dead at your feet.",
                "",
                "Pick your arena with care: the Wither breaks blocks as it fights. Three Wither Skeleton Skulls on four soul sand or soul soil summon it, and the Nether's skeletons drop skull fragments.",
            ],
            "tasks": [{"advancement": "apotheosis:progression/summit"}],
            "rewards": [{"xp": 25}, {"crate": "lantern"},
                        {"item": "apotheosis:gem", "components": {"apotheosis:gem": "apotheosis:core/guardian",
                                                                  "apotheosis:purity": "flawless"}}],
        },
        {
            "key": "summit_gate", "title": "The Thundering Summit", "optional": True, "icon": "gateways:gate_pearl",
            "desc": [
                "The Summit's challenge Gateway, another step up from the Ascent's. JEI has the pearl's recipe.",
            ],
            "tasks": [{"advancement": "apotheosis:gateways/summit"}],
            "rewards": [{"xp": 10}, {"crate": "ember"}],
        },
        {
            "key": "pinnacle", "title": "World Tier: Pinnacle", "shape": "hexagon", "size": 1.5, "icon": "minecraft:dragon_head",
            "desc": [
                "The last tier. Wear a full set of &5Epic&r gear, weapon included, and free the End by slaying the &cEnder Dragon&r.",
                "",
                "From here the monsters are as strong as they get, and so is the loot. You can always step back down with &eCtrl+T&r when you'd rather build in peace.",
            ],
            "tasks": [{"advancement": "apotheosis:progression/pinnacle"}],
            "rewards": [{"xp": 50}, {"crate": "ember"},
                        {"item": "apotheosis:gem", "components": {"apotheosis:gem": "apotheosis:core/warlord",
                                                                  "apotheosis:purity": "perfect"}}],
        },
        {
            "key": "pinnacle_gate", "title": "The Apothic Pinnacle", "optional": True, "icon": "gateways:gate_pearl",
            "desc": [
                "The hardest of the tier Gateways. Beat it and you've seen everything Apotheosis can throw at you, nearly.",
            ],
            "tasks": [{"advancement": "apotheosis:gateways/pinnacle"}],
            "rewards": [{"xp": 25}, {"crate": "ember"}],
        },
        {
            "key": "supremacy", "title": "Supremacy", "optional": True, "icon": "gateways:gate_pearl",
            "desc": [
                "Nearly. The &eEndless Gateway of Apothic Invaders&r never stops sending waves.",
                "",
                "Hold out to wave 100 and it gives up a &eSigil of Supremacy&r. Bragging rights don't come bigger.",
            ],
            "tasks": [{"advancement": "apotheosis:gateways/sigil_of_supremacy"}],
            "rewards": [{"xp": 50}, {"crate": "ember"}],
        },
    ],
}
