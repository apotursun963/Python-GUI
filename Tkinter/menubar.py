from tkinter import *
from tkinter import Menu

def open_file():
    print("Dosya Aç seçeneği tıklandı.")

root =  Tk()
root.title("Tkinter Menü Örneği")

# menu oluştur
menubar = Menu(root)
root.config(menu=menubar)

# menu öğrelerini ekle
file_menu = Menu(menubar,tearoff=0)                           # en üstteki çizgilerin görüntülenmesini istemiyorsak kulanılır.
menubar.add_cascade(label="Dosya", menu=file_menu)            # add_cascade() = üst menu ekler
file_menu.add_command(label="Aç", command=open_file)          # add_command() = alt menu ekler
file_menu.add_separator()                                     # add_separator() = alt menuler arasına çizgiler ekler.
file_menu.add_command(label="Çıkış", command=root.quit)

root.mainloop()


# örnek2:

from tkinter import *
from tkinter import Menu

window = Tk()
window.title("Menu Bar")

menu_bar = Menu(window)
window.config(menu=menu_bar)

edit_menu = Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="Edit",menu=edit_menu)
edit_menu.add_command(label="cut",activebackground="blue",activeforeground="yellow")
edit_menu.add_command(label="paste     Ctrl+C",activebackground="blue",activeforeground="yellow")
edit_menu.add_command(label="sil",activebackground="blue",activeforeground="yellow")
edit_menu.add_separator()

# iç içe menu
sub_menu = Menu(edit_menu,tearoff=0)
edit_menu.add_cascade(label="alt menu",menu=sub_menu)
sub_menu.add_command(label="alt öğe 1 ")
sub_menu.add_command(label="alt öğe 2 ")
sub_menu.add_separator()

sub_menu2 = Menu(sub_menu,tearoff=0)
sub_menu.add_cascade(label="seç",menu=sub_menu2)
sub_menu2.add_command(label="evet")
sub_menu2.add_command(label="hayır")

window.mainloop()

# örnek3:

from tkinter import *
from tkinter import Menu

window = Tk()
window.geometry("400x250")
window.title("Menu Örneği")

menu_bar = Menu(window)
window.config(menu=menu_bar)
file_menu = Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="File",font="verdana 10 bold",menu=file_menu)
file_menu.add_command(label="New Project")
file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_command(label="Rename Project")
file_menu.add_command(label="Save as")
file_menu.add_separator()
file_menu.add_command(label="settings")

edit_menu = Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="Edit",font="verdana 10 bold",menu=edit_menu)
edit_menu.add_command(label="Copey    (Ctrl+C)")
edit_menu.add_command(label="Cut")

sub_menu = Menu(edit_menu,tearoff=0)
edit_menu.add_cascade(label="Paste      (Ctrl+V)",menu=sub_menu)
sub_menu.add_command(label="Paste From History")
sub_menu.add_command(label="Paste as plain text")
edit_menu.add_separator()
edit_menu.add_command(label="Delete")
edit_menu.add_command(label="Quit")

view_bar = Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="View",font="verdana 10 bold",menu=view_bar)
sub_menu2 = Menu(view_bar,tearoff=0)
view_bar.add_cascade(label="Tool Windows",menu=sub_menu2)
sub_menu2.add_command(label="Commit")
sub_menu2.add_command(label="Project")
sub_menu2.add_command(label="Run")
sub_menu2.add_command(label="Bookmark")
sub_menu2.add_command(label="Find")
sub_menu2.add_command(label="Debug")

sub_menu3 = Menu(view_bar,tearoff=0)
view_bar.add_cascade(label="Appearence",menu=sub_menu3)
sub_menu4 = Menu(sub_menu3,tearoff=0)
sub_menu3.add_cascade(label="Navigation Bar",menu=sub_menu4)
sub_menu4.add_command(label="Top")
sub_menu4.add_radiobutton(label="İnstatues Bar")

window.mainloop()