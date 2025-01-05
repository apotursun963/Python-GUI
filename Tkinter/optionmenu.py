from tkinter import *

pencere = Tk()
pencere.title('arayüz')
pencere.geometry("500x400+500+200")

optinmenu_list = [
    "Ocak",
    "Şubat",
    "Mart",
    "Nisan",
    "Mayıs",
    "Haziran",
    "Temmuz",
    "Ağostuğs",
    "Eylül",
    "Ekim",
    "Kasım",
    "Aralık"
]

svar = StringVar(value=optinmenu_list[0])
optinmenu = OptionMenu(pencere,svar,*optinmenu_list)
optinmenu.place(x=200,y=160)
optinmenu.config(font="Times 15 bold",width=18,border=2)

pencere.mainloop()