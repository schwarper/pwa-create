import subprocess
import shutil
import os
import tempfile
import urllib.request
import json
from enum import Enum
from pwa_create.locale import t


class BrowserFamily(Enum):
    CHROMIUM = "chromium"
    FIREFOX  = "firefox"
    UNKNOWN  = "unknown"


class BrowserInfo:
    def __init__(self, name: str, family: BrowserFamily, exec_path: str, desktop_name: str,
                 is_flatpak: bool = False, is_snap: bool = False):
        self.name         = name
        self.family       = family
        self.exec_path    = exec_path
        self.desktop_name = desktop_name
        self.is_flatpak   = is_flatpak
        self.is_snap      = is_snap

    def __repr__(self):
        return f"BrowserInfo(name={self.name}, family={self.family.value}, flatpak={self.is_flatpak}, snap={self.is_snap})"


CHROMIUM_HINTS = ("chrom", "brave", "edge", "opera", "vivaldi", "epiphany")
FIREFOX_HINTS  = ("firefox", "librewolf", "waterfox", "floorp", "zen", "fox")

CHROMIUM_FLATPAK_HINTS = ("chrome", "chromium", "brave", "edge", "opera", "vivaldi")
FIREFOX_FLATPAK_HINTS  = ("firefox", "librewolf", "waterfox", "floorp", "zen")


def _family_from_name(name: str) -> BrowserFamily:
    n = name.lower()
    if any(h in n for h in CHROMIUM_HINTS):
        return BrowserFamily.CHROMIUM
    if any(h in n for h in FIREFOX_HINTS):
        return BrowserFamily.FIREFOX
    return BrowserFamily.UNKNOWN


def _flatpak_family(app_id: str) -> BrowserFamily:
    a = app_id.lower()
    if any(h in a for h in CHROMIUM_FLATPAK_HINTS):
        return BrowserFamily.CHROMIUM
    if any(h in a for h in FIREFOX_FLATPAK_HINTS):
        return BrowserFamily.FIREFOX
    return BrowserFamily.UNKNOWN


def _pretty_name(desktop_or_id: str) -> str:
    name = desktop_or_id.removesuffix(".desktop")
    if "." in name:
        name = name.split(".")[-1]
    return name.replace("-", " ").replace("_", " ").title()


def get_default_browser_desktop() -> str | None:
    try:
        result = subprocess.run(
            ["xdg-settings", "get", "default-web-browser"],
            capture_output=True, text=True, timeout=5
        )
        if result.returncode == 0:
            return result.stdout.strip()
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass
    browser_env = os.environ.get("BROWSER", "")
    if browser_env:
        return os.path.basename(browser_env)
    return None


def detect_default_browser() -> BrowserInfo | None:
    desktop_name = get_default_browser_desktop()
    if not desktop_name:
        return None

    desktop_lower = desktop_name.lower()
    bare          = desktop_lower.removesuffix(".desktop")

    if bare.count(".") >= 2:
        family = _flatpak_family(bare)
        if family != BrowserFamily.UNKNOWN:
            name = _pretty_name(bare)
            return BrowserInfo(f"{name} (Flatpak)", family, bare, desktop_name, is_flatpak=True)

    family    = _family_from_name(bare)
    exec_path = shutil.which(bare) or bare
    is_snap   = "/snap/" in (shutil.which(bare) or "")
    name      = _pretty_name(bare)

    if family != BrowserFamily.UNKNOWN:
        return BrowserInfo(name, family, exec_path, desktop_name, is_snap=is_snap)

    return BrowserInfo(desktop_name, BrowserFamily.UNKNOWN, desktop_name, desktop_name)


def is_firefoxpwa_installed() -> bool:
    return shutil.which("firefoxpwa") is not None


def get_firefoxpwa_install_instructions() -> str:
    return t("firefoxpwa_instructions")


def detect_distro() -> str:
    FAMILY_MAP = {
        "debian": ("debian", "ubuntu", "mint", "pop", "elementary", "zorin", "kali", "parrot", "linuxmint"),
        "fedora": ("fedora", "rhel", "centos", "rocky", "alma", "nobara", "opensuse", "suse"),
        "arch":   ("arch", "manjaro", "endeavouros", "garuda", "cachyos", "artix", "crystal"),
    }
    try:
        values = {}
        with open("/etc/os-release") as f:
            for line in f:
                line = line.strip()
                if "=" in line and not line.startswith("#"):
                    k, _, v = line.partition("=")
                    values[k.strip().lower()] = v.strip().strip('"').lower()
        ids = []
        if "id" in values:
            ids.append(values["id"])
        if "id_like" in values:
            ids.extend(values["id_like"].split())
        for family, hints in FAMILY_MAP.items():
            if any(i in hints for i in ids):
                return family
        name = values.get("name", "") + " " + values.get("pretty_name", "")
        for family, hints in FAMILY_MAP.items():
            if any(h in name for h in hints):
                return family
    except Exception:
        pass
    return "unknown"


def install_firefoxpwa_auto() -> tuple[bool, str]:
    distro = detect_distro()
    print(t("distro_detected", distro=distro))

    if distro == "arch":
        if shutil.which("paru"):
            mgr = ["paru", "-S", "--noconfirm", "firefox-pwa"]
        elif shutil.which("yay"):
            mgr = ["yay", "-S", "--noconfirm", "firefox-pwa"]
        else:
            return False, t("aur_no_helper")
        print(t("aur_installing", cmd=" ".join(mgr)))
        result = subprocess.run(mgr, timeout=300)
        return (True, t("firefoxpwa_installed")) if result.returncode == 0 else (False, t("aur_failed"))

    if distro in ("debian", "fedora"):
        ext = ".deb" if distro == "debian" else ".rpm"
        try:
            req = urllib.request.Request(
                "https://api.github.com/repos/filips123/PWAsForFirefox/releases/latest",
                headers={"User-Agent": "pwa-create"}
            )
            with urllib.request.urlopen(req, timeout=10) as resp:
                assets = json.loads(resp.read()).get("assets", [])
            pkg_url = next((a["browser_download_url"] for a in assets if a["name"].endswith(ext)), None)
            if not pkg_url:
                return False, t("pkg_not_found", ext=ext)
            print(t("downloading", url=pkg_url))
            with tempfile.NamedTemporaryFile(suffix=ext, delete=False) as tmp:
                tmp_path = tmp.name
            urllib.request.urlretrieve(pkg_url, tmp_path)
            if distro == "debian":
                result = subprocess.run(["sudo", "dpkg", "-i", tmp_path], timeout=60)
            else:
                if shutil.which("dnf"):
                    result = subprocess.run(["sudo", "dnf", "install", "-y", tmp_path], timeout=120)
                else:
                    result = subprocess.run(["sudo", "rpm", "-i", tmp_path], timeout=60)
            os.unlink(tmp_path)
            return (True, t("firefoxpwa_installed")) if result.returncode == 0 else (False, t("pkg_install_failed"))
        except Exception as e:
            return False, t("auto_install_failed", e=e)

    return False, t("distro_unknown_install")