# Optional AUR packages

Volkanos Setup installs packages from the enabled official Arch Linux repositories.
Some systems may provide additional Volkanos-related tools through the AUR.

## Before installing from the AUR

- Use an AUR helper you trust, such as `paru` or `yay`.
- Review the PKGBUILD before building a package.
- Do not run AUR helpers as root.
- Keep official repository packages and AUR packages clearly separated.

## Optional package candidates

These are optional candidates, not required dependencies of Volkanos:

| Package | Purpose |
| --- | --- |
| `quickshell-git` | Development version of Quickshell, when the stable package is unavailable or unsuitable |
| `niri-git` | Development version of Niri, when a user specifically wants the latest AUR snapshot |

Package names and availability can change. Check the AUR before installing, and prefer the official repository package when it meets your needs.

## Manual installation examples

```bash
paru -S quickshell-git
paru -S niri-git
```

Or with `yay`:

```bash
yay -S quickshell-git
yay -S niri-git
```

The main `scripts/volkanos-setup` installer intentionally does not install AUR packages automatically. This keeps the default setup predictable and avoids running third-party build scripts without explicit user review.
