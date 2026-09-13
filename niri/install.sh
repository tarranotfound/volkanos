#!/usr/bin/env bash
set -euo pipefail

CONFIG_DIR="${XDG_CONFIG_HOME:-$HOME/.config}/niri"
SOURCE_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
SOURCE_CONFIG="$SOURCE_DIR/config.kdl"
SOURCE_STARTUP="$SOURCE_DIR/startup.sh"
TARGET_CONFIG="$CONFIG_DIR/config.kdl"
TARGET_STARTUP="$CONFIG_DIR/startup.sh"

if [[ ! -f "$SOURCE_CONFIG" ]]; then
    printf 'Error: config.kdl was not found next to this script.\n' >&2
    exit 1
fi

mkdir -p "$CONFIG_DIR"

if [[ -f "$TARGET_CONFIG" ]]; then
    BACKUP="$TARGET_CONFIG.backup.$(date +%Y%m%d-%H%M%S)"
    cp -- "$TARGET_CONFIG" "$BACKUP"
    printf 'Backed up existing config to: %s\n' "$BACKUP"
fi

cp -- "$SOURCE_CONFIG" "$TARGET_CONFIG"
printf 'Installed Volkanos Niri config to: %s\n' "$TARGET_CONFIG"

if [[ -f "$SOURCE_STARTUP" ]]; then
    cp -- "$SOURCE_STARTUP" "$TARGET_STARTUP"
    printf 'Installed optional startup helper to: %s\n' "$TARGET_STARTUP"
fi

printf 'Review monitor, input, and application settings before reloading Niri.\n'
