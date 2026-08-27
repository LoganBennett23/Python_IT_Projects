"""
SecurePass // Password Generator
--------------------------------
The GUI version of my PASS_CG Program. 
With my Python skills, AI assistance, and creativity,
I aim to provide a secure and user-friendly password generation experience. 
May use cryptography module later for enhanced security

Enjoy :)

"""

#Modules imported
import secrets
import string
import tkinter as tk
from tkinter import ttk, messagebox


# --------------------------------------------------------------------------
# Word list
# --------------------------------------------------------------------------

DEFAULT_WORDS = [
    "war", "peace", "love", "hate", "friendship", "betrayal", "courage", "fear",
    "hope", "despair", "joy", "sorrow", "freedom", "oppression",
    "truth", "lies", "light", "darkness", "life", "death",
    "music", "art", "science", "technology", "nature", "society",
    "history", "future", "dreams", "reality", "imagination",
    "soldier", "king", "queen", "prince", "princess", "knight", "wizard",
    "dragon", "castle", "forest", "mountain", "river", "ocean", "desert", "island",
    "city", "village", "temple", "palace",
    "apple", "banana", "cherry", "date", "fig", "grape", "kiwi", "lemon", "mango",
    "nectarine", "orange", "papaya", "quince", "raspberry", "strawberry",
    "tangerine", "watermelon",
]


# --------------------------------------------------------------------------
# Theme
# --------------------------------------------------------------------------

BG = "#0a0e14"
BG_PANEL = "#0f1620"
BG_FIELD = "#111a24"
FG = "#c9d1d9"
FG_DIM = "#6b7785"
ACCENT = "#00ff9c"
ACCENT2 = "#00d9ff"
DANGER = "#ff496a"
WARN = "#ffb454"
BORDER = "#1e2a36"

FONT_MONO = ("Consolas", 11)
FONT_MONO_SM = ("Consolas", 9)
FONT_MONO_BOLD = ("Consolas", 12, "bold")
FONT_TITLE = ("Consolas", 19, "bold")
FONT_NAV = ("Consolas", 11, "bold")


# --------------------------------------------------------------------------
# Password generation
# --------------------------------------------------------------------------

def generate_secure_password(length, use_upper, use_lower, use_digits, use_symbols):
    pools = []

    if use_upper:
        pools.append(string.ascii_uppercase)

    if use_lower:
        pools.append(string.ascii_lowercase)

    if use_digits:
        pools.append(string.digits)

    if use_symbols:
        pools.append(string.punctuation)

    if not pools:
        raise ValueError("Select at least one character type.")

    if length < 1:
        raise ValueError("Password length must be at least 1.")

    all_chars = "".join(pools)

    if length < len(pools):
        chars = [secrets.choice(all_chars) for _ in range(length)]
    else:
        # Guarantee at least one character from every selected type.
        chars = [secrets.choice(pool) for pool in pools]
        chars += [
            secrets.choice(all_chars)
            for _ in range(length - len(chars))
        ]

    # Securely shuffle the password characters.
    for i in range(len(chars) - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        chars[i], chars[j] = chars[j], chars[i]

    return "".join(chars)


# --------------------------------------------------------------------------
# Memorable password generation
# --------------------------------------------------------------------------
def generate_memorable_password(
    words, num_words, add_number, add_symbol, separator=""
):
    parts = [secrets.choice(words) for _ in range(num_words)]
    password = separator.join(parts)

    if add_number:
        password += str(secrets.randbelow(10))

    if add_symbol:
        password += secrets.choice(string.punctuation)

    return password

# --------------------------------------------------------------------------
# Password evaluation
# --------------------------------------------------------------------------    
def evaluate_password(password):
    checks = [
        ("At least 12 characters", len(password) >= 12),
        ("At least 8 characters", len(password) >= 8),
        ("Contains an uppercase letter", any(c.isupper() for c in password)),
        ("Contains a lowercase letter", any(c.islower() for c in password)),
        ("Contains a digit", any(c.isdigit() for c in password)),
        ("Contains a special character", any(c in string.punctuation for c in password)),
    ]

    # Score out of 5:
    # length >= 12, uppercase, lowercase, digit, special character.
    score = sum(
        passed
        for label, passed in checks
        if label != "At least 8 characters"
    )

    return checks, score


# --------------------------------------------------------------------------
# Shared widgets
# --------------------------------------------------------------------------

def section_title(parent, text):
    return ttk.Label(parent, text=text, style="Title.TLabel")


def result_box(parent):
    var = tk.StringVar(value="")

    entry = tk.Entry(
        parent,
        textvariable=var,
        font=FONT_MONO_BOLD,
        fg=ACCENT,
        bg=BG_FIELD,
        insertbackground=ACCENT,
        relief="flat",
        justify="center",
        readonlybackground=BG_FIELD,
    )

    entry.configure(state="readonly")
    return entry, var


def copy_to_clipboard(app, text):
    if not text:
        return

    app.clipboard_clear()
    app.clipboard_append(text)
    messagebox.showinfo("Copied", "Password copied to clipboard.")


# --------------------------------------------------------------------------
# Main application
# --------------------------------------------------------------------------

class PasswordApp(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("SecurePass // Password Generator")
        self.geometry("880x600")
        self.minsize(820, 560)
        self.configure(bg=BG)

        self._build_style()
        self._build_layout()

        self.show_frame("generate")

    # ----------------------------------------------------------------------
    # Styling
    # ----------------------------------------------------------------------

    def _build_style(self):
        style = ttk.Style(self)
        style.theme_use("clam")

        style.configure("TFrame", background=BG_PANEL)
        style.configure("Root.TFrame", background=BG)

        style.configure(
            "TLabel",
            background=BG_PANEL,
            foreground=FG,
            font=FONT_MONO,
        )

        style.configure(
            "Title.TLabel",
            background=BG_PANEL,
            foreground=ACCENT,
            font=FONT_TITLE,
        )

        style.configure(
            "Dim.TLabel",
            background=BG_PANEL,
            foreground=FG_DIM,
            font=FONT_MONO_SM,
        )

        style.configure(
            "Nav.TFrame",
            background="#060a10",
        )

        style.configure(
            "TCheckbutton",
            background=BG_PANEL,
            foreground=FG,
            font=FONT_MONO,
            focuscolor=BG_PANEL,
        )

        style.map(
            "TCheckbutton",
            background=[("active", BG_PANEL)],
        )

        style.configure(
            "TRadiobutton",
            background=BG_PANEL,
            foreground=FG,
            font=FONT_MONO,
            focuscolor=BG_PANEL,
        )

        style.map(
            "TRadiobutton",
            background=[("active", BG_PANEL)],
        )

        style.configure(
            "Accent.TButton",
            background=ACCENT,
            foreground="#04140d",
            font=FONT_MONO_BOLD,
            borderwidth=0,
            focusthickness=0,
            padding=8,
        )

        style.map(
            "Accent.TButton",
            background=[("active", "#00d488")],
        )

        style.configure(
            "Secondary.TButton",
            background=BG_FIELD,
            foreground=ACCENT2,
            font=FONT_MONO,
            borderwidth=1,
            focusthickness=0,
            padding=6,
        )

        style.map(
            "Secondary.TButton",
            background=[("active", "#16222e")],
        )

        style.configure(
            "Nav.TButton",
            background="#060a10",
            foreground=FG_DIM,
            font=FONT_NAV,
            borderwidth=0,
            padding=12,
            anchor="w",
        )

        style.map(
            "Nav.TButton",
            background=[("active", "#0e1620")],
            foreground=[("active", ACCENT2)],
        )

        style.configure(
            "NavActive.TButton",
            background="#0e1620",
            foreground=ACCENT,
            font=FONT_NAV,
            borderwidth=0,
            padding=12,
            anchor="w",
        )

    # ----------------------------------------------------------------------
    # Layout
    # ----------------------------------------------------------------------

    def _build_layout(self):
        root = ttk.Frame(self, style="Root.TFrame")
        root.pack(fill="both", expand=True)

        # Sidebar
        self.nav = ttk.Frame(
            root,
            style="Nav.TFrame",
            width=210,
        )

        self.nav.pack(side="left", fill="y")
        self.nav.pack_propagate(False)

        header = tk.Label(
            self.nav,
            text="🔐 SecurePass",
            bg="#060a10",
            fg=ACCENT,
            font=("Consolas", 15, "bold"),
            pady=24,
        )

        header.pack(fill="x")

        self.nav_buttons = {}

        nav_items = [
            ("generate", "⚡ Generate"),
            ("memorable", "🧩 Memorable"),
            ("check", "🛡  Check Strength"),
        ]

        for key, label in nav_items:
            btn = ttk.Button(
                self.nav,
                text=label,
                style="Nav.TButton",
                command=lambda k=key: self.show_frame(k),
            )

            btn.pack(fill="x")
            self.nav_buttons[key] = btn

        footer = tk.Label(
            self.nav,
            bg="#060a10",
            fg=FG_DIM,
            font=FONT_MONO_SM,
            justify="left",
            pady=20,
        )

        footer.pack(
            side="bottom",
            fill="x",
            padx=12,
        )

        # Content area
        self.content = tk.Frame(
            root,
            bg=BG_PANEL,
        )

        self.content.pack(
            side="left",
            fill="both",
            expand=True,
        )

        self.frames = {
            "generate": GeneratePanel(self.content, self),
            "memorable": MemorablePanel(self.content, self),
            "check": CheckPanel(self.content, self),
        }

        for frame in self.frames.values():
            frame.place(
                x=0,
                y=0,
                relwidth=1,
                relheight=1,
            )

    def show_frame(self, key):
        for k, btn in self.nav_buttons.items():
            btn.configure(
                style="NavActive.TButton" if k == key else "Nav.TButton"
            )

        self.frames[key].tkraise()


# --------------------------------------------------------------------------
# Generate panel
# --------------------------------------------------------------------------

class GeneratePanel(tk.Frame):

    def __init__(self, parent, app):
        super().__init__(parent, bg=BG_PANEL)

        self.app = app
        pad = {"padx": 30, "pady": 8}

        section_title(
            self,
            "⚡ Generate a Secure Password",
        ).pack(anchor="w", **pad)

        ttk.Label(
            self,
            style="Dim.TLabel",
        ).pack(anchor="w", padx=30)

        opts = ttk.Frame(
            self,
            style="TFrame",
        )

        opts.pack(
            fill="x",
            padx=30,
            pady=20,
        )

        ttk.Label(
            opts,
            text="Length:",
        ).grid(
            row=0,
            column=0,
            sticky="w",
            pady=6,
        )

        self.length_var = tk.IntVar(value=16)

        length_spin = ttk.Spinbox(
            opts,
            from_=4,
            to=128,
            textvariable=self.length_var,
            width=6,
        )

        length_spin.grid(
            row=0,
            column=1,
            sticky="w",
            padx=10,
        )

        self.use_upper = tk.BooleanVar(value=True)
        self.use_lower = tk.BooleanVar(value=True)
        self.use_digits = tk.BooleanVar(value=True)
        self.use_symbols = tk.BooleanVar(value=True)

        ttk.Checkbutton(
            opts,
            text="Uppercase (A-Z)",
            variable=self.use_upper,
        ).grid(row=1, column=0, sticky="w", pady=4)

        ttk.Checkbutton(
            opts,
            text="Lowercase (a-z)",
            variable=self.use_lower,
        ).grid(row=1, column=1, sticky="w", pady=4)

        ttk.Checkbutton(
            opts,
            text="Digits (0-9)",
            variable=self.use_digits,
        ).grid(row=2, column=0, sticky="w", pady=4)

        ttk.Checkbutton(
            opts,
            text="Symbols (!@#$...)",
            variable=self.use_symbols,
        ).grid(row=2, column=1, sticky="w", pady=4)

        ttk.Button(
            self,
            text="GENERATE",
            style="Accent.TButton",
            command=self.generate,
        ).pack(
            padx=30,
            pady=(10, 4),
            anchor="w",
        )

        self.result_entry, self.result_var = result_box(self)

        self.result_entry.pack(
            fill="x",
            padx=30,
            pady=10,
            ipady=8,
        )

        btn_row = ttk.Frame(
            self,
            style="TFrame",
        )

        btn_row.pack(
            fill="x",
            padx=30,
        )

        ttk.Button(
            btn_row,
            text="Copy",
            style="Secondary.TButton",
            command=lambda: copy_to_clipboard(
                self.app,
                self.result_var.get(),
            ),
        ).pack(side="left")

        self.strength_label = ttk.Label(
            self,
            text="",
            style="Dim.TLabel",
        )

        self.strength_label.pack(
            anchor="w",
            padx=30,
            pady=(16, 0),
        )

    def generate(self):
        try:
            pw = generate_secure_password(
                self.length_var.get(),
                self.use_upper.get(),
                self.use_lower.get(),
                self.use_digits.get(),
                self.use_symbols.get(),
            )

        except ValueError as e:
            messagebox.showerror(
                "Cannot generate",
                str(e),
            )
            return

        self.result_var.set(pw)

        _, score = evaluate_password(pw)

        self.strength_label.configure(
            text=f"Estimated strength: {score}/5"
        )


# --------------------------------------------------------------------------
# Memorable password panel
# --------------------------------------------------------------------------

class MemorablePanel(tk.Frame):

    def __init__(self, parent, app):
        super().__init__(parent, bg=BG_PANEL)

        self.app = app
        pad = {"padx": 30, "pady": 8}

        section_title(
            self,
            "🧩 Memorable Password",
        ).pack(anchor="w", **pad)

        ttk.Label(
            self,
            style="Dim.TLabel",
        ).pack(anchor="w", padx=30)

        self.source_var = tk.StringVar(value="default")

        src_row = ttk.Frame(
            self,
            style="TFrame",
        )

        src_row.pack(
            fill="x",
            padx=30,
            pady=(16, 4),
        )

        ttk.Radiobutton(
            src_row,
            text="Default word list",
            variable=self.source_var,
            value="default",
            command=self._toggle_custom,
        ).pack(side="left")

        ttk.Radiobutton(
            src_row,
            text="Custom word list",
            variable=self.source_var,
            value="custom",
            command=self._toggle_custom,
        ).pack(side="left", padx=20)

        self.custom_text = tk.Text(
            self,
            height=3,
            bg=BG_FIELD,
            fg=ACCENT2,
            insertbackground=ACCENT2,
            font=FONT_MONO_SM,
            relief="flat",
        )

        self.custom_text.insert(
            "1.0",
            "e.g. tiger, umbrella, coffee, comet",
        )

        self.custom_text.configure(state="disabled")

        self.custom_text.pack(
            fill="x",
            padx=30,
            pady=6,
        )

        opts = ttk.Frame(
            self,
            style="TFrame",
        )

        opts.pack(
            fill="x",
            padx=30,
            pady=10,
        )

        ttk.Label(
            opts,
            text="Number of words:",
        ).grid(
            row=0,
            column=0,
            sticky="w",
            pady=4,
        )

        self.num_words_var = tk.IntVar(value=3)

        ttk.Spinbox(
            opts,
            from_=1,
            to=10,
            textvariable=self.num_words_var,
            width=5,
        ).grid(
            row=0,
            column=1,
            sticky="w",
            padx=10,
        )

        ttk.Label(
            opts,
            text="Separator:",
        ).grid(
            row=0,
            column=2,
            sticky="w",
            padx=(30, 0),
        )

        self.sep_var = tk.StringVar(value="-")

        ttk.Entry(
            opts,
            textvariable=self.sep_var,
            width=5,
        ).grid(
            row=0,
            column=3,
            sticky="w",
            padx=10,
        )

        self.add_number = tk.BooleanVar(value=True)
        self.add_symbol = tk.BooleanVar(value=True)

        ttk.Checkbutton(
            opts,
            text="Append a digit",
            variable=self.add_number,
        ).grid(
            row=1,
            column=0,
            columnspan=2,
            sticky="w",
            pady=6,
        )

        ttk.Checkbutton(
            opts,
            text="Append a symbol",
            variable=self.add_symbol,
        ).grid(
            row=1,
            column=2,
            columnspan=2,
            sticky="w",
            pady=6,
        )

        ttk.Button(
            self,
            text="GENERATE",
            style="Accent.TButton",
            command=self.generate,
        ).pack(
            padx=30,
            pady=(10, 4),
            anchor="w",
        )

        self.result_entry, self.result_var = result_box(self)

        self.result_entry.pack(
            fill="x",
            padx=30,
            pady=10,
            ipady=8,
        )

        btn_row = ttk.Frame(
            self,
            style="TFrame",
        )

        btn_row.pack(
            fill="x",
            padx=30,
        )

        ttk.Button(
            btn_row,
            text="Copy",
            style="Secondary.TButton",
            command=lambda: copy_to_clipboard(
                self.app,
                self.result_var.get(),
            ),
        ).pack(side="left")

    def _toggle_custom(self):
        if self.source_var.get() == "custom":
            self.custom_text.configure(state="normal")

            if self.custom_text.get("1.0", "end").strip().startswith("e.g."):
                self.custom_text.delete("1.0", "end")

        else:
            self.custom_text.configure(state="disabled")

    def generate(self):
        if self.source_var.get() == "custom":
            raw = self.custom_text.get(
                "1.0",
                "end",
            ).strip()

            words = [
                w.strip()
                for w in raw.split(",")
                if w.strip()
            ]

            if not words:
                messagebox.showerror(
                    "No words",
                    "Enter at least one custom word.",
                )
                return

        else:
            words = DEFAULT_WORDS

        try:
            num_words = self.num_words_var.get()

            if num_words < 1:
                raise ValueError("Number of words must be at least 1.")

            pw = generate_memorable_password(
                words,
                num_words,
                self.add_number.get(),
                self.add_symbol.get(),
                separator=self.sep_var.get(),
            )

        except (ValueError, tk.TclError) as e:
            messagebox.showerror(
                "Cannot generate",
                str(e),
            )
            return

        self.result_var.set(pw)


# --------------------------------------------------------------------------
# Password strength panel
# --------------------------------------------------------------------------

class CheckPanel(tk.Frame):

    def __init__(self, parent, app):
        super().__init__(parent, bg=BG_PANEL)

        self.app = app

        section_title(
            self,
            "🛡  Check Password Strength",
        ).pack(
            anchor="w",
            padx=30,
            pady=8,
        )

        ttk.Label(
            self,
            text="Nothing you type here is saved or transmitted.",
            style="Dim.TLabel",
        ).pack(
            anchor="w",
            padx=30,
        )

        row = ttk.Frame(
            self,
            style="TFrame",
        )

        row.pack(
            fill="x",
            padx=30,
            pady=20,
        )

        self.show_var = tk.BooleanVar(value=False)
        self.pw_var = tk.StringVar()

        self.entry = ttk.Entry(
            row,
            textvariable=self.pw_var,
            show="•",
            font=FONT_MONO,
            width=40,
        )

        self.entry.pack(
            side="left",
            ipady=6,
        )

        ttk.Checkbutton(
            row,
            text="Show",
            variable=self.show_var,
            command=self._toggle_show,
        ).pack(
            side="left",
            padx=10,
        )

        ttk.Button(
            row,
            text="Check",
            style="Accent.TButton",
            command=self.check,
        ).pack(
            side="left",
            padx=10,
        )

        self.results_frame = ttk.Frame(
            self,
            style="TFrame",
        )

        self.results_frame.pack(
            fill="x",
            padx=30,
            pady=10,
        )

        self.bar_canvas = tk.Canvas(
            self,
            height=14,
            bg=BG_FIELD,
            highlightthickness=0,
        )

        self.bar_canvas.pack(
            fill="x",
            padx=30,
            pady=(10, 0),
        )

        self.score_label = ttk.Label(
            self,
            text="",
            style="Dim.TLabel",
        )

        self.score_label.pack(
            anchor="w",
            padx=30,
            pady=(6, 0),
        )

    def _toggle_show(self):
        self.entry.configure(
            show="" if self.show_var.get() else "•"
        )

    def check(self):
        pw = self.pw_var.get()

        for widget in self.results_frame.winfo_children():
            widget.destroy()

        if not pw:
            messagebox.showwarning(
                "Empty",
                "Enter a password to check.",
            )
            return

        checks, score = evaluate_password(pw)

        for label, passed in checks:
            mark = "✔" if passed else "✘"
            color = ACCENT if passed else DANGER

            row = tk.Label(
                self.results_frame,
                text=f"{mark}  {label}",
                bg=BG_PANEL,
                fg=color,
                font=FONT_MONO,
                anchor="w",
            )

            row.pack(
                fill="x",
                pady=2,
            )

        self.bar_canvas.delete("all")

        width = self.bar_canvas.winfo_width() or 700
        pct = score / 5

        colors = [
            DANGER,
            DANGER,
            WARN,
            WARN,
            ACCENT,
            ACCENT,
        ]

        self.bar_canvas.create_rectangle(
            0,
            0,
            width,
            14,
            fill=BG_FIELD,
            outline="",
        )

        self.bar_canvas.create_rectangle(
            0,
            0,
            int(width * pct),
            14,
            fill=colors[score],
            outline="",
        )

        labels = {
            0: "Very weak",
            1: "Weak",
            2: "Fair",
            3: "Good",
            4: "Strong",
            5: "Excellent",
        }

        self.score_label.configure(
            text=f"Strength: {labels[score]} ({score}/5)"
        )


# --------------------------------------------------------------------------
# Start application
# --------------------------------------------------------------------------

if __name__ == "__main__":
    app = PasswordApp()
    app.mainloop()
