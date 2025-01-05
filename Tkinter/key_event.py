from tkinter import *

w = Tk()
w.geometry("600x500")

def tuş_basma(event):
    label.config(text=event.keysym)


w.bind("<Key>",tuş_basma)

label = Label(w,font=("Helvetica",100))
label.pack()

w.mainloop()
