import tkinter as tk
import winsound  # For sound on toggle (Windows only)

root = tk.Tk()
root.title("Fake Cheat Panel")
root.geometry("500x500")
root.configure(background="#2c2c2c")
root.resizable(False, False)

# Sound effect (beep)
def play_beep():
    winsound.Beep(800, 50)  # (frequency, duration)

# Feature names
features = ["AIMBOT", "ESP", "RapidFire", "Bhop", "Triggerbot"]
statuses = {}
labels = {}
buttons = {}

LABEL_FONT = ("Segoe UI", 20)
BUTTON_FONT = ("Segoe UI", 18)

# Toggle function
def toggle_feature(name):
    statuses[name] = "ON" if statuses[name] == "OFF" else "OFF"
    labels[name].config(
        text=f"{name}: {statuses[name]}",
        fg="#00ff00" if statuses[name] == "ON" else "#ff0000"
    )
    play_beep()

# --- Title Label ---
title_label = tk.Label(
    root, text="Fake Cheat Toggle Menu",
    fg="#ffffff", bg="#2c2c2c",
    font=("Segoe UI", 26, "bold")
)
title_label.pack(pady=(20, 10))

# --- Button/Label Frame ---
frame = tk.Frame(root, bg="#3a3a3a", bd=4, relief="groove")
frame.pack(pady=10)

# --- Create Labels & Buttons Dynamically ---
for i, feature in enumerate(features):
    statuses[feature] = "OFF"

    labels[feature] = tk.Label(
        frame,
        text=f"{feature}: OFF",
        fg="#ff0000",
        bg="#3a3a3a",
        font=LABEL_FONT,
        anchor="w",
        width=15
    )
    labels[feature].grid(row=i, column=0, padx=10, pady=6, sticky="w")

    buttons[feature] = tk.Button(
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
    )
    buttons[feature].grid(row=i, column=1, padx=10, pady=6)

# --- Final Run ---
root.mainloop()
