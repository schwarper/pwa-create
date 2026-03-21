strings = {
    "browser_detected":          "Обнаруженный браузер: {name} ({family})",
    "browser_confirm_prompt":    "Это верно? [Д/н]: ",
    "browser_not_detected":      "Не удалось автоматически определить браузер.",
    "browser_select_prompt":     "Какой движок браузера вы используете?",
    "browser_chromium_group":    "Chromium  (Chrome, Brave, Edge, Vivaldi, Opera...)",
    "browser_firefox_group":     "Firefox   (Firefox, LibreWolf, Waterfox, Zen...)",
    "browser_engine_prompt":     "Выбор [1/2]: ",
    "browser_pick_prompt":       "Выберите браузер [номер]: ",
    "browser_invalid_choice":    "Неверный выбор, попробуйте снова.",

    "setup_saved":               "==> Сохранено: {name} ({family})",
    "first_run_setup":           "Добро пожаловать в pwa-create! Сначала настроим ваш браузер.",

    "fetching_icon":             "Загрузка значка...",
    "icon_not_found":            "не найден, используется значок по умолчанию.",
    "icon_error":                "ошибка ({e}), используется значок по умолчанию.",

    "no_browser":                "Не удалось определить браузер по умолчанию.\nУбедитесь, что xdg-utils установлен.",
    "error_prefix":              "ОШИБКА",
    "unsupported_browser":       "'{name}' не поддерживается.\nПоддерживаются: Chrome, Chromium, Brave, Edge, Vivaldi, Firefox, LibreWolf.",

    "firefoxpwa_missing":        "firefoxpwa не найден. Требуется для браузеров на основе Firefox.",
    "firefoxpwa_not_in_path":    "Бинарный файл firefoxpwa не найден в PATH. Установлен ли он?",
    "firefoxpwa_still_missing":  "firefoxpwa по-прежнему не найден. Перезапустите терминал и повторите попытку.",
    "firefoxpwa_installed":      "firefoxpwa установлен!",
    "firefoxpwa_error":          "Ошибка firefoxpwa:\n{err}",
    "firefoxpwa_instructions":   (
        "PWAsForFirefox необходим для браузеров на основе Firefox.\n\n"
        "Установка:\n"
        "  • .deb (Ubuntu/Debian): https://github.com/filips123/PWAsForFirefox/releases\n"
        "  • .rpm (Fedora):        https://github.com/filips123/PWAsForFirefox/releases\n"
        "  • Cargo (Rust):         cargo install firefoxpwa\n\n"
        "Также может потребоваться расширение Firefox:\n"
        "  https://addons.mozilla.org/firefox/addon/pwas-for-firefox/"
    ),
    "flatpak_warning":           "PWAsForFirefox может не работать с Firefox Flatpak.",

    "runtime_missing":           "Среда выполнения firefoxpwa не установлена.",
    "runtime_installing":        "Установка среды выполнения firefoxpwa (это может занять некоторое время)...",
    "runtime_installed":         "Среда выполнения установлена.",
    "runtime_failed":            "Не удалось установить среду выполнения.",
    "runtime_timeout":           "Время операции истекло.",

    "install_auto_prompt":       "Установить автоматически? [д/н]: ",
    "install_auto_yes":          ("д", "да"),

    "distro_detected":           "Обнаруженный дистрибутив: {distro}",
    "aur_installing":            "Установка из AUR: {cmd}",
    "aur_no_helper":             "Помощник AUR не найден (paru/yay). Установите вручную:\n  yay -S firefox-pwa",
    "aur_failed":                "Установка из AUR не удалась.",
    "pkg_not_found":             "Пакет {ext} не найден.",
    "downloading":               "Загрузка: {url}",
    "pkg_install_failed":        "Установка пакета не удалась.",
    "auto_install_failed":       "Автоматическая установка не удалась: {e}",
    "distro_unknown_install":    (
        "Дистрибутив не определён.\n"
        "Ручная установка: https://github.com/filips423/PWAsForFirefox/releases\n"
        "  или: cargo install firefoxpwa"
    ),

    "pwa_installed":             "✓ '{name}' установлен!\n  Файл: {file}",
    "pwa_installed_firefox":     "✓ '{name}' установлен как Firefox PWA!\n{output}",
    "pwa_removed":               "✓ '{name}' удалён.",
    "pwa_removed_no_id":         (
        "✓ '{name}' удалён из записей.\n"
        "  Идентификатор сайта не найден — при необходимости удалите вручную: firefoxpwa site uninstall <ID>"
    ),
    "desktop_file_failed":       "Не удалось создать файл desktop: {e}",
    "file_delete_failed":        "Не удалось удалить файл: {e}",
    "no_pwas":                   "Установленные PWA не найдены.",
    "not_found":                 "'{id}' не найден.",

    "install_success_title":     "Установка выполнена",
    "install_fail_title":        "Ошибка установки",
    "removed_title":             "PWA удалён",
    "error_title":               "Ошибка",
    "confirm_title":             "Подтверждение",
    "missing_info_title":        "Отсутствуют данные",
    "remove_pwa_title":          "Удалить PWA",

    "confirm_remove":            "Удалить '{name}'?",
    "missing_info_body":         "Необходимо указать имя приложения и URL.",

    "uninstall_confirm_prompt":  "Вы уверены, что хотите удалить pwa-create? [д/Н]: ",
    "uninstall_data_prompt":     "Также удалить конфигурацию и все данные PWA? [д/Н]: ",
    "uninstall_data_removed":    "  Конфигурация и данные удалены.",
    "uninstall_success":         "==> pwa-create удалён.",
    "uninstall_cancelled":       "Удаление отменено.",

    "ui_install_title":          "Установить PWA",
    "ui_install_subtitle":       "Добавить веб-приложение на рабочий стол",
    "ui_field_name":             "Название приложения",
    "ui_field_url":              "URL",
    "ui_field_icon":             "Значок  ·  оставьте пустым для автоматической загрузки",
    "ui_icon_pick":              "Выбрать значок",
    "ui_btn_browse":             "Обзор",
    "ui_btn_refresh":            "🔄 Обновить значок",
    "ui_btn_install":            "Установить  →",
    "ui_btn_cancel":             "Отмена",
    "ui_btn_ok":                 "ОК",
    "ui_btn_yes":                "Да",
    "ui_btn_no":                 "Нет",
    "ui_btn_remove":             "Удалить",
    "ui_remove_title":           "🗑  Удалить PWA",
    "ui_remove_subtitle":        "Выберите приложение для удаления",
    "ui_col_name":               "Название",
    "ui_col_browser":            "Браузер",
}
