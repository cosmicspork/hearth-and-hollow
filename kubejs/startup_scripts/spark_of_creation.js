// The Spark of Creation: the Mekanism endgame's reward. It takes an antimatter pellet to make,
// and it's a catalyst for the creative recipes in server_scripts/creative.js: it stays in the
// grid, so one spark makes every creative item.
StartupEvents.registry('item', event => {
  event.create('hearthandhollow:spark_of_creation')
    .rarity('epic')
    .glow(true)
    .maxStackSize(16)
})
