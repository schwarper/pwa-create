strings = {
    "browser_detected":          "Browser rilevato: {name} ({family})",
    "browser_confirm_prompt":    "È corretto? [S/n]: ",
    "browser_not_detected":      "Impossibile rilevare il browser automaticamente.",
    "browser_select_prompt":     "Quale motore di browser stai utilizzando?",
    "browser_chromium_group":    "Chromium  (Chrome, Brave, Edge, Vivaldi, Opera...)",
    "browser_firefox_group":     "Firefox   (Firefox, LibreWolf, Waterfox, Zen...)",
    "browser_engine_prompt":     "Selezione [1/2]: ",
    "browser_pick_prompt":       "Seleziona browser [numero]: ",
    "browser_invalid_choice":    "Scelta non valida, riprova.",

    "setup_saved":               "==> Salvato: {name} ({family})",
    "first_run_setup":           "Benvenuto in pwa-create! Configuriamo prima il tuo browser.",

    "fetching_icon":             "Recupero icona...",
    "icon_not_found":            "non trovata, verrà usata l'icona predefinita.",
    "icon_error":                "errore ({e}), verrà usata l'icona predefinita.",

    "no_browser":                "Impossibile rilevare il browser predefinito.\nAssicurati che xdg-utils sia installato.",
    "error_prefix":              "ERRORE",
    "unsupported_browser":       "'{name}' non è supportato.\nSupportati: Chrome, Chromium, Brave, Edge, Vivaldi, Firefox, LibreWolf.",

    "firefoxpwa_missing":        "firefoxpwa non trovato. Necessario per i browser basati su Firefox.",
    "firefoxpwa_not_in_path":    "Il binario firefoxpwa non è nel PATH. È installato?",
    "firefoxpwa_still_missing":  "firefoxpwa ancora non trovato. Riavvia il terminale e riprova.",
    "firefoxpwa_installed":      "firefoxpwa installato!",
    "firefoxpwa_error":          "Errore firefoxpwa:\n{err}",
    "firefoxpwa_instructions":   (
        "PWAsForFirefox è necessario per i browser basati su Firefox.\n\n"
        "Installazione:\n"
        "  • .deb (Ubuntu/Debian): https://github.com/filips123/PWAsForFirefox/releases\n"
        "  • .rpm (Fedora):        https://github.com/filips123/PWAsForFirefox/releases\n"
        "  • Cargo (Rust):         cargo install firefoxpwa\n\n"
        "Potrebbe essere necessaria anche l'estensione Firefox:\n"
        "  https://addons.mozilla.org/firefox/addon/pwas-for-firefox/"
    ),
    "flatpak_warning":           "PWAsForFirefox potrebbe non funzionare con Firefox Flatpak.",

    "runtime_missing":           "Il runtime di firefoxpwa non è installato.",
    "runtime_installing":        "Installazione del runtime firefoxpwa (potrebbe richiedere del tempo)...",
    "runtime_installed":         "Runtime installato.",
    "runtime_failed":            "Installazione del runtime fallita.",
    "runtime_timeout":           "Operazione scaduta.",

    "install_auto_prompt":       "Installare automaticamente? [s/n]: ",
    "install_auto_yes":          ("s", "si", "sì"),

    "distro_detected":           "Distribuzione rilevata: {distro}",
    "aur_installing":            "Installazione da AUR: {cmd}",
    "aur_no_helper":             "Nessun helper AUR trovato (paru/yay). Installa manualmente:\n  yay -S firefox-pwa",
    "aur_failed":                "Installazione AUR fallita.",
    "pkg_not_found":             "Pacchetto {ext} non trovato.",
    "downloading":               "Download: {url}",
    "pkg_install_failed":        "Installazione del pacchetto fallita.",
    "auto_install_failed":       "Installazione automatica fallita: {e}",
    "distro_unknown_install":    (
        "Distribuzione non rilevata.\n"
        "Installazione manuale: https://github.com/filips423/PWAsForFirefox/releases\n"
        "  oppure: cargo install firefoxpwa"
    ),

    "pwa_installed":             "✓ '{name}' installato!\n  File: {file}",
    "pwa_installed_firefox":     "✓ '{name}' installato come PWA Firefox!\n{output}",
    "pwa_removed":               "✓ '{name}' rimosso.",
    "pwa_removed_no_id":         (
        "✓ '{name}' rimosso dai record.\n"
        "  Nessun ID sito trovato — rimuovi manualmente se necessario: firefoxpwa site uninstall <ID>"
    ),
    "desktop_file_failed":       "Creazione del file desktop fallita: {e}",
    "file_delete_failed":        "Eliminazione del file fallita: {e}",
    "no_pwas":                   "Nessuna PWA installata.",
    "not_found":                 "'{id}' non trovato.",

    "install_success_title":     "Installazione riuscita",
    "install_fail_title":        "Installazione fallita",
    "removed_title":             "PWA rimossa",
    "error_title":               "Errore",
    "confirm_title":             "Conferma",
    "missing_info_title":        "Informazioni mancanti",
    "remove_pwa_title":          "Rimuovi PWA",

    "confirm_remove":            "Rimuovere '{name}'?",
    "missing_info_body":         "Il nome dell'app e l'URL sono obbligatori.",

    "uninstall_confirm_prompt":  "Sei sicuro di voler disinstallare pwa-create? [s/N]: ",
    "uninstall_data_prompt":     "Rimuovere anche la configurazione e tutti i dati PWA? [s/N]: ",
    "uninstall_data_removed":    "  Configurazione e dati rimossi.",
    "uninstall_success":         "==> pwa-create disinstallato.",
    "uninstall_cancelled":       "Disinstallazione annullata.",

    "ui_install_title":          "Installa PWA",
    "ui_install_subtitle":       "Aggiungi un'app web al desktop",
    "ui_field_name":             "Nome app",
    "ui_field_url":              "URL",
    "ui_field_icon":             "Icona  ·  lascia vuoto per recuperarla automaticamente",
    "ui_icon_pick":              "Seleziona icona",
    "ui_btn_browse":             "Sfoglia",
    "ui_btn_refresh":            "🔄 Aggiorna icona",
    "ui_btn_install":            "Installa  →",
    "ui_btn_cancel":             "Annulla",
    "ui_btn_ok":                 "OK",
    "ui_btn_yes":                "Sì",
    "ui_btn_no":                 "No",
    "ui_btn_remove":             "Rimuovi",
    "ui_remove_title":           "🗑  Rimuovi PWA",
    "ui_remove_subtitle":        "Seleziona l'app da rimuovere",
    "ui_col_name":               "Nome",
    "ui_col_browser":            "Browser",
}
