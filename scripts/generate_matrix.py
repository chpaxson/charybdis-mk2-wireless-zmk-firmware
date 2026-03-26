import json
from pathlib import Path

# === CONFIGURATION ===
PERIPHERAL_BOARD = "nice_nano"      # left + right halves
DONGLE_BOARD     = "esp32c3_devkitm" # USB dongle (central)

# automatically find all *.keymap filenames under ../config/keymap
keymap_dir = Path(__file__).parent.parent / "config" / "keymap"
keymaps = sorted(p.stem for p in keymap_dir.glob("*.keymap"))

groups = []
for keymap in keymaps:
    # Dongle build: left + right peripherals on nice_nano,
    # dongle central on esp32c3_devkitm — emitted as two matrix entries
    # that share the same output directory name via the name field.
    groups.append({
        "keymap": keymap,
        "format": "dongle-peripheral",
        "name": f"{keymap}-dongle",
        "board": PERIPHERAL_BOARD,
    })
    groups.append({
        "keymap": keymap,
        "format": "dongle-central",
        "name": f"{keymap}-dongle",
        "board": DONGLE_BOARD,
    })

# single reset entry (nice_nano)
groups.append({
    "keymap": "default",
    "format": "reset",
    "name": "reset-nanov2",
    "board": PERIPHERAL_BOARD,
})

# Dump matrix as compact JSON (GitHub expects it this way)
print(json.dumps(groups))
