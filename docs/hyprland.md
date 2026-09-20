# Hyprland

Hyprland is the primary window-manager configuration in Volkanos.

## Main files

- `hyprland.conf` — main configuration
- `hyprland.lua` — Lua-based configuration used by the setup
- `monitors.conf` — optional monitor definitions
- `workspaces.conf` — workspace behavior
- `hyprlock.conf` — lock screen configuration

## Portability

Do not copy monitor and input settings blindly. Device names and available outputs differ between systems.

## Reloading

After a safe configuration change, reload the compositor using the reload mechanism supported by the installed Hyprland version. If the session becomes unstable, return to the last known-good Git revision.