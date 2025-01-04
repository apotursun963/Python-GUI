import tkinter as tk
from tkinter import colorchooser

def pick_color():
    color = colorchooser.askcolor(title="Renk Seç")
    if color:
        chosen_color = color[1]
        print("Seçilen Renk:", chosen_color)

root = tk.Tk()
button = tk.Button(root, text="Renk Seç", command=pick_color)
button.pack()

root.mainloop()
