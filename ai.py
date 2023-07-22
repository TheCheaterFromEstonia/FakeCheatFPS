import tkinter as tk
import os

def main():
  root = tk.Tk()
  root.configure(bg="black")

  def inject():
    root.after(3000, root.destroy)

  button = tk.Button(root, text="INJECT", command=inject)
  button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

  def open_fake_cheat():
    os.system("python FakeCheat.py")

  root.after(3000, open_fake_cheat)

  root.mainloop()

if __name__ == "__main__":
  main()
