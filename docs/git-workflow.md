# Git Workflow

Volkanos is intentionally developed through small, understandable commits.

## Recommended flow

```bash
git status
git diff
git add <path>
git commit -m "Describe the change"
git log --oneline -5
```

Each commit should ideally represent one logical change. Examples include a theme adjustment, a documentation improvement, or a single configuration fix.

## Before pushing

Review the diff and make sure personal secrets, machine-specific dumps, backups, and temporary files are not tracked.

```bash
git status --short
git diff --cached
```

Small commits make it easier to understand why a configuration changed and to revert a problematic experiment.