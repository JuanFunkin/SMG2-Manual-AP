#!/usr/bin/env python3
"""
Builds the .apworld from ./src

    python build.py

Output: dist/manual_supermariogalaxy2.apworld
(An .apworld is just a zip whose single top-level folder has the same name as the file.)
"""
import json
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
DIST = ROOT / "dist"

game = json.loads((SRC / "data" / "game.json").read_text(encoding="utf-8"))
folder = (f"manual_{game['game']}_{game['creator']}" if game.get("creator") else f"manual_{game['game']}").lower()
out = DIST / f"{folder}.apworld"

DIST.mkdir(exist_ok=True)
with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
    for path in sorted(SRC.rglob("*")):
        if path.is_dir() or "__pycache__" in path.parts or path.suffix == ".pyc":
            continue
        z.write(path, Path(folder) / path.relative_to(SRC))

print(f"Built {out.relative_to(ROOT)}")
