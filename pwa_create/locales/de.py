strings = {
    "browser_detected":          "Erkannter Browser: {name} ({family})",
    "browser_confirm_prompt":    "Ist das korrekt? [J/n]: ",
    "browser_not_detected":      "Browser konnte nicht automatisch erkannt werden.",
    "browser_select_prompt":     "Welche Browser-Engine verwendest du?",
    "browser_chromium_group":    "Chromium  (Chrome, Brave, Edge, Vivaldi, Opera...)",
    "browser_firefox_group":     "Firefox   (Firefox, LibreWolf, Waterfox, Zen...)",
    "browser_engine_prompt":     "Auswahl [1/2]: ",
    "browser_pick_prompt":       "Browser auswählen [Nummer]: ",
    "browser_invalid_choice":    "Ungültige Auswahl, bitte erneut versuchen.",

    "setup_saved":               "==> Gespeichert: {name} ({family})",
    "first_run_setup":           "Willkommen bei pwa-create! Richten wir zuerst deinen Browser ein.",

    "fetching_icon":             "Symbol wird abgerufen...",
    "icon_not_found":            "nicht gefunden, Standardsymbol wird verwendet.",
    "icon_error":                "Fehler ({e}), Standardsymbol wird verwendet.",

    "no_browser":                "Standardbrowser konnte nicht erkannt werden.\nBitte stelle sicher, dass xdg-utils installiert ist.",
    "error_prefix":              "FEHLER",
    "unsupported_browser":       "'{name}' wird nicht unterstützt.\nUnterstützt: Chrome, Chromium, Brave, Edge, Vivaldi, Firefox, LibreWolf.",

    "firefoxpwa_missing":        "firefoxpwa nicht gefunden. Für Firefox-basierte Browser erforderlich.",
    "firefoxpwa_not_in_path":    "firefoxpwa nicht im PATH gefunden. Ist es installiert?",
    "firefoxpwa_still_missing":  "firefoxpwa immer noch nicht gefunden. Terminal neu starten und erneut versuchen.",
    "firefoxpwa_installed":      "firefoxpwa installiert!",
    "firefoxpwa_error":          "firefoxpwa-Fehler:\n{err}",
    "firefoxpwa_instructions":   (
        "PWAsForFirefox ist für Firefox-basierte Browser erforderlich.\n\n"
        "Installation:\n"
        "  • .deb (Ubuntu/Debian): https://github.com/filips123/PWAsForFirefox/releases\n"
        "  • .rpm (Fedora):        https://github.com/filips123/PWAsForFirefox/releases\n"
        "  • Cargo (Rust):         cargo install firefoxpwa\n\n"
        "Möglicherweise wird auch die Firefox-Erweiterung benötigt:\n"
        "  https://addons.mozilla.org/firefox/addon/pwas-for-firefox/"
    ),
    "flatpak_warning":           "PWAsForFirefox funktioniert möglicherweise nicht mit Flatpak-Firefox.",

    "runtime_missing":           "firefoxpwa-Laufzeitumgebung ist nicht installiert.",
    "runtime_installing":        "firefoxpwa-Laufzeitumgebung wird installiert (dies kann eine Weile dauern)...",
    "runtime_installed":         "Laufzeitumgebung installiert.",
    "runtime_failed":            "Installation der Laufzeitumgebung fehlgeschlagen.",
    "runtime_timeout":           "Zeitüberschreitung bei der Operation.",

    "install_auto_prompt":       "Automatisch installieren? [j/n]: ",
    "install_auto_yes":          ("j", "ja"),

    "distro_detected":           "Erkannte Distribution: {distro}",
    "aur_installing":            "Installation aus AUR: {cmd}",
    "aur_no_helper":             "Kein AUR-Helfer gefunden (paru/yay). Manuell installieren:\n  yay -S firefox-pwa",
    "aur_failed":                "AUR-Installation fehlgeschlagen.",
    "pkg_not_found":             "{ext}-Paket nicht gefunden.",
    "downloading":               "Herunterladen: {url}",
    "pkg_install_failed":        "Paketinstallation fehlgeschlagen.",
    "auto_install_failed":       "Automatische Installation fehlgeschlagen: {e}",
    "distro_unknown_install":    (
        "Distribution konnte nicht erkannt werden.\n"
        "Manuelle Installation: https://github.com/filips423/PWAsForFirefox/releases\n"
        "  oder: cargo install firefoxpwa"
    ),

    "pwa_installed":             "✓ '{name}' installiert!\n  Datei: {file}",
    "pwa_installed_firefox":     "✓ '{name}' als Firefox-PWA installiert!\n{output}",
    "pwa_removed":               "✓ '{name}' entfernt.",
    "pwa_removed_no_id":         (
        "✓ '{name}' aus den Einträgen entfernt.\n"
        "  Keine Website-ID gefunden — bei Bedarf manuell entfernen: firefoxpwa site uninstall <ID>"
    ),
    "desktop_file_failed":       "Desktop-Datei konnte nicht erstellt werden: {e}",
    "file_delete_failed":        "Datei konnte nicht gelöscht werden: {e}",
    "no_pwas":                   "Keine installierten PWAs gefunden.",
    "not_found":                 "'{id}' nicht gefunden.",

    "install_success_title":     "Installation erfolgreich",
    "install_fail_title":        "Installation fehlgeschlagen",
    "removed_title":             "PWA entfernt",
    "error_title":               "Fehler",
    "confirm_title":             "Bestätigen",
    "missing_info_title":        "Fehlende Angaben",
    "remove_pwa_title":          "PWA entfernen",

    "confirm_remove":            "'{name}' entfernen?",
    "missing_info_body":         "App-Name und URL sind erforderlich.",

    "uninstall_confirm_prompt":  "pwa-create wirklich deinstallieren? [j/N]: ",
    "uninstall_data_prompt":     "Konfiguration und alle PWA-Daten ebenfalls entfernen? [j/N]: ",
    "uninstall_data_removed":    "  Konfiguration und Daten entfernt.",
    "uninstall_success":         "==> pwa-create deinstalliert.",
    "uninstall_cancelled":       "Deinstallation abgebrochen.",

    "ui_install_title":          "PWA installieren",
    "ui_install_subtitle":       "Web-App zum Desktop hinzufügen",
    "ui_field_name":             "App-Name",
    "ui_field_url":              "URL",
    "ui_field_icon":             "Symbol  ·  leer lassen für automatischen Abruf",
    "ui_icon_pick":              "Symbol auswählen",
    "ui_btn_browse":             "Durchsuchen",
    "ui_btn_refresh":            "🔄 Symbol aktualisieren",
    "ui_btn_install":            "Installieren  →",
    "ui_btn_cancel":             "Abbrechen",
    "ui_btn_ok":                 "OK",
    "ui_btn_yes":                "Ja",
    "ui_btn_no":                 "Nein",
    "ui_btn_remove":             "Entfernen",
    "ui_remove_title":           "🗑  PWA entfernen",
    "ui_remove_subtitle":        "App auswählen, die entfernt werden soll",
    "ui_col_name":               "Name",
    "ui_col_browser":            "Browser",
}
