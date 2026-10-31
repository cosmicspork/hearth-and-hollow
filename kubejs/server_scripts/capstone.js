// The Allthemodium Alloy Paxel capstone. Allthemodium only makes its alloy ingots through Tinkers'
// casting, which isn't in the pack, and ships no recipe for the alloy tools or the paxel, so the
// whole chain is ours: alloy ingots in Powah's Energizing Orb, the four alloy tools on an Advanced
// table, and the paxel on an Elite table with one finished piece from each tech line.

ServerEvents.recipes(event => {
  const VA = 'allthemodium:vibranium_allthemodium_alloy_ingot'
  const UA = 'allthemodium:unobtainium_allthemodium_alloy_ingot'
  const UV = 'allthemodium:unobtainium_vibranium_alloy_ingot'
  const id = name => `hearthandhollow:capstone/${name}`

  // Two ingots of each metal and a Piglich Heart make two alloy ingots. The unobtainium alloys
  // cost more power.
  const alloy = (result, a, b, energy) => {
    event.custom({
      type: 'powah:energizing',
      ingredients: [
        { tag: `c:ingots/${a}` }, { tag: `c:ingots/${a}` },
        { tag: `c:ingots/${b}` }, { tag: `c:ingots/${b}` },
        { item: 'allthemodium:piglich_heart' }
      ],
      energy: energy,
      result: { id: result, count: 2 }
    }).id(id(result.split(':')[1]))
  }
  alloy(VA, 'vibranium', 'allthemodium', 2000000)
  alloy(UA, 'unobtainium', 'allthemodium', 5000000)
  alloy(UV, 'unobtainium', 'vibranium', 10000000)

  // Extended Crafting tiers: 2 is the Advanced table (5x5), 3 the Elite table (7x7).
  const table = (name, tier, result, pattern, key) => {
    event.custom({ type: 'extendedcrafting:shaped_table', tier: tier, pattern: pattern, key: key, result: { id: result } })
      .id(id(name))
  }
  const ingots = { V: { item: VA }, A: { item: UA }, U: { item: UV }, R: { tag: 'c:rods/unobtainium' } }

  // Each alloy tool upgrades its unobtainium counterpart.
  table('alloy_pick', 2, 'allthemodium:alloy_pick',
    ['VAUAV', '  T  ', '  R  ', '  R  ', '  R  '],
    Object.assign({ T: { item: 'allthemodium:unobtainium_pickaxe' } }, ingots))
  table('alloy_axe', 2, 'allthemodium:alloy_axe',
    [' VAU ', ' AT  ', '  R  ', '  R  ', '  R  '],
    Object.assign({ T: { item: 'allthemodium:unobtainium_axe' } }, ingots))
  table('alloy_shovel', 2, 'allthemodium:alloy_shovel',
    ['  U  ', ' VTA ', '  R  ', '  R  ', '  R  '],
    Object.assign({ T: { item: 'allthemodium:unobtainium_shovel' } }, ingots))
  table('alloy_sword', 2, 'allthemodium:alloy_sword',
    ['  U  ', '  A  ', '  T  ', ' VRV ', '  R  '],
    Object.assign({ T: { item: 'allthemodium:unobtainium_sword' } }, ingots))

  // The first paxel: the four alloy tools, a ring of alloy ingots, Supremium essence, and a
  // well-advanced piece of each tech line.
  table('alloy_paxel', 3, 'allthemodium:alloy_paxel',
    [
      'VAUIUAV',
      'A  P  A',
      'U M D U',
      'IX O HI',
      'U  W  U',
      'A  S  A',
      'VAUIUAV'
    ],
    {
      V: { item: VA }, A: { item: UA }, U: { item: UV },
      P: { item: 'allthemodium:alloy_pick' },
      X: { item: 'allthemodium:alloy_axe' },
      H: { item: 'allthemodium:alloy_shovel' },
      S: { item: 'allthemodium:alloy_sword' },
      I: { item: 'mysticalagriculture:supremium_essence' },
      M: { item: 'mekanism:elite_control_circuit' },
      D: { item: 'refinedstorage:16k_storage_disk' },
      O: { item: 'oritech:machine_core_5' },
      W: {
        type: 'neoforge:components',
        items: 'hostilenetworks:prediction',
        components: { 'hostilenetworks:data_model': 'hostilenetworks:wither' }
      }
    })

  // More paxels after the first: the one you put in stays in the grid, so you end up with two.
  // Alloy blocks rather than ingots, so a copy still costs real work. It's on a crafting table
  // because ingredient actions only work on KubeJS's own recipe types.
  event.shaped('allthemodium:alloy_paxel', ['VAU', 'APA', 'UAV'], {
    V: 'allthemodium:vibranium_allthemodium_alloy_block',
    A: 'allthemodium:unobtainium_allthemodium_alloy_block',
    U: 'allthemodium:unobtainium_vibranium_alloy_block',
    P: 'allthemodium:alloy_paxel'
  })
    .keepIngredient('allthemodium:alloy_paxel')
    .id(id('alloy_paxel_copy'))
})
