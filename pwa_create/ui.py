import subprocess
import shutil
import os
import sys
import threading
from typing import Optional
from pwa_create.locale import t


def set_window_icon(root):
    try:
        from PIL import Image, ImageTk
        icon_path = os.path.join(os.path.dirname(__file__), "icon.png")
        if os.path.exists(icon_path):
            img   = Image.open(icon_path)
            photo = ImageTk.PhotoImage(img)
            root.iconphoto(True, photo)
            root._window_icon = photo
    except Exception:
        pass


BG      = "#1e1e2e"
BG2     = "#11111b"
BG3     = "#313244"
MANTLE  = "#181825"
SURFACE = "#45475a"
TEXT    = "#cdd6f4"
SUBTEXT = "#a6adc8"
MUTED   = "#6c7086"
ACCENT  = "#89b4fa"
MAUVE   = "#cba6f7"
GREEN   = "#a6e3a1"
RED     = "#f38ba8"

FONT    = ("Sans", 11)
FONT_B  = ("Sans", 11, "bold")
FONT_SM = ("Sans", 10)
FONT_H  = ("Sans", 18, "bold")
FONT_SH = ("Sans", 12)


def _detect_toolkit() -> str:
    try:
        import tkinter as _tk
        r = _tk.Tk()
        r.withdraw()
        r.destroy()
        return "tkinter"
    except Exception:
        pass
    if shutil.which("zenity"):
        return "zenity"
    if shutil.which("kdialog"):
        return "kdialog"
    return "none"


_TOOLKIT = None


def _tk() -> str:
    global _TOOLKIT
    if _TOOLKIT is None:
        _TOOLKIT = _detect_toolkit()
    return _TOOLKIT


def show_install_form(prefill_name: str = "", prefill_url: str = "") -> Optional[dict]:
    if _tk() == "tkinter":
        return _tk_install_form(prefill_name, prefill_url)
    if _tk() == "zenity":
        return _zenity_install_form(prefill_name, prefill_url)
    if _tk() == "kdialog":
        return _kdialog_install_form(prefill_name, prefill_url)
    return None


def show_info(title: str, message: str):
    import re
    message = re.sub(r'\x1b\[[0-9;]*m', '', message)
    if _tk() == "tkinter":
        _tk_msg(title, message, "info")
    elif _tk() == "zenity":
        _zenity("--info", f"--title={title}", f"--text={message}", "--width=420")
    elif _tk() == "kdialog":
        _kdialog("--msgbox", message, "--title", title)
    else:
        print(f"[INFO] {title}: {message}")


def show_error(title: str, message: str):
    import re
    message = re.sub(r'\x1b\[[0-9;]*m', '', message)
    if _tk() == "tkinter":
        _tk_msg(title, message, "error")
    elif _tk() == "zenity":
        _zenity("--error", f"--title={title}", f"--text={message}", "--width=420")
    elif _tk() == "kdialog":
        _kdialog("--error", message, "--title", title)
    else:
        print(f"[ERROR] {title}: {message}", file=sys.stderr)


def show_question(title: str, message: str) -> bool:
    if _tk() == "tkinter":
        return _tk_question(title, message)
    if _tk() == "zenity":
        rc, _ = _zenity("--question", f"--title={title}", f"--text={message}", "--width=420")
        return rc == 0
    if _tk() == "kdialog":
        rc, _ = _kdialog("--yesno", message, "--title", title)
        return rc == 0
    ans = input(f"{message} [y/n]: ").strip().lower()
    return ans in ("y", "yes", "e", "evet")


def show_list(title: str, items: list[dict]) -> Optional[str]:
    if not items:
        show_info(title, t("no_pwas"))
        return None
    if _tk() == "tkinter":
        return _tk_list(title, items)
    if _tk() == "zenity":
        return _zenity_list(title, items)
    if _tk() == "kdialog":
        return _kdialog_list(title, items)
    return None


def show_firefox_required(instructions: str):
    show_info("Firefox PWA", instructions)


def pick_file(title: str = "Select icon") -> Optional[str]:
    if _tk() == "tkinter":
        import tkinter as tk
        from tkinter import filedialog
        r = tk.Tk()
        r.withdraw()
        f = filedialog.askopenfilename(title=title,
            filetypes=[("Image", "*.png *.jpg *.jpeg *.webp *.ico *.svg")])
        r.destroy()
        return f or None
    if _tk() == "zenity":
        rc, out = _zenity("--file-selection", f"--title={title}",
                          "--file-filter=Image|*.png *.jpg *.webp *.ico *.svg")
        return out if rc == 0 else None
    if _tk() == "kdialog":
        rc, out = _kdialog("--getopenfilename", os.path.expanduser("~"),
                           "*.png *.jpg *.webp *.ico *.svg", "--title", title)
        return out if rc == 0 else None
    return None


def _tk_install_form(prefill_name: str, prefill_url: str) -> Optional[dict]:
    import tkinter as tk
    from tkinter import filedialog
    import io

    result = {}
    root   = tk.Tk()
    root.title("pwa-create")
    set_window_icon(root)
    root.configure(bg=BG)
    root.resizable(False, False)

    def field_label(parent, text):
        tk.Label(parent, text=text, bg=parent["bg"], fg=SUBTEXT,
                 font=FONT_B, anchor="w").pack(fill=tk.X, pady=(16, 4))

    def styled_entry(parent, var):
        f_outer = tk.Frame(parent, bg=SURFACE, padx=1, pady=1)
        f_outer.pack(fill=tk.X, pady=(0, 4))
        e = tk.Entry(f_outer, textvariable=var, font=FONT, bg=BG2,
                     fg=TEXT, insertbackground=TEXT, relief="flat", bd=0)
        e.pack(fill=tk.X, padx=12, pady=12)
        return e

    header = tk.Frame(root, bg=MANTLE, pady=28)
    header.pack(fill=tk.X)
    tk.Label(header, text="🌐", font=("Sans", 28), bg=MANTLE, fg=ACCENT).pack()
    tk.Label(header, text=t("ui_install_title"),    font=FONT_H,  bg=MANTLE, fg=TEXT).pack()
    tk.Label(header, text=t("ui_install_subtitle"), font=FONT_SM, bg=MANTLE, fg=MUTED).pack(pady=(2, 0))

    body = tk.Frame(root, bg=BG, padx=36, pady=24)
    body.pack(fill=tk.BOTH)

    field_label(body, t("ui_field_name"))
    name_var   = tk.StringVar(value=prefill_name)
    name_entry = styled_entry(body, name_var)

    field_label(body, t("ui_field_url"))
    url_var   = tk.StringVar(value=prefill_url)
    url_entry = styled_entry(body, url_var)

    field_label(body, t("ui_field_icon"))

    icon_var = tk.StringVar()
    icon_ef  = tk.Frame(body, bg=SURFACE, padx=1, pady=1)
    icon_ef.pack(fill=tk.X, pady=(0, 10))
    icon_entry = tk.Entry(icon_ef, textvariable=icon_var, font=FONT, bg=BG2,
                          fg=TEXT, insertbackground=TEXT, relief="flat", bd=0)
    icon_entry.pack(fill=tk.X, padx=12, pady=12)

    icon_row = tk.Frame(body, bg=BG)
    icon_row.pack(fill=tk.X)

    PREV   = 56
    canvas = tk.Canvas(icon_row, width=PREV, height=PREV, bg=BG3,
                       highlightthickness=1, highlightbackground=SURFACE, cursor="hand2")
    canvas.pack(side=tk.LEFT, padx=(0, 12))
    canvas._photo = None
    canvas.create_text(PREV // 2, PREV // 2, text="🖼", font=("Sans", 20), fill=MUTED, tags="placeholder")

    icon_right = tk.Frame(icon_row, bg=BG)
    icon_right.pack(side=tk.LEFT, fill=tk.X, expand=True)

    def set_preview(img_data_or_url):
        try:
            from PIL import Image, ImageTk
            import urllib.request as _ureq
            if isinstance(img_data_or_url, bytes):
                img = Image.open(io.BytesIO(img_data_or_url))
            elif isinstance(img_data_or_url, str) and img_data_or_url.startswith(("http://", "https://")):
                req = _ureq.Request(img_data_or_url,
                      headers={"User-Agent": "Mozilla/5.0 pwa-create/1.0"})
                with _ureq.urlopen(req, timeout=6) as r:
                    img = Image.open(io.BytesIO(r.read()))
            else:
                img = Image.open(img_data_or_url)
            img   = img.convert("RGBA").resize((PREV - 4, PREV - 4), Image.LANCZOS)
            photo = ImageTk.PhotoImage(img)
            canvas._photo = photo
            canvas.delete("all")
            canvas.create_image(PREV // 2, PREV // 2, image=photo)
        except Exception:
            pass

    def clear_preview():
        canvas.delete("all")
        canvas.create_text(PREV // 2, PREV // 2, text="🖼", font=("Sans", 20), fill=MUTED, tags="placeholder")

    def browse():
        f = filedialog.askopenfilename(title=t("ui_icon_pick"),
            filetypes=[("Image", "*.png *.jpg *.jpeg *.webp *.ico *.svg")])
        if f:
            icon_var.set(f)
            set_preview(f)

    b_br = tk.Button(icon_right, text=t("ui_btn_browse"), font=FONT_SM, bg=BG3, fg=TEXT,
              activebackground=SURFACE, relief="flat", padx=10, pady=6, cursor="hand2", command=browse)
    b_br.bind("<Enter>", lambda e: b_br.configure(bg=SURFACE))
    b_br.bind("<Leave>", lambda e: b_br.configure(bg=BG3))
    b_br.pack(fill=tk.X, pady=(0, 4))

    _timer      = [None]
    _refreshing = [False]

    def fetch_preview(url: str):
        """icon.py'deki fetch_icon_from_page'i thread'de çağırır."""
        if not url.startswith(("http://", "https://")):
            url = "https://" + url

        def worker():
            from pwa_create.icon import fetch_icon_from_page
            result = fetch_icon_from_page(url)
            if result:
                root.after(0, lambda r=result: (_write_icon_url(r), set_preview(r)))

        threading.Thread(target=worker, daemon=True).start()

    def _write_icon_url(url: str):
        if not icon_var.get().strip():
            _refreshing[0] = True
            icon_var.set(url)
            root.after(100, _reset_refreshing)

    def _reset_refreshing():
        _refreshing[0] = False

    def on_url_change(*_):
        if icon_var.get().strip():
            return
        if _timer[0]:
            root.after_cancel(_timer[0])
        url = url_var.get().strip()
        if len(url) > 8:
            _timer[0] = root.after(700, lambda: fetch_preview(url))
        else:
            root.after(0, clear_preview)

    def on_icon_change(*_):
        if _refreshing[0]:
            return
        path = icon_var.get().strip()
        if not path:
            clear_preview()
        elif path.startswith(("http://", "https://")):
            set_preview(path)
        elif os.path.isfile(path):
            set_preview(path)

    def do_refresh():
        url = url_var.get().strip()
        if not url:
            return
        _refreshing[0] = True
        icon_var.set("")
        clear_preview()
        root.after(100, lambda: _do_fetch(url))

    def _do_fetch(url):
        _refreshing[0] = False
        fetch_preview(url)

    url_var.trace_add("write",  on_url_change)
    icon_var.trace_add("write", on_icon_change)

    if prefill_url:
        root.after(400, lambda: fetch_preview(prefill_url))

    canvas.bind("<Button-1>", lambda e: browse())

    b_rf = tk.Button(icon_right, text=t("ui_btn_refresh"), font=FONT_SM, bg=BG3, fg=ACCENT,
              activebackground=SURFACE, relief="flat", padx=10, pady=6, cursor="hand2", command=do_refresh)
    b_rf.bind("<Enter>", lambda e: b_rf.configure(bg=SURFACE))
    b_rf.bind("<Leave>", lambda e: b_rf.configure(bg=BG3))
    b_rf.pack(fill=tk.X)

    tk.Frame(root, bg=SURFACE, height=1).pack(fill=tk.X)

    btn_row = tk.Frame(root, bg=MANTLE, padx=36, pady=20)
    btn_row.pack(fill=tk.X)

    def do_ok():
        name = name_var.get().strip()
        url  = url_var.get().strip()
        icon = icon_var.get().strip()
        if not name:
            name_entry.focus_set()
            return
        if not url:
            url_entry.focus_set()
            return
        if not url.startswith(("http://", "https://")):
            url = "https://" + url
        result.update(name=name, url=url, icon=icon or None)
        root.destroy()

    def do_cancel():
        root.destroy()

    def make_btn(parent, text, bg, fg, abg, afg, cmd, side):
        b = tk.Button(parent, text=text, font=FONT_B, bg=bg, fg=fg, activebackground=abg,
                      activeforeground=afg, relief="flat", padx=24, pady=10, cursor="hand2", command=cmd)
        b.bind("<Enter>", lambda e: b.configure(bg=abg, fg=afg))
        b.bind("<Leave>", lambda e: b.configure(bg=bg,  fg=fg))
        b.pack(side=side, padx=(12 if side == tk.RIGHT else 0, 0))
        return b

    make_btn(btn_row, t("ui_btn_cancel"),  BG3,   SUBTEXT, SURFACE, TEXT,   do_cancel, tk.RIGHT)
    make_btn(btn_row, t("ui_btn_install"), ACCENT, MANTLE, MAUVE,   MANTLE, do_ok,     tk.RIGHT)

    root.bind("<Return>", lambda e: do_ok())
    root.bind("<Escape>", lambda e: do_cancel())
    name_entry.focus_set()

    root.update_idletasks()
    sw, sh = root.winfo_screenwidth(), root.winfo_screenheight()
    w,  h  = root.winfo_width(),       root.winfo_height()
    root.geometry(f"{w}x{h}+{(sw - w) // 2}+{(sh - h) // 2}")
    root.mainloop()

    return result if result.get("name") else None


def _tk_list(title: str, items: list[dict]) -> Optional[str]:
    import tkinter as tk
    from tkinter import ttk

    result = {}
    root   = tk.Tk()
    root.title(title)
    set_window_icon(root)
    root.configure(bg=BG)
    root.geometry("720x400")
    root.resizable(False, False)

    hdr = tk.Frame(root, bg=MANTLE, pady=16)
    hdr.pack(fill=tk.X)
    tk.Label(hdr, text=t("ui_remove_title"),    font=FONT_H,  bg=MANTLE, fg=RED).pack()
    tk.Label(hdr, text=t("ui_remove_subtitle"), font=FONT_SM, bg=MANTLE, fg=MUTED).pack(pady=(2, 0))

    tk.Frame(root, bg=SURFACE, height=1).pack(fill=tk.X)

    frame = tk.Frame(root, bg=BG, padx=36, pady=24)
    frame.pack(fill=tk.BOTH, expand=True)

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("PWA.Treeview", background=BG2, foreground=TEXT,
                    fieldbackground=BG2, rowheight=44, borderwidth=0, font=FONT)
    style.configure("PWA.Treeview.Heading", background=BG3, foreground=ACCENT,
                    font=FONT_B, borderwidth=0)
    style.map("PWA.Treeview", background=[("selected", ACCENT)], foreground=[("selected", MANTLE)])

    cols = ("name", "url", "browser")
    tree = ttk.Treeview(frame, columns=cols, show="headings",
                        style="PWA.Treeview", selectmode="browse")
    tree.heading("name",    text=t("ui_col_name"))
    tree.heading("url",     text="URL")
    tree.heading("browser", text=t("ui_col_browser"))
    tree.column("name",    width=160, anchor="w")
    tree.column("url",     width=340, anchor="w")
    tree.column("browser", width=100, anchor="center")

    tree.tag_configure("odd",  background=BG2)
    tree.tag_configure("even", background=BG)
    for i, item in enumerate(items):
        tag = "even" if i % 2 == 0 else "odd"
        tree.insert("", tk.END, iid=item["id"],
                    values=(item["name"], item["url"], item.get("browser", "-")), tags=(tag,))
    if items:
        tree.selection_set(items[0]["id"])
    tree.pack(fill=tk.BOTH, expand=True)

    tk.Frame(root, bg=SURFACE, height=1).pack(fill=tk.X)

    btn_row = tk.Frame(root, bg=MANTLE, padx=36, pady=20)
    btn_row.pack(fill=tk.X)

    def do_remove():
        sel = tree.selection()
        if sel:
            result["id"] = sel[0]
        root.destroy()

    def do_cancel():
        root.destroy()

    def make_btn(parent, text, bg, fg, abg, afg, cmd, side):
        b = tk.Button(parent, text=text, font=FONT_B, bg=bg, fg=fg, activebackground=abg,
                      activeforeground=afg, relief="flat", padx=24, pady=10, cursor="hand2", command=cmd)
        b.bind("<Enter>", lambda e: b.configure(bg=abg, fg=afg))
        b.bind("<Leave>", lambda e: b.configure(bg=bg,  fg=fg))
        b.pack(side=side, padx=(12 if side == tk.RIGHT else 0, 0))
        return b

    make_btn(btn_row, t("ui_btn_cancel"), BG3, SUBTEXT, SURFACE, TEXT,   do_cancel, tk.RIGHT)
    make_btn(btn_row, t("ui_btn_remove"), RED, MANTLE,  RED,     MANTLE, do_remove, tk.RIGHT)

    tree.bind("<Double-1>", lambda e: do_remove())
    root.bind("<Escape>",   lambda e: do_cancel())
    root.bind("<Return>",   lambda e: do_remove())

    root.update_idletasks()
    sw, sh = root.winfo_screenwidth(), root.winfo_screenheight()
    w,  h  = root.winfo_width(),       root.winfo_height()
    root.geometry(f"{w}x{h}+{(sw - w) // 2}+{(sh - h) // 2}")
    root.mainloop()
    return result.get("id")


def _tk_msg(title: str, message: str, kind: str = "info"):
    import re
    import tkinter as tk
    message = re.sub(r'\x1b\[[0-9;]*m', '', message)
    root    = tk.Tk()
    root.title(title)
    set_window_icon(root)
    root.configure(bg=BG)
    root.resizable(False, False)

    color = GREEN if kind == "info" else RED
    icon  = "✓" if kind == "info" else "✗"

    hdr = tk.Frame(root, bg=MANTLE, pady=18)
    hdr.pack(fill=tk.X)
    tk.Label(hdr, text=f"{icon}  {title}", font=FONT_H, bg=MANTLE, fg=color).pack()

    tk.Label(root, text=message, font=FONT, bg=BG, fg=TEXT,
             wraplength=420, justify="left", padx=24, pady=16).pack()

    tk.Frame(root, bg=SURFACE, height=1).pack(fill=tk.X)
    bf = tk.Frame(root, bg=BG2, padx=20, pady=12)
    bf.pack(fill=tk.X)
    b_ok = tk.Button(bf, text=t("ui_btn_ok"), font=FONT_B, bg=ACCENT, fg=MANTLE,
              activebackground=MAUVE, activeforeground=MANTLE, relief="flat", padx=24, pady=10,
              cursor="hand2", command=root.destroy)
    b_ok.bind("<Enter>", lambda e: b_ok.configure(bg=MAUVE))
    b_ok.bind("<Leave>", lambda e: b_ok.configure(bg=ACCENT))
    b_ok.pack(side=tk.RIGHT)

    root.update_idletasks()
    sw, sh = root.winfo_screenwidth(), root.winfo_screenheight()
    w,  h  = root.winfo_width(),       root.winfo_height()
    root.geometry(f"{w}x{h}+{(sw - w) // 2}+{(sh - h) // 2}")
    root.mainloop()


def _tk_question(title: str, message: str) -> bool:
    import tkinter as tk
    result = {"v": False}
    root   = tk.Tk()
    root.title(title)
    set_window_icon(root)
    root.configure(bg=BG)
    root.resizable(False, False)

    hdr = tk.Frame(root, bg=MANTLE, pady=18)
    hdr.pack(fill=tk.X)
    tk.Label(hdr, text=f"❓  {title}", font=FONT_H, bg=MANTLE, fg=ACCENT).pack()
    tk.Label(root, text=message, font=FONT_SH, bg=BG, fg=TEXT,
             wraplength=380, justify="center", pady=16).pack(padx=24)

    tk.Frame(root, bg=SURFACE, height=1).pack(fill=tk.X)
    bf = tk.Frame(root, bg=BG2, padx=20, pady=12)
    bf.pack(fill=tk.X)

    def yes(): result["v"] = True;  root.destroy()
    def no():  result["v"] = False; root.destroy()

    def make_btn(parent, text, bg, fg, abg, afg, cmd, side):
        b = tk.Button(parent, text=text, font=FONT_B, bg=bg, fg=fg, activebackground=abg,
                      activeforeground=afg, relief="flat", padx=24, pady=10, cursor="hand2", command=cmd)
        b.bind("<Enter>", lambda e: b.configure(bg=abg, fg=afg))
        b.bind("<Leave>", lambda e: b.configure(bg=bg,  fg=fg))
        b.pack(side=side, padx=(12 if side == tk.RIGHT else 0, 0))
        return b

    make_btn(bf, t("ui_btn_no"),  BG3,   SUBTEXT, SURFACE, TEXT,   no,  tk.RIGHT)
    make_btn(bf, t("ui_btn_yes"), ACCENT, MANTLE, MAUVE,   MANTLE, yes, tk.RIGHT)

    root.bind("<Return>", lambda e: yes())
    root.bind("<Escape>", lambda e: no())
    root.update_idletasks()
    sw, sh = root.winfo_screenwidth(), root.winfo_screenheight()
    w,  h  = root.winfo_width(),       root.winfo_height()
    root.geometry(f"{w}x{h}+{(sw - w) // 2}+{(sh - h) // 2}")
    root.mainloop()
    return result["v"]


def _zenity(*args):
    try:
        r = subprocess.run(["zenity", *args], capture_output=True, text=True)
        return r.returncode, r.stdout.strip()
    except Exception:
        return 1, ""


def _kdialog(*args):
    try:
        r = subprocess.run(["kdialog", *args], capture_output=True, text=True)
        return r.returncode, r.stdout.strip()
    except Exception:
        return 1, ""


def _zenity_install_form(n, u):
    rc, out = _zenity("--forms", f"--title={t('ui_install_title')}",
                      f"--text={t('ui_install_subtitle')}",
                      f"--add-entry={t('ui_field_name')}{(':' + n) if n else ''}",
                      f"--add-entry=URL{(':' + u) if u else ''}",
                      f"--add-entry={t('ui_field_icon')}",
                      "--separator=|", "--width=480")
    if rc != 0:
        return None
    p = (out.split("|") + ["", "", ""])[:3]
    name, url, icon = p[0].strip() or n, p[1].strip() or u, p[2].strip()
    return {"name": name, "url": url, "icon": icon or None} if name and url else None


def _zenity_list(title, items):
    args = ["--list", f"--title={title}", f"--text={t('ui_remove_subtitle')}",
            "--column=ID", f"--column={t('ui_col_name')}", "--column=URL",
            "--hide-column=1", "--width=640", "--height=360"]
    for i in items:
        args += [i["id"], i["name"], i["url"]]
    rc, out = _zenity(*args)
    return out if rc == 0 else None


def _kdialog_install_form(n, u):
    rc, name = _kdialog("--inputbox", t("ui_field_name"), n or "", "--title", t("ui_install_title"))
    if rc:
        return None
    rc, url = _kdialog("--inputbox", "URL", u or "", "--title", t("ui_install_title"))
    if rc:
        return None
    _, icon = _kdialog("--inputbox", t("ui_field_icon"), "", "--title", t("ui_install_title"))
    return {"name": name.strip(), "url": url.strip(), "icon": icon.strip() or None} if name and url else None


def _kdialog_list(title, items):
    args = ["--menu", t("ui_remove_subtitle"), "--title", title]
    for i in items:
        args += [i["id"], f"{i['name']} — {i['url']}"]
    rc, out = _kdialog(*args)
    return out if rc == 0 else None