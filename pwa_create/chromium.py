import os
import subprocess
from pathlib import Path
from .browser import BrowserInfo
from .db import load_db, save_db, sanitize_id, APPS_DIR
from .locale import t


def _get_exec_command(browser: BrowserInfo, url: str, app_id: str) -> str:
    if browser.is_flatpak:
        return f"flatpak run {browser.exec_path} --app={url} --class={app_id}"
    elif browser.is_snap:
        snap_bin = f"/snap/bin/{os.path.basename(browser.exec_path)}"
        return f"{snap_bin} --app={url} --class={app_id}"
    else:
        return f"{browser.exec_path} --app={url} --class={app_id}"


def install_pwa(name: str, url: str, icon_path: str | None, browser: BrowserInfo) -> tuple[bool, str]:
    APPS_DIR.mkdir(parents=True, exist_ok=True)

    app_id  = sanitize_id(name)
    base_id = app_id
    counter = 1
    db      = load_db()

    while app_id in db and db[app_id]["url"] != url:
        app_id  = f"{base_id}_{counter}"
        counter += 1

    exec_cmd  = _get_exec_command(browser, url, app_id)
    icon_line = f"Icon={icon_path}" if icon_path else "Icon=application-x-executable"

    desktop_content = f"""[Desktop Entry]
Version=1.0
Type=Application
Name={name}
Comment=PWA: {url}
Exec={exec_cmd}
{icon_line}
Terminal=false
StartupNotify=true
StartupWMClass={app_id}
Categories=Network;WebApplication;
X-PWA-Create=true
X-PWA-URL={url}
X-PWA-Browser={browser.name}
"""

    desktop_file = APPS_DIR / f"pwa-create-{app_id}.desktop"
    try:
        desktop_file.write_text(desktop_content)
        desktop_file.chmod(0o755)
    except Exception as e:
        return False, t("desktop_file_failed", e=e)

    try:
        subprocess.run(["update-desktop-database", str(APPS_DIR)],
                       capture_output=True, timeout=5)
    except Exception:
        pass

    db[app_id] = {
        "name":           name,
        "url":            url,
        "icon":           icon_path,
        "browser":        browser.name,
        "browser_family": browser.family.value,
        "desktop_file":   str(desktop_file),
    }
    save_db(db)

    return True, t("pwa_installed", name=name, file=desktop_file)


def uninstall_pwa_chromium(app_id: str) -> tuple[bool, str]:
    db = load_db()
    if app_id not in db:
        return False, t("not_found", id=app_id)

    entry        = db[app_id]
    desktop_file = Path(entry.get("desktop_file", ""))

    try:
        if desktop_file.exists():
            desktop_file.unlink()
    except Exception as e:
        return False, t("file_delete_failed", e=e)

    del db[app_id]
    save_db(db)

    try:
        subprocess.run(["update-desktop-database", str(APPS_DIR)],
                       capture_output=True, timeout=5)
    except Exception:
        pass

    return True, t("pwa_removed", name=entry["name"])