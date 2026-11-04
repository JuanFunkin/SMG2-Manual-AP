#!/usr/bin/env python3
"""
Regenerates every data file of the Super Mario Galaxy 2 Manual (src/data/*.json and the docs)
from the single table below, so nothing has to be written by hand.

Source of every galaxy / mission name: Super Mario Wiki
  https://www.mariowiki.com/Template:SMG2_missions
  https://www.mariowiki.com/World_S   (unlock criteria of World S)

Usage:  python tools/generate_data.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "src" / "data"

GAME = "SuperMarioGalaxy2"
CREATOR = ""  # empty -> game name is just Manual_SuperMarioGalaxy2
GAME_NAME = f"Manual_{GAME}_{CREATOR}" if CREATOR else f"Manual_{GAME}"
WORLD_VERSION = "1.0.0"

# Mission flags:  c = Prankster Comet mission,  m = only appears after the Mailtoad letter
# Galaxy flags:   boss = boss galaxy,  luma = galaxy unlocked by feeding a Hungry Luma
C, M = "c", "m"

WORLDS = [
    ("World 1", [
        ("Sky Station Galaxy", [("Peewee Piranha's Temper Tantrum",), ("Storming the Sky Fleet",), ("Peewee Piranha's Speed Run", C)], {"start": True}),
        ("Yoshi Star Galaxy", [("Saddle Up with Yoshi",), ("Spiny Control",), ("Spiny Rainbow Romp", C)], {}),
        ("Spin-Dig Galaxy", [("Digga-Leg's Planet",), ("Silver Stars Down Deep",), ("Digga-Leg's Daredevil Run", C)], {}),
        ("Fluffy Bluff Galaxy", [("Search for the Toad Brigade Captain",), ("The Chimp's Stomp Challenge", M), ("Every Planet Has Its Price",)], {}),
        ("Rightside Down Galaxy", [("Breaking the Laws of Gravity",), ("The Great Crate Incinerator",)], {}),
        ("Bowser Jr.'s Fiery Flotilla", [("Gobblegut's Aching Belly",), ("Fiery Flotilla Speed Run", C)], {"boss": True}),
        ("Flip-Swap Galaxy", [("Think Before You Shake",), ("Purple Coin Flip 'n' Sprint", C)], {"luma": True}),
    ]),
    ("World 2", [
        ("Puzzle Plank Galaxy", [("The Puzzling Picture Block",), ("Purple Coin Shadow Vault", C), ("Bugaboom's Back",)], {}),
        ("Hightail Falls Galaxy", [("Hot-Stepping Dash Pepper",), ("Hightail Falls Speed Run", C), ("Silver Stars in Hightail Falls",)], {}),
        ("Boulder Bowl Galaxy", [("Rock and Rollodillo",), ("C'mere, Goomba", M), ("Rolling Crabber Romp", C)], {}),
        ("Cosmic Cove Galaxy", [("Twin Falls Hideaway",), ("Exploring the Cosmic Cavern",), ("Catch That Star Bunny",)], {}),
        ("Wild Glide Galaxy", [("Fluzzard's First Flight",), ("Jungle Fluzzard Race", M)], {}),
        ("Bowser's Lava Lair", [("Bowser's Big Lava Power Party",), ("Lava Lair Speed Run", C)], {"boss": True}),
        ("Honeybloom Galaxy", [("Bumble Beginnings",), ("The Secret Wall Jump",)], {"luma": True}),
    ]),
    ("World 3", [
        ("Tall Trunk Galaxy", [("The Flotacious Blimp Fruit",), ("Tall Trunk's Big Slide",), ("Tall Trunk's Purple Coin Slide", C)], {}),
        ("Cloudy Court Galaxy", [("Head in the Clouds",), ("The Shadow Lining", C), ("Silver Stars in the Purple Pond",)], {}),
        ("Haunty Halls Galaxy", [("A Glimmer of Bulb Berry",), ("Sneaking Down the Creepy Corridor",), ("Spooky Cosmic Clone Chase", C)], {}),
        ("Freezy Flake Galaxy", [("Bowser on Ice",), ("Sorbetti's Chilly Reception",), ("The Chimp's Skating Challenge",)], {}),
        ("Rolling Masterpiece Galaxy", [("Silver Chomp Grudge Match",), ("Masterpiece Speed Run", C)], {}),
        ("Bowser Jr.'s Fearsome Fleet", [("Bowser Jr.'s Mighty Megahammer",), ("Megahammer's Daredevil Bash", C)], {"boss": True}),
        ("Beat Block Galaxy", [("Step to the Beep",), ("Silver Stars in Double Time", C)], {"luma": True}),
    ]),
    ("World 4", [
        ("Supermassive Galaxy", [("Huge Trouble with Big Wigglers",), ("Big Wigglers Speed Run", C), ("In Full Bloom",)], {}),
        ("Flipsville Galaxy", [("Flip-Flopping in Flipsville",), ("Flipsville's New Digs",), ("Purple Coin Spin Speed Run", C)], {}),
        ("Honeyhop Galaxy", [("The Sweetest Silver Stars",), ("The Chimp's Score Challenge", M)], {}),
        ("Starshine Beach Galaxy", [("Surf, Sand, and Silver Stars",), ("Climbing the Cloudy Tower",), ("Purple Coin Beach Dash", C)], {}),
        ("Chompworks Galaxy", [("Where the Chomps Are Made of Gold",), ("Spring into the Chompworks",), ("Cosmic Clones in the Chompworks", C)], {}),
        ("Bowser's Gravity Gauntlet", [("Breaking into Bowser's Castle",), ("Gravity Star Speed Run", C)], {"boss": True}),
        ("Sweet Mystery Galaxy", [("Bulb Berry's Mysterious Glow",), ("Bulb Berry's Purple Coin Glow", C)], {"luma": True}),
    ]),
    ("World 5", [
        ("Space Storm Galaxy", [("Follow Me, Bob-omb",), ("To the Top of Topman's Tower",), ("C'mere, Topman", M)], {}),
        ("Slipsand Galaxy", [("Squizzard's Sandy Sinkhole",), ("Sailing the Sandy Seas",), ("Squizzard's Daredevil Run", C)], {}),
        ("Shiverburn Galaxy", [("Prince Pikante's Peppery Mood",), ("Octo-Army Icy Rainbow Romp", C), ("The Chimp's Ultimate Skating Challenge",)], {}),
        ("Boo Moon Galaxy", [("Silver Stars Pop-Up",), ("Haunting the Howling Tower",), ("The Star in the Sinking Swamp",)], {}),
        ("Upside Dizzy Galaxy", [("A Walk on the Weird Side",), ("Burning Upside Dizzy",)], {}),
        ("Bowser Jr.'s Boom Bunker", [("Bowser Jr.'s Boomsday Machine",), ("Boomsday Machine Daredevil Run", C)], {"boss": True}),
        ("Fleet Glide Galaxy", [("Fluzzard's Wild Battlefield Glide",), ("Fastest Feathers in the Galaxy", M)], {"luma": True}),
    ]),
    ("World 6", [
        ("Melty Monster Galaxy", [("The Magnificent Magma Sea",), ("A Stroll Down Rolling Lane",), ("The Chimp's Bowling Challenge",)], {}),
        ("Clockwork Ruins Galaxy", [("Time for Adventure",), ("The Adventure of the Purple Coins", C), ("The Ledge Hammer Trap",)], {}),
        ("Slimy Spring Galaxy", [("The Deep Shell Well",), ("The Chimp's Coin Challenge", M)], {}),
        ("Throwback Galaxy", [("Return of the Whomp King",), ("Silver Stars in the Whomp Fortress",), ("Whomp Silver Star Speed Run", C)], {}),
        ("Battle Belt Galaxy", [("Mini-Planet Mega-Run",), ("Mini-Planet Daredevil Run", C), ("Snacktime for Gobblegut",)], {}),
        ("Bowser's Galaxy Generator", [("Bowser's Fortified Fortress",), ("Bowser's Big Bad Speed Run", C)], {"boss": True}),
        ("Flash Black Galaxy", [("Jumping Around in the Dark",), ("Dark Octo-Army Romp", C)], {"luma": True}),
    ]),
    ("World S", [
        ("Mario Squared Galaxy", [("Make Mario a Star",), ("Luigi's Purple Coin Chaos", C)], {}),
        ("Rolling Coaster Galaxy", [("The Rainbow Road Roll",), ("Purple Coins on the Rainbow Road", C)], {}),
        ("Twisty Trials Galaxy", [("Spinning and Spinning and Spinning",), ("Turning Turning Double Time", C)], {}),
        ("Stone Cyclone Galaxy", [("Silver Stars on the Cyclone",), ("Tox Box Speed Run", C)], {}),
        ("Boss Blitz Galaxy", [("Throwback Throwdown",), ("Throwback Throwdown Speed Run", C)], {}),
        ("Flip-Out Galaxy", [("Wicked Wall Jumps",), ("Cosmic Clone Wall Jumpers", C)], {"luma": True}),
        ("Grandmaster Galaxy", [("The Ultimate Test",), ("The Perfect Run", C)], {"grandmaster": True}),
    ]),
]

# ---- Category names (hidden ones only exist to switch groups of checks on/off from the YAML) ----
CAT_UNLOCK = "Galaxy Unlocks"
CAT_COMET = "Prankster Comet Stars"
CAT_MAIL = "Mailtoad Letter Stars"
CAT_GREEN = "Green Stars"
CAT_GM = "Grandmaster Galaxy"
CAT_GOALS = "Goals"

OPT_UNLOCK = "include_galaxy_unlocks"
OPT_COMET = "include_prankster_comet_stars"
OPT_MAIL = "include_mailtoad_letter_stars"
OPT_GREEN = "include_green_stars"
OPT_GM = "include_grandmaster_galaxy"

GOALS = [
    "Defeat Bowser",
    "Collect 120 Power Stars",
    "Collect 120 Power and 120 Green Stars",
    "Clear Grandmaster Galaxy",
]


def build_locations():
    locs = []
    for world, galaxies in WORLDS:
        for galaxy, missions, flags in galaxies:
            gm = flags.get("grandmaster", False)
            base = [world]

            def cats(*extra):
                c = base + list(extra)
                if gm:
                    c.append(CAT_GM)
                return c

            # 1) the galaxy-unlocked check (Sky Station Galaxy is open from the start -> no check)
            if not flags.get("start"):
                locs.append({"name": f"Unlock {galaxy}", "category": cats(CAT_UNLOCK)})
            # 2) Power Stars of the galaxy, in the order the wiki lists them
            for mission in missions:
                name, flag = mission[0], (mission[1] if len(mission) > 1 else None)
                extra = [CAT_COMET] if flag == C else [CAT_MAIL] if flag == M else []
                locs.append({"name": f"{galaxy} - {name}", "category": cats(*extra)})
            # 3) Green Stars: each galaxy has as many as it has Power Stars (none in Grandmaster Galaxy)
            if not gm:
                for i in range(1, len(missions) + 1):
                    locs.append({"name": f"{galaxy} - Green Star {i}", "category": cats(CAT_GREEN)})
    for goal in GOALS:
        locs.append({"name": goal, "category": [CAT_GOALS], "victory": True})
    names = [l["name"] for l in locs]
    assert len(names) == len(set(names)), "duplicate location names"
    return locs


def write_json(path, obj):
    path.write_text(json.dumps(obj, indent=4, ensure_ascii=False) + "\n", encoding="utf-8")


def main():
    locs = build_locations()
    write_json(DATA / "locations.json", {
        "$schema": "https://github.com/ManualForArchipelago/Manual/raw/main/schemas/Manual.locations.schema.json",
        "data": locs,
    })

    write_json(DATA / "game.json", {
        "$schema": "https://github.com/ManualForArchipelago/Manual/raw/main/schemas/Manual.game.schema.json",
        "game": GAME,
        "creator": CREATOR,
        "filler_item_name": "Nothing",
        "death_link": False,
        "starting_index": 1,
        "unused_goals_are_locations": False,
    })

    # Manual needs at least one item defined. "Nothing" is also the filler item, so this is the only item in the world.
    write_json(DATA / "items.json", {
        "$schema": "https://github.com/ManualForArchipelago/Manual/raw/main/schemas/Manual.items.schema.json",
        "data": [
            {"name": "Nothing", "count": 1, "filler": True, "category": ["Filler"]},
        ],
    })

    # APWorld manifest (required by recent Archipelago versions)
    write_json(ROOT / "src" / "archipelago.json", {
        "game": GAME_NAME,
        "world_version": WORLD_VERSION,
        "compatible_version": 7,
        "version": 7,
    })

    write_json(DATA / "regions.json", {
        "$schema": "https://github.com/ManualForArchipelago/Manual/raw/main/schemas/Manual.regions.schema.json",
    })

    write_json(DATA / "events.json", {
        "$schema": "https://github.com/ManualForArchipelago/Manual/raw/main/schemas/Manual.events.schema.json",
        "data": [],
    })

    categories = {"$schema": "https://github.com/ManualForArchipelago/Manual/raw/main/schemas/Manual.categories.schema.json"}
    for i, (world, _) in enumerate(WORLDS):
        categories[world] = {"sort-key": f"{i}"}
    categories[CAT_GOALS] = {"sort-key": "9"}
    categories["Filler"] = {"hidden": True}
    categories[CAT_UNLOCK] = {"hidden": True, "yaml_option": [OPT_UNLOCK]}
    categories[CAT_COMET] = {"hidden": True, "yaml_option": [OPT_COMET]}
    categories[CAT_MAIL] = {"hidden": True, "yaml_option": [OPT_MAIL]}
    categories[CAT_GREEN] = {"hidden": True, "yaml_option": [OPT_GREEN]}
    categories[CAT_GM] = {"hidden": True, "yaml_option": [OPT_GM]}
    write_json(DATA / "categories.json", categories)

    def toggle(display, desc, default):
        return {"display_name": display, "description": desc, "type": "Toggle", "default": default, "group": "Checks"}

    write_json(DATA / "options.json", {
        "$schema": "https://raw.githubusercontent.com/ManualForArchipelago/Manual/main/schemas/Manual.options.schema.json",
        "core": {
            "goal": {
                "display_name": "Goal",
                "description": "What you have to do to finish your slot. Press the matching 'Goal' button in the Manual client when you do it.",
            },
            "death_link": {"default": False},
        },
        "user": {
            OPT_UNLOCK: toggle("Galaxy Unlock Checks",
                               "A check is sent every time you unlock a new galaxy (Sky Station Galaxy is open from the start, so it has none).", True),
            OPT_COMET: toggle("Prankster Comet Stars",
                              "Include the Power Stars that only appear while a Prankster Comet is orbiting the galaxy (speed runs, daredevil runs, purple coin runs...).", True),
            OPT_MAIL: toggle("Mailtoad Letter Stars",
                             "Include the Power Stars that only appear after the Mailtoad delivers a letter (The Chimp's challenges, C'mere Goomba/Topman, Jungle Fluzzard Race, Fastest Feathers in the Galaxy).", True),
            OPT_GREEN: toggle("Green Stars",
                              "Include the 120 Green Stars (needs the 120 Power Stars first). Forced on when the goal needs them.", False),
            OPT_GM: toggle("Grandmaster Galaxy",
                           "Include the Grandmaster Galaxy checks (needs all 240 Power + Green Stars). Forced on when the goal is the Grandmaster Galaxy.", False),
        },
    })

    # ---- docs/LOCATIONS.md: human readable list of every check ----
    lines = ["# Super Mario Galaxy 2 Manual - full list of checks", "",
             "Generated by `tools/generate_data.py`. Do not edit by hand.", "",
             "Legend: **[Comet]** Prankster Comet star, **[Letter]** needs a Mailtoad letter, **[Green]** Green Star, "
             "**[Unlock]** galaxy unlocked, **[GM]** Grandmaster Galaxy (off by default).", ""]
    by_world = {}
    for l in locs:
        if l.get("victory"):
            continue
        by_world.setdefault(l["category"][0], []).append(l)
    for world, items in by_world.items():
        lines += [f"## {world}  ({len(items)} checks with everything enabled)", ""]
        for l in items:
            tags = []
            if CAT_UNLOCK in l["category"]: tags.append("[Unlock]")
            if CAT_COMET in l["category"]: tags.append("[Comet]")
            if CAT_MAIL in l["category"]: tags.append("[Letter]")
            if CAT_GREEN in l["category"]: tags.append("[Green]")
            if CAT_GM in l["category"]: tags.append("[GM]")
            lines.append(f"- {l['name']} {' '.join(tags)}".rstrip())
        lines.append("")
    lines += ["## Goals", ""] + [f"- {g}" for g in GOALS] + [""]
    (ROOT / "docs").mkdir(exist_ok=True)
    (ROOT / "docs" / "LOCATIONS.md").write_text("\n".join(lines), encoding="utf-8")

    # ---- stats for README / docs ----
    gm = [l for l in locs if CAT_GM in l["category"]]
    real = [l for l in locs if not l.get("victory")]
    default = [l for l in real if CAT_GREEN not in l["category"] and CAT_GM not in l["category"]]
    print(f"total locations (everything on): {len(real)} + {len(GOALS)} goals")
    print(f"default locations: {len(default)}")
    print(f"  unlock: {sum(CAT_UNLOCK in l['category'] for l in default)}")
    print(f"  power stars: {sum(CAT_UNLOCK not in l['category'] for l in default)}"
          f" (comet: {sum(CAT_COMET in l['category'] for l in default)}, letter: {sum(CAT_MAIL in l['category'] for l in default)})")
    print(f"  green stars: {sum(CAT_GREEN in l['category'] for l in real)}   grandmaster: {len(gm)}")
    for world, items in by_world.items():
        d = [l for l in items if CAT_GREEN not in l['category'] and CAT_GM not in l['category']]
        print(f"  {world}: default {len(d)} / all {len(items)}")


if __name__ == "__main__":
    main()
