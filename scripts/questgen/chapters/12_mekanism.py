CHAPTER = {
    "file": "mekanism",
    "group": "hum",
    "title": "Mekanism",
    "subtitle": "Up to five ingots from every ore",
    "icon": "mekanism:enrichment_chamber",
    # Ore processing is the backbone; the rest are tracks you pick up as you need them.
    "layout": {
        "lines": [
            {"spine": ["start", "infuser", "steel", "enrich", "purify", "inject", "dissolve", "wash", "crystallize",
                       "finale"],
             "branches": {
                 "start": {"up": ["ores"]},
                 "enrich": {"up": ["crusher"]},
                 "dissolve": {"up": ["sulfur"], "down": ["fluorite"]},
             }},
            {"spine": ["circuit", "infused", "advanced", "reinforced", "elite", "refined", "atomic", "ultimate"],
             "branches": {"refined": {"up": ["glowstone"]}}},
            {"spine": ["heat_gen", "wind", "solar", "adv_solar", "gas_gen", "bio_gen", "energy_cube", "induction"],
             "branches": {
                 "energy_cube": {"up": ["chargepad"], "down": ["ultimate_cube"]},
                 "induction": {"up": ["induction_ultimate"]},
             }},
            {"spine": ["separator", "brine", "hcl", "rotary", "prc", "hdpe", "evaporation"],
             "branches": {"separator": {"up": ["pump"]}}},
            {"spine": ["cables", "transporter", "sorter", "mech_pipe", "tube", "conductor", "configurator"],
             "branches": {"configurator": {"up": ["config_card"]}}},
            {"spine": ["bin", "fluid_tank", "chem_tank", "personal_chest", "dynamic_tank", "qio"],
             "branches": {"bin": {"up": ["cardboard"]}}},
            {"spine": ["factory", "installer", "ultimate_factory", "smelter", "sawmill", "combiner", "compressor",
                       "assemblicator", "upgrades"],
             "branches": {"upgrades": {"up": ["upgrade_energy", "upgrade_chemical"], "down": ["upgrade_muffling"]}}},
            {"spine": ["disassembler", "jetpack", "free_runners", "scuba", "portable_teleporter", "meka_tool",
                       "mekasuit", "modules"],
             "branches": {
                 "meka_tool": {"up": ["module_excavation", "module_vein"]},
                 "modules": {"up": ["module_gravity", "module_jetpack"], "down": ["module_magnet", "module_elytra"]},
             }},
            {"spine": ["teleporter", "robit", "digital_miner", "entangloporter"]},
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
            "key": "heat_gen", "title": "Something to Run It On", "shape": "hexagon",
            "desc": [
                "Mekanism's machines run on power, and the &eHeat Generator&r is the easy first source. It burns lava or anything a furnace would take.",
                "",
                "It's made from iron, copper, planks and one osmium ingot, so you can build it today.",
            ],
            "tasks": [{"item": "mekanismgenerators:heat_generator"}],
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
            "key": "cables", "title": "Power Lines", "shape": "hexagon",
            "desc": [
                "Steel and redstone make eight &eBasic Universal Cables&r. Run them from your generators to your machines and the power follows.",
                "",
                "Every Mekanism machine has a side configuration tab in its screen. Use it to choose which faces take power, items and chemicals, and which push them out.",
            ],
            "tasks": [{"item": "mekanism:basic_universal_cable", "count": 8}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "wind", "title": "Catch the Wind",
            "desc": [
                "A &eWind Generator&r needs no fuel at all. It makes more power the higher up it stands, so hilltops and tall towers are worth the climb.",
                "",
                "A row of them along a ridge makes a fine little wind farm.",
            ],
            "tasks": [{"item": "mekanismgenerators:wind_generator"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "solar", "title": "Soak Up the Sun",
            "desc": [
                "&eSolar Generators&r run whenever the sun can see them. Four of them and some Infused Alloy make an &eAdvanced Solar Generator&r, which does the job in one block.",
                "",
                "Pair your solar farm with wind or a Heat Generator so the lights stay on at night.",
            ],
            "tasks": [{"any": ["mekanismgenerators:solar_generator", "mekanismgenerators:advanced_solar_generator"],
                       "title": "Four solar generators, either kind", "icon": "mekanismgenerators:solar_generator",
                       "count": 4}],
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
            "key": "adv_solar", "title": "Bigger Panels",
            "desc": [
                "Four Solar Generators and some Infused Alloy make an &eAdvanced Solar Generator&r. It makes far more power than the four did, in one block.",
                "",
                "It still sleeps at night, so keep something else running beside it.",
            ],
            "tasks": [{"item": "mekanismgenerators:advanced_solar_generator"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "gas_gen", "title": "Burning Gas",
            "desc": [
                "The &eGas-Burning Generator&r runs on gases like &ehydrogen&r and ethylene.",
                "",
                "Your Electrolytic Separator makes hydrogen from water, so a separator and this generator side by side turn water into power. It's not free: the separator needs some of that power back.",
            ],
            "tasks": [{"item": "mekanismgenerators:gas_burning_generator"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "bio_gen", "title": "Compost Power",
            "desc": [
                "The &eBio-Generator&r burns &eBio Fuel&r, which the Crusher makes from almost anything that grows: crops, seeds, saplings, leaves, mushrooms, kelp.",
                "",
                "Hook it to a farm and your harvest powers your machines.",
            ],
            "tasks": [{"item": "mekanismgenerators:bio_generator"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}, {"item": "mekanism:block_bio_fuel", "count": 4}],
        },
        {
            "key": "energy_cube", "title": "Store the Spare", "shape": "hexagon",
            "desc": [
                "An &eEnergy Cube&r is a battery. It fills up while your generators run and pays it out when they stop.",
                "",
                "Each face can be set to take power in or push it out, and a cube can charge an item you put in it.",
            ],
            "tasks": [{"item": "mekanism:basic_energy_cube"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "ultimate_cube", "title": "A Bigger Battery", "optional": True,
            "desc": [
                "Energy Cubes go from Basic up to Ultimate, each holding far more than the one before. Craft each tier from the one below.",
            ],
            "tasks": [{"item": "mekanism:ultimate_energy_cube"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "chargepad", "title": "Stand Here", "optional": True,
            "desc": [
                "A &eChargepad&r charges anything powered in your inventory while you stand on it, from any mod: tools, jetpacks, gadgets.",
                "",
                "Put one by the door.",
            ],
            "tasks": [{"item": "mekanism:chargepad"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "induction", "title": "The Induction Matrix", "shape": "hexagon", "wide": True,
            "desc": [
                "For serious storage, build an &eInduction Matrix&r: a hollow box of &eInduction Casing&r with a port or two, filled with &eInduction Cells&r and &eProviders&r.",
                "",
                "Cells set how much it holds. Providers set how fast power moves in and out. Look it up in JEI to see the layout.",
            ],
            "tasks": [{"item": "mekanism:induction_casing", "count": 8}, {"item": "mekanism:induction_port"}, {"item": "mekanism:basic_induction_cell"}, {"item": "mekanism:basic_induction_provider"}],
            "rewards": [{"xp": 25}, {"crate": "lantern"}],
        },
        {
            "key": "induction_ultimate", "title": "Ultimate Cells", "optional": True,
            "desc": [
                "Induction Cells and Providers go up to Ultimate too. A matrix full of Ultimate Cells holds more power than you'll likely ever need.",
                "",
                "Almost: the end of this chapter asks for a lot.",
            ],
            "tasks": [{"item": "mekanism:ultimate_induction_cell"}, {"item": "mekanism:ultimate_induction_provider"}],
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
            "key": "transporter", "title": "Moving Items",
            "desc": [
                "A &eLogistical Transporter&r carries items from one inventory to another. You can watch them ride along the pipe.",
                "",
                "Machines push their output into a transporter by themselves if the side config says so.",
            ],
            "tasks": [{"item": "mekanism:basic_logistical_transporter", "count": 8}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "sorter", "title": "Sort It Out",
            "desc": [
                "A &eLogistical Sorter&r sits on a chest and pulls items out by filter, sending each kind down the transporter you choose.",
                "",
                "It's also a part in the Digital Miner.",
            ],
            "tasks": [{"item": "mekanism:logistical_sorter"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "mech_pipe", "title": "Moving Fluids",
            "desc": [
                "&eMechanical Pipes&r carry fluids: water to the washer, lava to the Heat Generator.",
            ],
            "tasks": [{"item": "mekanism:basic_mechanical_pipe", "count": 8}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "tube", "title": "Moving Gases",
            "desc": [
                "&ePressurized Tubes&r carry chemicals: gases, slurries and the rest. Oxygen, hydrogen chloride and sulfuric acid all travel in them.",
            ],
            "tasks": [{"item": "mekanism:basic_pressurized_tube", "count": 8}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "conductor", "title": "Moving Heat", "optional": True,
            "desc": [
                "&eThermodynamic Conductors&r carry heat between blocks that use it, like a Resistive Heater and the Thermal Evaporation Plant.",
            ],
            "tasks": [{"item": "mekanism:basic_thermodynamic_conductor", "count": 4}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "configurator", "title": "The Configurator", "shape": "hexagon",
            "desc": [
                "The &eConfigurator&r is Mekanism's wrench. It can set a machine's sides, empty its tanks, rotate it, or pick it up.",
                "",
                "Hover over it to see its current mode and the key that switches it.",
            ],
            "tasks": [{"item": "mekanism:configurator"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "config_card", "title": "Copy the Settings", "optional": True,
            "desc": [
                "A &eConfiguration Card&r copies a machine's side configuration. Sneak and right-click one machine to copy, then right-click another to paste.",
                "",
                "Set up one factory the way you like and stamp the rest.",
            ],
            "tasks": [{"item": "mekanism:configuration_card"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "bin", "title": "Bins", "shape": "hexagon",
            "desc": [
                "A &eBin&r holds a huge stack of one item. Left-click to take a stack, right-click to put in what you're holding.",
                "",
                "Bins come in tiers, each holding more than the last.",
            ],
            "tasks": [{"item": "mekanism:basic_bin"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "cardboard", "title": "Moving Day, Mekanism Style", "optional": True,
            "desc": [
                "A &eCardboard Box&r picks up a block, contents and all. Sneak and right-click a full chest, carry it anywhere, and put it down again.",
            ],
            "tasks": [{"item": "mekanism:cardboard_box"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "fluid_tank", "title": "Fluid Tanks",
            "desc": [
                "A &eFluid Tank&r holds one fluid and keeps it when you pick the tank up. Stack them for more.",
            ],
            "tasks": [{"item": "mekanism:basic_fluid_tank"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "chem_tank", "title": "Chemical Tanks",
            "desc": [
                "A &eChemical Tank&r does the same for gases and slurries. A full tank of hydrogen in your pocket fills a jetpack anywhere.",
            ],
            "tasks": [{"item": "mekanism:basic_chemical_tank"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "personal_chest", "title": "Personal Storage",
            "desc": [
                "A &ePersonal Chest&r is a 54-slot chest you can open straight from your inventory. A &ePersonal Barrel&r is the same, barrel-shaped.",
                "",
                "It's also the heart of the Robit.",
            ],
            "tasks": [{"any": ["mekanism:personal_chest", "mekanism:personal_barrel"], "title": "A Personal Chest or Barrel", "icon": "mekanism:personal_chest"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "dynamic_tank", "title": "The Dynamic Tank", "optional": True,
            "desc": [
                "A &eDynamic Tank&r is a multiblock box of casing and valves that stores a vast amount of one fluid or chemical. Make it any size you like, within limits.",
                "",
                "JEI shows how to build it.",
            ],
            "tasks": [{"item": "mekanism:dynamic_tank", "count": 8}, {"item": "mekanism:dynamic_valve"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "qio", "title": "Quantum Item Orchestration", "optional": True,
            "desc": [
                "Mekanism has its own storage network, &eQIO&r: a Drive Array full of QIO Drives, reached from a Dashboard anywhere on the same frequency.",
                "",
                "Refined Storage does the same job here, so this is for anyone who'd rather keep it all Mekanism.",
            ],
            "tasks": [{"item": "mekanism:qio_drive_array"}, {"item": "mekanism:qio_dashboard"}],
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
            "key": "disassembler", "title": "The Atomic Disassembler", "shape": "hexagon",
            "desc": [
                "The &eAtomic Disassembler&r is a powered tool that mines, chops and digs anything. Its modes trade speed for power use.",
                "",
                "It also has a vein mode for ores and logs. Charge it like any other powered tool.",
            ],
            "tasks": [{"item": "mekanism:atomic_disassembler"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "jetpack", "title": "Hydrogen Jetpack",
            "desc": [
                "Mekanism's &eJetpack&r burns hydrogen instead of FE. Fill it from your Electrolytic Separator or a Chemical Tank.",
                "",
                "It has a hover mode too. An &eArmored Jetpack&r adds protection, if you can spare the chest slot.",
            ],
            "tasks": [{"any": ["mekanism:jetpack", "mekanism:jetpack_armored"], "title": "A Jetpack, plain or armored", "icon": "mekanism:jetpack"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "free_runners", "title": "Free Runners",
            "desc": [
                "&eFree Runners&r stop fall damage and let you walk straight up single blocks. They run on power.",
            ],
            "tasks": [{"item": "mekanism:free_runners"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "scuba", "title": "Under the Sea", "optional": True,
            "desc": [
                "A &eScuba Mask&r and a &eScuba Tank&r full of oxygen let you breathe underwater for a good long while.",
            ],
            "tasks": [{"item": "mekanism:scuba_mask"}, {"item": "mekanism:scuba_tank"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "portable_teleporter", "title": "Teleporter in Your Pocket", "optional": True,
            "desc": [
                "A &ePortable Teleporter&r takes you to any Teleporter on a frequency you can use, from anywhere. It runs on power, and longer trips cost more.",
            ],
            "tasks": [{"item": "mekanism:portable_teleporter"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "meka_tool", "title": "The Meka-Tool", "shape": "hexagon",
            "desc": [
                "The &eMeka-Tool&r is the Atomic Disassembler grown up: a pick, axe, shovel, hoe, shears and sword in one, made better with modules.",
                "",
                "It needs Polonium Pellets, so it waits for a fission reactor. See the Reactors chapter.",
            ],
            "tasks": [{"item": "mekanism:meka_tool"}],
            "rewards": [{"xp": 25}, {"crate": "lantern"}],
        },
        {
            "key": "module_excavation", "title": "Excavation Escalation Unit", "optional": True,
            "desc": [
                "Makes the Meka-Tool dig faster. Install several to stack the effect.",
            ],
            "tasks": [{"item": "mekanism:module_excavation_escalation_unit"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "module_vein", "title": "Vein Mining Unit", "optional": True,
            "desc": [
                "Lets the Meka-Tool break a whole vein of ore, or a whole tree, at once.",
            ],
            "tasks": [{"item": "mekanism:module_vein_mining_unit"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "mekasuit", "title": "The MekaSuit", "shape": "hexagon", "wide": True,
            "desc": [
                "The &eMekaSuit&r is armor that runs on power. Each piece is made from its netherite counterpart with HDPE, Polonium and Ultimate Control Circuits.",
                "",
                "On its own it's tough. With modules it flies, breathes underwater, feeds you and keeps the radiation out.",
            ],
            "tasks": [{"item": "mekanism:mekasuit_helmet"}, {"item": "mekanism:mekasuit_bodyarmor"}, {"item": "mekanism:mekasuit_pants"}, {"item": "mekanism:mekasuit_boots"}],
            "rewards": [{"xp": 25}, {"crate": "ember"}],
        },
        {
            "key": "modules", "title": "The Modification Station",
            "desc": [
                "Modules go into the Meka-Tool and MekaSuit at a &eModification Station&r. Every module starts from a &eModule Base&r: HDPE, tin and bronze.",
                "",
                "Put the gear in, then the module. Most modules can be installed several times for a stronger effect.",
            ],
            "tasks": [{"item": "mekanism:modification_station"}, {"item": "mekanism:module_base"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "module_gravity", "title": "Gravitational Modulating Unit", "optional": True,
            "desc": [
                "Real flight, the creative kind, for the MekaSuit's chestplate. It drinks power while you fly.",
            ],
            "tasks": [{"item": "mekanism:module_gravitational_modulating_unit"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "module_jetpack", "title": "Jetpack Unit", "optional": True,
            "desc": [
                "A hydrogen jetpack built into the MekaSuit chestplate.",
            ],
            "tasks": [{"item": "mekanism:module_jetpack_unit"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "module_magnet", "title": "Magnetic Attraction Unit", "optional": True,
            "desc": [
                "Pulls nearby items straight to you.",
            ],
            "tasks": [{"item": "mekanism:module_magnetic_attraction_unit"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "module_elytra", "title": "Elytra Unit", "optional": True,
            "desc": [
                "Glide like you're wearing an elytra, without giving up the chestplate.",
            ],
            "tasks": [{"item": "mekanism:module_elytra_unit"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "teleporter", "title": "The Teleporter", "shape": "hexagon",
            "desc": [
                "A &eTeleporter&r sends you to any other Teleporter on the same frequency. Build it into a frame of &eTeleporter Frames&r and set a frequency in its screen.",
                "",
                "JEI shows the frame. It takes power for every trip, more for longer ones.",
            ],
            "tasks": [{"item": "mekanism:teleporter"}, {"item": "mekanism:teleporter_frame", "count": 9}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "robit", "title": "A Robot Friend",
            "desc": [
                "The &eRobit&r follows you around, picks up items, and has a crafting table, a furnace and an inventory of its own. It goes back to a Chargepad on its own when it runs low.",
                "",
                "It's also the brain of the Digital Miner.",
            ],
            "tasks": [{"item": "mekanism:robit"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "digital_miner", "title": "The Digital Miner",
            "desc": [
                "The &eDigital Miner&r mines whatever blocks you tell it to, in a radius around it, without you lifting a finger. Set filters for the ores you want and leave the stone in place.",
                "",
                "It's hungry for power, and it needs somewhere to put what it finds. A chest or a transporter on top will do.",
            ],
            "tasks": [{"item": "mekanism:digital_miner"}],
            "rewards": [{"xp": 25}, {"crate": "lantern"}],
        },
        {
            "key": "entangloporter", "title": "Quantum Entangloporter", "optional": True,
            "desc": [
                "The &eQuantum Entangloporter&r sends items, fluids, chemicals, heat and power to every other entangloporter on its frequency, even across dimensions.",
            ],
            "tasks": [{"item": "mekanism:quantum_entangloporter"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
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
    ],
}
