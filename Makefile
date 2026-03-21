PREFIX   ?= $(HOME)/.local
BIN      := $(PREFIX)/bin
APPS     := $(PREFIX)/share/applications
SRC_DEST := $(HOME)/.local/share/pwa-create-src

.PHONY: install uninstall _install_deps

install: _install_deps
	mkdir -p $(BIN) $(APPS) $(SRC_DEST) $(PREFIX)/share/icons/hicolor/512x512/apps
	cp -r pwa_create $(SRC_DEST)/
	cp -r pwa_create/locales $(SRC_DEST)/pwa_create/
	@printf '#!/usr/bin/env python3\nimport sys\nsys.path.insert(0, "%s")\nfrom pwa_create.main import main\nmain()\n' "$(SRC_DEST)" > $(BIN)/pwa-create
	chmod +x $(BIN)/pwa-create
	cp pwa-create.desktop $(APPS)/pwa-create.desktop
	cp pwa-create.png $(PREFIX)/share/icons/hicolor/512x512/apps/pwa-create.png
	chmod 644 $(APPS)/pwa-create.desktop
	@update-desktop-database $(APPS) 2>/dev/null || true
	@echo ""
	@echo "==> pwa-create installed!"
	@echo ""
	@echo "  pwa-create                           # Open GUI (runs setup on first launch)"
	@echo "  pwa-create Github https://...        # Quick install"
	@echo "  pwa-create --setup                   # Configure browser"
	@echo "  pwa-create --list                    # List installed PWAs"
	@echo "  pwa-create --remove                  # Remove a PWA"
	@echo "  pwa-create --uninstall               # Uninstall pwa-create"
	@echo ""
	@SHELL_NAME=$$(basename "$$SHELL"); \
	if echo "$$PATH" | grep -q "$(BIN)"; then \
		echo "  PATH already includes $(BIN)"; \
	elif [ "$$SHELL_NAME" = "fish" ]; then \
		echo "  Add to PATH: fish_add_path $(BIN)"; \
	elif [ "$$SHELL_NAME" = "zsh" ]; then \
		echo "  Add to PATH: echo 'export PATH=\"$(BIN):$$PATH\"' >> ~/.zshrc"; \
	else \
		echo "  Add to PATH: echo 'export PATH=\"$(BIN):$$PATH\"' >> ~/.bashrc"; \
	fi

_install_deps:
	@echo "==> Checking dependencies..."
	@python3 -c "import tkinter" 2>/dev/null && echo "  [✓] tkinter" || { \
		echo "  [!] Installing tkinter..."; \
		if   command -v pacman  >/dev/null 2>&1; then sudo pacman -S --noconfirm tk; \
		elif command -v apt-get >/dev/null 2>&1; then sudo apt-get install -y python3-tk; \
		elif command -v dnf     >/dev/null 2>&1; then sudo dnf install -y python3-tkinter; \
		elif command -v zypper  >/dev/null 2>&1; then sudo zypper install -y python3-tk; \
		else echo "  [!] Could not install tkinter. Please install python3-tk manually."; fi; \
	}
	@python3 -c "from PIL import Image" 2>/dev/null && echo "  [✓] Pillow" || { \
		echo "  [!] Installing Pillow..."; \
		if   command -v pacman  >/dev/null 2>&1; then sudo pacman -S --noconfirm python-pillow; \
		elif command -v apt-get >/dev/null 2>&1; then sudo apt-get install -y python3-pil python3-pil.imagetk; \
		elif command -v dnf     >/dev/null 2>&1; then sudo dnf install -y python3-pillow; \
		else echo "  [!] Could not install Pillow. Icon preview may not work."; fi; \
	}
	@command -v xdg-settings >/dev/null 2>&1 && echo "  [✓] xdg-utils" || { \
		echo "  [!] Installing xdg-utils..."; \
		if   command -v pacman  >/dev/null 2>&1; then sudo pacman -S --noconfirm xdg-utils; \
		elif command -v apt-get >/dev/null 2>&1; then sudo apt-get install -y xdg-utils; \
		elif command -v dnf     >/dev/null 2>&1; then sudo dnf install -y xdg-utils; \
		elif command -v zypper  >/dev/null 2>&1; then sudo zypper install -y xdg-utils; \
		else echo "  [!] Could not install xdg-utils. Browser detection may not work."; fi; \
	}
	@echo "==> Dependencies OK."

uninstall:
	rm -f $(BIN)/pwa-create
	rm -f $(APPS)/pwa-create.desktop
	rm -f $(PREFIX)/share/icons/hicolor/512x512/apps/pwa-create.png
	rm -rf $(SRC_DEST)
	@update-desktop-database $(APPS) 2>/dev/null || true
	@printf "Remove config and PWA data? [y/N]: "; \
	read ans; \
	if [ "$$ans" = "y" ] || [ "$$ans" = "Y" ]; then \
		rm -rf $(HOME)/.local/share/pwa-create; \
		echo "  Config and data removed."; \
	fi
	@echo "==> pwa-create uninstalled."