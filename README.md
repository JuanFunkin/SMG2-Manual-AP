# Super Mario Galaxy 2 - Archipelago Manual (send-only)

A [Manual](https://github.com/ManualForArchipelago/Manual) APWorld for **Super Mario Galaxy 2** (Wii / Nintendo Switch)
for the [Archipelago](https://archipelago.gg) multiworld randomizer.

It is a **send-only** world: you play Super Mario Galaxy 2 completely normally, and every **galaxy you unlock** and every
**star you collect** is a check that sends an item to *another* player. **You never receive real items**, so nothing in
Galaxy 2 is ever locked behind the multiworld.

> Manual worlds work on the honor system: nothing is injected into the game. You click the check in the Manual client
> when you do it in-game.

## Features

- Everything is generated from one table ([`tools/generate_data.py`](tools/generate_data.py)), no hand-written JSON.
- Names of galaxies and missions come from the [Super Mario Wiki](https://www.mariowiki.com/Template:SMG2_missions) and
  are listed **in map order**: World 1 -> World 6 -> World S, galaxy by galaxy.
- Pick what counts as a check from the YAML: galaxy unlocks, Prankster Comet stars, Mailtoad letter stars, Green Stars,
  Grandmaster Galaxy.
- Four goals: beat Bowser, 120 Power Stars, 120 Power + 120 Green Stars, or clear the Grandmaster Galaxy.
- The goal automatically turns on the checks it needs (e.g. the Grandmaster goal enables Green Stars + Grandmaster Galaxy).

## Checks

| Group | Checks | Default |
|---|---:|:---:|
| Galaxy unlocks (every galaxy except Sky Station Galaxy, which is open from the start) | 47 | on |
| Power Stars (the regular 120) | 120 | always |
| - of which Prankster Comet stars | 35 | on |
| - of which Mailtoad letter stars | 7 | on |
| Green Stars (each galaxy has as many as it has Power Stars) | 120 | off |
| Grandmaster Galaxy (unlock + The Ultimate Test + The Perfect Run) | 3 | off |

Default pool: **167 checks**. With everything enabled: **290 checks**.
The full list is in [`docs/LOCATIONS.md`](docs/LOCATIONS.md).

| World | Default | Everything on |
|---|---:|---:|
| World 1 | 24 | 42 |
| World 2 | 25 | 43 |
| World 3 | 25 | 43 |
| World 4 | 25 | 43 |
| World 5 | 25 | 43 |
| World 6 | 25 | 43 |
| World S | 18 | 33 |

In the Manual client the locations are grouped by world, in this order. Each galaxy shows its *Unlock* check first,
then its stars (and its Green Stars if enabled).

### Goals

| `goal` value | What to do |
|---|---|
| `defeat bowser` | Beat Bowser in Bowser's Galaxy Generator |
| `collect 120 power stars` | Collect the 120 Power Stars |
| `collect 120 power and 120 green stars` | Collect all 240 stars |
| `clear grandmaster galaxy` | Finish The Ultimate Test and The Perfect Run |

When you finish your goal, click the matching **Goal** button at the bottom of the Manual client.

## How "send-only" works

Archipelago needs every world to have as many items as locations. This world has no real items, so the pool is filled with
a harmless filler called **`Nothing`**. The template YAML sets `non_local_items: [Nothing]`, which forces all of those
fillers into *other* players' worlds. The result: every location in your slot holds an item that belongs to someone else.

Because the SMG2 slot never needs anything to progress, there is no logic: every check is reachable from the start in
Archipelago's eyes and you can play in whatever order you like. Use `exclude_locations` / the toggles to keep very hard
checks (e.g. *The Perfect Run*) from holding important items.

> If the rest of the multiworld has **fewer locations than your slot has checks**, generation fails because the `Nothing`
> fillers have nowhere to go. Either enable fewer groups of checks or remove the `non_local_items` line.

## Installation

1. Install [Archipelago](https://github.com/ArchipelagoMW/Archipelago/releases).
2. Download `manual_supermariogalaxy2.apworld` from the [Releases](../../releases) page (or build it, see below).
3. Double-click the `.apworld` (or copy it into the `custom_worlds` folder of your Archipelago install) and restart the Launcher.
4. Copy [`yaml/Manual_SuperMarioGalaxy2.yaml`](yaml/Manual_SuperMarioGalaxy2.yaml), set your name,
   choose a goal and groups of checks, and give it to whoever generates the multiworld.
5. Open the Archipelago Launcher -> **Manual Client**, connect with your slot name and play.

Game name inside Archipelago: `Manual_SuperMarioGalaxy2`.

## Building from source

Requires Python 3.10+ (no extra packages).

```bash
python tools/generate_data.py   # regenerates src/data/*.json, src/archipelago.json and docs/LOCATIONS.md
python build.py                 # builds dist/manual_supermariogalaxy2.apworld
```

Repository layout:

```
tools/generate_data.py   the single table of galaxies / missions + generator of all data files
build.py                 zips src/ into the .apworld
src/                     the Manual framework + generated data (this is what ends up in the .apworld)
  data/                  game.json, items.json, locations.json, categories.json, options.json, meta.json ...
  hooks/World.py         small hook that forces the checks needed by the chosen goal
  docs/                  game page + setup guide shown on the Archipelago website
yaml/                    ready-to-use player YAML template
docs/LOCATIONS.md        every check, in order (generated)
```

### Changing things

- **Rename the game / creator**: edit `GAME` and `CREATOR` in `tools/generate_data.py`, regenerate and rebuild. (Also rename
  the `en_Manual_...md` file in `src/docs/` and the game name inside the YAML.)
- **Add, remove or rename a check or an option**: edit the tables in `tools/generate_data.py`, regenerate, rebuild.
- Never edit `src/data/*.json` by hand, they are overwritten by the generator.

## Credits and licenses

- Built on the [Manual for Archipelago](https://github.com/ManualForArchipelago/Manual) framework (MIT).
- Galaxy and mission names: [Super Mario Wiki](https://www.mariowiki.com) (CC BY-SA 4.0).
- This is an unofficial fan project. It is not affiliated with or endorsed by Nintendo or the Archipelago project.
  *Super Mario Galaxy 2* is a trademark of Nintendo. No game assets are included.

Released under the [MIT License](LICENSE).
