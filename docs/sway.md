# Sway

Volkanos also provides a Sway-oriented configuration so the visual identity can be used without Hyprland-specific features.

## Portability rules

Sway uses i3-compatible configuration concepts, but Hyprland syntax cannot be copied directly into Sway.

When adapting components:

1. Keep application commands the same where possible.
2. Translate keybinds to Sway syntax.
3. Re-check output and input names.
4. Avoid assuming Hyprland-only IPC features.

The goal is a recognizable Volkanos workflow while keeping the configuration native to Sway.