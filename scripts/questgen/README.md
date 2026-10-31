# Quest book source

The FTB Quests book in `config/ftbquests/quests` is generated. Its source is here: one Python file per chapter in `chapters/`, with crate tables and chapter groups in `content.py`. Edit these, never the SNBT, and never the book in game: the next regenerate overwrites both, and CI fails when the committed SNBT doesn't match this source.

All text is original. Don't copy from ATM10's or any other pack's quest files.

## Commands

```bash
just quests        # regenerate config/ftbquests from the chapters
just quest-check   # validate the chapters (needs the index)
just quest-index   # build the index from the dev instance; run `just sync` first
just quest-book    # the whole book as Markdown in run/quests.md, for proofreading
python3 scripts/questgen/preview.py wanderlust   # ASCII sketch of a chapter's layout
python3 scripts/questgen/render.py run/layouts wanderlust   # PNG of a chapter's layout
```

`check.py` looks every id up in `index/`, which `build_index.py` builds from the mod jars and the vanilla client jar. The index isn't committed; rebuild it after adding or updating mods. Look ids up there too: `grep -i 'name' index/items.tsv` (id, English name, jar), and `item_tags.txt`, `entities.tsv`, `structures.txt`, `structure_tags.txt`, `biomes.txt`, `biome_tags.txt`, `advancements.txt`, `dimensions.txt`.

Quest, task and reward ids are hashes of readable keys (`chapter_file:quest_key`), so regenerating keeps players' progress. Renaming a chapter's `file` or a quest's `key` resets that progress; change titles instead.

To research a mechanic, unzip the mod jar into a fresh directory under `run/inspect/` and read `data/<ns>/recipe/`, `assets/<ns>/lang/en_us.json` and the configs. Never run code from an extracted jar.

## Chapter format

```python
CHAPTER = {
    "file": "tools_of_the_trade",          # snbt filename, lowercase; part of every id
    "group": "settled",                    # settled | world | hum | long; leave out to sit above the groups
    "title": "Tools of the Trade",
    "subtitle": "One short line",
    "icon": "minecraft:iron_pickaxe",
    "layout": {...},                       # see Layout
    "links": [...],                        # optional, see Layout
    "quests": [ {...}, ... ],
}
```

Chapters are ordered by their `NN_` filename prefix. `chapters/01_welcome_home.py` is the reference for voice, structure and formatting.

Quest keys: `key` (unique, short), `title`, `desc` (list of lines; `""` is a blank line), `tasks`, `rewards`, and optionally `subtitle`, `shape` (circle default; `hexagon` for a chapter's milestones and finale, `gear` for an info-only quest), `size` (1.5 for the chapter's first quest and finale), `icon` (an item id, when the task's item isn't a good icon), `optional` (side quests a player may skip), `wide` (long lists), `repeat` (Bounty Board only).

Tasks (a list of dicts; most quests have one):

| Task | Form | Notes |
|---|---|---|
| Have an item | `{"item": "mod:id", "count": 4}` | Completes on its own. Best default. |
| Any item in a tag | `{"tag": "c:ingots/steel", "title": "...", "icon": "mod:id"}` | Use for metals and anything Almost Unified merges. |
| Any of several items | `{"any": ["mod:a", "mod:b"], "title": "...", "icon": "mod:a"}` | Variants: colors, tiers, wood types. |
| Kill | `{"kill": "minecraft:zombie", "count": 10}` | Exact entity id from `entities.tsv`. |
| Find a structure | `{"structure": "mod:id" or "#mod:tag", "title": "...", "icon": "..."}` | Completes when the player stands in it. |
| Visit a biome | `{"biome": "mod:id" or "#mod:tag", "title": "...", "icon": "..."}` | |
| Enter a dimension | `{"dimension": "allthemodium:mining", "title": "...", "icon": "..."}` | |
| Advancement | `{"advancement": "mod:path"}` | Only when no item task fits. |
| Statistic | `{"stat": "mod:stat", "value": 1, "title": "...", "icon": "..."}` | e.g. `waystones:waystone_activated`. |
| Read and click | `{"check": "Got it"}` | Info quests, and things the game can't detect. |

Prefer a task the game can detect over a checkmark. A checkmark quest with nothing before it in the layout gets no rewards and no icon: it reads as information. Purely informational quests further in also leave out the icon.

Item tasks take `"components": {...}` for a specific variant. FTB Quests compares each listed component whole, so `minecraft:custom_data` must match exactly: fine for an item a quest reward created (the Almanac pages), useless for items that carry extra data (a dropped trophy). Don't use observation or energy tasks; they don't work reliably here.

Rewards: `{"xp": 10}`, `{"xp_levels": 30}`, `{"crate": "kindling" | "hearth" | "lantern" | "ember", "count": 1}`, `{"item": "mod:id", "count": 4, "components": {...}}`, `{"book": "minecraft:mending", "level": 1}`, `{"command": "/tellraw ..."}` (`{p}` is the player's name).

## Layout

Lines between quests must never cross. Most chapters use one straight main line with short branches:

```python
"layout": {
    "spine": ["start", "a", "b", "c", "finale"],      # left to right; each depends on the previous
    "branches": {
        "a": {"up": ["a1", "a2"], "down": ["a3"]},     # columns above and below a spine quest
        "c": {"up": ["c1"]},
    },
},
```

- Every quest appears exactly once in the layout, and dependencies come only from it.
- The spine is the chapter's backbone: 6 to 14 quests, from an introduction to a finale. Branches are side topics, 1 to 3 quests long.
- `"direction": "down"` or `"up"` turns the whole spine.
- `{"lines": [...]}` stacks several tracks top to bottom, each centred and with no lines between them. Use it when a chapter covers things players do in parallel (Monsters & Mettle: World Tiers, the gear guide, challenges). Each line can be shorter than 6. A line is one of:
  - `{"spine": [...], "branches": {...}}`, as above.
  - `{"flow": [...], "branches": {...}}`: a spine where a stage can be a list of keys, stacked in one column. Each key in a list depends on the stage before, and the stage after depends on all of them, so the line fans out and back in: a wrench, then every pipe type, then the pipe that needs them all. Two lists of the same length in a row pair up instead, for parallel tracks.
  - `{"rows": [...], "per_row": 10}`: keys in centred, wrapped rows with no dependencies, for catalogs (backpack upgrades, seeds, trash cans).
- `{"grid": [[row keys], ...]}` lays out rows with no lines (the Bounty Board, Wanderlust, Curios & Keepsakes): for things the world hands out in no particular order. Make each row one theme.
- `"info": [keys]`, alongside any layout but `free`, sets explainer quests in a row above everything, with no dependencies. With nothing before them they follow the ungated checkmark rule below.
- `{"hub": True, ...}` puts `spine[0]` in the middle with straight spokes around it.
- `{"free": {key: (x, y)}, "deps": {key: [keys]}}` places quests by hand (the Alloy Paxel, the Almanac).

`"links": [{"quest": "chapter_file:key", "pos": (x, y)}]` shows a quest from another chapter here as well, at a position in the chapter's final coordinates, with no lines. Wanderlust uses them to point at Monsters & Mettle.

Every chapter is open from the start (flexible progression): a player can finish a quest's tasks at any time, but can't claim its rewards until the quests before it are done. So a dependency is a real gate on rewards. Use one only where the order is real (a tier needs the tier before it, a machine needs its parts) and put everything else in `rows` or a grid. Collections never chain: the third fishing spot doesn't wait on the first two.

Keep each chapter balanced: lines centred, branches about as long above as below, and no line much wider than the rest. Render the chapter and look at it before calling it done. A chapter taller than about 25 units is probably two chapters.

## Voice

Short, warm and practical. Each quest says what the thing is, why you'd want it, and one useful tip. Two to five short paragraphs, usually under 80 words. Talk to the player as "you". A light touch of humor is welcome; whimsy isn't.

- Lead with what matters to the player, not with the mod's name.
- Name items as the game does, and highlight key items, blocks and keys with `&e...&r`. Use other colors sparingly: `&c` for hearts or danger, `&a` for success, `&9` for links.
- No em dashes or en dashes, anywhere. Use a colon, a comma, or a new sentence.
- Don't promise numbers or behavior you haven't checked in the jar, the config or the recipe. If you can't verify a detail, leave it out or keep it general.
- Write `&` as plain `&` in text; the generator escapes it.
- No magic: the pack has no magic mods. Don't mention mods that aren't in it.

## Rewards and pacing

- Every quest: `{"xp": 10}` plus a crate. Milestones `{"xp": 25}`, finales `{"xp": 50}`.
- Crates by stage: **Kindling** for early and easy quests; **Hearth** for mid-game quests; **Lantern** for a chapter's milestones (2 to 4 per chapter); **Ember** for a chapter finale in the mid and late game.
- Milestone and finale quests can also give something from the chapter's own mod. Rewards help without skipping a mod's progression: never give the thing the next quest asks for.
- Settled-stage chapters (Tools of the Trade, Hearth & Table, The Builder's Bench) stay in Kindling and Hearth, with Lantern for milestones and the finale.

## Pack facts you can rely on

- Keybinds: `` ` `` Ultimine, `B` backpack, `M` FTB Chunks claim map, `J` JourneyMap, `Shift+B` waypoint, `Shift+G` Curios, `Shift+E` Crafting on a Stick and the Universal Grid, `Ctrl+M` Simple Magnets toggle, `R`/`U` JEI recipes/uses, `Shift+V` Supplementaries quiver, `Ctrl+V` Easy Villagers pick up, `Shift+U` Hostile Networks deep learner, `Ctrl+G` Oritech augments, `Ctrl+H` Mekanism HUD, `Shift+H` Building Gadgets anchor, `Ctrl+C` Modular Routers configure. `H` is the jetpack hover; never bind anything else to it.
- Ores: AllTheOres is the only ore source. Mekanism, Oritech (nickel, platinum) and XyCraft (aluminum) ores are off, and AllTheOres' cinnabar, iridium, peridot, ruby and sapphire don't generate. Almost Unified merges metals to AllTheOres items, so ask for ingots and dusts by `c:` tag (for example `c:ingots/osmium`).
- Oritech resource nodes use AllTheOres blocks.
- Waystones are free to use and common in villages. Explorer's and Nature's Compass can't teleport. Flux Networks can't chunk-load (FTB Chunks force-loading does that).
- Spice of Life: milestones at 25, 50, 75, 100, 150, 200, 250, 300, 400, 500 unique foods, 3 hearts each; only foods worth 4 or more drumsticks count; hearts are kept on death.
- Mystical Agriculture: grass doesn't drop inferium or seeds; essence drops from mobs are off for Wither and dragon. Mystical Customization adds Allthemodium, Vibranium and Unobtainium Seeds (`config/mysticalcustomization/crops`): Insanium tier, made from ingots, and each needs a block of its own metal as its crux. Eight essence craft one ingot.
- The mining dimension also has Powah uraninite, Mystical Agriculture inferium, prosperity and soulstone (with the Agradditions Nether and End ores in its netherrack and end stone layers), XyCraft xychorium, and AllTheOres sulfur and fluorite.
- Refined Storage 2 (not AE2) is the storage network.
- Crates also drop in the world: a mob killed by a player sometimes drops a Kindling crate, and bosses always drop a Lantern or Ember crate. These are global loot modifiers in `kubejs/data/hearthandhollow`; FTB Quests' own `drop_loot_crates` stays off because it counts every dying mob as a boss.
- The Spark of Creation (`hearthandhollow:spark_of_creation`, registered in `kubejs/startup_scripts`) ends the Mekanism Reactors chapter. It's a catalyst: `kubejs/server_scripts/creative.js` uses it, unconsumed, to craft creative items. `check.py` reads item ids registered in `kubejs/startup_scripts`, since they aren't in any mod jar.
- There are two capstones. The Alloy Paxel (chapter 17) takes one finished piece from each tech chapter: an ultimate control circuit (`mekanism:ultimate_control_circuit`), an Ultimate Machine Core (`oritech:machine_core_7`), a 64K disk (`refinedstorage:64k_storage_disk`), Insanium essence (`mysticalagradditions:insanium_essence`) and a Wither prediction; chapter finales don't give these as rewards. The Almanac (chapter 19) is the non-tech one: each of its four pages ends by giving an Almanac Page, and the capstone asks for all four.
