CHAPTER = {
    "file": "mekanism",
    "group": "hum",
    "title": "Mekanism",
    "subtitle": "Up to five ingots from every ore",
    "icon": "mekanism:enrichment_chamber",
    # Two ladders where the order is real, ore processing and the alloys and circuits, and the
    # factory tiers. Machines, upgrades and the chemistry kit need no order, so they sit in blocks.
    "layout": {
        "lines": [
            {"flow": ["start", "infuser", "steel", "enrich", "purify", "inject", "dissolve", "wash", "crystallize",
                      "finale"]},
            {"flow": ["circuit", "infused", "advanced", "reinforced", "elite", "refined", "atomic", "ultimate"]},
            {"flow": ["factory", "installer", "ultimate_factory"]},
            {"rows": ["ores", "crusher", "sulfur", "fluorite", "glowstone", "smelter", "sawmill", "combiner",
                      "compressor", "assemblicator", "upgrades", "upgrade_energy", "upgrade_chemical",
                      "upgrade_muffling"],
             "per_row": 7},
            {"rows": ["separator", "pump", "brine", "evaporation", "hcl", "rotary", "prc", "hdpe"]},
        ],
    },
    "quests": [
        {
            "key": "start", "title": "Mekanism",
            "shape": "hexagon", "size": 1.5, "icon": "mekanism:metallurgic_infuser",
            "desc": [
                "Mekanism turns one ore into two ingots, then three, then four, and finally five. Each step is a new machine and a new chemical, and each one pays you back on every ore you mine from then on.",
                "",
                "Almost all of it starts with &eosmium&r. Smelt a stack and keep it handy.",
            ],
            "tasks": [{"tag": "c:ingots/osmium", "title": "Osmium Ingot", "icon": "alltheores:osmium_ingot"}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}],
        },
        {
            "key": "infuser", "title": "The Metallurgic Infuser",
            "desc": [
                "The &eMetallurgic Infuser&r soaks an item in an infusion: carbon from coal, redstone, diamond and more. It's where Mekanism's alloys, circuits and steel come from.",
                "",
                "The infusion is stored in a gauge, so you can top it up ahead of time and let it work through a stack.",
                "",
                "Hover over the infuser and press &eU&r to see everything it makes.",
            ],
            "tasks": [{"item": "mekanism:metallurgic_infuser"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "steel", "title": "Steel, the Mekanism Way",
            "desc": [
                "Infuse an iron ingot with carbon for &eEnriched Iron&r, then infuse that with carbon again for Steel Dust. Smelt the dust and you have steel.",
                "",
                "Steel, glass and osmium make the &eSteel Casing&r at the heart of most Mekanism machines. Steel also goes into Universal Cables.",
            ],
            "tasks": [{"tag": "c:ingots/steel", "title": "Steel Ingot", "icon": "mekanism:ingot_steel", "count": 8}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "enrich", "title": "Double Your Ores", "shape": "hexagon",
            "desc": [
                "The &eEnrichment Chamber&r turns one ore into two dusts. Smelt them and every ore you mine is worth two ingots.",
                "",
                "Raw ore works too, at a lower rate: three raw ores make four dusts. Ore blocks get the full deal.",
                "",
                "That's the first tier of five. Keep going.",
            ],
            "tasks": [{"item": "mekanism:enrichment_chamber"}],
            "rewards": [{"xp": 25}, {"crate": "lantern"}, {"item": "mekanism:alloy_infused", "count": 4},
                        {"item": "mekanism:basic_control_circuit", "count": 2}],
        },
        {
            "key": "purify", "title": "Triple Your Ores", "shape": "hexagon",
            "desc": [
                "The &ePurification Chamber&r feeds &eoxygen&r into each ore and gets three &eClumps&r out.",
                "",
                "Crush the clumps into Dirty Dust, enrich that into dust, and smelt it. Three ingots per ore.",
                "",
                "Oxygen comes from the Electrolytic Separator, on the chemistry line below.",
            ],
            "tasks": [{"item": "mekanism:purification_chamber"}],
            "rewards": [{"xp": 25}, {"crate": "lantern"}, {"item": "mekanism:advanced_control_circuit", "count": 2}],
        },
        {
            "key": "inject", "title": "Quadruple Your Ores", "shape": "hexagon",
            "desc": [
                "The &eChemical Injection Chamber&r uses &ehydrogen chloride&r to break each ore into four &eShards&r.",
                "",
                "Send the shards through the Purification Chamber to make clumps, then on through the Crusher, the Enrichment Chamber and the furnace. Four ingots per ore.",
                "",
                "Hydrogen chloride takes a little chemistry: see the chemistry line below.",
            ],
            "tasks": [{"item": "mekanism:chemical_injection_chamber"}],
            "rewards": [{"xp": 25}, {"crate": "lantern"}, {"item": "mekanism:alloy_reinforced", "count": 4}],
        },
        {
            "key": "dissolve", "title": "Dissolving Ore",
            "desc": [
                "Tier five starts by dissolving ore in &esulfuric acid&r. The &eChemical Dissolution Chamber&r turns each ore into a big helping of &eDirty Slurry&r.",
                "",
                "Slurry is a chemical, not an item, so it travels through Pressurized Tubes like the gases do.",
            ],
            "tasks": [{"item": "mekanism:chemical_dissolution_chamber"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "wash", "title": "Washing Slurry",
            "desc": [
                "Dirty slurry needs a wash. The &eChemical Washer&r cleans it with water, turning Dirty Slurry into Clean Slurry.",
                "",
                "It drinks a lot of water. An &eElectric Pump&r over a lake keeps it well fed.",
            ],
            "tasks": [{"item": "mekanism:chemical_washer"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "crystallize", "title": "Quintuple Your Ores", "shape": "hexagon",
            "desc": [
                "The &eChemical Crystallizer&r turns clean slurry into &eCrystals&r: five from every ore.",
                "",
                "Crystals go into the Chemical Injection Chamber to become shards, and from there down the same line as tier four. Five ingots per ore.",
            ],
            "tasks": [{"item": "mekanism:chemical_crystallizer"}],
            "rewards": [{"xp": 25}, {"crate": "lantern"}, {"item": "mekanism:alloy_atomic", "count": 2}],
        },
        {
            "key": "finale", "title": "Five From One",
            "shape": "hexagon", "size": 1.5, "icon": "mekanism:ultimate_control_circuit",
            "desc": [
                "Five ingots from every ore. Every swing of the pickaxe is worth five times what it used to be.",
                "",
                "The &eUltimate Control Circuit&r is also one of the pieces of the &eAllthemodium Alloy Paxel&r, the pack's capstone. The paxel quest gives it back once you've crafted the paxel.",
                "",
                "From here, swap your machines for factories and let the line chew through everything you dig up.",
            ],
            "tasks": [
                {"tag": "c:crystals", "title": "Crystals of any metal", "icon": "mekanism:crystal_iron", "count": 25},
                {"item": "mekanism:ultimate_control_circuit"},
            ],
            "rewards": [{"xp": 50}, {"crate": "ember"}, {"item": "mekanism:upgrade_speed", "count": 4}],
        },
        {
            "key": "circuit", "title": "Basic Control Circuit", "shape": "hexagon",
            "desc": [
                "Nearly every Mekanism machine needs a &eBasic Control Circuit&r. Infuse an osmium ingot with redstone to make one.",
                "",
                "Better circuits build on this one, all the way up to Ultimate. Make a few extra while you're here.",
            ],
            "tasks": [{"item": "mekanism:basic_control_circuit", "count": 4}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "infused", "title": "Infused Alloy",
            "desc": [
                "Infuse a &ecopper ingot&r with redstone and you get &eInfused Alloy&r, the first of Mekanism's three alloys.",
                "",
                "You'll go through a lot of it. Generators, the Electrolytic Separator, the Purification Chamber and the chemical machines all want some.",
            ],
            "tasks": [{"item": "mekanism:alloy_infused", "count": 8}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "advanced", "title": "Advanced Control Circuit",
            "desc": [
                "A Basic Control Circuit between two Infused Alloys makes an &eAdvanced Control Circuit&r. You can also infuse a Basic circuit with more redstone, if you'd rather save the alloy.",
                "",
                "The Purification Chamber needs two.",
            ],
            "tasks": [{"item": "mekanism:advanced_control_circuit", "count": 2}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "reinforced", "title": "Reinforced Alloy",
            "desc": [
                "Infuse &eInfused Alloy&r with diamond for &eReinforced Alloy&r, the second of the three alloys.",
                "",
                "Two of them and an Advanced Control Circuit make the next circuit up.",
            ],
            "tasks": [{"item": "mekanism:alloy_reinforced", "count": 4}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "elite", "title": "Elite Control Circuit",
            "desc": [
                "An Advanced Control Circuit between two Reinforced Alloys makes an &eElite Control Circuit&r.",
                "",
                "The Chemical Injection Chamber needs two, plus Reinforced Alloy, gold, and a Purification Chamber to build on.",
            ],
            "tasks": [{"item": "mekanism:elite_control_circuit", "count": 2}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "refined", "title": "Refined Obsidian",
            "desc": [
                "The last tier is built with &eRefined Obsidian&r.",
                "",
                "Crush obsidian into dust, infuse the dust with diamond, then press the result into an ingot in an &eOsmium Compressor&r. The compressor burns osmium to do it.",
            ],
            "tasks": [{"item": "mekanism:ingot_refined_obsidian", "count": 4}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "atomic", "title": "Atomic Alloy",
            "desc": [
                "Infuse Reinforced Alloy with refined obsidian for &eAtomic Alloy&r, the top of the alloy ladder.",
                "",
                "Two Atomic Alloys around an Elite Control Circuit make an &eUltimate Control Circuit&r. Each machine in the last tier needs two, so make plenty.",
            ],
            "tasks": [{"item": "mekanism:alloy_atomic", "count": 4}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "ultimate", "title": "Ultimate Control Circuit", "shape": "hexagon",
            "desc": [
                "Two Atomic Alloys around an Elite Control Circuit make the &eUltimate Control Circuit&r, the top of the ladder.",
                "",
                "The last tier of ore processing, the MekaSuit and the Meka-Tool all need them. It's also one of the pieces of the &eAllthemodium Alloy Paxel&r.",
            ],
            "tasks": [{"item": "mekanism:ultimate_control_circuit", "count": 2}],
            "rewards": [{"xp": 25}, {"crate": "lantern"}],
        },
        {
            "key": "factory", "title": "More Lanes", "shape": "hexagon",
            "desc": [
                "A &eFactory&r is a machine with several lanes, so it works on more than one stack at a time.",
                "",
                "Craft one from the machine it replaces, or upgrade a machine where it stands with a &eTier Installer&r. Installers run from Basic up to Ultimate, and each step adds lanes.",
            ],
            "tasks": [{"any": ["mekanism:basic_enriching_factory", "mekanism:basic_smelting_factory",
                               "mekanism:basic_crushing_factory", "mekanism:basic_purifying_factory",
                               "mekanism:basic_injecting_factory"],
                       "title": "Any basic factory", "icon": "mekanism:basic_enriching_factory"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "installer", "title": "Upgrade in Place",
            "desc": [
                "A &eTier Installer&r turns a machine into a factory, or a factory into the next tier up, without picking it up.",
                "",
                "Right-click the machine with it. Basic, Advanced, Elite and Ultimate each add lanes.",
            ],
            "tasks": [{"item": "mekanism:basic_tier_installer"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "ultimate_factory", "title": "Nine Lanes",
            "desc": [
                "An &eUltimate Factory&r runs nine stacks side by side. Put one at each step of your ore line and nothing will keep up with you.",
            ],
            "tasks": [{"any": ["mekanism:ultimate_enriching_factory", "mekanism:ultimate_smelting_factory", "mekanism:ultimate_crushing_factory", "mekanism:ultimate_purifying_factory", "mekanism:ultimate_injecting_factory"], "title": "Any ultimate factory", "icon": "mekanism:ultimate_enriching_factory"}],
            "rewards": [{"xp": 25}, {"crate": "lantern"}],
        },
        {
            "key": "ores", "title": "Where the Osmium Is",
            "desc": [
                "Mekanism's own ores are switched off here. Osmium, tin, lead, uranium and fluorite come from the same AllTheOres veins as everything else, and Mekanism's machines take them happily.",
                "",
                "Save some ore blocks whole with &eSilk Touch&r. Every machine in this chapter pays out more for an ore block than for raw ore.",
            ],
            "tasks": [{"tag": "c:ores/osmium", "title": "Osmium Ore", "icon": "alltheores:osmium_ore"}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}],
        },
        {
            "key": "crusher", "title": "The Crusher",
            "desc": [
                "The &eCrusher&r grinds ingots back into dust and, more to the point, turns &eClumps&r into &eDirty Dust&r.",
                "",
                "Dirty Dust goes back through the Enrichment Chamber to come out clean. Every higher tier of ore processing ends with this pair, so build them side by side.",
            ],
            "tasks": [{"item": "mekanism:crusher"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "sulfur", "title": "Sulfuric Acid",
            "desc": [
                "Sulfur Ore drops Sulfur straight out of the ground.",
                "",
                "A &eChemical Oxidizer&r turns it into sulfur dioxide. A Chemical Infuser adds oxygen to make sulfur trioxide, and a second infuser mixes that with water vapor for &esulfuric acid&r. A &eRotary Condensentrator&r turns water into water vapor.",
                "",
                "It's a long chain, so build it once and leave it running.",
            ],
            "tasks": [{"tag": "c:dusts/sulfur", "title": "Sulfur", "icon": "alltheores:sulfur", "count": 16}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "fluorite", "title": "Fluorite",
            "desc": [
                "The &eChemical Crystallizer&r needs two &eFluorite&r gems along with its Ultimate Control Circuits.",
                "",
                "Fluorite Ore turns up at most depths. It's never plentiful, so pocket every piece you see.",
            ],
            "tasks": [{"tag": "c:gems/fluorite", "title": "Fluorite", "icon": "alltheores:fluorite", "count": 2}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "glowstone", "title": "Refined Glowstone", "optional": True,
            "desc": [
                "Glowstone dust pressed in the &eOsmium Compressor&r becomes &eRefined Glowstone&r.",
                "",
                "It glows, and it goes into Teleporter Frames and a few of the fancier machines.",
            ],
            "tasks": [{"item": "mekanism:ingot_refined_glowstone", "count": 4}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "smelter", "title": "The Energized Smelter", "optional": True,
            "desc": [
                "An electric furnace. The &eEnergized Smelter&r cooks anything a furnace would, on power instead of fuel, and takes upgrades.",
            ],
            "tasks": [{"item": "mekanism:energized_smelter"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "sawmill", "title": "The Precision Sawmill", "optional": True,
            "desc": [
                "The &ePrecision Sawmill&r cuts logs into more planks than a crafting table does, with sawdust on the side.",
            ],
            "tasks": [{"item": "mekanism:precision_sawmill"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "combiner", "title": "The Combiner", "optional": True,
            "desc": [
                "The &eCombiner&r presses things together, like dust and stone back into ore. JEI shows what it makes.",
            ],
            "tasks": [{"item": "mekanism:combiner"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "compressor", "title": "The Osmium Compressor", "optional": True,
            "desc": [
                "The &eOsmium Compressor&r burns osmium to press dusts into Refined Obsidian and Refined Glowstone.",
            ],
            "tasks": [{"item": "mekanism:osmium_compressor"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "assemblicator", "title": "The Formulaic Assemblicator", "optional": True,
            "desc": [
                "The &eFormulaic Assemblicator&r crafts for you. Write a recipe onto a &eCrafting Formula&r, slot it in, and it crafts from its inventory on its own.",
                "",
                "It doubles as a crafting table that keeps its ingredients.",
            ],
            "tasks": [{"item": "mekanism:formulaic_assemblicator"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "upgrades", "title": "Faster, Please",
            "desc": [
                "Mekanism machines have upgrade slots. &eSpeed Upgrades&r make a machine work faster and use more power, and &eEnergy Upgrades&r bring the power bill back down.",
                "",
                "The slowest machine in your line sets the pace for the whole thing, so upgrade that one first.",
            ],
            "tasks": [{"item": "mekanism:upgrade_speed"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "upgrade_energy", "title": "Energy Upgrade", "optional": True,
            "desc": [
                "&eEnergy Upgrades&r cut a machine's power use and let it store more. Pair them with Speed Upgrades.",
            ],
            "tasks": [{"item": "mekanism:upgrade_energy"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "upgrade_chemical", "title": "Chemical Upgrade", "optional": True,
            "desc": [
                "&eChemical Upgrades&r make a machine go further on its gas, like the oxygen in a Purification Chamber.",
            ],
            "tasks": [{"item": "mekanism:upgrade_chemical"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "upgrade_muffling", "title": "Muffling Upgrade", "optional": True,
            "desc": [
                "A room full of machines gets loud. &eMuffling Upgrades&r quiet them down.",
            ],
            "tasks": [{"item": "mekanism:upgrade_muffling"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "separator", "title": "Splitting Water", "shape": "hexagon",
            "desc": [
                "The &eElectrolytic Separator&r splits water into &ehydrogen&r and &eoxygen&r. Pipe water in, and run Pressurized Tubes from the oxygen side to your Purification Chamber.",
                "",
                "Each output has a button to dump what you don't need, but don't throw the hydrogen away for long. Tier four wants it.",
            ],
            "tasks": [{"item": "mekanism:electrolytic_separator"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "pump", "title": "Drain the Lake", "optional": True,
            "desc": [
                "The &eElectric Pump&r pulls fluid up from the world: water for your Chemical Washer, or lava from the Nether.",
                "",
                "It works its way outward through connected fluid, so one pump over a lake goes a long way.",
            ],
            "tasks": [{"item": "mekanism:electric_pump"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "brine", "title": "Brine",
            "desc": [
                "Hydrogen chloride needs &echlorine&r, and chlorine comes from &ebrine&r.",
                "",
                "The quick way is a &eChemical Oxidizer&r fed with salt. Salt Blocks form patches on the beds of lakes and seas, where you'd find clay, and the Enrichment Chamber turns each one into four Salt. Salt Ore underground works too.",
                "",
                "The grand way is a &eThermal Evaporation Plant&r, a multiblock that draws brine out of plain water. Look up its controller in JEI: Just Enough Mekanism Multiblocks shows every Mekanism multiblock layer by layer, with the full bill of materials.",
            ],
            "tasks": [{"any": ["mekanism:chemical_oxidizer", "mekanism:thermal_evaporation_controller"],
                       "title": "A Chemical Oxidizer or a Thermal Evaporation Controller",
                       "icon": "mekanism:chemical_oxidizer"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "evaporation", "title": "Brine From Seawater", "optional": True,
            "desc": [
                "The &eThermal Evaporation Plant&r is a tall tower of Thermal Evaporation Blocks with a controller and a valve. Pour water in and brine comes out, faster the hotter it runs.",
                "",
                "Just Enough Mekanism Multiblocks shows the shape in JEI. Look up the controller.",
            ],
            "tasks": [{"item": "mekanism:thermal_evaporation_controller"}, {"item": "mekanism:thermal_evaporation_valve"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "hcl", "title": "Hydrogen Chloride",
            "desc": [
                "Run brine through a second &eElectrolytic Separator&r to get chlorine, with some sodium on the side.",
                "",
                "A &eChemical Infuser&r then combines that chlorine with hydrogen from your first separator. Pipe the &ehydrogen chloride&r into the Chemical Injection Chamber and tier four is running.",
            ],
            "tasks": [{"item": "mekanism:chemical_infuser"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "rotary", "title": "Gas to Liquid",
            "desc": [
                "The &eRotary Condensentrator&r turns chemicals into their fluid form and back again. Flip the switch on its screen to choose which way.",
                "",
                "It's how water becomes water vapor for sulfuric acid, and how ethylene becomes a liquid for plastic.",
            ],
            "tasks": [{"item": "mekanism:rotary_condensentrator"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "prc", "title": "Pressurized Reactions",
            "desc": [
                "The &ePressurized Reaction Chamber&r takes an item, a fluid and a gas all at once, and gives an item and a gas back.",
                "",
                "Feed it Bio Fuel, water and hydrogen and you get &eSubstrate&r and ethylene. That's the road to plastic.",
            ],
            "tasks": [{"item": "mekanism:pressurized_reaction_chamber"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "hdpe", "title": "Plastic", "shape": "hexagon",
            "desc": [
                "Substrate with liquid ethylene and oxygen makes &eHDPE Pellets&r in the PRC. Three pellets in an Enrichment Chamber press into an &eHDPE Sheet&r.",
                "",
                "Sheets go into module bases, the MekaSuit, the Meka-Tool and their workbench.",
            ],
            "tasks": [{"item": "mekanism:hdpe_sheet", "count": 4}],
            "rewards": [{"xp": 25}, {"crate": "lantern"}],
        },
    ],
}
