from tkinter import *

w = Tk()
w.geometry("350x160")
w.title("Miles To Kilometers")

def kilometreye_cevir():
    deger_al = entry.get()
    sonuc = float(deger_al) * 1.60934
    label2.config(text=f"{deger_al} Mil ≈ {sonuc} Km")

label = Label(w,text="Mil'den Kilometreye Çevirme",font=("Ink free",18))
label.pack(pady=7)

entry = Entry(w,font="Times 15 bold",border=2)
entry.place(x=35,y=60)

botun = Button(w,text="Çevir",font=("Ink free",15),width=5,height=0,bg="red",border=2,command=kilometreye_cevir)
botun.place(x=250,y=50)

label2 = Label(w,text="",font=("Ink free",20))
label2.place(x=40,y=100)
w.mainloop()
