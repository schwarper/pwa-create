import subprocess
import json
import re
import urllib.request
import urllib.parse
import urllib.error
import html.parser
from pathlib import Path
from .browser import BrowserInfo
from .db import load_db, save_db, sanitize_id
from .locale import t


def _find_manifest_url(site_url: str) -> str | None:
    class ManifestParser(html.parser.HTMLParser):
        def __init__(self):
            super().__init__()
            self.manifest = None

        def handle_starttag(self, tag, attrs):
            if tag == "link":
                d = dict(attrs)
                if d.get("rel") == "manifest" and d.get("href"):
                    self.manifest = d["href"]

    try:
        req = urllib.request.Request(
            site_url,
            headers={"User-Agent": "Mozilla/5.0 pwa-create/1.0"}
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            html_bytes = resp.read(65536)
        parser = ManifestParser()
        parser.feed(html_bytes.decode("utf-8", errors="replace"))
        if parser.manifest:
            return urllib.parse.urljoin(site_url, parser.manifest)
    except (urllib.error.URLError, TimeoutError, OSError):
        pass
    return None


def _get_firefoxpwa_site_id_by_name(name: str) -> str | None:
    db = load_db()
    for app_id, entry in db.items():
        if entry.get("name", "").lower() == name.lower():
            return entry.get("firefox_site_id")
    return None


def install_pwa_firefox(name: str, url: str, icon_path: str | None, browser: BrowserInfo) -> tuple[bool, str]:
    cmd = ["firefoxpwa", "site", "install", "--name", name]

    if icon_path and icon_path.startswith("https://"):
        cmd += ["--icon-url", icon_path]

    manifest_url = _find_manifest_url(url)

    if manifest_url:
        cmd_main = cmd + [manifest_url]
    else:
        cmd_main = cmd + ["--document-url", url]

    try:
        result = subprocess.run(cmd_main, capture_output=True, text=True, timeout=60)

        if result.returncode != 0 and manifest_url:
            out_err = result.stderr + result.stdout
            if any(kw in out_err.lower() for kw in ("manifest", "invalid", "403", "404")):
                cmd_fallback = cmd + ["--document-url", url]
                result = subprocess.run(cmd_fallback, capture_output=True, text=True, timeout=60)

    except FileNotFoundError:
        return False, t("firefoxpwa_not_in_path")
    except subprocess.TimeoutExpired:
        return False, t("runtime_timeout")

    if result.returncode != 0:
        err = result.stderr.strip() or result.stdout.strip()
        return False, t("firefoxpwa_error", err=err)

    output  = result.stdout.strip()
    site_id = None
    match   = (
        re.search(r"Web app installed:\s*([A-Z0-9]+)", output)
        or re.search(r"([A-Z0-9]{20,})", output)
    )
    if match:
        site_id = match.group(1)

    if site_id and icon_path and icon_path.startswith("https://"):
        try:
            subprocess.run(
                ["firefoxpwa", "site", "update", site_id, "--icon-url", icon_path],
                capture_output=True, timeout=15
            )
        except Exception:
            pass

    app_id = sanitize_id(name)
    db     = load_db()
    db[app_id] = {
        "name":            name,
        "url":             url,
        "icon":            icon_path,
        "browser":         browser.name,
        "browser_family":  browser.family.value,
        "firefox_site_id": site_id,
        "desktop_file":    None,
    }
    save_db(db)

    return True, t("pwa_installed_firefox", name=name, output=output)


def uninstall_pwa_firefox(app_id: str) -> tuple[bool, str]:
    db = load_db()
    if app_id not in db:
        return False, t("not_found", id=app_id)

    entry   = db[app_id]
    site_id = entry.get("firefox_site_id") or _get_firefoxpwa_site_id_by_name(entry.get("name", app_id))

    if not site_id:
        del db[app_id]
        save_db(db)
        return True, t("pwa_removed_no_id", name=entry["name"])

    try:
        result = subprocess.run(
            ["firefoxpwa", "site", "uninstall", site_id],
            input="y\n", capture_output=True, text=True, timeout=30
        )
    except FileNotFoundError:
        return False, t("firefoxpwa_not_in_path")
    except subprocess.TimeoutExpired:
        return False, t("runtime_timeout")

    if result.returncode != 0:
        err = result.stderr.strip() or result.stdout.strip()
        return False, t("firefoxpwa_error", err=err)

    del db[app_id]
    save_db(db)

    return True, t("pwa_removed", name=entry["name"])


def check_runtime_installed() -> bool:
    runtime_dir = Path.home() / ".local" / "share" / "firefoxpwa" / "runtime"
    return runtime_dir.exists() and any(runtime_dir.iterdir())


def install_runtime() -> tuple[bool, str]:
    try:
        print(t("runtime_installing"))
        result = subprocess.run(
            ["firefoxpwa", "runtime", "install"],
            timeout=300
        )
        return (True, t("runtime_installed")) if result.returncode == 0 else (False, t("runtime_failed"))
    except FileNotFoundError:
        return False, t("firefoxpwa_not_in_path")
    except subprocess.TimeoutExpired:
        return False, t("runtime_timeout")