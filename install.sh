#!/usr/bin/env bash
# pwa-create installer
# Usage: curl -fsSL https://raw.githubusercontent.com/schwarper/pwa-create/main/install.sh | bash
#    or: bash install.sh

set -euo pipefail

REPO_URL="https://github.com/schwarper/pwa-create"
INSTALL_DIR="$HOME/.local/share/pwa-create-src"
BIN_DIR="$HOME/.local/bin"
DESKTOP_DIR="$HOME/.local/share/applications"
ICON_DIR="$HOME/.local/share/icons/hicolor/512x512/apps"

RED='\033[0;31m'; GREEN='\033[0;32m'; YELLOW='\033[1;33m'; CYAN='\033[0;36m'; NC='\033[0m'

info()    { echo -e "${CYAN}ℹ  $*${NC}"; }
success() { echo -e "${GREEN}✓  $*${NC}"; }
warn()    { echo -e "${YELLOW}⚠  $*${NC}"; }
err()     { echo -e "${RED}✗  $*${NC}"; exit 1; }

echo ""
echo -e "${CYAN}╔══════════════════════════════╗${NC}"
echo -e "${CYAN}║      pwa-create installer    ║${NC}"
echo -e "${CYAN}╚══════════════════════════════╝${NC}"
echo ""

info "Checking Python..."
command -v python3 &>/dev/null || err "Python3 is required but not found."
python3 -c 'import sys; exit(0 if sys.version_info >= (3,10) else 1)' \
    || err "Python 3.10+ required."
PY_VER=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
success "Python $PY_VER"

command -v xdg-settings &>/dev/null \
    && success "xdg-utils" \
    || warn "xdg-settings not found — browser detection may not work (install xdg-utils)"

if python3 -c "import tkinter" 2>/dev/null; then
    success "tkinter"
else
    warn "tkinter not found — installing..."
    if   command -v pacman  &>/dev/null; then sudo pacman -S --noconfirm tk
    elif command -v apt-get &>/dev/null; then sudo apt-get install -y python3-tk
    elif command -v dnf     &>/dev/null; then sudo dnf install -y python3-tkinter
    elif command -v zypper  &>/dev/null; then sudo zypper install -y python3-tk
    else warn "Could not install tkinter. Please install python3-tk manually."; fi
    python3 -c "import tkinter" 2>/dev/null \
        && success "tkinter" \
        || warn "tkinter still not found — GUI may not work"
fi

if python3 -c "from PIL import Image" 2>/dev/null; then
    success "Pillow"
else
    warn "Pillow not found — installing..."
    if   command -v pacman  &>/dev/null; then sudo pacman -S --noconfirm python-pillow
    elif command -v apt-get &>/dev/null; then sudo apt-get install -y python3-pil python3-pil.imagetk
    elif command -v dnf     &>/dev/null; then sudo dnf install -y python3-pillow
    else warn "Could not install Pillow. Icon preview may not work."; fi
    python3 -c "from PIL import Image" 2>/dev/null \
        && success "Pillow" \
        || warn "Pillow still not found — icon preview may not work"
fi

success "Dependencies OK"

info "Downloading pwa-create..."
mkdir -p "$INSTALL_DIR" "$BIN_DIR" "$DESKTOP_DIR" "$ICON_DIR"

if command -v git &>/dev/null; then
    if [ -d "$INSTALL_DIR/.git" ]; then
        info "Updating existing installation..."
        git -C "$INSTALL_DIR" pull --ff-only
    else
        git clone --depth=1 "$REPO_URL" "$INSTALL_DIR"
    fi
elif command -v curl &>/dev/null; then
    TMP=$(mktemp -d)
    curl -fsSL "$REPO_URL/archive/refs/heads/main.tar.gz" -o "$TMP/src.tar.gz"
    tar -xzf "$TMP/src.tar.gz" -C "$TMP"
    cp -r "$TMP"/pwa-create-main/. "$INSTALL_DIR/"
    rm -rf "$TMP"
else
    err "git or curl is required but neither was found."
fi
success "Files: $INSTALL_DIR"

info "Installing pwa-create..."
printf '#!/usr/bin/env python3\nimport sys\nsys.path.insert(0, "%s")\nfrom pwa_create.main import main\nmain()\n' \
    "$INSTALL_DIR" > "$BIN_DIR/pwa-create"
chmod +x "$BIN_DIR/pwa-create"
success "Binary: $BIN_DIR/pwa-create"

cp "$INSTALL_DIR/pwa-create.desktop" "$DESKTOP_DIR/pwa-create.desktop"
chmod 644 "$DESKTOP_DIR/pwa-create.desktop"
cp "$INSTALL_DIR/pwa-create.png" "$ICON_DIR/pwa-create.png" 2>/dev/null || true
command -v update-desktop-database &>/dev/null \
    && update-desktop-database "$DESKTOP_DIR" 2>/dev/null || true
success ".desktop entry created"

echo ""
if [[ ":$PATH:" != *":$BIN_DIR:"* ]]; then
    SHELL_NAME=$(basename "$SHELL")
    warn "$BIN_DIR is not in PATH."
    if   [ "$SHELL_NAME" = "fish" ]; then echo "  Run: fish_add_path $BIN_DIR"
    elif [ "$SHELL_NAME" = "zsh"  ]; then echo "  Run: echo 'export PATH=\"$BIN_DIR:\$PATH\"' >> ~/.zshrc && source ~/.zshrc"
    else                                   echo "  Run: echo 'export PATH=\"$BIN_DIR:\$PATH\"' >> ~/.bashrc && source ~/.bashrc"
    fi
else
    success "$BIN_DIR is already in PATH"
fi

echo ""
echo -e "${GREEN}══════════════════════════════════════════${NC}"
echo -e "${GREEN}  pwa-create installed successfully!      ${NC}"
echo -e "${GREEN}══════════════════════════════════════════${NC}"
echo ""
echo "  First run:          pwa-create           (opens setup + GUI)"
echo "  Quick install:      pwa-create WhatsApp https://web.whatsapp.com"
echo "  Setup browser:      pwa-create --setup"
echo "  List:               pwa-create --list"
echo "  Remove PWA:         pwa-create --remove"
echo "  Uninstall:          pwa-create --uninstall"
echo ""