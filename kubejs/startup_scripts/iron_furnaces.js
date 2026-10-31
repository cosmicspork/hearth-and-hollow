// Iron Furnaces registers its Allthemodium, Vibranium and Unobtainium furnaces and upgrades, and
// its recipes for them load when Allthemodium is present, but it leaves them out of its creative
// tab. JEI builds its item list from the tabs, so without this they can't be found there either.

StartupEvents.modifyCreativeTab('ironfurnaces:ironfurnaces_tab', event => {
  for (const metal of ['allthemodium', 'vibranium', 'unobtainium']) {
    event.add(`ironfurnaces:${metal}_furnace`)
    event.add(`ironfurnaces:upgrade_${metal}`)
  }
})
