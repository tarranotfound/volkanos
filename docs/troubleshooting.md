# Troubleshooting

## Window manager does not start

Check the configuration before restarting the session. For Hyprland, inspect the config with the validation command available on your installed version.

## Waybar or launcher is missing

Check that the package is installed and that its configuration exists under `~/.config`.

## Fonts look wrong

Verify that the configured Nerd Font is installed and that the application is using the expected font family.

## Monitor settings fail

Monitor names vary between machines. Check the current output names and compare them with `monitors.conf` before copying the file.

## A config breaks after an update

Compare the changed configuration with the previous working version in Git:

```bash
git log --oneline --all
 git diff HEAD~1 -- <path>
```

Restore only the affected change instead of replacing the whole repository.