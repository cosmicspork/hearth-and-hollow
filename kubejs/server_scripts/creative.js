// The Spark of Creation and the creative items it unlocks. The spark takes The Ultimate Ingot, which
// takes one of every singularity, plus an antimatter pellet and the best of Mekanism's alloys and
// circuits, all on the Ultimate Crafting Table. Each creative recipe then takes top-tier versions of
// the thing it makes infinite, and gives the spark back.

ServerEvents.recipes(event => {
  const SPARK = 'hearthandhollow:spark_of_creation'
  const id = name => `hearthandhollow:creative/${name}`
  // Extended Crafting tier 4 is the Ultimate table (9x9).
  const ultimate = (name, result, pattern, key) => {
    event.custom({ type: 'extendedcrafting:shaped_table', tier: 4, pattern: pattern, key: key, result: { id: result } })
      .id(id(name))
  }

  // Extended Crafting has no recipe that makes The Ultimate Ingot, only one that puts nine nuggets
  // back together, so this is ours.
  ultimate('the_ultimate_ingot', 'extendedcrafting:the_ultimate_ingot',
    ['B K B', ' KKK ', 'KKUKK', ' KKK ', 'B K B'],
    {
      U: { item: 'extendedcrafting:ultimate_singularity' },
      K: { tag: 'c:ingots/crystaltine' },
      B: { item: 'extendedcrafting:black_iron_block' }
    })

  ultimate('spark_of_creation', SPARK,
    [
      'N   C   N',
      ' A  K  A ',
      '  A P A  ',
      '   KKK   ',
      'CKKKIKKKC',
      '   KKK   ',
      '  A K A  ',
      ' A  K  A ',
      'N   C   N'
    ],
    {
      I: { item: 'extendedcrafting:the_ultimate_ingot' },
      P: { item: 'mekanism:pellet_antimatter' },
      K: { tag: 'c:ingots/crystaltine' },
      A: { item: 'mekanism:alloy_atomic' },
      C: { item: 'mekanism:ultimate_control_circuit' },
      N: { item: 'minecraft:nether_star' }
    })

  // Ingredient actions only work on KubeJS's own recipe types, so these are plain crafting.
  const creative = (name, result, outer, inner) => {
    event.shaped(result, ['OIO', 'ISI', 'OIO'], { O: outer, I: inner, S: SPARK })
      .keepIngredient(SPARK)
      .id(id(name))
  }

  // A crafted creative cube is empty unless it's made full, so the result carries the energy.
  creative('energy_cube',
    Item.of('mekanism:creative_energy_cube[mekanism:energy={energy_containers:[L;9223372036854775807L]}]'),
    'mekanism:ultimate_energy_cube', 'mekanism:ultimate_induction_cell')
  creative('chemical_tank', 'mekanism:creative_chemical_tank', 'mekanism:ultimate_chemical_tank', 'mekanism:alloy_atomic')
  creative('fluid_tank', 'mekanism:creative_fluid_tank', 'mekanism:ultimate_fluid_tank', 'mekanism:alloy_atomic')
  creative('bin', 'mekanism:creative_bin', 'mekanism:ultimate_bin', 'mekanism:alloy_atomic')
  creative('energy_cell', 'powah:energy_cell_creative', 'powah:energy_cell_nitro', 'powah:crystal_nitro')
  creative('controller', 'refinedstorage:creative_controller', 'refinedstorage:controller', 'mekanism:ultimate_induction_provider')
  creative('universal_grid', 'universalgrid:creative_wireless_universal_grid', 'universalgrid:wireless_universal_grid', 'mekanism:ultimate_induction_cell')
  creative('mining_battery', 'mininggadgets:upgrade_battery_creative', 'mininggadgets:upgrade_battery_3', 'mekanism:ultimate_induction_cell')

  // The creative jetpack upgrades an unobtainium one. Iron Jetpacks keeps the tier in a component,
  // so the ingredient matches on it and ignores the jetpack's charge. KubeJS's builder can't read
  // a components ingredient, so this one is written out as JSON.
  const jetpack = event.custom({
    type: 'kubejs:shaped',
    pattern: ['CIC', 'ISI', 'CJC'],
    key: {
      C: { item: 'mekanism:ultimate_induction_cell' },
      I: { item: 'mekanism:alloy_atomic' },
      S: { item: SPARK },
      J: { type: 'neoforge:components', items: 'ironjetpacks:jetpack', components: { 'ironjetpacks:jetpack_id': 'ironjetpacks:unobtainium' } }
    },
    result: { id: 'ironjetpacks:jetpack', components: { 'ironjetpacks:jetpack_id': 'ironjetpacks:creative' } }
  }).keepIngredient(SPARK).id(id('jetpack'))
  console.info(`creative jetpack recipe: ${jetpack.json}`)
})
