WOODS = ["oak", "spruce", "birch", "jungle", "acacia", "dark_oak", "mangrove", "cherry", "crimson", "warped", "bamboo"]
WOODS8 = WOODS[:8]  # the overworld trees, for blocks that skip the nether woods and bamboo
WOODS10 = WOODS[:10]
# Gaps in the variant grids below: these combinations don't exist in the mods.
MISSING = {"mcwdoors:dark_oak_four_panel_door", "mcwtrpdoors:bamboo_ranch_trapdoor",
           "mcwtrpdoors:crimson_barred_trapdoor", "mcwtrpdoors:dark_oak_four_panel_trapdoor",
           "mcwpaths:mossy_stone_basket_weave_paving", "mcwpaths:mossy_stone_honeycomb_paving",
           "mcwpaths:mossy_stone_square_paving", "mcwpaths:stone_basket_weave_paving",
           "mcwpaths:stone_honeycomb_paving", "mcwpaths:stone_square_paving"}


def have(ids):
    return [i for i in ids if i not in MISSING]


ROOFS = ([f"mcwroofs:{w}_roof" for w in WOODS] + [f"mcwroofs:{w}_planks_roof" for w in WOODS]
         + [f"mcwroofs:{s}_roof" for s in ["cobblestone", "stone_bricks", "bricks", "stone", "deepslate", "andesite",
                                            "granite", "diorite", "blackstone", "sandstone", "thatch", "mud_brick"]])
WINDOWS = ([f"mcwwindows:{w}_window" for w in WOODS8] + [f"mcwwindows:{w}_plank_window" for w in WOODS8]
           + [f"mcwwindows:{w}_pane_window" for w in WOODS10]
           + [f"mcwwindows:{s}_window" for s in ["metal", "andesite", "bricks", "deepslate", "diorite", "granite",
                                                  "blackstone", "quartz"]])
DOORS = have([f"mcwdoors:{w}_{s}_door" for w in WOODS for s in ["barn", "glass", "barn_glass", "four_panel", "stable",
                                                            "western", "japanese"]])
TRAPDOORS = have([f"mcwtrpdoors:{w}_{s}_trapdoor" for w in WOODS for s in ["barn", "barred", "barrel", "glass",
                                                                       "four_panel", "ranch", "bark"]])
FENCES = ([f"mcwfences:{w}_{s}" for w in WOODS10 for s in ["picket_fence", "stockade_fence", "horse_fence",
                                                           "wired_fence"]]
          + [f"mcwfences:{w}_hedge" for w in WOODS8]
          + [f"mcwfences:modern_{s}_wall" for s in ["stone_brick", "andesite", "diorite", "granite", "sandstone"]])
BRIDGES = ([f"mcwbridges:rope_{w}_bridge" for w in WOODS10] + [f"mcwbridges:{w}_rail_bridge" for w in WOODS10]
           + [f"mcwbridges:{s}_bridge" for s in ["cobblestone", "stone_brick", "brick", "andesite", "granite",
                                                  "diorite", "sandstone", "iron", "glass", "bamboo"]])
BALCONIES = ([f"mcwstairs:{w}_{s}" for w in WOODS10 for s in ["balcony", "railing", "platform"]]
             + [f"mcwstairs:{s}_{t}" for s in ["cobblestone", "stone_brick", "brick", "andesite", "sandstone"]
                for t in ["balcony", "railing"]])
CURTAINS = [f"mcwwindows:{c}_curtain" for c in ["white", "orange", "magenta", "light_blue", "yellow", "lime", "pink",
                                               "gray", "light_gray", "cyan", "purple", "blue", "brown", "green",
                                               "red", "black"]]
PATHS = have([f"mcwpaths:{w}_planks_path" for w in WOODS]
         + [f"mcwpaths:{s}_{t}" for s in ["stone", "andesite", "granite", "diorite", "brick", "sandstone",
                                          "cobbled_deepslate", "mossy_stone", "blackstone"]
            for t in ["flagstone_path", "running_bond_path", "windmill_weave_path", "strewn_rocky_path",
                      "crystal_floor_path", "honeycomb_paving", "basket_weave_paving", "square_paving"]])
LIGHTS = ([f"mcwlights:{w}_tiki_torch" for w in WOODS]
          + [f"mcwlights:{s}" for s in ["chain_lantern", "bell_lantern", "cross_lantern", "festive_lantern",
                                        "striped_lantern", "tavern_lantern", "covered_lantern", "wall_lantern",
                                        "classic_street_lamp", "double_street_lamp", "garden_light", "lava_lamp",
                                        "iron_chandelier", "golden_chandelier", "copper_chandelier",
                                        "iron_candle_holder", "rustic_torch", "white_lamp", "white_paper_lamp"]])
FURNITURE = [f"mcwfurnitures:{w}_{s}" for w in WOODS10 for s in ["chair", "table", "drawer", "wardrobe", "desk",
                                                                 "coffee_table", "kitchen_cabinet", "bookshelf"]]
HOLIDAYS = ([f"mcwholidays:{c}_oak_leaves" for c in ["red", "orange", "yellow", "brown", "mixed", "snowy"]]
            + [f"mcwholidays:{s}" for s in ["carved_friendly_pumpkin", "carved_smile_pumpkin", "small_pumpkin",
                                            "pair_of_pumpkins", "scarecrow", "pumpkin_wheelbarrow", "snowman",
                                            "garland", "wavy_garland", "colorful_string_lights", "wreath_wall_deco_1",
                                            "icicle", "wooden_sled", "christmas_tree_base"]])
CLUTTER = [f"cluttered:{s}" for s in ["teddy_bear", "stack_of_books", "small_glass_jars", "picnic_basket",
                                      "glass_vase_of_flowers", "two_flower_pots", "cottage_chair", "small_bookcase",
                                      "wine_bottle_rack", "starry_wallpaper", "mint_wallpaper", "pancake_stack",
                                      "sewing_machine_antique", "traditional_radio"]]
ODDS = [f"supplementaries:{s}" for s in ["jar", "flower_box", "item_shelf", "notice_board", "globe", "planter",
                                         "pedestal", "sack", "doormat", "candle_holder", "hat_stand", "clock_block",
                                         "wind_vane"]]
TIMBER = [f"supplementaries:{s}" for s in ["timber_frame", "timber_brace", "timber_cross_brace", "daub",
                                           "daub_frame", "daub_brace", "daub_cross_brace"]]
COPPER = [f"everythingcopper:{s}" for s in ["copper_lantern", "copper_soul_lantern", "copper_chain", "copper_bars",
                                            "copper_ladder", "copper_door", "copper_trapdoor", "copper_lamp",
                                            "copper_rail", "copper_button", "copper_pressure_plate"]]

CHAPTER = {
    "file": "builders_bench",
    "group": "settled",
    "title": "The Builder's Bench",
    "subtitle": "Roofs, chairs, lamps and a gadget that builds walls",
    "icon": "handcrafted:oak_chair",
    "layout": {
        "hub": True,
        "spine": ["bench", "chairs", "framed", "roofs", "windows", "doors", "odds", "lights", "paths", "gadget",
                  "copypaste", "home"],
        "branches": {
            "bench": {"up": ["chisel"], "down": ["twigs"]},
            "chairs": {"up": ["fancy_bed"], "down": ["mcw_furniture", "clutter"]},
            "framed": {"up": ["framing_saw"]},
            "roofs": {"up": ["balconies"]},
            "windows": {"up": ["curtains"], "down": ["trapdoors"]},
            "doors": {"up": ["fences"], "down": ["bridges"]},
            "odds": {"up": ["timber"], "down": ["amendments"]},
            "lights": {"up": ["luminax"], "down": ["copper"]},
            "paths": {"up": ["holidays"]},
            "gadget": {"up": ["exchanger"], "down": ["destruction"]},
            "copypaste": {"up": ["template"], "down": ["cut_paste"]},
        },
    },
    # The Charging Station lives in Sparks; it shows here too, by the gadgets that need it.
    "links": [{"quest": "sparks:charging_station", "pos": (-7.2, 2.2)}],
    "quests": [
        {
            "key": "bench", "title": "The Builder's Bench",
            "shape": "hexagon", "size": 1.5,
            "desc": [
                "Four walls keep the rain off. This chapter is about making them feel like home, and it all starts at a &ecrafting table&r.",
                "",
                "Each quest shows you one family of blocks from the pack's building mods and hands you a few to try. Do them in any order, or skip the ones that don't suit your style.",
                "",
                "Most of these blocks are made from everyday materials. Hover over one and press &eR&r to see how. Many also have a second trick when you right-click them, so poke at everything.",
            ],
            "tasks": [{"item": "minecraft:crafting_table"}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}, {"item": "minecraft:scaffolding", "count": 16}],
        },
        {
            "key": "chisel", "title": "A Chisel for Everything",
            "desc": [
                "The &eChisel&r turns plain blocks into fancier versions of themselves: stone into tiles, planks into panels, bricks into patterns.",
                "",
                "Use it to open its menu, drop in a stack, and pick the look you want. &eChisel all&r converts the whole stack at once.",
                "",
                "Many variants have connected textures that join up across a wall. Turn that on or off in the same menu.",
            ],
            "tasks": [{"item": "rechiseled:chisel"}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}, {"item": "minecraft:stone_bricks", "count": 32}],
        },
        {
            "key": "twigs", "title": "Bits on the Ground",
            "desc": [
                "Look down as you walk. &eTwigs&r lie about in forests and taiga, and &ePebbles&r on plains, beaches and riverbanks. Pick them up.",
                "",
                "A twig crafts into two sticks, and four pebbles make a cobblestone, so they're handy on your first day. Pebbles can be thrown, too.",
                "",
                "Twigs also adds small tables made from a fence and a slab, paper lanterns, seashells on the beach, and a few new kinds of stone underground.",
            ],
            "tasks": [{"item": "twigs:twig"}, {"item": "twigs:pebble"}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}, {"item": "twigs:paper_lantern", "count": 4}],
        },
        {
            "key": "chairs", "title": "Pull Up a Chair",
            "desc": [
                "Handcrafted makes proper furniture: chairs, couches, benches, tables, desks, shelves and cupboards, in every kind of wood.",
                "",
                "Right-click a chair or couch to sit down.",
                "",
                "Dress things up with fabric. Right-click a chair with a &eCushion&r, or a table with a &eSheet&r, to give it a seat pad or a tablecloth in that color.",
            ],
            "tasks": [
                {"tag": "handcrafted:chairs", "title": "Any Handcrafted chair", "icon": "handcrafted:oak_chair"},
                {"tag": "handcrafted:tables", "title": "Any Handcrafted table", "icon": "handcrafted:oak_table"},
            ],
            "rewards": [{"xp": 10}, {"crate": "kindling"}, {"item": "handcrafted:red_cushion", "count": 2},
                        {"item": "handcrafted:white_sheet", "count": 2}],
        },
        {
            "key": "fancy_bed", "title": "Sweet Dreams",
            "desc": [
                "A &eFancy Bed&r has a proper wooden frame and works just like any other bed.",
                "",
                "Right-click it with a &eSheet&r to change the bedding, or with a &eCushion&r to change the pillow. Put a nightstand next to it and a lamp on top, and you've got a bedroom.",
            ],
            "tasks": [{"tag": "handcrafted:fancy_beds", "title": "Any fancy bed", "icon": "handcrafted:oak_fancy_bed"}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}, {"item": "handcrafted:oak_nightstand"}],
        },
        {
            "key": "mcw_furniture", "title": "A Second Opinion on Furniture",
            "desc": [
                "Macaw's Furniture is another full set: chairs, tables, desks, kitchen cabinets, bookshelves, drawers and wardrobes.",
                "",
                "Chairs seat you, and many of the cabinets and drawers open up to store things, so a kitchen can hold your food as well as look the part.",
                "",
                "Mix it freely with Handcrafted. Nobody's checking.",
            ],
            "tasks": [{"any": FURNITURE, "title": "Any Macaw's chair, table, desk, drawer or wardrobe",
                       "icon": "mcwfurnitures:oak_chair"}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}, {"item": "mcwfurnitures:oak_drawer", "count": 2}],
        },
        {
            "key": "clutter", "title": "A Little Clutter", "optional": True,
            "desc": [
                "Real homes are full of small things. Cluttered has hundreds of them: stacks of books, teddy bears, vases of flowers, sewing machines, radios, picnic baskets and patterned wallpaper.",
                "",
                "Most are simple crafts. A stack of books is three books, a teddy bear is brown wool. Press &eU&r on an everyday item to see what it makes.",
            ],
            "tasks": [{"any": CLUTTER, "title": "Any of these knick-knacks", "icon": "cluttered:teddy_bear"}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}, {"item": "cluttered:starry_wallpaper", "count": 8}],
        },
        {
            "key": "framed", "title": "Wear Any Face",
            "desc": [
                "A &eFramed Cube&r is an empty frame that can look like any other block. Right-click it with a block in hand and it takes on that block's look.",
                "",
                "There are framed slopes, stairs, slabs, panels, doors and dozens more, so you can make shapes no ordinary block comes in, in any material you like.",
                "",
                "Right-click a framed block with &eGlowstone Dust&r to make it glow. A &eFramed Hammer&r takes the look back off.",
            ],
            "tasks": [{"item": "framedblocks:framed_cube", "count": 4}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}, {"item": "framedblocks:framed_slope", "count": 4},
                        {"item": "framedblocks:framed_stairs", "count": 4}],
        },
        {
            "key": "framing_saw", "title": "The Framing Saw",
            "desc": [
                "Crafting every framed shape by hand gets old. The &eFraming Saw&r turns Framed Cubes into any other framed block.",
                "",
                "Put cubes in, pick a shape from the list, take it out. If you're short of material, it tells you what's missing.",
            ],
            "tasks": [{"item": "framedblocks:framing_saw"}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}, {"item": "framedblocks:framed_cube", "count": 16}],
        },
        {
            "key": "roofs", "title": "A Proper Roof", "shape": "hexagon",
            "desc": [
                "Stairs make a fine roof. Macaw's Roofs makes a better one: steep pitches, low pitches, attic pieces and top caps in wood, stone, brick, concrete, terracotta and thatch.",
                "",
                "Try a steep roof on a narrow cottage and a low one on a wide barn, and finish the peak with a top piece so it doesn't look chopped off.",
            ],
            "tasks": [{"any": ROOFS, "title": "Any Macaw's roof", "icon": "mcwroofs:oak_roof"}],
            "rewards": [{"xp": 25}, {"crate": "lantern"}, {"item": "mcwroofs:thatch_roof", "count": 16}],
        },
        {
            "key": "balconies", "title": "Up and Out",
            "desc": [
                "Macaw's Stairs adds new stair styles, railings, platforms and balconies.",
                "",
                "A &eBalcony&r can be placed up to four times on the same block. A &eRailing&r goes along the side of a stair. Hit either with &eShears&r to change its style.",
            ],
            "tasks": [{"any": BALCONIES, "title": "Any balcony, railing or platform", "icon": "mcwstairs:oak_balcony"}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}, {"item": "mcwstairs:oak_railing", "count": 8}],
        },
        {
            "key": "windows", "title": "Let the Light In",
            "desc": [
                "Glass panes are fine. Macaw's Windows has framed windows in every wood and stone, and many of them open with a right-click.",
                "",
                "Stack windows together and they join into one bigger window. A &eWindow Hammer&r changes a window's shape, and a &eWindow Key&r locks it.",
                "",
                "Shutters, blinds and parapets come in the same woods.",
            ],
            "tasks": [{"any": WINDOWS, "title": "Any Macaw's window", "icon": "mcwwindows:oak_window"}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}, {"item": "mcwwindows:hammer"},
                        {"item": "mcwwindows:oak_shutter", "count": 4}],
        },
        {
            "key": "curtains", "title": "Draw the Curtains",
            "desc": [
                "Every window deserves curtains. Macaw's Windows has them in all sixteen colors, plus curtain rods to hang them from.",
                "",
                "Right-click a curtain to tie it back to one side.",
            ],
            "tasks": [{"any": CURTAINS, "title": "Curtains, any color", "icon": "mcwwindows:red_curtain"}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}, {"item": "mcwwindows:oak_curtain_rod", "count": 4}],
        },
        {
            "key": "trapdoors", "title": "Hatches and Shutters",
            "desc": [
                "Macaw's Trapdoors comes in the same styles as its doors: barn, ranch, barred, glass and more, in every wood.",
                "",
                "They make good shutters on a wall, cupboard doors on a shelf, or a cellar hatch in the floor.",
            ],
            "tasks": [{"any": TRAPDOORS, "title": "Any Macaw's trapdoor", "icon": "mcwtrpdoors:oak_barn_trapdoor"}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}, {"item": "mcwtrpdoors:oak_cottage_trapdoor", "count": 4}],
        },
        {
            "key": "doors", "title": "Come On In",
            "desc": [
                "A front door says a lot about a house. Macaw's Doors has barn doors, stable doors, glass doors, paper doors, western doors and plenty more.",
                "",
                "Metal doors need redstone power to open, like vanilla iron ones. A &eGarage Door&r goes on the ceiling and rolls down when opened.",
            ],
            "tasks": [{"any": DOORS, "title": "Any Macaw's door", "icon": "mcwdoors:oak_barn_door"}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}, {"item": "mcwdoors:oak_cottage_door", "count": 2}],
        },
        {
            "key": "fences", "title": "Good Fences",
            "desc": [
                "Macaw's Fences and Walls has picket fences, stockade walls, horse fences, wrought-iron railings, hedges and modern stone walls.",
                "",
                "Some of them stack upward into a taller wall, and the tooltip says which. Wired fences hurt anything that pushes through them, so keep them away from the path.",
                "",
                "Fences in this pack also join up corner to corner, so a fence can run diagonally.",
            ],
            "tasks": [{"any": FENCES, "title": "Any Macaw's fence, hedge or wall", "icon": "mcwfences:oak_picket_fence"}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}, {"item": "mcwfences:oak_picket_fence", "count": 16}],
        },
        {
            "key": "bridges", "title": "Across the River",
            "desc": [
                "Macaw's Bridges builds bridges in rope, wood, stone and iron. Lay the pieces in a line and they connect on their own.",
                "",
                "Use &ePliers&r on a bridge two or more blocks wide to open a gap in the railing for a side entrance. Bridge lanterns and torches sit on the handrails.",
            ],
            "tasks": [{"any": BRIDGES, "title": "Any Macaw's bridge", "icon": "mcwbridges:rope_oak_bridge"}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}, {"item": "mcwbridges:rope_oak_bridge", "count": 16},
                        {"item": "mcwbridges:pliers"}],
        },
        {
            "key": "odds", "title": "Odds and Ends",
            "desc": [
                "Supplementaries is a box of useful oddments. A few to start with:",
                "",
                "A &eJar&r holds bottles, buckets, cookies or even a small mob. An &eItem Shelf&r shows off one item on a wall. A &eFlower Box&r holds any big plant under a window. A &eGlobe&r spins when you hit it.",
                "",
                "There are notice boards, hat stands, sacks, doormats and a lot more. Browse the mod in JEI.",
            ],
            "tasks": [{"any": ODDS, "title": "Any of these", "icon": "supplementaries:jar"}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}, {"item": "supplementaries:flower_box", "count": 2},
                        {"item": "supplementaries:item_shelf", "count": 4}],
        },
        {
            "key": "timber", "title": "Half-Timbered",
            "desc": [
                "A &eTimber Frame&r is a wooden frame that holds any full block. Right-click one with a block and it fills in behind the beams.",
                "",
                "Braces and cross braces give you the diagonal beams, and &eDaub&r is the plaster to fill them with. That's a cottage wall in two blocks.",
            ],
            "tasks": [{"any": TIMBER, "title": "Any timber frame or daub", "icon": "supplementaries:timber_frame"}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}, {"item": "supplementaries:timber_frame", "count": 8},
                        {"item": "supplementaries:daub", "count": 8}],
        },
        {
            "key": "amendments", "title": "Small Touches", "shape": "gear", "wide": True,
            "desc": [
                "Amendments lets ordinary blocks go where they couldn't before:",
                "",
                "Lanterns hang on walls",
                "Carpet lies on stairs and slabs",
                "Flower pots hang from the ceiling",
                "Banners hang from the ceiling, too",
                "Tools hang on tripwire hooks",
                "Items sit on hanging signs",
                "Cakes stack, and can be eaten from any side",
                "",
                "No new blocks to learn. Just try it.",
            ],
            "tasks": [{"check": "Got it"}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}],
        },
        {
            "key": "lights", "title": "Lamps and Lanterns", "shape": "hexagon",
            "desc": [
                "Torches keep monsters away. Macaw's Lights does it with style: chandeliers, street lamps, candle holders, paper lamps, garden lights and a dozen kinds of lantern.",
                "",
                "Tiki torches stack: put one on top of another for a taller one. Some lamps take a dye to change color, and the tooltip tells you which.",
            ],
            "tasks": [{"any": LIGHTS, "title": "Any Macaw's light", "icon": "mcwlights:chain_lantern"}],
            "rewards": [{"xp": 25}, {"crate": "lantern"}, {"item": "mcwlights:oak_tiki_torch", "count": 4},
                        {"item": "mcwlights:chain_lantern", "count": 4}],
        },
        {
            "key": "luminax", "title": "Glow in Color",
            "desc": [
                "&eLuminax&r blocks are colored stone that gives off light, made from stone, a dye and glowstone dust.",
                "",
                "They come as blocks, stairs, slabs, walls, buttons and pressure plates in all sixteen colors, so a floor or a ceiling can be the light. Dim versions are made with wool instead of glowstone.",
            ],
            "tasks": [{"tag": "luminax:blocks", "title": "Any Luminax block", "icon": "luminax:light_blue_luminax_block"}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}, {"item": "luminax:yellow_luminax_block", "count": 8}],
        },
        {
            "key": "copper", "title": "Everything Copper",
            "desc": [
                "All that copper from the mines has somewhere to go: copper lanterns, chains, bars, ladders, doors, trapdoors, rails, even copper tools and armor.",
                "",
                "Like copper blocks, they turn green with age. Wax them with a &eHoneycomb&r to keep the color you like.",
            ],
            "tasks": [{"any": COPPER, "title": "Anything copper from Everything Copper",
                       "icon": "everythingcopper:copper_lantern"}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}, {"item": "everythingcopper:copper_lantern", "count": 4}],
        },
        {
            "key": "paths", "title": "The Garden Path",
            "desc": [
                "The ground around a house matters as much as the house. Macaw's Paths and Pavings has flagstones, cobbled paths, running bond brick, basket weave and more, in most kinds of stone and wood.",
                "",
                "Some pavings change when you right-click them: a pickaxe engraves them and a shovel flattens them. The tooltip says which.",
            ],
            "tasks": [{"any": PATHS, "title": "Any Macaw's path or paving", "icon": "mcwpaths:stone_flagstone_path"}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}, {"item": "mcwpaths:stone_flagstone_path", "count": 32}],
        },
        {
            "key": "holidays", "title": "For the Season", "optional": True,
            "desc": [
                "Macaw's Holidays has decorations for autumn and winter: carved pumpkins, scarecrows, autumn leaves in red, orange and yellow, snowmen, garlands, wreaths and string lights.",
                "",
                "Some pieces have more than one look. Right-click them to switch, and check the tooltip.",
            ],
            "tasks": [{"any": HOLIDAYS, "title": "Any of these decorations", "icon": "mcwholidays:carved_smile_pumpkin"}],
            "rewards": [{"xp": 10}, {"crate": "kindling"}, {"item": "mcwholidays:red_oak_leaves", "count": 16},
                        {"item": "mcwholidays:orange_oak_leaves", "count": 16}],
        },
        {
            "key": "gadget", "title": "A Wall in One Click", "shape": "hexagon",
            "desc": [
                "The &eBuilding Gadget&r places whole rows, columns and walls of blocks at once.",
                "",
                "Shift-right-click a block to choose what to build with, then right-click to place. You'll see a ghost of what's coming first. Hold &eG&r to open its menu, where you pick the mode and the size. &eShift+H&r anchors the preview so you can look around.",
                "",
                "The blocks come out of your inventory, and the gadget runs on FE, so charge it before you start.",
            ],
            "tasks": [{"item": "buildinggadgets2:gadget_building"}],
            "rewards": [{"xp": 25}, {"crate": "lantern"}, {"item": "minecraft:coal_block", "count": 8}],
        },
        {
            "key": "exchanger", "title": "Swap It Out",
            "desc": [
                "The &eExchanging Gadget&r replaces blocks that are already there. Shift-right-click the block you want, then right-click a wall or floor to swap a whole area for it.",
                "",
                "You get the old blocks back. Put Silk Touch on the gadget if you want grass back as grass rather than dirt.",
            ],
            "tasks": [{"item": "buildinggadgets2:gadget_exchanging"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "destruction", "title": "Clear the Site",
            "desc": [
                "The &eDestruction Gadget&r clears a whole box of blocks in front of you: a hillside in the way, a wall you changed your mind about, the dirt hut from your first night.",
                "",
                "Hold &eG&r to set how wide, tall and deep it digs. The preview shows exactly what goes before you commit.",
                "",
                "If you clear the wrong thing, &eUndo&r in its menu puts it back.",
            ],
            "tasks": [{"item": "buildinggadgets2:gadget_destruction"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "copypaste", "title": "Copy That",
            "desc": [
                "Built something you like? The &eCopy Paste Gadget&r builds it again.",
                "",
                "In copy mode, right-click one corner of your build and shift-right-click the opposite corner. A green box shows what's copied. Switch to paste mode, look where you want it, and right-click.",
                "",
                "It uses blocks from your inventory. The &eMaterial List&r in its menu shows what you need and what you're short of.",
            ],
            "tasks": [{"item": "buildinggadgets2:gadget_copy_paste"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}, {"item": "minecraft:coal_block", "count": 8}],
        },
        {
            "key": "template", "title": "Blueprints", "optional": True,
            "desc": [
                "The &eTemplate Manager&r saves a copied build onto paper, so you can keep a library of designs and load one back onto the gadget later.",
                "",
                "It can also copy a design to your clipboard as text, to share with friends in another world. They paste it in, and it's theirs.",
            ],
            "tasks": [{"item": "buildinggadgets2:template_manager"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}, {"item": "minecraft:paper", "count": 16}],
        },
        {
            "key": "cut_paste", "title": "Moving House", "optional": True,
            "desc": [
                "The &eCut Paste Gadget&r picks a build up and puts it down somewhere else, chests and their contents included. No blocks needed.",
                "",
                "Mark the corners as you would with the Copy Paste Gadget, press &eCut&r in its menu, then paste.",
                "",
                "&cIt has no undo&r, and it only holds one build at a time. Check where you're pasting before you click.",
            ],
            "tasks": [{"item": "buildinggadgets2:gadget_cut_paste"}],
            "rewards": [{"xp": 10}, {"crate": "hearth"}],
        },
        {
            "key": "home", "title": "A Place of Your Own", "shape": "hexagon", "size": 1.5,
            "icon": "handcrafted:oak_fancy_bed",
            "desc": [
                "A roof with a ridge, windows with curtains, a chair by the fire and a path to the door. That's not a shelter any more, that's a home.",
                "",
                "There's always one more thing to add. Have fun with it.",
            ],
            "tasks": [{"check": "Home sweet home"}],
            "rewards": [{"xp": 50}, {"crate": "lantern"}],
        },
    ],
}
