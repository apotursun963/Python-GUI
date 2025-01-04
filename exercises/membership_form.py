from tkinter import *
from tkinter import  messagebox

pencere = Tk()
pencere.title('Üyelik Girişi')
pencere.geometry('700x600+375+150')

# (ad,yaş,doğum,cinsiyet) için label
label1 = Label(pencere,text="İsim         : ",font="Times 20 bold")
label1.place(x=35,y=40)
label2 = Label(pencere,text="Yaş          : ",font="Times 20 bold")
label2.place(x=35,y=100)
label3 = Label(pencere,text="Doğum    : ",font="Times 20 bold")
label3.place(x=35,y=160)
label4 = Label(pencere,text="Cinsiyet   : ",font="Times 20 bold")
label4.place(x=35,y=220)

# kullanıcının isminin gireceği yer
entry1 = Entry(pencere,width=21,font="Times 15 bold",border=3)
entry1.place(x=200,y=45)

# kullanıcının yaşını seçebildiği yer
spinbox = Spinbox(pencere,from_=12,to=50,width=20,font="Times 15 bold",border=3,justify="center")
spinbox.place(x=200,y=108)

# kullanıcının doğum ayını seçebilgiği yer.
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

# kul lanıcının erkek veya kadın seçim yapabilmesini sağlar.
intvar = IntVar()
radiobutton = Radiobutton(pencere,text="Erkek",variable=intvar,value=0,font="Times 15 bold")
radiobutton.place(x=200,y=225)
radiobutton2 = Radiobutton(pencere,text="Kadın",variable=intvar,value=1,font="Times 15 bold")
radiobutton2.place(x=325,y=225)

# kullanıcının kontorl kutusu yaptığı yer.
chekbox = Checkbutton(pencere,text="Formu Okudum,Onaylıyorum",font="Times 14 bold")
chekbox.place(x=175,y=285)

# kaydet veya temizle botununa tıklayabildiği yer.
def kaydet():
    bilgi_goster = messagebox.showinfo("Kaydet","Bilgileriniz Başarıyla Kaydedildi.")
    print(bilgi_goster)
    entry1.delete(0,END)
    spinbox.delete(0,END)
    spinbox.insert(0,12)


bottun1 = Button(text="Kaydet",font="Times 18 bold",width=17,height=2,command=kaydet)
bottun1.place(x=70,y=400)

def cikis_yap():
    pencere.quit()

bottun2 = Button(text="Çıkış Yap",font="Times 18 bold",width=17,height=2,command=cikis_yap)
bottun2.place(x=360,y=400)
pencere.mainloop()