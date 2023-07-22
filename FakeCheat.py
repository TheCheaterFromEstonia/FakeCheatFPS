import tkinter as tk

root = tk.Tk()
root.geometry("640x360")
root.configure(background="#000000")

def toggle_aimbot():
    global aimbot_status
    aimbot_status = "ON" if aimbot_status == "OFF" else "OFF"
    label_aimbot.config(text=f"AIMBOT:{aimbot_status}", fg="#00ff00" if aimbot_status == "ON" else "#ff0000",
                        bg="#000000", highlightbackground="#ffffff")

def toggle_esp():
    global esp_status
    esp_status = "ON" if esp_status == "OFF" else "OFF"
    label_esp.config(text=f"ESP:{esp_status}", fg="#00ff00" if esp_status == "ON" else "#ff0000",
                     bg="#000000", highlightbackground="#ffffff")

aimbot_status = "OFF"
esp_status = "OFF"

label_aimbot = tk.Label(root, text="AIMBOT:OFF", fg="#ffffff", bg="black", font=("Arial", 16))
label_esp = tk.Label(root, text="ESP:OFF", fg="#ffffff", bg="black", font=("Arial", 16))

button_aimbot = tk.Button(root, text="Enable/Disable", fg="#ffffff", bg="black")
button_esp = tk.Button(root, text="Enable/Disable", fg="#ffffff", bg="black")

button_aimbot.config(command=toggle_aimbot)
button_esp.config(command=toggle_esp)

label_aimbot.grid(row=0, column=0, sticky=tk.W)
label_esp.grid(row=1, column=0, sticky=tk.W)
button_aimbot.grid(row=0, column=1, sticky=tk.W)
button_esp.grid(row=1, column=1, sticky=tk.W)

root.mainloop()
