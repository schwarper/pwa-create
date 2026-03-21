import json
import re
from pathlib import Path

PWA_DB   = Path.home() / ".local" / "share" / "pwa-create" / "pwas.json"
APPS_DIR = Path.home() / ".local" / "share" / "applications"


def load_db() -> dict:
    if PWA_DB.exists():
        try:
            return json.loads(PWA_DB.read_text())
        except Exception:
            pass
    return {}


def save_db(db: dict):
    PWA_DB.parent.mkdir(parents=True, exist_ok=True)
    PWA_DB.write_text(json.dumps(db, indent=2, ensure_ascii=False))


def sanitize_id(name: str) -> str:
    return re.sub(r"[^a-zA-Z0-9_-]", "_", name).strip("_").lower()


def list_pwas() -> list[dict]:
    db = load_db()
    return [{"id": app_id, **entry} for app_id, entry in db.items()]