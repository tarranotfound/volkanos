# Volkanos Setup

Volkanos Setup is a terminal-based installer for selected desktop components used by the rice.

## Main installer

Run it from the repository root:

```bash
chmod +x scripts/volkanos-setup
./scripts/volkanos-setup
```

The installer lets you:

- select packages through a `gum` menu;
- review the selected packages;
- check package availability with `pacman`;
- back up existing configuration directories;
- install selected packages with `pacman`;
- optionally deploy matching Volkanos configuration files.

The installer must not be run as root. It may ask for `sudo` when installing packages.

## Dry run

To inspect the local environment without installing packages or copying configuration files:

```bash
chmod +x scripts/volkanos-setup-dry-run
./scripts/volkanos-setup-dry-run
```

The dry run checks required commands and reports which configuration paths exist in the checkout.

## Notes

- Run the scripts from a cloned Volkanos repository.
- Review the selected components before confirming installation.
- A missing configuration directory is skipped rather than fabricated.
- The setup scripts currently target Arch Linux and use `pacman`.
