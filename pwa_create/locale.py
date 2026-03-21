import locale
import os
import importlib


def _detect_lang() -> str:
    for var in ("LANGUAGE", "LANG", "LC_ALL", "LC_MESSAGES"):
        val = os.environ.get(var, "")
        if val:
            lang = val.split("_")[0].split(".")[0].lower()
            if _exists(lang):
                return lang
    try:
        code = locale.getlocale()[0] or ""
        lang = code.split("_")[0].lower()
        if _exists(lang):
            return lang
    except Exception:
        pass
    return "en"


def _exists(lang: str) -> bool:
    try:
        mod = importlib.import_module(f"pwa_create.locales.{lang}")
        return hasattr(mod, "strings")
    except ImportError:
        return False


def _load(lang: str) -> dict:
    try:
        mod = importlib.import_module(f"pwa_create.locales.{lang}")
        if hasattr(mod, "strings"):
            return mod.strings
    except ImportError:
        pass
    from pwa_create.locales import en
    return en.strings


_LANG = _detect_lang()
_S    = _load(_LANG)
_FB   = _load("en")


def t(key: str, **kwargs) -> str:
    template = _S.get(key) or _FB.get(key, key)
    if kwargs:
        try:
            return template.format(**kwargs)
        except Exception:
            return template
    return template


def yes_answers() -> tuple:
    return _S.get("install_auto_yes", ("y", "yes"))