strings = {
    "browser_detected":          "Algılanan tarayıcı: {name} ({family})",
    "browser_confirm_prompt":    "Bu doğru mu? [E/h]: ",
    "browser_not_detected":      "Tarayıcı otomatik olarak algılanamadı.",
    "browser_select_prompt":     "Hangi tarayıcı motorunu kullanıyorsunuz?",
    "browser_chromium_group":    "Chromium  (Chrome, Brave, Edge, Vivaldi, Opera...)",
    "browser_firefox_group":     "Firefox   (Firefox, LibreWolf, Waterfox, Zen...)",
    "browser_engine_prompt":     "Seçim [1/2]: ",
    "browser_pick_prompt":       "Tarayıcı seçin [numara]: ",
    "browser_invalid_choice":    "Geçersiz seçim, lütfen tekrar deneyin.",

    "setup_saved":               "==> Kaydedildi: {name} ({family})",
    "first_run_setup":           "pwa-create'e hoş geldiniz! Önce tarayıcınızı ayarlayalım.",

    "fetching_icon":             "Simge alınıyor...",
    "icon_not_found":            "bulunamadı, varsayılan simge kullanılacak.",
    "icon_error":                "hata ({e}), varsayılan simge kullanılacak.",

    "no_browser":                "Varsayılan tarayıcı algılanamadı.\nxdg-utils'in kurulu olduğundan emin olun.",
    "error_prefix":              "HATA",
    "unsupported_browser":       "'{name}' desteklenmiyor.\nDesteklenenler: Chrome, Chromium, Brave, Edge, Vivaldi, Firefox, LibreWolf.",

    "firefoxpwa_missing":        "firefoxpwa bulunamadı. Firefox tabanlı tarayıcılar için gereklidir.",
    "firefoxpwa_not_in_path":    "firefoxpwa ikili dosyası PATH içinde bulunamadı. Kurulu mu?",
    "firefoxpwa_still_missing":  "firefoxpwa hâlâ bulunamadı. Terminali yeniden başlatın ve tekrar deneyin.",
    "firefoxpwa_installed":      "firefoxpwa kuruldu!",
    "firefoxpwa_error":          "firefoxpwa hatası:\n{err}",
    "firefoxpwa_instructions":   (
        "PWAsForFirefox, Firefox tabanlı tarayıcılar için gereklidir.\n\n"
        "Kurulum:\n"
        "  • .deb (Ubuntu/Debian): https://github.com/filips123/PWAsForFirefox/releases\n"
        "  • .rpm (Fedora):        https://github.com/filips123/PWAsForFirefox/releases\n"
        "  • Cargo (Rust):         cargo install firefoxpwa\n\n"
        "Firefox eklentisi de gerekebilir:\n"
        "  https://addons.mozilla.org/firefox/addon/pwas-for-firefox/"
    ),
    "flatpak_warning":           "PWAsForFirefox, Flatpak Firefox ile çalışmayabilir.",

    "runtime_missing":           "firefoxpwa çalışma zamanı kurulu değil.",
    "runtime_installing":        "firefoxpwa çalışma zamanı kuruluyor (bu biraz sürebilir)...",
    "runtime_installed":         "Çalışma zamanı kuruldu.",
    "runtime_failed":            "Çalışma zamanı kurulumu başarısız oldu.",
    "runtime_timeout":           "İşlem zaman aşımına uğradı.",

    "install_auto_prompt":       "Otomatik olarak kursun mu? [e/h]: ",
    "install_auto_yes":          ("e", "evet"),

    "distro_detected":           "Algılanan dağıtım ailesi: {distro}",
    "aur_installing":            "AUR'dan kuruluyor: {cmd}",
    "aur_no_helper":             "AUR yardımcısı bulunamadı (paru/yay). Manuel kurulum:\n  yay -S firefox-pwa",
    "aur_failed":                "AUR kurulumu başarısız oldu.",
    "pkg_not_found":             "{ext} paketi bulunamadı.",
    "downloading":               "İndiriliyor: {url}",
    "pkg_install_failed":        "Paket kurulumu başarısız oldu.",
    "auto_install_failed":       "Otomatik kurulum başarısız oldu: {e}",
    "distro_unknown_install":    (
        "Dağıtım algılanamadı.\n"
        "Manuel kurulum: https://github.com/filips423/PWAsForFirefox/releases\n"
        "  veya: cargo install firefoxpwa"
    ),

    "pwa_installed":             "✓ '{name}' kuruldu!\n  Dosya: {file}",
    "pwa_installed_firefox":     "✓ '{name}' Firefox PWA olarak kuruldu!\n{output}",
    "pwa_removed":               "✓ '{name}' kaldırıldı.",
    "pwa_removed_no_id":         (
        "✓ '{name}' kayıtlardan silindi.\n"
        "  Site kimliği bulunamadı — gerekirse manuel olarak kaldırın: firefoxpwa site uninstall <ID>"
    ),
    "desktop_file_failed":       "Masaüstü dosyası oluşturulamadı: {e}",
    "file_delete_failed":        "Dosya silinemedi: {e}",
    "no_pwas":                   "Kurulu PWA bulunamadı.",
    "not_found":                 "'{id}' bulunamadı.",

    "install_success_title":     "Kurulum Başarılı",
    "install_fail_title":        "Kurulum Başarısız",
    "removed_title":             "PWA Kaldırıldı",
    "error_title":               "Hata",
    "confirm_title":             "Onayla",
    "missing_info_title":        "Eksik Bilgi",
    "remove_pwa_title":          "PWA Kaldır",

    "confirm_remove":            "'{name}' kaldırılsın mı?",
    "missing_info_body":         "Uygulama adı ve URL gereklidir.",

    "uninstall_confirm_prompt":  "pwa-create'i kaldırmak istediğinizden emin misiniz? [e/H]: ",
    "uninstall_data_prompt":     "Yapılandırma ve tüm PWA verileri de silinsin mi? [e/H]: ",
    "uninstall_data_removed":    "  Yapılandırma ve veriler silindi.",
    "uninstall_success":         "==> pwa-create kaldırıldı.",
    "uninstall_cancelled":       "Kaldırma işlemi iptal edildi.",

    "ui_install_title":          "PWA Kur",
    "ui_install_subtitle":       "Masaüstüne web uygulaması ekle",
    "ui_field_name":             "Uygulama Adı",
    "ui_field_url":              "URL",
    "ui_field_icon":             "Simge  ·  otomatik almak için boş bırakın",
    "ui_icon_pick":              "Simge seçin",
    "ui_btn_browse":             "Gözat",
    "ui_btn_refresh":            "🔄 Simgeyi yenile",
    "ui_btn_install":            "Kur  →",
    "ui_btn_cancel":             "İptal",
    "ui_btn_ok":                 "Tamam",
    "ui_btn_yes":                "Evet",
    "ui_btn_no":                 "Hayır",
    "ui_btn_remove":             "Kaldır",
    "ui_remove_title":           "🗑  PWA Kaldır",
    "ui_remove_subtitle":        "Kaldırmak istediğiniz uygulamayı seçin",
    "ui_col_name":               "Ad",
    "ui_col_browser":            "Tarayıcı",
}
