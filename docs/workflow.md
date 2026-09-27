# Configuration Workflow

Volkanos evolves through small configuration changes that are tested on the target Wayland session.

A useful workflow is:

1. Change one component.
2. Reload or restart only that component.
3. Check the result on the target hardware.
4. Keep the change when it is useful and reproducible.
5. Record larger workflow changes in the repository documentation.

This keeps experimental desktop changes easier to understand and recover later.
