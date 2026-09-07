#!/bin/bash
# ~/.config/waybar/toggle.sh
# Spawns the real waybar (config.jsonc) if it's not running, kills it if it is.
# The Hyprland layerrule handles the slide-down/up animation on spawn/close.

MAIN_CFG="$HOME/.config/waybar/config.jsonc"
MAIN_CSS="$HOME/.config/waybar/style.css"

if pgrep -f "waybar -c $MAIN_CFG" > /dev/null; then
    pkill -f "waybar -c $MAIN_CFG"
else
    waybar -c "$MAIN_CFG" -s "$MAIN_CSS" &
    disown
fi
