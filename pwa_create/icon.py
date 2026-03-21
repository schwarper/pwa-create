import urllib.request
import urllib.parse
import urllib.error
import html.parser
import hashlib
import json
import shutil
from pathlib import Path

ICONS_DIR = Path.home() / ".local" / "share" / "pwa-create" / "icons"


class LinkTagParser(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.icons        = []
        self.manifest_url = None

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if tag == "link":
            rel  = attrs_dict.get("rel", "").lower()
            href = attrs_dict.get("href", "")
            if "icon" in rel and href:
                sizes = attrs_dict.get("sizes", "0x0")
                self.icons.append((rel, href, sizes))
            if rel == "manifest":
                self.manifest_url = href


def _get_icon_size(sizes_str: str) -> int:
    try:
        return int(sizes_str.lower().split("x")[0])
    except (ValueError, IndexError):
        return 0


def _make_request(url: str, timeout: int = 8) -> bytes | None:
    try:
        req = urllib.request.Request(
            url,
            headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) pwa-create/1.0"}
        )
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read()
    except (urllib.error.URLError, TimeoutError, OSError):
        return None


def _save_icon(data: bytes, url: str) -> str | None:
    ICONS_DIR.mkdir(parents=True, exist_ok=True)
    ext      = ".png"
    url_path = urllib.parse.urlparse(url).path.lower()
    for candidate in (".ico", ".png", ".svg", ".webp", ".jpg", ".jpeg"):
        if url_path.endswith(candidate):
            ext = candidate
            break
    name = hashlib.md5(url.encode()).hexdigest()[:12] + ext
    path = ICONS_DIR / name
    try:
        path.write_bytes(data)
        return str(path)
    except OSError:
        return None


def _resolve_url(base: str, href: str) -> str:
    return urllib.parse.urljoin(base, href)


def fetch_icon_from_page(url: str) -> str | None:
    parsed   = urllib.parse.urlparse(url)
    base_url = f"{parsed.scheme}://{parsed.netloc}"

    html_data     = _make_request(url)
    best_icon_url = None
    best_size     = 0

    if html_data:
        html_text = html_data.decode("utf-8", errors="replace")
        parser    = LinkTagParser()
        try:
            parser.feed(html_text)
        except html.parser.HTMLParseError:
            pass

        if parser.manifest_url:
            manifest_url  = _resolve_url(url, parser.manifest_url)
            manifest_data = _make_request(manifest_url)
            if manifest_data:
                try:
                    manifest = json.loads(manifest_data.decode("utf-8", errors="replace"))
                    for icon in manifest.get("icons", []):
                        src  = icon.get("src", "")
                        size = _get_icon_size(icon.get("sizes", "0x0"))
                        if size > best_size and src:
                            best_size     = size
                            best_icon_url = _resolve_url(manifest_url, src)
                except (json.JSONDecodeError, ValueError):
                    pass

        if not best_icon_url:
            for rel, href, sizes in parser.icons:
                size = _get_icon_size(sizes)
                if "apple-touch-icon" in rel:
                    size = max(size, 180)
                if size > best_size:
                    best_size     = size
                    best_icon_url = _resolve_url(url, href)

    if not best_icon_url:
        best_icon_url = f"{base_url}/favicon.ico"

    if best_icon_url:
        data = _make_request(best_icon_url)
        if data and len(data) > 64:
            if best_icon_url.startswith("https://"):
                return best_icon_url
            saved = _save_icon(data, best_icon_url)
            if saved:
                return saved

    favicon_url = f"{base_url}/favicon.ico"
    data = _make_request(favicon_url)
    if data and len(data) > 64:
        saved = _save_icon(data, favicon_url)
        if saved:
            return saved

    return None


def get_icon_for_url(url: str, user_provided: str | None = None) -> str | None:
    if user_provided:
        if Path(user_provided).is_file():
            ICONS_DIR.mkdir(parents=True, exist_ok=True)
            dest = ICONS_DIR / Path(user_provided).name
            shutil.copy2(user_provided, dest)
            return str(dest)
        elif user_provided.startswith(("http://", "https://")):
            data = _make_request(user_provided)
            if data and len(data) > 64:
                if user_provided.startswith("https://"):
                    return user_provided
                saved = _save_icon(data, user_provided)
                if saved:
                    return saved
    return fetch_icon_from_page(url)