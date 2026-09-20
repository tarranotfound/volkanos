# Configuration Principles

Volkanos follows a few rules to keep the repository maintainable.

### Separate concerns

Window-manager behavior should stay separate from application themes and visualizer settings.

### Prefer readable configuration

A slightly longer configuration is preferable when it makes behavior obvious to someone learning Linux.

### Avoid hidden dependencies

Commands should point to files that exist in the repository or clearly document external requirements.

### Keep hardware assumptions visible

Machine-specific monitor, input, or device settings should be clearly identified instead of silently being treated as universal defaults.