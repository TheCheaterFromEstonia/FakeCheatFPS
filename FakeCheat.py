import tkinter as tk

# --- Constants ---
WINDOW_TITLE = "Mercury"
WINDOW_SIZE = "710x500"
BG_COLOR = "#2c2c2c"
FRAME_BG = "#3a3a3a"
LABEL_FONT = ("Segoe UI", 20)
BUTTON_FONT = ("Segoe UI", 18)
FEATURES = ["AIMBOT", "ESP", "RapidFire", "Bhop", "Triggerbot"]

# --- GUI Setup ---
root = tk.Tk()
root.title(WINDOW_TITLE)
root.geometry(WINDOW_SIZE)
root.configure(background=BG_COLOR)
root.resizable(True, True)

# --- UI Element Containers ---
statuses = {feature: "OFF" for feature in FEATURES}
labels = {}

# --- Toggle Function ---
def toggle_feature(name):
    statuses[name] = "ON" if statuses[name] == "OFF" else "OFF"
    labels[name].config(
        text=f"{name}: {statuses[name]}",
        fg="#00ff00" if statuses[name] == "ON" else "#ff0000"
    )

# --- Title ---
tk.Label(
    root, text=WINDOW_TITLE,
    fg="#ffffff", bg=BG_COLOR,
    font=("Segoe UI", 26, "bold")
).pack(pady=(20, 10))

# --- Frame for Buttons/Labels ---
frame = tk.Frame(root, bg=FRAME_BG, bd=4, relief="groove")
frame.pack(pady=10)

# --- Feature Rows ---
for i, feature in enumerate(FEATURES):
    labels[feature] = tk.Label(
        frame,
        text=f"{feature}: OFF",
        fg="#ff0000",
        bg=FRAME_BG,
        font=LABEL_FONT,
        anchor="w",
        width=15
    )
    labels[feature].grid(row=i, column=0, padx=10, pady=6, sticky="w")

    tk.Button(
        frame,
        text="Enable/Disable",
        fg="#ffffff",
        bg="#545454",
        activebackground="#3d3d3d",
        activeforeground="#00ff00",
        font=BUTTON_FONT,
        command=lambda f=feature: toggle_feature(f),
        bd=3,
        relief="solid",
        highlightthickness=2,
        highlightbackground="#000000",
        width=15
    ).grid(row=i, column=1, padx=10, pady=6)

# --- Start GUI Loop ---
root.mainloop()
