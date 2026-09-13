# Volkanos on Niri

Volkanos is a personal Arch Linux rice built around a dark, minimal style with thin borders, red accents, and low-resource visuals.

This directory contains the Niri version of Volkanos. It is separate from the Hyprland configuration so users can choose the window manager that fits their workflow.

## What is included

- Niri window-manager configuration
- Volkanos keybinds and window rules
- Startup commands for the optional Volkanos components
- Notes for adapting the configuration to different hardware

## Requirements

Install Niri and the applications you want to use. The configuration may reference optional programs such as Kitty, Fuzzel, Waybar, Hyprlock, btop, Cava, Fastfetch, and Vibe.

You do not need to install every component to use the Niri configuration. Review startup commands and keybinds before enabling them.

## Installation

### Automatic installation

From the repository root, run:

```bash
chmod +x niri/install.sh
./niri/install.sh
```

The installer creates `~/.config/niri` if needed, backs up an existing `config.kdl`, and copies the Volkanos configuration into place. If `startup.sh` is present, copy it to `~/.config/niri/startup.sh` as well.

To test the optional helper manually:

```bash
bash ~/.config/niri/startup.sh
```

The helper only starts commands that are installed. Review it before enabling it automatically.

### Manual installation

1. Back up your current Niri configuration.
2. Copy `config.kdl` to `~/.config/niri/config.kdl`.
3. Optionally copy `startup.sh` to `~/.config/niri/startup.sh`.
4. Review commands, monitor names, input settings, and application paths.
5. Reload Niri or log in again.

The configuration is a starting point, not a universal installer. Hardware, display names, installed applications, and Niri versions can require changes.

## Safety notes

- Review `config.kdl` before applying it to your daily setup.
- Check your monitor name with `niri msg outputs` and adjust the output section if needed.
- Make sure Kitty, Fuzzel, and other optional programs are installed before using their keybinds.
- Keep the generated backup until you confirm that the new configuration works.

## Philosophy

Volkanos on Niri aims to keep the visual identity consistent while respecting Niri's scrolling-column workflow. Hyprland-specific settings are not copied directly because Niri uses its own configuration syntax and behavior.
