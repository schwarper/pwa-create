strings = {
    "browser_detected":          "Detected browser: {name} ({family})",
    "browser_confirm_prompt":    "Is this correct? [Y/n]: ",
    "browser_not_detected":      "Could not detect your browser automatically.",
    "browser_select_prompt":     "Which browser engine are you using?",
    "browser_chromium_group":    "Chromium  (Chrome, Brave, Edge, Vivaldi, Opera...)",
    "browser_firefox_group":     "Firefox   (Firefox, LibreWolf, Waterfox, Zen...)",
    "browser_engine_prompt":     "Select [1/2]: ",
    "browser_pick_prompt":       "Select browser [number]: ",
    "browser_invalid_choice":    "Invalid choice, please try again.",

    "setup_saved":               "==> Saved: {name} ({family})",
    "first_run_setup":           "Welcome to pwa-create! Let's set up your browser first.",

    "fetching_icon":             "Fetching icon...",
    "icon_not_found":            "not found, using default.",
    "icon_error":                "error ({e}), using default.",

    "no_browser":                "Could not detect default browser.\nMake sure xdg-utils is installed.",
    "error_prefix":              "ERROR",
    "unsupported_browser":       "'{name}' is not supported.\nSupported: Chrome, Chromium, Brave, Edge, Vivaldi, Firefox, LibreWolf.",

    "firefoxpwa_missing":        "firefoxpwa not found. Required for Firefox-based browsers.",
    "firefoxpwa_not_in_path":    "firefoxpwa binary not found in PATH. Is it installed?",
    "firefoxpwa_still_missing":  "firefoxpwa still not found. Restart your terminal and try again.",
    "firefoxpwa_installed":      "firefoxpwa installed!",
    "firefoxpwa_error":          "firefoxpwa error:\n{err}",
    "firefoxpwa_instructions":   (
        "PWAsForFirefox is required for Firefox-based browsers.\n\n"
        "Install:\n"
        "  • .deb (Ubuntu/Debian): https://github.com/filips123/PWAsForFirefox/releases\n"
        "  • .rpm (Fedora):        https://github.com/filips123/PWAsForFirefox/releases\n"
        "  • Cargo (Rust):         cargo install firefoxpwa\n\n"
        "You may also need the Firefox extension:\n"
        "  https://addons.mozilla.org/firefox/addon/pwas-for-firefox/"
    ),
    "flatpak_warning":           "PWAsForFirefox may not work with Flatpak Firefox.",

    "runtime_missing":           "firefoxpwa runtime is not installed.",
    "runtime_installing":        "Installing firefoxpwa runtime (this may take a while)...",
    "runtime_installed":         "Runtime installed.",
    "runtime_failed":            "Runtime install failed.",
    "runtime_timeout":           "Operation timed out.",

    "install_auto_prompt":       "Install automatically? [y/n]: ",
    "install_auto_yes":          ("y", "yes"),

    "distro_detected":           "Detected distro family: {distro}",
    "aur_installing":            "Installing from AUR: {cmd}",
    "aur_no_helper":             "No AUR helper found (paru/yay). Install manually:\n  yay -S firefox-pwa",
    "aur_failed":                "AUR install failed.",
    "pkg_not_found":             "{ext} package not found.",
    "downloading":               "Downloading: {url}",
    "pkg_install_failed":        "Package install failed.",
    "auto_install_failed":       "Auto-install failed: {e}",
    "distro_unknown_install":    (
        "Could not detect distro.\n"
        "Manual install: https://github.com/filips423/PWAsForFirefox/releases\n"
        "  or: cargo install firefoxpwa"
    ),

    "pwa_installed":             "✓ '{name}' installed!\n  File: {file}",
    "pwa_installed_firefox":     "✓ '{name}' installed as Firefox PWA!\n{output}",
    "pwa_removed":               "✓ '{name}' removed.",
    "pwa_removed_no_id":         (
        "✓ '{name}' removed from records.\n"
        "  No site ID found — remove manually if needed: firefoxpwa site uninstall <ID>"
    ),
    "desktop_file_failed":       "Failed to create desktop file: {e}",
    "file_delete_failed":        "Failed to delete file: {e}",
    "no_pwas":                   "No installed PWAs found.",
    "not_found":                 "'{id}' not found.",

    "install_success_title":     "Install Successful",
    "install_fail_title":        "Install Failed",
    "removed_title":             "PWA Removed",
    "error_title":               "Error",
    "confirm_title":             "Confirm",
    "missing_info_title":        "Missing Info",
    "remove_pwa_title":          "Remove PWA",

    "confirm_remove":            "Remove '{name}'?",
    "missing_info_body":         "App name and URL are required.",

    "uninstall_confirm_prompt":  "Are you sure you want to uninstall pwa-create? [y/N]: ",
    "uninstall_data_prompt":     "Also remove config and all PWA data? [y/N]: ",
    "uninstall_data_removed":    "  Config and data removed.",
    "uninstall_success":         "==> pwa-create uninstalled.",
    "uninstall_cancelled":       "Uninstall cancelled.",

    "ui_install_title":          "Install PWA",
    "ui_install_subtitle":       "Add a web app to your desktop",
    "ui_field_name":             "App Name",
    "ui_field_url":              "URL",
    "ui_field_icon":             "Icon  ·  leave empty to fetch automatically",
    "ui_icon_pick":              "Select icon",
    "ui_btn_browse":             "Browse",
    "ui_btn_refresh":            "🔄 Refresh icon",
    "ui_btn_install":            "Install  →",
    "ui_btn_cancel":             "Cancel",
    "ui_btn_ok":                 "OK",
    "ui_btn_yes":                "Yes",
    "ui_btn_no":                 "No",
    "ui_btn_remove":             "Remove",
    "ui_remove_title":           "🗑  Remove PWA",
    "ui_remove_subtitle":        "Select the app you want to remove",
    "ui_col_name":               "Name",
    "ui_col_browser":            "Browser",
}