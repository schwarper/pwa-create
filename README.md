# pwa-create

**pwa-create** is a Linux tool for installing web apps as native desktop applications (PWAs). Supports both a graphical interface and a command-line interface.

---

<p align="center">
  <img width="392" alt="Install GUI" src="https://github.com/user-attachments/assets/7fd91698-4d63-4892-8601-57713c886057" />
  &nbsp;&nbsp;
  <img width="729" alt="Remove PWA" src="https://github.com/user-attachments/assets/7672d0ff-afd2-4198-a6e6-b2f6fe08b0d7" />
</p>

## Features

- **GUI & CLI** — Install PWAs from a clean GUI or directly from the terminal
- **Auto icon fetching** — Automatically downloads and sets the app icon from the site's manifest
- **Multi-browser support** — Works with Chromium-based browsers and Firefox-based browsers
- **Flatpak & Snap** — Detects and supports browser installations via Flatpak and Snap
- **Auto dependency install** — Installs missing dependencies (`tk`, `pillow`, `xdg-utils`) during setup
---

## Installation

### Method 1 — Automatic (recommended)

```bash
curl -fsSL https://raw.githubusercontent.com/schwarper/pwa-create/main/install.sh | bash
```

### Method 2 — Manual

```bash
git clone https://github.com/schwarper/pwa-create.git
cd pwa-create
make install
```

After installation, run `pwa-create` — it will guide you through browser setup on first launch.

---

## Usage

### GUI

```bash
pwa-create
```

### Quick Install (CLI)

```bash
pwa-create WhatsApp https://web.whatsapp.com
pwa-create "YouTube" https://youtube.com
```

### List Installed PWAs

```bash
pwa-create --list
```

### Remove a PWA

```bash
pwa-create --remove              # GUI picker
pwa-create --remove whatsapp     # by ID
```

### Configure Browser

```bash
pwa-create --setup
```

### Uninstall pwa-create

```bash
pwa-create --uninstall
```

---

## Browser Support

| Browser | Installation Method |
|---|---|
| Chrome, Chromium, Brave, Edge, Vivaldi, Opera | `.desktop` file with `--app=` flag |
| Chrome, Brave, Edge (Flatpak) | `flatpak run ... --app=` |
| Firefox, LibreWolf, Waterfox, Floorp, Zen | [PWAsForFirefox](https://github.com/filips123/PWAsForFirefox) |

> **Firefox users:** `firefoxpwa` is required. pwa-create can install it automatically when you run `--setup`.

---

## Requirements

| Dependency | Purpose |
|---|---|
| Python 3.10+ | Runtime |
| `xdg-utils` | Browser detection |
| `tk` (tkinter) | GUI |
| `python-pillow` | Icon preview in GUI |
| `firefoxpwa` | Firefox-based browsers only |

## License

MIT
