from tkinter import *

pencere = Tk()
pencere.title('To Do List')
pencere.geometry('550x450+500+200')

pencere.iconbitmap("C:\\Users\\90507\\OneDrive\\Masaüstü\\Python-GUI\\images\\note.png")
listb = Listbox(pencere,width=25,height=15,font="Times 12 bold",selectmode=BROWSE)
listb.place(x=300, y=110)
lab = Label(pencere,text="Yapılacaklar Listesi",font="Times 15 bold")
lab.place(x=308, y=80)

entry = Entry(pencere, font="Times 12 bold")
entry.place(x=70,y=110)
lab2 = Label(pencere,text="Görevleri Gir : ",font="Times 13 bold")
lab2.place(x=70,y=80)

# ekle
def ekle():
    metin = entry.get()
    listb.insert(END,metin)
    entry.delete(0,END)

button = Button(pencere,text="Ekle",font="Times 12 bold",width=17,border=5,command=ekle)
button.place(x=70,y=150)

#sil
def sil():
    listb.delete(listb.curselection())
button = Button(pencere,text="Sil",font="Times 12 bold",width=17,border=5,command=sil)
button.place(x=70,y=210)

# temizle
def temizle():
    listb.delete(0,END)
button = Button(pencere,text="Temizle",font="Times 12 bold",width=17,border=5,command=temizle)
button.place(x=70,y=270)

#çık
button = Button(pencere,text="Çıkış",font="Times 12 bold",width=17,border=5,command=pencere.destroy)
button.place(x=70,y=330)

pencere.mainloop()
