# Niri

Niri is supported as a separate window-manager target rather than as a compatibility layer for Hyprland.

## Configuration principle

Keep Niri-specific behavior inside the Niri configuration directory. Shared application themes can remain independent of the compositor.

## Before switching

Check:

- monitor names
- keyboard and pointer settings
- launcher command
- status bar command
- screenshot bindings
- lock command

This keeps the Volkanos visual identity consistent while allowing each compositor to use its own native configuration.