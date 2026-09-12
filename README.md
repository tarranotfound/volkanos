# VOLKANOS

> **A sharp, minimal Hyprland rice for Arch Linux.**
>
> Red accents, cozy sage tones, and a clean terminal-focused setup.

![Volkanos](2026-09-06_14-44-22.png)

## ✦ About

**Volkanos** is my personal Linux rice and one of my first open-source projects.

The goal is simple: keep the desktop **minimal, sharp, lightweight, and comfortable to use** without relying on heavy visual effects.

## 🧩 Components

- **Hyprland** — window manager and keybinds
- **Kitty** — terminal
- **Waybar** — status bar
- **Fuzzel** — application launcher
- **Hyprlock** — lock screen
- **Fastfetch** — system information
- **Cava** — audio visualizer
- **Vibe** — visual/background component

Thunar and btop are used by the setup but do not have dedicated configuration directories in this repository.

## 🎨 Style

- Dark and minimal
- Sharp red accents
- Sage green details
- Thin borders
- No unnecessary glassmorphism
- Terminal-focused workflow
- Lightweight configuration

## 📁 Structure

```text
volkanos/
├── cava/                 # Cava config
├── fastfetch/            # Fastfetch theme
├── fuzzel/               # Fuzzel launcher
├── kitty/                # Kitty terminal
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

> **Note:** The Hyprland, Hyprlock, and monitor files currently live at the repository root. Check the paths before copying them into `~/.config`.

## ⚡ Installation

### 1. Clone

```bash
git clone https://github.com/tarranotfound/volkanos.git
cd volkanos
```

### 2. Back up your current configs

```bash
mkdir -p ~/.config/volkanos-backup
cp -r ~/.config/hypr ~/.config/volkanos-backup/ 2>/dev/null || true
cp -r ~/.config/kitty ~/.config/volkanos-backup/ 2>/dev/null || true
cp -r ~/.config/fuzzel ~/.config/volkanos-backup/ 2>/dev/null || true
cp -r ~/.config/waybar ~/.config/volkanos-backup/ 2>/dev/null || true
cp -r ~/.config/hyprlock ~/.config/volkanos-backup/ 2>/dev/null || true
cp -r ~/.config/vibe ~/.config/volkanos-backup/ 2>/dev/null || true
```

### 3. Install individual components

```bash
cp -r cava ~/.config/
cp -r fuzzel ~/.config/
cp -r kitty ~/.config/
cp -r vibe ~/.config/
cp -r waybar ~/.config/
cp -r fastfetch ~/.config/
```

For the root Hyprland files, review and merge them into your existing setup rather than blindly replacing your configuration:

```bash
cp hyprland.conf ~/.config/hypr/
cp hyprland.lua ~/.config/hypr/
cp hyprlock.conf ~/.config/hypr/
cp monitors.conf ~/.config/hypr/
```

> **Important:** These configs are hardware- and setup-dependent. Review monitor names, input settings, paths, keybinds, and installed programs before using them.

## 📦 Dependencies

### Core

- Arch Linux
- Hyprland
- Waybar
- Kitty
- Fuzzel
- Hyprlock
- Fastfetch

### Optional

- Cava
- Vibe
- btop
- Thunar

Install only what you need with your preferred Arch Linux package manager.

## ⚠️ Disclaimer

Volkanos is a **personal rice, not a universal installer**. Some settings are specific to the author's hardware and workflow.

Always back up your existing configuration before replacing files.

## 🤝 Contributing

Volkanos is an open-source learning project. Bug reports, suggestions, and improvements are welcome.

See [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.

## 📸 Screenshots

The screenshot above shows the current Volkanos setup. More screenshots and configuration updates may be added as the project evolves.

---

**Made while learning Linux, Hyprland, and GitHub.**
