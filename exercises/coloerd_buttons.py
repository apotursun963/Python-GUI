from tkinter import *

w = Tk()
w.geometry("500x350")

def kirmizi():
    w.config(bg="red")

def yesil():
    w.config(bg="green")

def mavi():
    w.config(bg="blue")

def pembe():
    w.config(bg="pink")

frame = Frame(w,highlightcolor="orange",height=140,width=270,bg="gray")
frame.pack(pady=80)

kirmizi_botun = Button(frame,text="Kırmızı",bg="red",height=2,width=15,command=kirmizi)
kirmizi_botun.place(x=10,y=10)

yesil_botun = Button(frame,text="Yeşil",bg="green",height=2,width=15,command=yesil)
yesil_botun.place(x=10,y=75)

mavi_botun = Button(frame,text="Mavi",bg="blue",height=2,width=15,command=mavi)
mavi_botun.place(x=150,y=10)

pembe_botun = Button(frame,text="pembe",bg="pink",height=2,width=15,command=pembe)
pembe_botun.place(x=150,y=75)
w.mainloop()
