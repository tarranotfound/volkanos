#!/usr/bin/env bash
set -u

# Start optional Volkanos services without duplicating running processes.
command -v waybar >/dev/null 2>&1 && pgrep -x waybar >/dev/null 2>&1 || command -v waybar >/dev/null 2>&1 && waybar >/dev/null 2>&1 &
command -v swaybg >/dev/null 2>&1 && [ -f "$HOME/Pictures/Wallpapers/wallpaper.jpg" ] && swaybg -m fill -i "$HOME/Pictures/Wallpapers/wallpaper.jpg" >/dev/null 2>&1 &
