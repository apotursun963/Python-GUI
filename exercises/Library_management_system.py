from tkinter import messagebox
from tkinter.ttk import *
from customtkinter import *

kitap_Bilgileri = dict()
uye_Bilgileri = dict()
odunc_Bilgileri = dict()

set_appearance_mode("dark")
set_default_color_theme("blue")

pencere = CTk()
pencere.title("Kütüphane Otomasyonu")
pencere.geometry("1000x650+330+100")

#label
label = CTkLabel(pencere,text="Kütüpane Yönetim Sistemi",font=("Ink Free",60))
label.place(x=165,y=80)

def kitap_ekleme_metodu():
    toplevel1 = CTkToplevel(pencere)
    toplevel1.geometry("850x600+430+130")
    toplevel1.title("Kitap Ekleme")
    toplevel1.resizable(False,False)
    toplevel1.grab_set()

    label1 = CTkLabel(toplevel1,text="Kitap Adı      :",font=("Times bold",30))
    label1.place(x=15,y=30)
    label2 = CTkLabel(toplevel1,text="Kitap Yazarı :",font=("Times bold",30))
    label2.place(x=15,y=100)
    label3 = CTkLabel(toplevel1,text="Sayfa Sayısı :",font=("Times bold",30))
    label3.place(x=15,y=170)
    label4 = CTkLabel(toplevel1,text="Yayın Evi      :",font=("Times bold",30))
    label4.place(x=15,y=240)
    label5 = CTkLabel(toplevel1,text="Kitap Türü     :",font=("Times bold",30))
    label5.place(x=15,y=310)
    label6 = CTkLabel(toplevel1,text="ISBN             :",font=("Times bold",30))
    label6.place(x=15,y=370)

    entry1 = CTkEntry(toplevel1,width=500,height=40,font=("Times bold",20))
    entry1.place(x=250,y=30)
    entry2 = CTkEntry(toplevel1,width=500,height=40,font=("Times bold",20))
    entry2.place(x=250,y=100)
    entry3 = CTkEntry(toplevel1,width=500,height=40,font=("Times bold",20))
    entry3.place(x=250,y=170)
    entry4 = CTkEntry(toplevel1,width=500,height=40,font=("Times bold",20))
    entry4.place(x=250,y=240)
    entry5 = CTkEntry(toplevel1,width=500,height=40,font=("Times bold",20))
    entry5.place(x=250,y=310)
    entry6 = CTkEntry(toplevel1,width=500,height=40,font=("Times bold",20))
    entry6.place(x=250,y=370)

    def kitap_ekleme_butonu():
        if not entry1.get().strip() or not entry2.get().strip() or not entry3.get().strip() or not entry4.get().strip() or\
        not entry5.get().strip() or not entry6.get().strip():
            messagebox.showwarning("Uyarı","Lütfen Boş Olan Yerleri Doldurun.")
        else:
            kitap_Bilgileri["Kitap Adı"] = entry1.get()
            kitap_Bilgileri["Kitabın Yazarı"] = entry2.get()
            kitap_Bilgileri["Sayfa Sayısı"] = entry3.get()
            kitap_Bilgileri["Yayın Evi"] = entry4.get()
            kitap_Bilgileri["Kitap Türü"] = entry5.get()
            kitap_Bilgileri["ISBN"] = entry6.get()

            for key,value in kitap_Bilgileri.items():
                print(f"{key}: {value}")

            messagebox.showinfo("Tebrikler","Kitap Bilgileri Başarıyla Kaydedildi.")
            entry1.delete(0,END)
            entry2.delete(0,END)
            entry3.delete(0,END)
            entry4.delete(0,END)
            entry5.delete(0,END)
            entry6.delete(0,END)

    botun = CTkButton(toplevel1,text="Kitabı Ekle",height=80,width=320,font=("Times bold",50),command=kitap_ekleme_butonu)
    botun.place(x=250,y=460)


def uye_ekleme_metodu():
    toplevel1 = CTkToplevel(pencere)
    toplevel1.geometry("800x600+440+130")
    toplevel1.title("Üye Ekleme")
    toplevel1.resizable(False,False)
    toplevel1.grab_set()

    label1 = CTkLabel(toplevel1,text="Ad Soyad        :",font=("Times bold",30))
    label1.place(x=15,y=30)
    label2 = CTkLabel(toplevel1,text="Doğum Tarihi  :",font=("Times bold",30))
    label2.place(x=15,y=100)
    label3 = CTkLabel(toplevel1,text="TC Numarası  :",font=("Times bold",30))
    label3.place(x=15,y=170)
    label4 = CTkLabel(toplevel1,text="Telefon No      :",font=("Times bold",30))
    label4.place(x=15,y=240)
    label5 = CTkLabel(toplevel1,text="E-Posta          :",font=("Times bold",30))
    label5.place(x=15,y=310)


    entry1 = CTkEntry(toplevel1,width=500,height=40,font=("Times bold",20))
    entry1.place(x=250,y=30)
    entry2 = CTkEntry(toplevel1,width=500,height=40,font=("Times bold",20))
    entry2.place(x=250,y=100)
    entry3 = CTkEntry(toplevel1,width=500,height=40,font=("Times bold",20))
    entry3.place(x=250,y=170)
    entry4 = CTkEntry(toplevel1,width=500,height=40,font=("Times bold",20))
    entry4.place(x=250,y=240)
    entry5 = CTkEntry(toplevel1,width=500,height=40,font=("Times bold",20))
    entry5.place(x=250,y=310)

    def uye_ekleme_butonu():
        if not entry1.get().strip() or not entry2.get().strip() or not entry3.get().strip() or not entry4.get().strip() or\
        not entry5.get().strip():
            messagebox.showwarning("Uyarı","Lütfen Boş Olan Yerleri Doldurun.")
        else:
            kitap_Bilgileri["Ad Soyad"] = entry1.get()
            kitap_Bilgileri["Doğum Tarihi"] = entry2.get()
            kitap_Bilgileri["TC Numarası"] = entry3.get()
            kitap_Bilgileri["Telefon No"] = entry4.get()
            kitap_Bilgileri["E-Posta"] = entry5.get()


            for key,value in kitap_Bilgileri.items():
                print(f"{key}: {value}")

            messagebox.showinfo("Tebrikler","Üye Bilgileri Başarıyla Kaydedildi.")
            entry1.delete(0,END)
            entry2.delete(0,END)
            entry3.delete(0,END)
            entry4.delete(0,END)
            entry5.delete(0,END)


    botun2 = CTkButton(toplevel1,text="Üyeyi Ekle",height=100,width=400,font=("Times bold",50),command=uye_ekleme_butonu)
    botun2.place(x=200,y=430)

def odunc_ekleme_metodu():
    toplevel1 = CTkToplevel(pencere)
    toplevel1.geometry("900x500+400+180")
    toplevel1.title("Ödünç Verme")
    toplevel1.resizable(False,False)
    toplevel1.grab_set()

    label1 = CTkLabel(toplevel1,text="Ödünç Verilecek Kitap :",font=("Times bold",30))
    label1.place(x=15,y=30)
    label2 = CTkLabel(toplevel1,text="Ödünç Verilecek üye   :",font=("Times bold",30))
    label2.place(x=15,y=100)
    label3 = CTkLabel(toplevel1,text="Ödünç Alma Tarihi      :",font=("Times bold",30))
    label3.place(x=15,y=170)
    label4 = CTkLabel(toplevel1,text="Kitap İade Tarihi          :",font=("Times bold",30))
    label4.place(x=15,y=240)

    entry1 = CTkEntry(toplevel1,width=500,height=40,font=("Times bold",20))
    entry1.place(x=350,y=30)
    entry2 = CTkEntry(toplevel1,width=500,height=40,font=("Times bold",20))
    entry2.place(x=350,y=100)
    entry3 = CTkEntry(toplevel1,width=500,height=40,font=("Times bold",20))
    entry3.place(x=350,y=170)
    entry4 = CTkEntry(toplevel1,width=500,height=40,font=("Times bold",20))
    entry4.place(x=350,y=240)

    def odunc_verme_butonu():
        if not entry1.get().strip() or not entry2.get().strip() or not entry3.get().strip() or not entry4.get().strip():
            messagebox.showwarning("Uyarı","Lütfen Boş Olan Yerleri Doldurun.")
        else:
            kitap_Bilgileri["Ödünç Verilecek Kitap"] = entry1.get()
            kitap_Bilgileri["Ödünç Verilecek üye"] = entry2.get()
            kitap_Bilgileri["Ödünç Alma Tarihi"] = entry3.get()
            kitap_Bilgileri["Kitap İade Tarihi"] = entry4.get()

            for key,value in kitap_Bilgileri.items():
                print(f"{key}: {value}")

            messagebox.showinfo("Tebrikler","Ödünç Bilgileri Başarıyla Kaydedildi.")
            entry1.delete(0,END)
            entry2.delete(0,END)
            entry3.delete(0,END)
            entry4.delete(0,END)

    botun3 = CTkButton(toplevel1,text="Ödünç Ver",height=100,width=400,font=("Times bold",50),command=odunc_verme_butonu)
    botun3.place(x=250,y=350)

buton1 = CTkButton(pencere,text="Kitap Ekle",height=100,width=250,font=("Times bold",30),command=kitap_ekleme_metodu)
buton1.place(x=30,y=250)
buton2 = CTkButton(pencere,text="Kitap Listele",height=100,width=250,font=("Times bold",30))
buton2.place(x=30,y=450)
buton3 = CTkButton(pencere,text="Üye Ekle",height=100,width=250,font=("Times bold",30),command=uye_ekleme_metodu)
buton3.place(x=380,y=250)
buton4 = CTkButton(pencere,text="Üye Listele",height=100,width=250,font=("Times bold",30))
buton4.place(x=380,y=450)
buton5 = CTkButton(pencere,text="Ödünç Verme",height=100,width=250,font=("Times bold",30),command=odunc_ekleme_metodu)
buton5.place(x=720,y=250)
buton6 = CTkButton(pencere,text="Ödünç Listele",height=100,width=250,font=("Times bold",30))
buton6.place(x=720,y=450)
pencere.mainloop()
