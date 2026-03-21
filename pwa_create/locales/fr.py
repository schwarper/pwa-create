strings = {
    "browser_detected":          "Navigateur détecté : {name} ({family})",
    "browser_confirm_prompt":    "Est-ce correct ? [O/n] : ",
    "browser_not_detected":      "Impossible de détecter le navigateur automatiquement.",
    "browser_select_prompt":     "Quel moteur de navigateur utilisez-vous ?",
    "browser_chromium_group":    "Chromium  (Chrome, Brave, Edge, Vivaldi, Opera...)",
    "browser_firefox_group":     "Firefox   (Firefox, LibreWolf, Waterfox, Zen...)",
    "browser_engine_prompt":     "Sélection [1/2] : ",
    "browser_pick_prompt":       "Choisir le navigateur [numéro] : ",
    "browser_invalid_choice":    "Choix invalide, veuillez réessayer.",

    "setup_saved":               "==> Enregistré : {name} ({family})",
    "first_run_setup":           "Bienvenue dans pwa-create ! Configurons d'abord votre navigateur.",

    "fetching_icon":             "Récupération de l'icône...",
    "icon_not_found":            "introuvable, icône par défaut utilisée.",
    "icon_error":                "erreur ({e}), icône par défaut utilisée.",

    "no_browser":                "Impossible de détecter le navigateur par défaut.\nAssurez-vous que xdg-utils est installé.",
    "error_prefix":              "ERREUR",
    "unsupported_browser":       "'{name}' n'est pas pris en charge.\nPris en charge : Chrome, Chromium, Brave, Edge, Vivaldi, Firefox, LibreWolf.",

    "firefoxpwa_missing":        "firefoxpwa introuvable. Requis pour les navigateurs basés sur Firefox.",
    "firefoxpwa_not_in_path":    "Le binaire firefoxpwa est introuvable dans le PATH. Est-il installé ?",
    "firefoxpwa_still_missing":  "firefoxpwa toujours introuvable. Redémarrez le terminal et réessayez.",
    "firefoxpwa_installed":      "firefoxpwa installé !",
    "firefoxpwa_error":          "Erreur firefoxpwa :\n{err}",
    "firefoxpwa_instructions":   (
        "PWAsForFirefox est requis pour les navigateurs basés sur Firefox.\n\n"
        "Installation :\n"
        "  • .deb (Ubuntu/Debian) : https://github.com/filips123/PWAsForFirefox/releases\n"
        "  • .rpm (Fedora) :        https://github.com/filips123/PWAsForFirefox/releases\n"
        "  • Cargo (Rust) :         cargo install firefoxpwa\n\n"
        "L'extension Firefox peut également être nécessaire :\n"
        "  https://addons.mozilla.org/firefox/addon/pwas-for-firefox/"
    ),
    "flatpak_warning":           "PWAsForFirefox peut ne pas fonctionner avec Firefox Flatpak.",

    "runtime_missing":           "L'environnement d'exécution firefoxpwa n'est pas installé.",
    "runtime_installing":        "Installation de l'environnement d'exécution firefoxpwa (cela peut prendre un moment)...",
    "runtime_installed":         "Environnement d'exécution installé.",
    "runtime_failed":            "L'installation de l'environnement d'exécution a échoué.",
    "runtime_timeout":           "Délai d'attente dépassé.",

    "install_auto_prompt":       "Installer automatiquement ? [o/n] : ",
    "install_auto_yes":          ("o", "oui"),

    "distro_detected":           "Distribution détectée : {distro}",
    "aur_installing":            "Installation depuis AUR : {cmd}",
    "aur_no_helper":             "Aucun assistant AUR trouvé (paru/yay). Installation manuelle :\n  yay -S firefox-pwa",
    "aur_failed":                "Échec de l'installation AUR.",
    "pkg_not_found":             "Paquet {ext} introuvable.",
    "downloading":               "Téléchargement : {url}",
    "pkg_install_failed":        "Échec de l'installation du paquet.",
    "auto_install_failed":       "Échec de l'installation automatique : {e}",
    "distro_unknown_install":    (
        "Distribution non détectée.\n"
        "Installation manuelle : https://github.com/filips423/PWAsForFirefox/releases\n"
        "  ou : cargo install firefoxpwa"
    ),

    "pwa_installed":             "✓ '{name}' installé !\n  Fichier : {file}",
    "pwa_installed_firefox":     "✓ '{name}' installé comme PWA Firefox !\n{output}",
    "pwa_removed":               "✓ '{name}' supprimé.",
    "pwa_removed_no_id":         (
        "✓ '{name}' supprimé des enregistrements.\n"
        "  Aucun identifiant de site trouvé — supprimez manuellement si nécessaire : firefoxpwa site uninstall <ID>"
    ),
    "desktop_file_failed":       "Échec de la création du fichier desktop : {e}",
    "file_delete_failed":        "Échec de la suppression du fichier : {e}",
    "no_pwas":                   "Aucune PWA installée.",
    "not_found":                 "'{id}' introuvable.",

    "install_success_title":     "Installation réussie",
    "install_fail_title":        "Échec de l'installation",
    "removed_title":             "PWA supprimée",
    "error_title":               "Erreur",
    "confirm_title":             "Confirmer",
    "missing_info_title":        "Informations manquantes",
    "remove_pwa_title":          "Supprimer une PWA",

    "confirm_remove":            "Supprimer '{name}' ?",
    "missing_info_body":         "Le nom de l'application et l'URL sont requis.",

    "uninstall_confirm_prompt":  "Voulez-vous vraiment désinstaller pwa-create ? [o/N] : ",
    "uninstall_data_prompt":     "Supprimer également la configuration et toutes les données PWA ? [o/N] : ",
    "uninstall_data_removed":    "  Configuration et données supprimées.",
    "uninstall_success":         "==> pwa-create désinstallé.",
    "uninstall_cancelled":       "Désinstallation annulée.",

    "ui_install_title":          "Installer une PWA",
    "ui_install_subtitle":       "Ajouter une application web au bureau",
    "ui_field_name":             "Nom de l'application",
    "ui_field_url":              "URL",
    "ui_field_icon":             "Icône  ·  laisser vide pour récupérer automatiquement",
    "ui_icon_pick":              "Sélectionner une icône",
    "ui_btn_browse":             "Parcourir",
    "ui_btn_refresh":            "🔄 Actualiser l'icône",
    "ui_btn_install":            "Installer  →",
    "ui_btn_cancel":             "Annuler",
    "ui_btn_ok":                 "OK",
    "ui_btn_yes":                "Oui",
    "ui_btn_no":                 "Non",
    "ui_btn_remove":             "Supprimer",
    "ui_remove_title":           "🗑  Supprimer une PWA",
    "ui_remove_subtitle":        "Sélectionnez l'application à supprimer",
    "ui_col_name":               "Nom",
    "ui_col_browser":            "Navigateur",
}
