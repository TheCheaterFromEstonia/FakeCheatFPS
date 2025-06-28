import tkinter as tk

root = tk.Tk()
root.geometry("640x360")
root.configure(background="#000000")

def toggle_aimbot():
    global aimbot_status
    aimbot_status = "ON" if aimbot_status == "OFF" else "OFF"
    label_aimbot.config(text=f"AIMBOT:{aimbot_status}", fg="#00ff00" if aimbot_status == "ON" else "#ff0000",
                        bg="#9F2B68", font=("Helvetica", 24), highlightbackground="#ffffff")

def toggle_esp():
    global esp_status
    esp_status = "ON" if esp_status == "OFF" else "OFF"
    label_esp.config(text=f"ESP:{esp_status}", fg="#00ff00" if esp_status == "ON" else "#ff0000",
                     bg="#9F2B68", font=("Helvetica", 24), highlightbackground="#ffffff")
    
def toggle_RapidFire():
    global RapidFire_status
    RapidFire_status = "ON" if RapidFire_status == "OFF" else "OFF"
    label_RapidFire.config(text=f"RapidFire:{RapidFire_status}",  fg="#00ff00" if RapidFire_status == "ON" else "#ff0000" ,
                           bg="#9F2B68", font=("Helvetica", 24), highlightbackground="#ffffff")
    
def toggle_Bhop():
    global Bhop_status
    Bhop_status = "ON" if Bhop_status == "OFF" else "OFF"
    label_Bhop.config(text=f"Bhop:{Bhop_status}", fg="#00ff00" if Bhop_status == "ON" else "#ff0000" ,
                      bg="#9F2B68", font=("Helvetica", 24), highlightbackground= "#ffffff")
    
def toggle_Triggerbot():
    global Triggerbot_status
    Triggerbot_status = "ON" if Triggerbot_status == "OFF" else "OFF"
    label_Triggerbot.config(text=f"Triggerbot:{Triggerbot_status}", fg="#00ff00" if Triggerbot_status == "ON" else "#ff0000" ,
                            bg="#9F2B68", font=("Helvetica", 24), highlightbackground= "#ffffff")

aimbot_status = "OFF"
esp_status = "OFF"
RapidFire_status = "OFF"
Bhop_status = "OFF"
Triggerbot_status = "OFF"

label_aimbot = tk.Label(root, text="AIMBOT:OFF", fg="#ffffff", bg="#9F2B68", font=("Helvetica", 20))
label_esp = tk.Label(root, text="ESP:OFF", fg="#ffffff", bg="#9F2B68", font=("Helvetica", 20))
label_RapidFire = tk.Label(root, text= "RapidFire:OFF", fg="#ffffff", bg="#9F2B68", font=("Helvetica", 20))
label_Bhop = tk.Label(root, text= "Bhop:OFF", fg="#ffffff", bg="#9F2B68", font=("Helvetica", 20))
label_Triggerbot = tk.Label(root, text= "Triggerbot:OFF", fg="#ffffff", bg="#9F2B68", font=("Helvetica", 20))

button_aimbot = tk.Button(root, text="Enable/Disable", fg="#ffffff", bg="#9F2B68", font=("Helvetica", 24), command=toggle_aimbot)
button_esp = tk.Button(root, text="Enable/Disable", fg="#ffffff", bg="#9F2B68", font=("Helvetica", 24), command=toggle_esp)
button_RapidFire = tk.Button(root, text="Enable/Disable", fg="#ffffff", bg="#9F2B68", font=("Helvetica", 24), command=toggle_RapidFire)
button_Bhop = tk.Button(root, text="Enable/Disable", fg="#ffffff", bg="#9F2B68", font=("Helvetica", 24),command=toggle_Bhop)
button_Triggerbot = tk.Button(root, text="Enable/Disable", fg="#ffffff", bg="#9F2B68", font=("Helvetica", 24),command=toggle_Triggerbot)

label_aimbot.grid(row=0, column=0, sticky=tk.W)
label_esp.grid(row=1, column=0, sticky=tk.W)
label_RapidFire.grid(row=2, column=0, sticky=tk.W)
label_Bhop.grid(row=3, column=0, sticky=tk.W)
label_Triggerbot.grid(row=4, column=0,sticky=tk.W)
button_aimbot.grid(row=0, column=1, sticky=tk.W)
button_esp.grid(row=1, column=1, sticky=tk.W)
button_RapidFire.grid(row=2, column=1, sticky=tk.W)
button_Bhop.grid(row=3, column=1, sticky=tk.W)
button_Triggerbot.grid(row=4, column=1,sticky=tk.W)
root.mainloop()
