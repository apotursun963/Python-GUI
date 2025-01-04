from tkinter import *
from tkinter.ttk import Combobox, Progressbar
from tkinter import filedialog, messagebox
import time

w = Tk()
w.geometry("600x500+450+175")
w.title("Bilgi Giriş Formu")
w.resizable(height=False,width=False)

label = Label(w, text="Ad ve Soyad : ", font="verdana 15 bold")
label.place(x=20, y=30)
label2 = Label(w, text="E-posta adresi : ", font="verdana 15 bold")
label2.place(x=20, y=90)
label3 = Label(w, text="Telefon Numarası : ", font="verdana 15 bold")
label3.place(x=20, y=150)
label4 = Label(w, text="Memleketiniz : ", font="verdana 15 bold")
label4.place(x=20, y=210)
label5 = Label(w, text="Doğum Yılınız : ", font="verdana 15 bold")
label5.place(x=20, y=270)

entry = Entry(w, font="verdana 15 bold")
entry.place(x=270, y=30)
entry2 = Entry(w, font="verdana 15 bold")
entry2.place(x=270, y=90)
entry3 = Entry(w, font="verdana 15 bold")
entry3.place(x=270, y=150)
entry4 = Entry(w, font="verdana 15 bold")
entry4.place(x=270, y=210)

yilllar = [str(yil) for yil in range(1980, 2024)]
combobox = Combobox(w, values=yilllar, font="verdana 15")
combobox.place(x=270, y=270)
combobox.set(2023)


def bilgileri_kaydet(event=None):
    kullanici_bilgileri = {
        "Ad ve Soyad": entry.get(),
        "E-posta adresi": entry2.get(),
        "Telefon Numarsı": entry3.get(),
        "Memleketiniz": entry4.get(),
        "Doğum Yılınız": combobox.get(),
    }
    print(kullanici_bilgileri)

    kaydet = filedialog.asksaveasfile(
        initialdir="",
        title="Dosya Kaydet",
        filetypes=(("Metin Dosyaları", "*.txt"), ("Tüm Dosyalar", "*.*")),
    )
    if kaydet:
        with open(kaydet.name, "w") as dosya:
            dosya.write(f"Ad ve Soyad: {kullanici_bilgileri['Ad ve Soyad']}\n")
            dosya.write(f"E-posta adresi: {kullanici_bilgileri['E-posta adresi']}\n")
            dosya.write(f"Telefon Numarası: {kullanici_bilgileri['Telefon Numarsı']}\n")
            dosya.write(f"Memleket: {kullanici_bilgileri['Memleketiniz']}\n")
            dosya.write(f"Doğum Yılı: {kullanici_bilgileri['Doğum Yılınız']}\n")

        Toplevel1 = Toplevel(w)
        Toplevel1.geometry("350x180+580+310")
        label1 = Label(
            Toplevel1, text="Bilgileriniz Kaydediliyor...", font="verdana 15"
        )
        label1.place(x=45, y=100)

        Progress_var = IntVar()
        Progress_var.set(0)
        Progressbar1 = Progressbar(
            Toplevel1,
            orient="horizontal",
            mode="determinate",
            length=300,
            variable=Progress_var,
        )
        Progressbar1.place(x=30, y=40)

        def simulate_progress():
            for i in range(101):
                Progress_var.set(i)
                Toplevel1.update_idletasks()
                time.sleep(0.05)
            Toplevel1.destroy()
            messagebox.showinfo("Bilgi Mesajı", "Bilgileriniz Başarıyla Kaydedildi")
            entry.delete(0, END)
            entry2.delete(0, END)
            entry3.delete(0, END)
            entry4.delete(0, END)
            combobox.set(2023)

        Toplevel1.after(1000, simulate_progress)

botun1 = Button(
    w,
    text="Kaydet",
    font="verdana 15 bold",
    width=15,
    height=2,
    border=3,
    activebackground="black",
    activeforeground="white",
    command=bilgileri_kaydet,
    bg="pink",
)
botun1.place(x=185, y=330)

botun2 = Button(
    w,
    text="Çıkış",
    font="verdana 15 bold",
    width=10,
    height=2,
    border=3,
    activebackground="black",
    activeforeground="white",
    command=lambda:w.destroy(),
)
botun2.place(x=220, y=420)

w.bind("<Return>", bilgileri_kaydet)
w.mainloop()