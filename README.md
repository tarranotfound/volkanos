# VOLKANOS

My personal Arch Linux + Hyprland setup.

Volkanos is a rice I build while learning Linux, window managers, configuration files, and Git. It is made for my ThinkPad X390 Yoga, so some parts may need changes on other hardware.

![Volkanos](2026-09-06_14-44-22.png)

## What I use

- **Hyprland** — window management, keybinds, and input settings
- **Kitty** — terminal
- **Waybar** — status bar
- **Fuzzel** — application launcher
- **Hyprlock** — lock screen
- **Fastfetch** — system information
- **Cava** — audio visualizer
- **Vibe** — background/visual configuration
- **btop** — system monitor

## Design choices

The setup is intentionally simple:

- Dark background with red accents
- Sage green used for small details
- Thin borders instead of heavy window effects
- Mostly keyboard-driven workflow
- Avoid unnecessary animations and resource usage
- Keep each program's configuration separate

The colors and layout are personal preferences, not a universal theme.

## Repository layout

```text
volkanos/
├── btop/                 # btop config, theme, and notes
├── cava/                 # Cava config
├── fastfetch/            # Fastfetch theme
├── fuzzel/               # Fuzzel launcher config
├── kitty/                # Kitty terminal config
├── vibe/                 # Vibe config
├── waybar/               # Waybar config and modules
├── hyprland.conf         # Hyprland config
├── hyprland.lua          # Hyprland Lua config
├── hyprlock.conf         # Hyprlock config
├── monitors.conf         # Optional monitor config
├── README.md
├── LICENSE
└── CONTRIBUTING.md
```

The root-level Hyprland files are kept this way because this repository started as a copy of my working configuration. Check the paths before copying anything into `~/.config`.

## Installation

Clone the repository:

```bash
git clone https://github.com/tarranotfound/volkanos.git
cd volkanos
```

Back up your current configuration before changing anything:

```bash
mkdir -p ~/.config/volkanos-backup
cp -r ~/.config/hypr ~/.config/volkanos-backup/ 2>/dev/null || true
cp -r ~/.config/kitty ~/.config/volkanos-backup/ 2>/dev/null || true
cp -r ~/.config/fuzzel ~/.config/volkanos-backup/ 2>/dev/null || true
cp -r ~/.config/waybar ~/.config/volkanos-backup/ 2>/dev/null || true
cp -r ~/.config/hyprlock ~/.config/volkanos-backup/ 2>/dev/null || true
cp -r ~/.config/vibe ~/.config/volkanos-backup/ 2>/dev/null || true
```

Install only the components you want:

```bash
cp -r cava ~/.config/
cp -r fuzzel ~/.config/
cp -r kitty ~/.config/
cp -r vibe ~/.config/
cp -r waybar ~/.config/
cp -r fastfetch ~/.config/
```

For btop, read the instructions in [`btop/README.md`](btop/README.md).

Review the Hyprland files before using them:

```bash
cp hyprland.conf ~/.config/hypr/
cp hyprland.lua ~/.config/hypr/
cp hyprlock.conf ~/.config/hypr/
cp monitors.conf ~/.config/hypr/
```

Do not blindly replace your existing setup. Check monitor names, input settings, keybinds, file paths, and installed programs first.

## Current limitations

- This is not an automatic installer.
- The configs are not tested on every computer.
- Some settings depend on my ThinkPad and display name.
- The Lua and Hyprland files may need manual merging.
- The repository contains personal preferences and experimental changes.

## Development notes

I change this repository gradually as I test things on my own system. A configuration is kept here when it is useful, readable, or worth recovering later. Not every file is perfect, and breaking changes may happen while I learn.

AI tools may be used for explanations, troubleshooting, or drafting parts of configuration files, but the settings are adjusted and tested against my actual setup before I keep them.

## Contributing

Suggestions, bug reports, and improvements are welcome. Please explain what was tested and include the relevant application, distro, and configuration details.

See [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.

## License

See [LICENSE](LICENSE).

---

Built while learning Arch Linux, Hyprland, and Git.
