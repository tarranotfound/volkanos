#!/usr/bin/env bash

# Optional Volkanos startup helpers for Niri.
# Each command is checked before it is launched so missing components
# do not prevent the rest of the session from starting.

run_if_available() {
    command -v "$1" >/dev/null 2>&1 || return 0
    "$@" >/dev/null 2>&1 &
}

# Bar
run_if_available waybar

# Wallpaper daemon: configure your wallpaper separately if needed.
# Example:
# run_if_available swww-daemon

# Optional terminal visualizer
# run_if_available cava

# Optional system information terminal
# run_if_available kitty --hold fastfetch

exit 0
