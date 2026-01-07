# TheCore Lite for Kinesis Advantage2

This is a transformed version of TheCore Lite optimized for the Kinesis Advantage2 split keyboard, with the hand position shifted one column to the right (index finger on F instead of D).

## Installation

1. Copy `TheCore Lite.SC2Hotkeys` to your SC2 Hotkeys folder:
   - **macOS**: `~/Library/Application Support/Blizzard/StarCraft II/Accounts/<ID>/Hotkeys/`
   - **Windows**: `Documents\StarCraft II\Accounts\<ID>\Hotkeys\`

2. In StarCraft II, go to Menu → Hotkeys and select "TheCore Lite"

## Mac Mode Note

If your Kinesis is in Mac mode, you may need to remap Left Command to Left Control at the keyboard firmware level (using onboard programming or SmartSet app), or switch to Windows mode.

## How It Works

### Hand Position Shift

With index finger on F (instead of D), all left-hand keys shift one column right:

```
1→2  2→3  3→4  4→5
Tab→Q  Q→W  W→E  E→R  R→T
CapsLock→A  A→S  S→D  D→F  F→G
Z→X  X→C  C→V  V→B
```

### Edge Key Remapping

Keys at the right edge of the accessible left-hand area can't shift further right (they'd cross the keyboard split), so they remap to keys below the bottom letter row:

| Original | Transformed | Location |
|----------|-------------|----------|
| 5 | Grave | Grave/tilde key |
| T | OEM102 | International Backslash key, left of Left arrow |
| G | Left | Left arrow key |
| B | Right | Right arrow key |

### Camera Controls

To free up the arrow keys for abilities, camera scrolling moves to IJKL:

```
CameraMoveUp=I
CameraMoveDown=K
CameraMoveLeft=J
CameraMoveRight=L
```

## Freed Keys

The transformation leaves these keys accessible but unbound: **Tab**, **CapsLock**, **Z**, **Equals**, and **Delete**.

Suggested uses: IdleWorker, Cancel, WarpIn, push-to-talk, remap edge keys here instead of the bottom row, or remap Z to Shift for easier modifier access.

## Regenerating the Hotkey File

The Kinesis layout is defined in `KeyboardLayouts.ini` and generated automatically by `TheCoreRemapper.py` along with all other keyboard layouts:

```bash
python3 TheCoreRemapper.py
```
