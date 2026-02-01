#!/usr/bin/env python3
"""
Generate a personal Kinesis hotkey file with custom key remappings.

This script takes the generated KinesisAdvantage2/TheCore Lite.SC2Hotkeys
and creates a "Personal" version with customizations applied.
"""

import re
from pathlib import Path

# Configuration: key remappings to apply
# Format: (from_key, to_key)
KEY_REMAPS = [
]

# Configuration: bindings to override
# Format: (command, new_value)
BINDING_OVERRIDES = [
    ("IdleWorker", "Tab"),  # IdleWorker on Tab (was F1)
]

def remap_key(line: str, from_key: str, to_key: str) -> str:
    """Remap a key in a hotkey line, handling modifiers correctly."""
    # Pattern matches the key at the end of the value, with optional modifiers
    # Examples: =A, =Shift+A, =Control+Alt+A, =A,B (alternate keys)

    # Match key as the entire value or after + or , but not as part of another key name
    # Handles: =A, =Shift+A, =A,B, =Shift+A,Shift+B

    patterns = [
        (f'={from_key}$', f'={to_key}'),           # =A at end of line
        (f'={from_key},', f'={to_key},'),          # =A, (with alternates)
        (f'\\+{from_key}$', f'+{to_key}'),         # +A at end (after modifier)
        (f'\\+{from_key},', f'+{to_key},'),        # +A, (modifier with alternates)
        (f',{from_key}$', f',{to_key}'),           # ,A at end (alternate key)
        (f',{from_key},', f',{to_key},'),          # ,A, (middle alternate)
    ]

    result = line
    for pattern, replacement in patterns:
        result = re.sub(pattern, replacement, result)

    return result


def apply_binding_override(line: str, command: str, new_value: str) -> str:
    """Override a specific command's binding."""
    # Match command= at start of line (possibly with unit suffix like Command/Unit=)
    if line.startswith(command + "=") or line.startswith(command + "/"):
        # Only override the base command, not unit-specific variants
        if line.startswith(command + "="):
            return f"{command}={new_value}\n"
    return line


def generate_personal_hotkeys():
    base_dir = Path(__file__).parent
    source = base_dir / "KinesisAdvantage2" / "TheCore Lite.SC2Hotkeys"
    dest = base_dir / "KinesisAdvantage2" / "TheCore Lite Personal.SC2Hotkeys"

    if not source.exists():
        print(f"Error: Source file not found: {source}")
        print("Run 'python TheCoreRemapper.py' first to generate the base hotkey file.")
        return False

    with open(source, 'r') as f:
        lines = f.readlines()

    # Apply remappings and overrides
    remapped_lines = []
    changes = []

    for i, line in enumerate(lines, 1):
        original = line
        for from_key, to_key in KEY_REMAPS:
            line = remap_key(line, from_key, to_key)
        for command, new_value in BINDING_OVERRIDES:
            line = apply_binding_override(line, command, new_value)

        if line != original:
            changes.append((i, original.strip(), line.strip()))
        remapped_lines.append(line)

    # Write output
    with open(dest, 'w') as f:
        f.writelines(remapped_lines)

    print(f"Generated: {dest}")
    print(f"Applied {len(changes)} remappings:")
    for line_num, old, new in changes:
        print(f"  Line {line_num}: {old} -> {new}")

    return True


if __name__ == "__main__":
    generate_personal_hotkeys()
