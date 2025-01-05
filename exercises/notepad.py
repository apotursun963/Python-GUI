from tkinter import *
from tkinter.font import *
from tkinter import filedialog, Menu, colorchooser
import datetime

w = Tk()
w.title("NotePad")
w.geometry("700x500+500+100")
icon = PhotoImage(file="C:\\Users\\90507\\OneDrive\\Masaüstü\\Python-GUI\\images\\note.png")
w.iconphoto(True,icon)

def karanlık_tema():
    if karanlık_tema:
        text.config(background="#16191A",foreground="white")

def açık_tema():
    if açık_tema:
        text.config(background="white",foreground="black")

def kaydet():
    if kaydet:
        file = filedialog.asksaveasfilename(initialdir="C:\\Users\\90507\\OneDrive\\Masaüstü\\yeni klasör",
                                        title="Dosya Kaydetme",
                                        filetypes=[("Metin Dosyası","*.txt"),("Varsayılan Dosya","*.*")])
        metni_al = text.get(1.0,END)
        file.write(str(metni_al))

def dosya_ac():
    if dosya_ac:
        file_yolu = filedialog.askopenfilename(initialdir="C:\\Users\\90507\\OneDrive\\Masaüstü\\yeni klasör",
                                    title="Dosya Aç",
                                    filetypes=[("Metin Dosyası","*.txt"),("Varsayılan Dosya","*.*")])
        ac= open(str(file_yolu),"r")
        print(ac.read())           # sonra texte yazdır.


def sil():
        global text
        text.delete(1.0,END)

def datetime1():
    x = datetime.datetime.now()
    if datetime:
        text.insert(100.0,x)

def kopyala():
        global text
        text.event_generate("<<Copy>>")

def yapistir():
    global text
    text.event_generate("<<Paste>>")

def kes():
    global text
    text.event_generate("<<Cut>>")

def tumunu_sec():
    global text
    text.tag_add(SEL,1.0,END)

def times_tipi():
    font1.config(family="Times")

def symbol_tipi():
    font1.config(family="symbol")

def helvetica_tipi():
    font1.config(family="Helvetica")

def ınk_free_tipi():
    font1.config(family="Ink free")

def verdana_tipi():
    font1.config(family="verdana")

def underline():
    if underline:
        font1.config(underline=True)
    else:
        font1.config(underline=False)

def Overstrike():
    if Overstrike:
        font1.config(overstrike=True)
    else:
        font1.config(overstrike=False)

def kalin_yazi():
        font1.config(weight="bold")

def normal_yazi():
        font1.config(weight="normal")


def yazi_rengi():
    renk = colorchooser.askcolor(title="Yazı Rengi Seç...")
    text.config(fg=renk[1])

font1 = Font(family="",size=15,weight="normal",slant="italic",underline=False,overstrike=False)

Yscroll_bar = Scrollbar(w,orient=VERTICAL)
Yscroll_bar.pack(side=RIGHT,fill=Y)

text = Text(font=font1,wrap="word",padx=5,pady=5,undo=True,yscrollcommand=Yscroll_bar.set)
text.pack(expand=True,fill=BOTH)

Yscroll_bar.config(command=text.yview)


menu_bar = Menu(w)
w.config(menu=menu_bar,background="black")

newtab_image= PhotoImage(file="C:\\Users\\90507\\OneDrive\\Masaüstü\\resimlericon\\browsers.png")
save_image =   PhotoImage(file="C:\\Users\\90507\\OneDrive\\Masaüstü\\resimlericon\\save.png")
open_image =    PhotoImage(file="C:\\Users\\90507\\OneDrive\\Masaüstü\\resimlericon\\open-folder.png")
closetab_image = PhotoImage(file="C:\\Users\\90507\\OneDrive\\Masaüstü\\resimlericon\\close.png")
quit_image =      PhotoImage(file="C:\\Users\\90507\\OneDrive\\Masaüstü\\resimlericon\\logout.png")

dosya_menu = Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="Dosya",menu=dosya_menu)
# dosya_menu.add_command(label="       Yeni Sekme         (Ctrl+N)",image=newtab_image,compound="left")
dosya_menu.add_command(label="       Kaydet                  (Ctrl+S)",command=kaydet,image=save_image,compound="left")
dosya_menu.add_command(label="       Aç                         (Ctrl+O)",command=dosya_ac,image=open_image,compound="left")
dosya_menu.add_separator()
# dosya_menu.add_command(label="       Sekmeyi Kapat    (Ctrl+W)",image=closetab_image,compound="left")
dosya_menu.add_command(label="       Çıkış",command=w.quit,image=quit_image,compound="left")

undo_image = PhotoImage(file="C:\\Users\\90507\\OneDrive\\Masaüstü\\resimlericon\\left-arrow.png")
copy_image = PhotoImage(file="C:\\Users\\90507\\OneDrive\\Masaüstü\\resimlericon\\copy-two-paper-sheets-interface-symbol.png")
paste_image = PhotoImage(file="C:\\Users\\90507\\OneDrive\\Masaüstü\\resimlericon\\paste.png")
delete_image = PhotoImage(file="C:\\Users\\90507\\OneDrive\\Masaüstü\\resimlericon\\trash.png")
scissor_image = PhotoImage(file="C:\\Users\\90507\\OneDrive\\Masaüstü\\resimlericon\\scissor.png")
calendar_image = PhotoImage(file="C:\\Users\\90507\\OneDrive\\Masaüstü\\resimlericon\\calendar.png")
checkmark_image = PhotoImage(file="C:\\Users\\90507\\OneDrive\\Masaüstü\\resimlericon\\check-mark.png")

Düzenle_menu = Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="Düzenle",menu=Düzenle_menu)
Düzenle_menu.add_command(label="     Geri Al            (Ctrl+Z)",command=text.edit_undo,image=undo_image,compound="left")
Düzenle_menu.add_command(label="     İleri Al            (Ctrl+Y)",command=text.edit_redo,image=undo_image,compound="left")
Düzenle_menu.add_separator()
Düzenle_menu.add_command(label="     Kopyala          (Ctrl+C)",command=kopyala,image=copy_image,compound="left")
Düzenle_menu.add_command(label="     Yapıştır           (Ctrl+V)",command=yapistir,image=paste_image,compound="left")
Düzenle_menu.add_command(label="     Hepsini Sil",command=sil,image=delete_image,compound="left")
Düzenle_menu.add_command(label="     Kes                  (Ctrl+X) ",command=kes,image=scissor_image,compound="left")
Düzenle_menu.add_separator()
Düzenle_menu.add_command(label="     Tarih/Saat           F5 ",command=datetime1,image=calendar_image,compound="left")
Düzenle_menu.add_command(label="     Tümünü Seç   (Ctrl+A) ",command=tumunu_sec,image=checkmark_image,compound="left")

yakınlaştırma_image = PhotoImage(file="C:\\Users\\90507\\OneDrive\\Masaüstü\\resimlericon\\search.png")
yakınlaştır_image = PhotoImage(file="C:\\Users\\90507\\OneDrive\\Masaüstü\\resimlericon\\magnifying-glass.png")

Görünüm_menu = Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="Görünüm",menu=Görünüm_menu)
iç_yakınlaştima = Menu(Görünüm_menu,tearoff=0)
Görünüm_menu.add_cascade(label="     Yakınlaştırma",menu=iç_yakınlaştima,image=yakınlaştırma_image,compound="left")
Görünüm_menu.add_checkbutton(label="       Sözcük Kaydır")
iç_yakınlaştima.add_command(label="  Yakınlaştır    (Ctrl+Artı)",image=yakınlaştır_image,compound="left")
iç_yakınlaştima.add_command(label="Uzaklaştır     (Ctrl+Eksi)")
iç_yakınlaştima.add_command(label="Varsayılan Yakınlaştırma")

tema_menu = Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="Tema",menu=tema_menu)
tema_menu.add_radiobutton(label="Koyu",command=karanlık_tema)
tema_menu.add_radiobutton(label="Açık",command=açık_tema)

yazi_menu = Menu(menu_bar,tearoff=0)
yazi_menu.add_cascade(label="Yazi Rengi",command=yazi_rengi)
menu_bar.add_cascade(label="Yazı Ayarı",menu=yazi_menu)
iç_yazi = Menu(yazi_menu,tearoff=0)
yazi_menu.add_cascade(label="Yazı Adı",menu=iç_yazi)
iç_yazi.add_radiobutton(label="Times",command=times_tipi)
iç_yazi.add_radiobutton(label="Symbol",command=symbol_tipi)
iç_yazi.add_radiobutton(label="Helvetica",command=helvetica_tipi)
iç_yazi.add_radiobutton(label="Ink free",command=ınk_free_tipi)
iç_yazi.add_radiobutton(label="Verdana",command=verdana_tipi)

iç_yazi_kalınlıgı = Menu(yazi_menu,tearoff=0)
yazi_menu.add_cascade(label="Yazı Kalınlığı",menu=iç_yazi_kalınlıgı)
iç_yazi_kalınlıgı.add_radiobutton(label="Kalın",command=kalin_yazi)
iç_yazi_kalınlıgı.add_radiobutton(label="Normal",command=normal_yazi)


iç_yazi_boyutu = Menu(yazi_menu,tearoff=0)
yazi_menu.add_cascade(label="Yazı Boyutu",menu=iç_yazi_boyutu)
for i in range(2,33,2):
    iç_yazi_boyutu.add_radiobutton(label=i)

iç_yazi_cizili = Menu(yazi_menu,tearoff=0)
yazi_menu.add_cascade(label="Yazı şekli",menu=iç_yazi_cizili)
iç_yazi_cizili.add_radiobutton(label="Underline",command=underline)
iç_yazi_cizili.add_radiobutton(label="Overstrike",command=Overstrike)

w.mainloop()