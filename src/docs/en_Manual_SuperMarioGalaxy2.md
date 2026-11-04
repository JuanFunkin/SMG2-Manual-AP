# Super Mario Galaxy 2 (Manual, send-only)

## Where is the options page?

The [player options page for this game](../player-options) contains all the options you need to configure and export a config file.

## What does randomization do to this game?

Nothing changes inside the game. This is a **send-only** Manual: you play Super Mario Galaxy 2 exactly as normal
and every check you complete sends an item to another player in the multiworld.
**You never receive real items**, so no part of Galaxy 2 is ever locked behind the multiworld.
(Your slot only ever receives "Nothing" filler, which is required by Archipelago to keep the item pool balanced.)

## What is a check?

| Group | Description | Default |
|---|---|---|
| Galaxy Unlocks | Each time a new galaxy becomes available on the map (Sky Station Galaxy is open from the start, so it has no check). | On |
| Power Stars | Every regular mission star of every galaxy, listed in the same order as the Super Mario Wiki. | Always |
| Prankster Comet Stars | Stars that only appear while a Prankster Comet orbits the galaxy. | On |
| Mailtoad Letter Stars | Stars that only appear after the Mailtoad delivers a letter. | On |
| Green Stars | The 120 Green Stars (each galaxy has as many as it has Power Stars). | Off |
| Grandmaster Galaxy | Unlock + The Ultimate Test + The Perfect Run. | Off |

## What is the goal?

Pick one with the `goal` option:

1. `defeat bowser` - beat Bowser in Bowser's Galaxy Generator (story ending)
2. `collect 120 power stars`
3. `collect 120 power and 120 green stars`
4. `clear grandmaster galaxy` - finish both missions of the Grandmaster Galaxy

When you finish your goal, click the matching **Goal** button at the bottom of the Manual client.

## Which items can be in another player's world?

Because your slot has no item pool of its own, every location in this game will contain an item that belongs to another player.
The `Nothing` filler of your slot is set up (in the template YAML) so it is never placed in your own locations.
