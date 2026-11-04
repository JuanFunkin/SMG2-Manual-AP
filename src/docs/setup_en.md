# Super Mario Galaxy 2 Manual Setup Guide

## Required Software

- [Archipelago](https://github.com/ArchipelagoMW/Archipelago/releases) (0.5.0 or newer)
- Super Mario Galaxy 2 for the Wii, or *Super Mario Galaxy + Super Mario Galaxy 2* for the Nintendo Switch
  (nothing is patched, any version works)

## Installation

1. Download `manual_supermariogalaxy2.apworld` from the releases page.
2. Double-click it (Archipelago will install it) or copy it into the `custom_worlds` folder of your Archipelago install.
3. Restart the Archipelago Launcher.

## Generating a YAML

Use the template `Manual_SuperMarioGalaxy2.yaml`, or open the Launcher -> **Generate Template Options** and edit the generated file.
Put your own player name at the top, choose a `goal` and the groups of checks you want.

## Joining a MultiWorld game

1. Open the Archipelago Launcher and start **Manual Client**.
2. Connect to the server with your slot name. The game must be `Manual_SuperMarioGalaxy2`.
3. Play Super Mario Galaxy 2 normally. Whenever you unlock a galaxy or collect a star, click the matching location in the Manual client.
4. When you reach your goal, click the **Goal** button at the bottom of the list.

## Tips

- Your slot never receives useful items, so there is no logic to follow, play in any order you like.
- Don't want some check (for example *The Perfect Run*)? Add it to `exclude_locations` in your YAML.
- Locations are grouped by world (World 1 ... World 6, World S), in the same order as the in-game map.
