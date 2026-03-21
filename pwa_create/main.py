#!/usr/bin/env python3
import sys
import shutil
import subprocess
import argparse
import json as _json
from pathlib import Path as _Path
from pwa_create.locale import t, yes_answers

_CONFIG_FILE = _Path.home() / ".local" / "share" / "pwa-create" / "config.json"


def _ensure_url(url: str) -> str:
    if not url.startswith(("http://", "https://")):
        return "https://" + url
    return url


def _load_config() -> dict:
    if _CONFIG_FILE.exists():
        try:
            return _json.loads(_CONFIG_FILE.read_text())
        except Exception:
            pass
    return {}


def _save_config(data: dict):
    _CONFIG_FILE.parent.mkdir(parents=True, exist_ok=True)
    _CONFIG_FILE.write_text(_json.dumps(data, indent=2))


def _get_saved_browser():
    from pwa_create.browser import BrowserFamily, BrowserInfo
    cfg = _load_config()
    if "browser" not in cfg:
        return None
    b = cfg["browser"]
    try:
        family = BrowserFamily(b["family"])
        return BrowserInfo(b["name"], family, shutil.which(b["exec"]) or b["exec"], b["desktop"])
    except Exception:
        return None


def _confirm_browser(browser, gui_fallback: bool):
    from pwa_create.browser import BrowserFamily, BrowserInfo

    CHROMIUM_CHOICES = [
        ("Google Chrome",  "google-chrome"),
        ("Chromium",       "chromium"),
        ("Brave",          "brave-browser"),
        ("Microsoft Edge", "microsoft-edge"),
        ("Vivaldi",        "vivaldi-stable"),
        ("Opera",          "opera"),
    ]
    FIREFOX_CHOICES = [
        ("Firefox",      "firefox"),
        ("LibreWolf",    "librewolf"),
        ("Waterfox",     "waterfox"),
        ("Floorp",       "floorp"),
        ("Zen Browser",  "zen-browser"),
    ]

    def make_browser(name, exe, family):
        path = shutil.which(exe) or exe
        return BrowserInfo(name, family, path, exe + ".desktop")

    def pick_manually():
        print()
        print(t("browser_select_prompt"))
        print(f"  1) {t('browser_chromium_group')}")
        print(f"  2) {t('browser_firefox_group')}")
        print()
        while True:
            ans = input(t("browser_engine_prompt")).strip()
            if ans == "1":
                family  = BrowserFamily.CHROMIUM
                choices = CHROMIUM_CHOICES
                break
            elif ans == "2":
                family  = BrowserFamily.FIREFOX
                choices = FIREFOX_CHOICES
                break
            print(t("browser_invalid_choice"))

        print()
        for i, (name, _) in enumerate(choices, 1):
            print(f"  {i}) {name}")
        print()
        while True:
            ans = input(t("browser_pick_prompt")).strip()
            try:
                idx = int(ans) - 1
                if 0 <= idx < len(choices):
                    name, exe = choices[idx]
                    return make_browser(name, exe, family)
            except ValueError:
                pass
            print(t("browser_invalid_choice"))

    if browser and browser.family != BrowserFamily.UNKNOWN:
        print(t("browser_detected", name=browser.name, family=browser.family.value))
        ans = input(t("browser_confirm_prompt")).strip().lower()
        if ans in yes_answers() or ans == "":
            return browser
        return pick_manually()

    print(t("browser_not_detected"))
    return pick_manually()


def cmd_setup():
    from pwa_create.browser import detect_default_browser
    print()
    browser = detect_default_browser()
    browser = _confirm_browser(browser, gui_fallback=False)
    if not browser:
        print(f'{t("error_prefix")}: {t("no_browser")}')
        return
    _save_config({
        "browser": {
            "name":    browser.name,
            "family":  browser.family.value,
            "exec":    browser.exec_path,
            "desktop": browser.desktop_name,
        }
    })
    print(t("setup_saved", name=browser.name, family=browser.family.value))

    if browser.family.value == "firefox":
        from pwa_create.browser import is_firefoxpwa_installed, install_firefoxpwa_auto
        from pwa_create.firefox import install_runtime, check_runtime_installed
        if not is_firefoxpwa_installed():
            print()
            print(t("firefoxpwa_missing"))
            ans = input(t("install_auto_prompt")).strip().lower()
            if ans in yes_answers():
                ok, msg = install_firefoxpwa_auto()
                print(msg)
                if not ok:
                    return
        if is_firefoxpwa_installed() and not check_runtime_installed():
            print()
            print(t("runtime_missing"))
            ans = input(t("install_auto_prompt")).strip().lower()
            if ans in yes_answers():
                ok, msg = install_runtime()
                print(msg)


def cmd_uninstall():
    """Terminalde `pwa-create --uninstall` ile çalışır, make gerektirmez."""
    BIN_FILE = _Path.home() / ".local" / "bin"   / "pwa-create"
    DESKTOP  = _Path.home() / ".local" / "share" / "applications" / "pwa-create.desktop"
    ICON     = _Path.home() / ".local" / "share" / "icons" / "hicolor" / "512x512" / "apps" / "pwa-create.png"
    SRC_DIR  = _Path.home() / ".local" / "share" / "pwa-create-src"
    APPS_DIR = _Path.home() / ".local" / "share" / "applications"

    print()
    ans = input(t("uninstall_confirm_prompt")).strip().lower()
    if ans not in yes_answers():
        print(t("uninstall_cancelled"))
        return

    for p in (DESKTOP, ICON):
        try:
            p.unlink(missing_ok=True)
        except OSError:
            pass

    shutil.rmtree(SRC_DIR, ignore_errors=True)

    try:
        subprocess.run(["update-desktop-database", str(APPS_DIR)],
                       capture_output=True, timeout=5)
    except Exception:
        pass

    ans2 = input(t("uninstall_data_prompt")).strip().lower()
    if ans2 in yes_answers():
        data_dir = _Path.home() / ".local" / "share" / "pwa-create"
        shutil.rmtree(data_dir, ignore_errors=True)
        print(t("uninstall_data_removed"))

    # Binary en son silinir — bu noktadan sonra process zaten kapanıyor
    try:
        BIN_FILE.unlink(missing_ok=True)
    except OSError:
        pass

    print(t("uninstall_success"))


def cmd_install(name: str, url: str, icon: str | None, gui_fallback: bool = False):
    from pwa_create.browser import (
        BrowserFamily,
        is_firefoxpwa_installed,
        get_firefoxpwa_install_instructions,
    )
    from pwa_create import ui

    url     = _ensure_url(url)
    browser = _get_saved_browser()

    if not browser:
        from pwa_create.browser import detect_default_browser
        browser = detect_default_browser()
        browser = _confirm_browser(browser, gui_fallback)

    if not browser:
        msg = t("no_browser")
        if gui_fallback:
            ui.show_error(t("error_title"), msg)
        else:
            print(f'{t("error_prefix")}: {msg}', file=sys.stderr)
        sys.exit(1)

    print(t("browser_detected", name=browser.name, family=browser.family.value))

    if browser.family == BrowserFamily.FIREFOX:
        if browser.is_flatpak:
            msg = t("flatpak_warning") + "\n\n" + get_firefoxpwa_install_instructions()
            if gui_fallback:
                ui.show_firefox_required(msg)
            else:
                print(msg)
            sys.exit(1)

        if not is_firefoxpwa_installed():
            print(t("firefoxpwa_missing"))
            if gui_fallback:
                do_install = ui.show_question(t("confirm_title"), t("firefoxpwa_missing"))
            else:
                ans        = input(t("install_auto_prompt")).strip().lower()
                do_install = ans in yes_answers()

            if do_install:
                from pwa_create.browser import install_firefoxpwa_auto
                ok, msg = install_firefoxpwa_auto()
                print(msg)
                if not ok:
                    if gui_fallback:
                        ui.show_error(t("install_fail_title"), msg)
                    sys.exit(1)
                if not is_firefoxpwa_installed():
                    err = t("firefoxpwa_still_missing")
                    print(err, file=sys.stderr)
                    sys.exit(1)
                from pwa_create.firefox import install_runtime
                install_runtime()
            else:
                print(get_firefoxpwa_install_instructions())
                sys.exit(0)

        icon_path = _get_icon(url, icon, gui_fallback)
        from pwa_create.firefox import install_pwa_firefox
        ok, msg = install_pwa_firefox(name, url, icon_path, browser)
        _report(ok, msg, gui_fallback)

    elif browser.family == BrowserFamily.CHROMIUM:
        icon_path = _get_icon(url, icon, gui_fallback)
        from pwa_create.chromium import install_pwa
        ok, msg = install_pwa(name, url, icon_path, browser)
        _report(ok, msg, gui_fallback)

    else:
        msg = t("unsupported_browser", name=browser.name)
        if gui_fallback:
            ui.show_error(t("error_title"), msg)
        else:
            print(f'{t("error_prefix")}: {msg}', file=sys.stderr)
        sys.exit(1)


def _get_icon(url: str, user_icon: str | None, gui_fallback: bool) -> str | None:
    from pwa_create.icon import get_icon_for_url
    print(t("fetching_icon"), end=" ", flush=True)
    try:
        path = get_icon_for_url(url, user_icon)
        if path:
            print(f"✓ {path}")
        else:
            print(t("icon_not_found"))
        return path
    except Exception as e:
        print(t("icon_error", e=e))
        return None


def _report(ok: bool, msg: str, gui_fallback: bool):
    from pwa_create import ui
    if ok:
        print(msg)
        if gui_fallback:
            ui.show_info(t("install_success_title"), msg)
    else:
        print(f'{t("error_prefix")}: {msg}', file=sys.stderr)
        if gui_fallback:
            ui.show_error(t("install_fail_title"), msg)
        sys.exit(1)


def cmd_list():
    from pwa_create.db import list_pwas
    pwas = list_pwas()
    if not pwas:
        print(t("no_pwas"))
        return
    print(f"{'ID':<20} {'Name':<20} {'URL':<40} {'Browser'}")
    print("-" * 90)
    for p in pwas:
        print(f"{p['id']:<20} {p['name']:<20} {p['url']:<40} {p.get('browser', '-')}")


def cmd_remove_gui():
    from pwa_create.db import list_pwas
    from pwa_create.chromium import uninstall_pwa_chromium
    from pwa_create.firefox import uninstall_pwa_firefox
    from pwa_create import ui

    pwas   = list_pwas()
    app_id = ui.show_list(t("remove_pwa_title"), pwas)
    if not app_id:
        return

    selected = next((p for p in pwas if p["id"] == app_id), None)
    if not selected:
        return

    if not ui.show_question(t("confirm_title"), t("confirm_remove", name=selected["name"])):
        return

    if selected.get("browser_family") == "firefox":
        ok, msg = uninstall_pwa_firefox(app_id)
    else:
        ok, msg = uninstall_pwa_chromium(app_id)

    if ok:
        ui.show_info(t("removed_title"), msg)
    else:
        ui.show_error(t("error_title"), msg)


def cmd_remove_cli(app_id: str):
    from pwa_create.db import list_pwas
    from pwa_create.chromium import uninstall_pwa_chromium
    from pwa_create.firefox import uninstall_pwa_firefox

    pwas     = list_pwas()
    selected = next((p for p in pwas if p["id"] == app_id), None)
    if not selected:
        print(f'{t("error_prefix")}: {t("not_found", id=app_id)}', file=sys.stderr)
        cmd_list()
        sys.exit(1)

    if selected.get("browser_family") == "firefox":
        ok, msg = uninstall_pwa_firefox(app_id)
    else:
        ok, msg = uninstall_pwa_chromium(app_id)

    if ok:
        print(msg)
    else:
        print(f'{t("error_prefix")}: {msg}', file=sys.stderr)
        sys.exit(1)


def cmd_gui():
    from pwa_create import ui
    data = ui.show_install_form()
    if not data:
        sys.exit(0)
    name = data.get("name", "").strip()
    url  = data.get("url",  "").strip()
    icon = data.get("icon")
    if not name or not url:
        ui.show_error(t("missing_info_title"), t("missing_info_body"))
        sys.exit(1)
    cmd_install(name, url, icon, gui_fallback=True)


def _run_first_time_setup():
    """Config yoksa setup'a yönlendir. Hem GUI hem CLI quick install için ortak."""
    if not _get_saved_browser():
        print(t("first_run_setup"))
        cmd_setup()
        print()


def main():
    args_raw = sys.argv[1:]

    if args_raw and not args_raw[0].startswith("-"):
        if len(args_raw) >= 2:
            _run_first_time_setup()
            cmd_install(args_raw[0], args_raw[1], args_raw[2] if len(args_raw) > 2 else None)
            return

    parser = argparse.ArgumentParser(
        prog="pwa-create",
        description="Linux PWA Installer",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  pwa-create                                     # Open GUI
  pwa-create WhatsApp https://web.whatsapp.com   # Quick install
  pwa-create --list                              # List installed PWAs
  pwa-create --remove                            # Remove via GUI
  pwa-create --remove whatsapp                   # Remove by ID
  pwa-create --uninstall                         # Uninstall pwa-create itself
        """
    )
    parser.add_argument("--setup",     action="store_true",                            help="Configure default browser")
    parser.add_argument("--list",      "-l", action="store_true",                      help="List installed PWAs")
    parser.add_argument("--remove",    "-r", nargs="?", const="__GUI__", metavar="ID", help="Remove a PWA")
    parser.add_argument("--uninstall", action="store_true",                            help="Uninstall pwa-create")
    parser.add_argument("--version",   "-v", action="store_true",                      help="Show version")

    parsed = parser.parse_args(args_raw)

    if parsed.version:
        from pwa_create import __version__
        print(f"pwa-create {__version__}")
        return

    if parsed.uninstall:
        cmd_uninstall()
        return

    if parsed.setup:
        cmd_setup()
        return

    if parsed.list:
        cmd_list()
        return

    if parsed.remove is not None:
        if parsed.remove == "__GUI__":
            cmd_remove_gui()
        else:
            cmd_remove_cli(parsed.remove)
        return

    # Argümansız çalıştırma → GUI, gerekirse önce setup
    _run_first_time_setup()
    cmd_gui()


if __name__ == "__main__":
    main()