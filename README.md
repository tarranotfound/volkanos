# VOLKANOS

> **A sharp, minimal Hyprland rice for Arch Linux.**
>
> Red accents, cozy sage tones, and a clean terminal-focused setup.

![Volkanos](2026-09-06_14-44-22.png)

## ✦ About

**Volkanos** is my personal Linux rice and one of my first open-source projects.

The goal is simple: keep the desktop **minimal, sharp, lightweight, and comfortable to use** without relying on heavy visual effects.

Built around:

- Hyprland
- Kitty
- Waybar
- Fuzzel
- Hyprlock
- Fastfetch
- Cava
- btop
- Vibe
- Thunar

> This project is still evolving. Configs may change as I experiment with my setup.

## 🎨 Style

- Dark and minimal
- Sharp red accents
- Sage green details
- Thin borders
- No unnecessary glassmorphism
- Terminal-focused workflow
- Lightweight configuration for everyday use

## 📁 Structure

```text
volkanos/
├── cava/          # Cava visualizer config
├── fuzzel/        # Application launcher
├── hyprland/      # Hyprland configuration
├── hyprlock/      # Lock screen configuration
├── kitty/         # Terminal configuration
├── vibe/          # Vibe configuration
├── waybar/        # Status bar
├── fastfetch/     # System information
└── README.md
```

## ⚡ Installation

### 1. Clone the repository

```bash
git clone https://github.com/tarranotfound/volkanos.git
cd volkanos
```

### 2. Back up your existing configs

It is recommended to back up your current configuration before installing.

```bash
mkdir -p ~/.config/volkanos-backup
cp -r ~/.config/hypr ~/.config/volkanos-backup/ 2>/dev/null || true
cp -r ~/.config/kitty ~/.config/volkanos-backup/ 2>/dev/null || true
cp -r ~/.config/fuzzel ~/.config/volkanos-backup/ 2>/dev/null || true
cp -r ~/.config/waybar ~/.config/volkanos-backup/ 2>/dev/null || true
```

### 3. Install the configs

Copy only the directories you want to use:

```bash
cp -r cava ~/.config/
cp -r fuzzel ~/.config/
cp -r kitty ~/.config/
cp -r vibe ~/.config/
cp -r waybar ~/.config/
cp -r fastfetch ~/.config/
cp -r hyprland ~/.config/
cp -r hyprlock ~/.config/
```

> **Tip:** You don't have to install everything. Pick the configs that fit your setup.

## 📦 Dependencies

### Required / core

- [Hyprland](https://hyprland.org/)
- [Waybar](https://github.com/Alexays/Waybar)
- [Kitty](https://sw.kovidgoyal.net/kitty/)
- [Fuzzel](https://codeberg.org/dnkl/fuzzel)
- [Hyprlock](https://github.com/hyprwm/hyprlock)
- [Fastfetch](https://github.com/fastfetch-cli/fastfetch)

### Optional

- Cava — audio visualizer
- btop — system monitor
- Vibe — visual/background component
- Thunar — file manager

Install the packages you need with your preferred Arch Linux package manager.

## 🖥️ Recommended Setup

Volkanos is designed around **Arch Linux + Hyprland**, but most of the individual configs can be adapted to other setups.

Before using the Hyprland configuration, make sure your monitor, input devices, keybinds, and hardware-specific settings match your system.

## ⚠️ Notes

This is a personal rice, not a universal installer. Some paths, keybinds, dependencies, and settings may need to be adjusted for your machine.

**Back up your configs before replacing them.**

## ⭐ Credits & Inspiration

Shoutout to:

- [termflix](https://github.com/termflix) — terminal visualizer inspiration
- [snglrtty](https://github.com/the-unknown/snglrtty) — audio visualizer
- The Hyprland community — inspiration and documentation

## 📸 Screenshots

The screenshot above shows the Volkanos setup in action.

More screenshots and configuration updates will be added as the project grows.

## 🤝 Feedback

Volkanos is an open-source learning project. **Criticism, suggestions, and improvements are welcome.**

If you like the project, consider giving it a ⭐ on GitHub.

---

**Made while learning Linux, Hyprland, and GitHub.**
