# Testing Checklist

Before considering a Volkanos change finished:

- [ ] Check `git diff` for unintended changes.
- [ ] Run the relevant configuration validation command.
- [ ] Start or reload the affected application.
- [ ] Verify keyboard shortcuts that were changed.
- [ ] Check monitor and input behavior after WM changes.
- [ ] Confirm the configuration does not depend on an undeclared local path.
- [ ] Test the fallback or previous configuration if the change is risky.

For documentation-only changes, verify Markdown formatting and referenced paths.