# Backup and Recovery

Volkanos is configuration, so recovery should be easy and predictable.

## Before installing

Keep a copy of the current configuration:

```bash
mkdir -p ~/.config/volkanos-backup
cp -a ~/.config/hypr ~/.config/volkanos-backup/ 2>/dev/null || true
cp -a ~/.config/kitty ~/.config/volkanos-backup/ 2>/dev/null || true
cp -a ~/.config/waybar ~/.config/volkanos-backup/ 2>/dev/null || true
```

The automatic installer stores timestamped backups under `~/.local/share/volkanos/backups`.

## Recovery

1. Stop or reload the affected application.
2. Identify the backup directory from the installation time.
3. Restore only the component that needs recovery.
4. Reload the application and verify it.

Avoid restoring the entire `.config` directory when only one component is broken.