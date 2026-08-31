import tkinter as tk

# ---------- Colors & Fonts ----------
BG_COLOR = "#1e1e2f"
CARD_COLOR = "#2a2a40"
ACCENT = "#7c5cff"
TEXT_COLOR = "#f5f5f5"
SUBTEXT_COLOR = "#a0a0b8"
ERROR_COLOR = "#ff6b6b"
SUCCESS_COLOR = "#4ade80"

FONT_HEADER = ("Segoe UI", 24, "bold")
FONT_LABEL = ("Segoe UI", 13)
FONT_ENTRY = ("Segoe UI", 14)
FONT_RESULT = ("Segoe UI", 16, "bold")
FONT_BUTTON = ("Segoe UI", 16, "bold")

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("480x560")
root.resizable(False, False)
root.configure(bg=BG_COLOR)

# ---------- Header ----------
header_label = tk.Label(root, text="Simple Calculator", font=FONT_HEADER, bg=BG_COLOR, fg=TEXT_COLOR)
header_label.pack(pady=(30, 20))

# ---------- Card container ----------
card = tk.Frame(root, bg=CARD_COLOR, padx=30, pady=30)
card.pack(padx=30, fill="both", expand=True)

# ---------- Input fields ----------
tk.Label(card, text="Value 1", font=FONT_LABEL, bg=CARD_COLOR, fg=SUBTEXT_COLOR).grid(
    row=0, column=0, sticky="w", pady=(0, 5)
)
val1_entry = tk.Entry(
    card, font=FONT_ENTRY, bg="#3a3a55", fg=TEXT_COLOR, insertbackground=TEXT_COLOR,
    relief="flat", justify="center"
)
val1_entry.grid(row=1, column=0, columnspan=2, sticky="ew", ipady=8, pady=(0, 15))

tk.Label(card, text="Value 2", font=FONT_LABEL, bg=CARD_COLOR, fg=SUBTEXT_COLOR).grid(
    row=2, column=0, sticky="w", pady=(0, 5)
)
val2_entry = tk.Entry(
    card, font=FONT_ENTRY, bg="#3a3a55", fg=TEXT_COLOR, insertbackground=TEXT_COLOR,
    relief="flat", justify="center"
)
val2_entry.grid(row=3, column=0, columnspan=2, sticky="ew", ipady=8, pady=(0, 20))

card.grid_columnconfigure(0, weight=1)
card.grid_columnconfigure(1, weight=1)

# ---------- Result display ----------
result_label = tk.Label(
    card, text="Result will appear here", font=FONT_RESULT, bg="#3a3a55", fg=TEXT_COLOR,
    wraplength=360, pady=15
)
result_label.grid(row=4, column=0, columnspan=2, sticky="ew", pady=(0, 20))


def get_values():
    val1 = float(val1_entry.get())
    val2 = float(val2_entry.get())
    return val1, val2


def show_result(text, color=TEXT_COLOR):
    result_label.config(text=text, fg=color, bg="#3a3a55")


def add():
    try:
        val1, val2 = get_values()
        show_result(f"{val1:g} + {val2:g} = {val1 + val2:g}", SUCCESS_COLOR)
    except ValueError:
        show_result("Please enter valid numbers!", ERROR_COLOR)


def subtract():
    try:
        val1, val2 = get_values()
        show_result(f"{val1:g} - {val2:g} = {val1 - val2:g}", SUCCESS_COLOR)
    except ValueError:
        show_result("Please enter valid numbers!", ERROR_COLOR)


def multiply():
    try:
        val1, val2 = get_values()
        show_result(f"{val1:g} x {val2:g} = {val1 * val2:g}", SUCCESS_COLOR)
    except ValueError:
        show_result("Please enter valid numbers!", ERROR_COLOR)


def divide():
    try:
        val1, val2 = get_values()
        result = val1 / val2
        show_result(f"{val1:g} \u00f7 {val2:g} = {result:g}", SUCCESS_COLOR)
    except ValueError:
        show_result("Please enter valid numbers!", ERROR_COLOR)
    except ZeroDivisionError:
        show_result("Error, cannot divide by zero!", ERROR_COLOR)


# ---------- Styled operation buttons ----------
def make_button(parent, text, command):
    btn = tk.Button(
        parent, text=text, font=FONT_BUTTON, command=command,
        bg=ACCENT, fg="white", activebackground="#6a4ce0", activeforeground="white",
        relief="flat", bd=0, cursor="hand2"
    )
    btn.bind("<Enter>", lambda e: btn.config(bg="#6a4ce0"))
    btn.bind("<Leave>", lambda e: btn.config(bg=ACCENT))
    return btn


button_frame = tk.Frame(card, bg=CARD_COLOR)
button_frame.grid(row=5, column=0, columnspan=2, sticky="ew")
button_frame.grid_columnconfigure(0, weight=1)
button_frame.grid_columnconfigure(1, weight=1)

add_button = make_button(button_frame, "+", add)
add_button.grid(row=0, column=0, sticky="ew", padx=(0, 5), pady=(0, 10), ipady=12)

sub_button = make_button(button_frame, "\u2212", subtract)
sub_button.grid(row=0, column=1, sticky="ew", padx=(5, 0), pady=(0, 10), ipady=12)

mul_button = make_button(button_frame, "\u00d7", multiply)
mul_button.grid(row=1, column=0, sticky="ew", padx=(0, 5), ipady=12)

div_button = make_button(button_frame, "\u00f7", divide)
div_button.grid(row=1, column=1, sticky="ew", padx=(5, 0), ipady=12)

root.mainloop()
