# Volkanos Sway

Sway configuration for the Volkanos rice.

## Install

On Arch Linux:

```bash
sudo pacman -S --needed sway swaybg grim slurp
```

Volkanos components such as Kitty, Fuzzel, Waybar, Vibe, and Hyprlock can be installed separately.

Copy the configuration:

```bash
mkdir -p ~/.config/sway
cp config ~/.config/sway/config
```

Or select **Sway** from the Volkanos setup script.

## Session

Start Sway from a TTY:

```bash
sway
```

The configuration keeps the Volkanos workflow keyboard-first and uses Waybar for the status bar.

## Keybinds

| Key | Action |
|---|---|
| Super + Enter | Kitty |
| Super + R | Fuzzel |
| Super + Q | Close window |
| Super + V | Toggle floating |
| Super + F | Fullscreen |
| Super + L | Hyprlock |
| Super + D | Waybar |
| Super + X | Screenshot |
| Super + Shift + C | Reload config |
| Super + Shift + R | Restart Sway |
| Super + Tab | Previous workspace |
| Super + Arrow | Focus |
| Super + Shift + Arrow | Move container |
| Super + Ctrl + Arrow | Resize |
| Super + 1–0 | Workspace |
| Super + Shift + 1–0 | Move to workspace |
| Super + E | Toggle split |
| Super + W | Tabbed layout |
| Super + S | Stacking layout |
| Super + Shift + E | Exit Sway |

## Notes

- The palette follows Volkanos: red `#e0283b`, sage/blue-gray supporting tones, and cream text.
- Monitor-specific settings are intentionally omitted so the config can start on different displays.
- Wallpaper expects `~/Pictures/Wallpapers/wallpaper.jpg`. Change that line if your wallpaper has another name.
- Vibe is optional; remove its startup line if it is not installed.

## Startup

The session uses `sway/startup.sh` to start optional Waybar and the Volkanos wallpaper without duplicating already-running processes.
