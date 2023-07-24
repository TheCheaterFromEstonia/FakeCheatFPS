import tkinter as tk

root = tk.Tk()
root.geometry("640x360")
root.configure(background="#000000")

bg_image = tk.PhotoImage(file="CloudTheme.png")

background_label = tk.Label(root, image=bg_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

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
    
def toggle_RapidFire():
    global RapidFire_status
    RapidFire_status = "ON" if RapidFire_status == "OFF" else "OFF"
    label_RapidFire.config(text=f"RapidFire:{RapidFire_status}",  fg="#00ff00" if RapidFire_status == "ON" else "#ff0000" ,
                           bg="#000000" , highlightbackground="#ffffff")

aimbot_status = "OFF"
esp_status = "OFF"
RapidFire_status = "OFF"

label_aimbot = tk.Label(root, text="AIMBOT:OFF", fg="#ffffff", bg="black", font=("Helvetica", 20))
label_esp = tk.Label(root, text="ESP:OFF", fg="#ffffff", bg="black", font=("Helvetica", 20))
label_RapidFire = tk.Label(root, text= "RapidFire:OFF", fg="#ffffff", bg="black", font=("Helvetica", 20))

button_aimbot = tk.Button(root, text="Enable/Disable", fg="#ffffff", bg="black")
button_esp = tk.Button(root, text="Enable/Disable", fg="#ffffff", bg="black")
button_RapidFire = tk.Button(root, text="Enable/Disable", fg="#ffffff", bg="black")

button_aimbot.config(command=toggle_aimbot)
button_esp.config(command=toggle_esp)
button_RapidFire.config(command=toggle_RapidFire)

label_aimbot.grid(row=0, column=0, sticky=tk.W)
label_esp.grid(row=1, column=0, sticky=tk.W)
label_RapidFire.grid(row=2, column=0, sticky=tk.W)
button_aimbot.grid(row=0, column=1, sticky=tk.W)
button_esp.grid(row=1, column=1, sticky=tk.W)
button_RapidFire.grid(row=2, column=1, sticky=tk.W)


root.mainloop()
