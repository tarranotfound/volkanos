# Performance Notes

Volkanos is designed around a lightweight desktop workflow rather than heavy visual effects.

## Principles

- Prefer thin borders over expensive effects.
- Keep animations limited and purposeful.
- Avoid running duplicate status bars or daemons.
- Use low-power visualizer settings when possible.
- Keep background services explicit.
- Prefer simple shell scripts over continuously running helpers.

## Measuring changes

Before and after a visual change, compare memory and CPU usage with `btop` or standard tools such as:

```bash
free -h
ps -eo pid,comm,%cpu,%mem --sort=-%mem | head
```

Aesthetic changes should not quietly introduce a large always-running process.