from tkinter import *
from tkinter.ttk import Combobox

def ekrana_yazdir():
    print(Combo.get())

root = Tk()
root.geometry("200x150")

degerler = ["python","java","julia","C#","C++","swift","javascrip"]

Combo = Combobox(values=degerler)
Combo.current(0)
Combo.pack(padx=5, pady=5)

Button = Button(text="Yazdır", command=ekrana_yazdir)
Button.pack(padx=5, pady=5)

root.mainloop()
