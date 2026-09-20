 # Volkanos Quick Start

A short path from a fresh Arch install to a working Volkanos session.

## 1. Clone

```bash
git clone https://github.com/tarranotfound/volkanos.git
cd volkanos
```

## 2. Inspect before installing

Review the files for your window manager and check package availability.

```bash
bash scripts/volkanos-setup-dry-run
```

## 3. Install selected components

```bash
bash scripts/volkanos-setup
```

The installer creates a timestamped backup before deployment.

## 4. Verify

Restart or reload the affected applications, then check the terminal, launcher, bar, lock screen, and window manager one at a time.

## 5. Hardware-specific checks

Review monitor names, input devices, paths, and installed fonts before copying personal settings to another machine.