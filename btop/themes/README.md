# Volkanos btop Themes

This directory contains custom themes for **btop++**.

## Available themes

- `mono-red.theme` — a minimal dark theme using the Volkanos mono-red palette.

## Installation

Copy the theme into your local btop themes directory:

```bash
mkdir -p ~/.config/btop/themes
cp mono-red.theme ~/.config/btop/themes/
```

Then set the theme in `~/.config/btop/btop.conf`:

```ini
color_theme = "mono-red"
```

Restart btop to apply the theme.
