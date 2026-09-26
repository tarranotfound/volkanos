# VOLKANOS

My personal Arch Linux + Hyprland setup.

Volkanos is a rice I build while learning Linux, window managers, configuration files, and Git. It is made for my ThinkPad X390 Yoga, so some parts may need changes on other hardware.

![Volkanos](2026-09-06_14-44-22.png)

## What I use

- **Hyprland** — window management, keybinds, and input settings
- **Sway** — lightweight i3-compatible Wayland window management
- **Kitty** — terminal
- **Waybar** — status bar
- **Fuzzel** — application launcher
- **Hyprlock** — lock screen
- **Fastfetch** — system information
- **Cava** — audio visualizer
- **Vibe** — background/visual configuration
- **btop** — system monitor
- **Neovim** — lightweight editor and Volkanos theme

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
├── btop/                    # btop config, theme, and notes
├── cava/                    # Cava config
├── fastfetch/               # Fastfetch theme
├── fuzzel/                  # Fuzzel launcher config
├── kitty/                   # Kitty terminal config
├── nvim/                    # Neovim config and Volkanos theme
├── vibe/                    # Vibe config
├── waybar/                  # Waybar config and modules
├── scripts/
│   ├── volkanos-setup       # Interactive installer
│   └── volkanos-setup-dry-run # Repository/setup checks
├── docs/
│   └── aur-packages.md      # Optional AUR package notes
├── hyprland.conf            # Hyprland config
├── hyprland.lua             # Hyprland Lua config
├── hyprlock.conf            # Hyprlock config
├── monitors.conf            # Optional monitor config
├── workspaces.conf          # Workspace config
├── README.md
├── LICENSE
└── CONTRIBUTING.md
```

The root-level Hyprland files are kept this way because this repository started as a copy of my working configuration. Sway and Niri configurations live in their own directories. Check the paths before copying anything into `~/.config`.

## Installation

### Automatic setup

Volkanos includes a terminal-based setup script for Arch Linux. It lets you select the components you want, checks that selected packages are available, creates a timestamped backup before deployment, and then copies the selected configurations into `~/.config`.

Clone the repository:

```bash
git clone https://github.com/tarranotfound/volkanos.git
cd volkanos
```

Run the setup script:

```bash
bash scripts/volkanos-setup
```

The installer uses **gum** for its terminal menu. If **gum** is not installed, the script offers to install it with `pacman`.

The setup script includes **Hyprland, Sway, and Niri** as separate window-manager choices.

The setup script:

1. Checks the local environment and required commands.
2. Lets you select Volkanos components interactively.
3. Verifies that selected packages are available through the local Arch package database.
4. Installs the selected packages with `pacman`.
5. Creates a timestamped backup under `~/.local/share/volkanos/backups`.
6. Deploys the selected configuration files.

The setup script should be run as a normal user. It uses `sudo` only when package installation requires it.

### Dry run

If you want to inspect whether the repository has the files expected by the installer without changing your configuration, run:

```bash
bash scripts/volkanos-setup-dry-run
```

For help:

```bash
bash scripts/volkanos-setup-dry-run --help
```

The dry run checks the setup environment and expected repository configuration paths without installing packages or deploying your configs.

### Manual installation

You can also install components manually if you prefer full control.

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
cp -r ~/.config/nvim ~/.config/volkanos-backup/ 2>/dev/null || true
```

Install only the components you want:

```bash
cp -r cava ~/.config/
cp -r fuzzel ~/.config/
cp -r kitty ~/.config/
cp -r vibe ~/.config/
cp -r waybar ~/.config/
cp -r fastfetch ~/.config/
cp -r nvim ~/.config/
```

For btop, read the instructions in [`btop/README.md`](btop/README.md).

Review the Hyprland files before using them:

```bash
cp hyprland.conf ~/.config/hypr/
cp hyprland.lua ~/.config/hypr/
cp hyprlock.conf ~/.config/hypr/
cp monitors.conf ~/.config/hypr/
cp workspaces.conf ~/.config/hypr/
```

Do not blindly replace your existing setup. Check monitor names, input settings, keybinds, file paths, and installed programs first.

## Optional AUR packages

Some newer or development versions of components may be available through the Arch User Repository (AUR). See [`docs/aur-packages.md`](docs/aur-packages.md) for notes and examples.

AUR packages are optional and are not required just because they appear in the documentation. Always inspect a PKGBUILD before installing an AUR package.

## Current limitations

- The automatic setup targets Arch Linux and uses `pacman`.
- The configs are not tested on every computer.
- Some settings depend on my ThinkPad and display name.
- The installer does not automatically merge an existing configuration with Volkanos.
- Some components may require additional packages or manual setup.
- The repository contains personal preferences and experimental changes.

## Development notes

I change this repository gradually as I test things on my own system. A configuration is kept here when it is useful, readable, or worth recovering later. Not every file is perfect, and breaking changes may happen while I learn.

AI tools may be used for explanations, troubleshooting, or drafting parts of configuration files, but the settings are adjusted and tested against my actual setup before I keep them.

## Contributing

Suggestions, bug reports, and improvements are welcome. Please explain what was tested and include the relevant application, distro, and configuration details.

See [`CONTRIBUTING.md`](CONTRIBUTING.md) before opening a pull request.

## License

See [LICENSE](LICENSE).

---

Built while learning Arch Linux, Hyprland, and Git.

## Recent changes

- Added a small README change log for easier project history.
- Clarified that configuration choices are personal preferences.
- Documented the keyboard-driven workflow.
- Added a note about keeping component configurations separate.
- Clarified the purpose of the repository layout.
- Added a reminder to review hardware-specific settings.
- Documented the dry-run command more explicitly.
- Clarified that the installer is intended for normal-user execution.
- Added a note about optional AUR packages.
- Clarified that AUR packages should be inspected before installation.
- Added a note about experimental configuration changes.
- Documented gradual configuration updates.
- Clarified that not every component is tested on every machine.
- Added a note about checking installed programs before copying configs.
- Refined the README history section for future maintenance.


### Configuration workflow
Volkanos keeps each desktop component in its own directory or configuration file so changes can be tested independently.


### Hardware scope
The default layout is designed around a laptop workflow, while monitor and workspace overrides remain available for other setups.


### Visual priorities
Volkanos prioritizes readable spacing, thin borders, keyboard navigation, and a small set of accent colors.


### Component isolation
Individual components can be copied into `~/.config` without requiring the complete Volkanos setup.


### Experimental settings
Some window-manager settings are intentionally easy to adjust as the configuration evolves.


### Testing
Configuration changes should be checked on the target Wayland session before being treated as hardware-independent defaults.


### Backups
The setup workflow creates a timestamped backup before deploying selected components, making configuration changes easier to revert.
