
#                                             "tkinter kütüphanesi"

#                                                (pencere oluşturma)


# from tkinter import *
#
# pencere = Tk()
#
# pencere.geometry('500x400+500+200')
# pencere.title('tkinter öğreniyorum')
# pencere.configure(background='white')
# pencere.attributes('-topmost',1)
# pencere.resizable(width=False , height=False)
#
# pencere.mainloop()

print("-------------------------------------------------------------------------------------------------------------------------------------------------")

#                                            (label oluşturma)
    

# from tkinter import *

# pencere = Tk()
# #pencere.title('tkinter öğreniyorum')
# pencere.geometry('500x400+500+200')
# Label(pencere,text='hoşgeldiniz').pack()
# Label(pencere,text='hoşgeldiniz',font=('times',15,'underline')).pack()
# Label(pencere,text='hoşgeldiniz',font=('times',20),bg='red',fg='yellow').pack()
# Label(pencere,text='hoşgeldiniz',font=('times',20),bg='blue',fg='pink',width=18,height=6).pack()
# Label(pencere,text='hoşgeldiniz',font=('times',20),bg='green',fg='purple',width=24,height=12,anchor='nw').pack()
# Label(pencere,font=('times',15,),bitmap='warning',).pack()

# Label(pencere,text='hoşgeldiniz',font=('times',15),bg='red',fg='yellow').pack()
# Label(pencere,text='hoşgeldiniz',font=('times',15),bg='red',fg='yellow',padx=20).pack()
# Label(pencere,text='hoşgeldiniz',font=('times',15),bg='red',fg='yellow',pady=15).pack()

# Label(pencere,text='hoşgeldiniz',font=('times',15),relief='raised').pack()

# pencere.mainloop()

print("-------------------------------------------------------------------------------------------------------------------------------------------------")


#                                            (widget hizalama (pack/grid/place))

# from tkinter import *
#
# pencere = Tk()
# pencere.title('arayüz')
# pencere.geometry('500x400+500+200')

# Label(pencere,text='merhabalar ben deneme 1').pack(side='top')
# Label(pencere,text='merhabalar ben deneme 2').pack(side='left')
# Label(pencere,text='merhabalar ben deneme 3').pack(side='right')
# Label(pencere,text='merhabalar ben deneme 4').pack(side='bottom')

# lab1 = Label(pencere,text='merhabalar ben deneme 1')
# lab1.grid(row=0,column=0)
# lab2 = Label(pencere,text='merhabalar ben deneme 2')
# lab2.grid(row=1,column=0)
# lab3 = Label(pencere,text='merhabalar ben deneme 3')
# lab3.grid(row=2,column=0,padx= 20,pady=20)

# Label(pencere,text='merhabalar ben deneme 1').place(x=195,y=180)
# lab2 = Label(pencere,text='merhabalar ben deneme 2')
# lab2.place(x=300,y=250)


# pencere.mainloop()




print("-------------------------------------------------------------------------------------------------------------------------------------------------")
#                                               (frame(çerçve))


# from tkinter import *
#
# pencere = Tk()
# pencere.title('arayüz')
# pencere.geometry('500x400+500+200')
#
# Frame(pencere,height=120,width=150,bg='orange',highlightbackground='blue',highlightthickness=6,cursor='spider',).pack()
#
# frame1 = Frame(pencere,height=120,width=150,bg='orange',highlightbackground='blue',highlightthickness=6,
#                cursor='spider',padx=5,pady=5)
# frame1.pack()
#
# lab1 = Label(frame1,text='herkese salam ')
# lab1.place(x=0,y=0)
#
# pencere.mainloop()



print("-------------------------------------------------------------------------------------------------------------------------------------------------")

#                                                   (Enty)


# from tkinter import *
#
# pencere = Tk()
# pencere.title('arayüz')
# pencere.geometry('500x400+500+200')

# Entry(pencere).pack()
# Entry(pencere,font=('Arial 15 bold '),bg='yellow',fg='red',border=6,width=25,cursor='pirate').pack()

# Entry(pencere,relief='raised').pack(pady= 15)
# Entry(pencere,relief='groove').pack(pady= 15)
# Entry(pencere,relief='sunken').pack(pady= 15)

# Entry(pencere,show='*').pack()

# Entry(pencere,justify='right').pack()

# Entry(pencere,selectbackground='blue',selectforeground='white').pack()

# Entry(pencere).pack()
# Entry(pencere,state='disabled').pack()
# Entry(pencere,state='normal').pack()

# ent1 = Entry(pencere)
# ent1.pack()
# def click_button():
#     # print(ent1.get())
#     ent1.insert(5,'/')
#
# Button(pencere,text='cick here',command=click_button).pack()

# pencere.mainloop()


print("-------------------------------------------------------------------------------------------------------------------------------------------------")

#                                             (botun ekleme)

# from tkinter import *
#
# pencere = Tk()
# pencere.title('arayüz')
# pencere.geometry('500x400+500+200')

# Button(pencere,text='tıkla!',font='times 15',bg='red',fg='white').pack()
# Button(pencere,text='tıkla!',font='times 15',activebackground='blue',activeforeground='yellow').pack(pady=10)

# cursor_list = [
#  'arrow',
#  'circle',
#  'clock',
#  'cross',
#  'dotbox',
#  'exchange'
# ]
#
# for cursor_item in cursor_list:
#     Button(pencere,text='tıkla',cursor=cursor_item).pack(pady=5)

# Button(pencere,text='tıkla!',font='times 15',bg='red',fg='white',height=10,width=20,bd=6).pack()
#
# def tıklanmak():
#     print('tamam tıkladın yeter')
# Button(pencere,text='tıkla!',font='times 15',bg='red',fg='white',command=tıklanmak).pack(pady=15)

# Button(pencere,text='tıkla!',font='times 15',pady=15).pack(pady=5)
# Button(pencere,text='tıkla!',font='times 15',padx=15).pack(pady=5)
# Button(pencere,text='tıkla!',font='times 15',pady=15).pack(pady=5)

# relief_list = [
#     'groove',
#     'sunken',
#     'raised'
# ]
#
# for relief_item in relief_list:
#     Button(pencere,text='hadi buraya tıkla',relief=relief_item).pack(pady=3)

# Button(pencere,text='tıkla!',state='normal').pack()
# Button(pencere,text='tıkla!',state='disabled').pack()

# pencere.mainloop()



print("-------------------------------------------------------------------------------------------------------------------------------------------------")

#                                                 (messagebox)

# from tkinter import *
# from tkinter import messagebox
#
# pencere = Tk()
# pencere.title('arayüz')
# pencere.geometry('500x400+500+200')
#
# def tıklanmak():
#
#     messagebox.showinfo('bilgi göster','işleminiz başarıyla gerçekleşti')
#     messagebox.showwarning('Uyarı göster','işleminiz uyarı gösteriyor')
#     err = messagebox.showerror('hata göster', 'işleminiz hatalı oldu')
#     print(err)
#     yes_no = messagebox.askyesno('yes or no ','are you sure ? ')
#     print(yes_no)
#     ok_cancel = messagebox.askokcancel('okey or cancel','do you want to countinue')
#     print(ok_cancel)
#     retry_cancel = messagebox.askretrycancel('retry or cancel', '482789373')
#     print(retry_cancel)
#     ques = messagebox.askquestion('nice', '482789373')
#     print(ques)
#     yes_no_cancel = messagebox.askyesnocancel('yes or no or cancel', 'devammmı etmek istiyorsun')
#     print(yes_no_cancel)
#
# Button(pencere,text='tıkla!',command=tıklanmak).pack()
#
# pencere.mainloop()




print("-------------------------------------------------------------------------------------------------------------------------------------------------")

#                                                     (spinbox)


# from tkinter import *
#
# pencere = Tk()
# pencere.title('arayüz')
# pencere.geometry('500x400+500+200')
#
# def yazdir():
#     print(spin1.get())
#
# spin1 = Spinbox(pencere,from_=1,to=15,increment=2,justify= 'center',width=25,font=('times 8 bold'),command=yazdir)
# spin1.pack()
#
# pencere.mainloop()
print("-------------------------------------------------------------------------------------------------------------------------------------------------")

#                                                    (listbox)


# from tkinter import *
#
# pencere = Tk()
# pencere.title('arayüz')
# pencere.geometry('500x400+500+200')
#
# lb = Listbox(selectmode=EXTENDED)
#
# # lb.insert(0,"elma")
# # lb.insert(1,"nar")
# # lb.insert(2,"karpuz")
# # lb.insert(3,"kavun")
# # lb.insert(4,"muz")
# # lb.insert(0,"elma")
# # lb.insert(1,"nar")
# # lb.insert(2,"karpuz")
# # lb.insert(3,"kavun")
# # lb.insert(4,"muz")
# # lb.insert(2,"karpuz")
# lb.pack()
#
# pencere.mainloop()


print("-------------------------------------------------------------------------------------------------------------------------------------------------")



#                                                (optionmenu)

# from tkinter import *

# pencere = Tk()
# pencere.title('arayüz')
# pencere.geometry("500x400+500+200")

# optinmenu_list = [
#     "Ocak",
#     "Şubat",
#     "Mart",
#     "Nisan",
#     "Mayıs",
#     "Haziran",
#     "Temmuz",
#     "Ağostuğs",
#     "Eylül",
#     "Ekim",
#     "Kasım",
#     "Aralık"
# ]

# svar = StringVar(value=optinmenu_list[0])
# optinmenu = OptionMenu(pencere,svar,*optinmenu_list)
# optinmenu.place(x=200,y=160)
# optinmenu.config(font="Times 15 bold",width=18,border=2)


# pencere.mainloop()

print("-------------------------------------------------------------------------------------------------------------------------------------------------")


#                                                                  (combobox)


# from tkinter import *
# from tkinter.ttk import Combobox
#
# window = Tk()
# window.geometry('550x450+450+170')
#
# degerler = ["python","java","julia","C#","C++","swift","javascrip"]
# combobox = Combobox(window,values=degerler,height=7,state=NORMAL,width=30)
# combobox.pack()
#
# #combobox.set("eleman seç")         #  varsayılan olarak değeri yazar
# combobox.current(0)                 # varsayılan olarak verdiğimiz elemanın indexini yazar
#
# window.mainloop()




# örnek
# from tkinter import *
# from tkinter.ttk import Combobox
#
# def ekrana_yazdir():
#     print(Combo.get())
#
# root = Tk()
# root.geometry("200x150")
#
# degerler = ["python","java","julia","C#","C++","swift","javascrip"]
#
# Combo = Combobox(values=degerler)
# Combo.current(0)
# Combo.pack(padx=5, pady=5)
#
# Button = Button(text="Yazdır", command=ekrana_yazdir)
# Button.pack(padx=5, pady=5)
#
# root.mainloop()


print("-------------------------------------------------------------------------------------------------------------------------------------------------")


#                                                            (scrollbar)


# from tkinter import *
#
# # Ana pencereyi oluştur
# root = Tk()
# root.title("Dikey ve Yatay Scrollbar Örneği")
#
# # Dikey scrollbar oluştur
# y_scrollbar = Scrollbar(root, orient=VERTICAL)
# y_scrollbar.pack(side=RIGHT, fill=Y)
#
# # Yatay scrollbar oluştur
# x_scrollbar = Scrollbar(root, orient=HORIZONTAL)
# x_scrollbar.pack(side=BOTTOM, fill=X)
#
# # Listbox oluştur ve scrollbar'lar ile bağla
# my_listbox = Listbox(root, yscrollcommand=y_scrollbar.set, xscrollcommand=x_scrollbar.set)
# my_listbox.pack(fill=BOTH)
#
# # Scrollbar'ları Listbox ile bağla(scrollo listbox'a yerleştirmek)
# y_scrollbar.config(command=my_listbox.yview)    # (y_scrollbar) listbox'ın y eksenine yerlştir demek.
# x_scrollbar.config(command=my_listbox.xview)    # (x_scrollbar) listbox'ın x eksenine yerlştir demek.
#
# # Listbox'a örnek veri ekle
# for i in range(50):
#     my_listbox.insert(END, f"Merhabalr hoş geldiniz 0'dan 49'a kadar olan sayıları göstericem {i}")
#
# # Ana döngüyü başlat
# root.mainloop()




#örnek
# from tkinter import *
#
# window = Tk()
# scrollbar = Scrollbar(window)
# scrollbar.pack(side=RIGHT, fill=Y)       # side: çubuğun hangi tarafata duracağını belirtir./ fill: eksene göre tamamımını kaplar
#
# mylist = Listbox(window, yscrollcommand=scrollbar.set)
# for line in range(100):
#     mylist.insert(END, "This is line number " + str(line))
#
# mylist.pack(side=RIGHT, fill=BOTH)
# scrollbar.config(command=mylist.yview)
#
# mainloop()


print("-------------------------------------------------------------------------------------------------------------------------------------------------")


#                                                         (progress bar)


# botuna her tıklandığında progress bar 10 adım ilerliyecek.

# from tkinter import *
# from tkinter.ttk import *
#
# root = Tk()
# root.title("Progress Bar Örneği")
#
# progress = Progressbar(root, orient=HORIZONTAL, length=300, mode="determinate")
# progress.pack()
#
# def ilerle():
#     current_value = progress["value"]
#     if current_value < 100:
#         progress["value"] = current_value + 10
#     else:
#         progress["value"] = 0
#
# ilerleme_dugmesi = Button(root, text="İlerle", command=ilerle)
# ilerleme_dugmesi.pack()
#
# root.mainloop()




#örnek

# from tkinter import *
# from tkinter.ttk import *
# import time
#
# def copy_file():
#     for i in range(1, 101):
#         time.sleep(0.1)
#         progress_var.set(i)
#         root.update_idletasks()  # İlerleme çubuğunu güncelle, ancak ana döngüyü bekletme
#
# root = Tk()
# root.title("Dosya Kopyalama İlerleme Çubuğu")
#
# progress_var = IntVar()
# progress_var.set(0)                # set() ile progress_var değişkenin değerini 0 olarak ayarladık
#
# progress_bar = Progressbar(root, variable=progress_var, maximum=100)
# progress_bar.pack(pady=10)
#
# start_button = Button(root, text="Başlat", command=copy_file)
# start_button.pack()
#
# root.mainloop()
#




# from tkinter import *
# from tkinter.ttk import *
# from tkinter import messagebox
#
# window = Tk()
# window.geometry("400x200")
#
# progress_bar = Progressbar(window,orient=HORIZONTAL,length=300,mode="determinate")
# progress_bar.pack(pady=15)
#
# def ilerlet():
#     yeni_deger = progress_bar["value"]
#     if yeni_deger < 100:
#         progress_bar["value"] = yeni_deger + 10
#     else:
#         progress_bar["value"] = 0
#
# botun = Button(window,text="Tıkla",command=ilerlet)
# botun.pack()
#
# window.mainloop()


print("-------------------------------------------------------------------------------------------------------------------------------------------------")


#                                                                    (toplevel)


#örnek
# from tkinter import *
#
# window = Tk()
# window.title("Ana Pencere")
#
# toplevel = Toplevel(window,bg="red")
#
# window.mainloop()


#örnek
# from tkinter import *
#
# window = Tk()
# window.title("Ana Pencere")
# window.geometry("300x200")
#
# def pencere_olustur():
#     toplevel = Toplevel(window, bg="red",height=150,width=300)
#
# button = Button(window,text="pencere oluştur",command=pencere_olustur)
# button.pack()
# window.mainloop()



#örnek
# from tkinter import *
#
# window = Tk()
# window.title("Ana Pencere")
# window.geometry("300x200")
#
# def pencere_olustur():
#     toplevel = Toplevel(window, bg="red")
#     toplevel.geometry("400x500")
#     toplevel.title("ikincil pencere")
#     button2 = Button(toplevel,text="tıkla",width=10,height=3)
#     button2.pack()
#
# button = Button(window,text="pencere oluştur",command=pencere_olustur)
# button.pack()
# window.mainloop()





print("-------------------------------------------------------------------------------------------------------------------------------------------------")

#                                                                (menu bar)

# menüye fotoğrafta ekleyebiliriz.


# from tkinter import *
# from tkinter import Menu
# def open_file():
#     print("Dosya Aç seçeneği tıklandı.")
#
# root =  Tk()
# root.title("Tkinter Menü Örneği")
#
# # menu oluştur
# menubar = Menu(root)
# root.config(menu=menubar)
#
# # menu öğrelerini ekle
# file_menu = Menu(menubar,tearoff=0)                           # en üstteki çizgilerin görüntülenmesini istemiyorsak kulanılır.
# menubar.add_cascade(label="Dosya", menu=file_menu)            # add_cascade() = üst menu ekler
# file_menu.add_command(label="Aç", command=open_file)          # add_command() = alt menu ekler
# file_menu.add_separator()                                     # add_separator() = alt menuler arasına çizgiler ekler.
# file_menu.add_command(label="Çıkış", command=root.quit)
# root.mainloop()




# #örnek
# from tkinter import *
# from tkinter import Menu
#
# window = Tk()
# window.title("Menu Bar")
#
#
# menu_bar = Menu(window)
# window.config(menu=menu_bar)
#
# def yapma():
#     print("Şu an hiç bir şey yapamam")
#
# dosya_menu = Menu(menu_bar,tearoff=0)
# menu_bar.add_cascade(label="File",font="verdana 7 bold",menu=dosya_menu)
# dosya_menu.add_command(label="Open",font="verdana 7 bold",command=yapma,activebackground="green",activeforeground="red")
# dosya_menu.add_checkbutton(label="Close",font="verdana 7 bold",activebackground="green",activeforeground="red")
# dosya_menu.add_command(label="Save",font="verdana 7 bold",activebackground="green",activeforeground="red")
# dosya_menu.add_separator()
# dosya_menu.add_radiobutton(label="çık",font="verdana 7 bold",activebackground="green",activeforeground="red")
#
# window.mainloop()



#örnek
# from tkinter import *
# from tkinter import Menu
#
# window = Tk()
# window.title("Menu Bar")
#
# menu_bar = Menu(window)
# window.config(menu=menu_bar)
#
# edit_menu = Menu(menu_bar,tearoff=0)
# menu_bar.add_cascade(label="Edit",menu=edit_menu)
# edit_menu.add_command(label="cut",activebackground="blue",activeforeground="yellow")
# edit_menu.add_command(label="paste     Ctrl+C",activebackground="blue",activeforeground="yellow")
# edit_menu.add_command(label="sil",activebackground="blue",activeforeground="yellow")
# edit_menu.add_separator()
# # iç içe menu
# sub_menu = Menu(edit_menu,tearoff=0)
# edit_menu.add_cascade(label="alt menu",menu=sub_menu)
# sub_menu.add_command(label="alt öğe 1 ")
# sub_menu.add_command(label="alt öğe 2 ")
# sub_menu.add_separator()
#
# sub_menu2 = Menu(sub_menu,tearoff=0)
# sub_menu.add_cascade(label="seç",menu=sub_menu2)
# sub_menu2.add_command(label="evet")
# sub_menu2.add_command(label="hayır")
#
# window.mainloop()




# güzel örnek
# from tkinter import *
# from tkinter import Menu
#
# window = Tk()
# window.geometry("400x250")
# window.title("Menu Örneği")
#
# menu_bar = Menu(window)
# window.config(menu=menu_bar)
# file_menu = Menu(menu_bar,tearoff=0)
# menu_bar.add_cascade(label="File",font="verdana 10 bold",menu=file_menu)
# file_menu.add_command(label="New Project")
# file_menu.add_command(label="New")
# file_menu.add_command(label="Open")
# file_menu.add_command(label="Rename Project")
# file_menu.add_command(label="Save as")
# file_menu.add_separator()
# file_menu.add_command(label="settings")
#
# edit_menu = Menu(menu_bar,tearoff=0)
# menu_bar.add_cascade(label="Edit",font="verdana 10 bold",menu=edit_menu)
# edit_menu.add_command(label="Copey    (Ctrl+C)")
# edit_menu.add_command(label="Cut")
#
# sub_menu = Menu(edit_menu,tearoff=0)
# edit_menu.add_cascade(label="Paste      (Ctrl+V)",menu=sub_menu)
# sub_menu.add_command(label="Paste From History")
# sub_menu.add_command(label="Paste as plain text")
# edit_menu.add_separator()
# edit_menu.add_command(label="Delete")
# edit_menu.add_command(label="Quit")
#
# view_bar = Menu(menu_bar,tearoff=0)
# menu_bar.add_cascade(label="View",font="verdana 10 bold",menu=view_bar)
# sub_menu2 = Menu(view_bar,tearoff=0)
# view_bar.add_cascade(label="Tool Windows",menu=sub_menu2)
# sub_menu2.add_command(label="Commit")
# sub_menu2.add_command(label="Project")
# sub_menu2.add_command(label="Run")
# sub_menu2.add_command(label="Bookmark")
# sub_menu2.add_command(label="Find")
# sub_menu2.add_command(label="Debug")
#
# sub_menu3 = Menu(view_bar,tearoff=0)
# view_bar.add_cascade(label="Appearence",menu=sub_menu3)
# sub_menu4 = Menu(sub_menu3,tearoff=0)
# sub_menu3.add_cascade(label="Navigation Bar",menu=sub_menu4)
# sub_menu4.add_command(label="Top")
# sub_menu4.add_radiobutton(label="İnstatues Bar")
#
# window.mainloop()




print("-------------------------------------------------------------------------------------------------------------------------------------------------")

#                                                                        (canvas)

# cavas:kullanıcıların bu alanda çizimler, şekiller, metinler ve diğer grafik nesneleri oluşturmasına izin verir

# from tkinter import *
#
# pencere = Tk()
# pencere.title("Canvas")
# pencere.geometry("600x600")
#
# canvas = Canvas(pencere,background="gray",height=500,width=500)

# canvas.create_line(0,0,200,200,dash=5)       # İki nokta arasında bir çizgi oluşturur.
# canvas.create_rectangle(400,400,100,100,fill="blue",outline="red",width=3)       # diktörtgen oluşturur.
# canvas.create_oval(10,10,400,500,fill="red",outline="blue",width=3)              # elips oluşturur
# canvas.create_polygon(0,75,75,0,150,75,75,150)                                   # istediğimiz şekli çizebiliriz
# canvas.create_text(50,50,text="abdullah tursun")                                 # metin eklemimize işe yarıyor.
# canvas.create_arc(10,10,100,100,start=45,extent=90)                              # açı çizmemize işe yarıyuor.
# canvas.pack()
#
#
# pencere.mainloop()


# import tkinter as tk
# from tkinter import colorchooser
#
# class CizimUygulamasi:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Gelişmiş Çizim Uygulaması")
#
#         self.canvas = tk.Canvas(root, width=800, height=600, bg="white")
#         self.canvas.pack()
#
#         self.cizim_rengi = "black"
#
#         self.canvas.bind("<Button-1>", self.baslat_cizim)
#         self.canvas.bind("<B1-Motion>", self.cizim)
#
#         self.rengi_sec = tk.Button(root, text="Rengi Seç", command=self.rengi_sec)
#         self.rengi_sec.pack()
#
#         self.temizle = tk.Button(root, text="Temizle", command=self.temizle_canvas)
#         self.temizle.pack()
#
#     def baslat_cizim(self, event):
#         self.x1, self.y1 = event.x, event.y
#
#     def cizim(self, event):
#         x2, y2 = event.x, event.y
#         self.canvas.create_line(self.x1, self.y1, x2, y2, fill=self.cizim_rengi, width=2)
#         self.x1, self.y1 = x2, y2
#
#     def rengi_sec(self):
#         renk = tk.colorchooser.askcolor()[1]
#         if renk:
#             self.cizim_rengi = renk
#
#     def temizle_canvas(self):
#         self.canvas.delete("all")
#
# if __name__ == "__main__":
#     root = tk.Tk()
#     uygulama = CizimUygulamasi(root)
#     root.mainloop()





print("-------------------------------------------------------------------------------------------------------------------------------------------------")

#                                                                  (Text area)



# from tkinter import *
#
# w = Tk()
# w.geometry("400x300")
# w.title("Text area")
#
# text = Text(w,bg="black",font=("Ink free",20),padx=20,pady=20,fg="white")
# text.pack()
#
# w.mainloop()





# import tkinter as tk
#
# root = tk.Tk()
#
# label = tk.Label(root, text="Büyüyen içerik",bg="pink")
# label.pack(expand=True,fill="both" )
#
# root.mainloop()





#örnek2
# from tkinter import *
#
# w = Tk()
# w.geometry("400x300")
# w.title("Text area")
#
# label = Label(w,text="Metin Gir:",font="Times 12 bold")
# label.place(x=150,y=10)
#
# entry = Entry(w,font="Times 15 bold")
# entry.place(x=90,y=35)
#
# text = Text(w,bg="black",wrap="word",padx=10,pady=10,fg="white",font=("Ink free",20),height=7,width=26)
# text.place(x=0,y=65)
# def donustur():
#     cumleyi_al = entry.get()
#     text.insert(END,cumleyi_al)
# def metin_sil():
#     text.delete("1.0",END)
#
# botun = Button(w,text="Yazdır",font="Times 12 bold",bg="pink",command=donustur)
# botun.place(x=310,y=25)
#
# botun2 = Button(w,text="Text Sil",font="Times 12 bold",bg="pink",command=metin_sil)
# botun2.place(x=10,y=25)
#
# w.mainloop()



print("-------------------------------------------------------------------------------------------------------------------------------------------------")

#                                                                 (grid kullanımı)


# columnspan: widgetin kaç sütün kaplayacağı belirtir
# rowspan: Widget'ın kaç satırı kaplayacağını belirtir.

# from tkinter import *
#
# w = Tk()
# w.geometry("250x100")
#
# firs_name_label = Label(w,text="First Name : ",font="Times 10 bold").grid(row=0,column=0)
# firs_name_entry = Entry(w,font="Times 10 bold").grid(row=0,column=1)
#
# last_name_label = Label(w,text="last Name : ",font="Times 10 bold").grid(row=1,column=0)
# last_name_entry = Entry(w,font="Times 10 bold").grid(row=1,column=1)
#
# email_label = Label(w,text="Email : ",font="Times 10 bold").grid(row=2,column=0)
# email_entry = Entry(w,font="Times 10 bold").grid(row=2,column=1)
#
# botun = Button(w,text="Kaydet",font="Times 10 bold",).grid(row=3,column=0,columnspan=2)
#
# w.mainloop()



print("-------------------------------------------------------------------------------------------------------------------------------------------------")

#                                                                (key event)

# from tkinter import *
#
# w = Tk()
# def tuş_basma(event):
#     print(event.keysym + " " +"Tuşuna Bastın")      # keysym => basılan tuşun adını/sembolünü söyler
#
# w.bind("<Key>",tuş_basma)        # key => herhangi tuşun basıldğı durumunda adını söyler.
# w.bind("<Up>",tuş_basma)
# w.bind("<Down>",tuş_basma)
# w.bind("<Right>",tuş_basma)
# w.bind("<Left>",tuş_basma)

# w.mainloop()


#örnek2
# from tkinter import *
#
# w = Tk()
# w.geometry("600x500")
# def tuş_basma(event):
#     label.config(text=event.keysym)
#
#
# w.bind("<Key>",tuş_basma)
#
# label = Label(w,font=("Helvetica",100))
# label.pack()
#
# w.mainloop()


print("-------------------------------------------------------------------------------------------------------------------------------------------------")

#                                                                (mouse event)

#
# from tkinter import *
# #
# w = Tk()
# #
# def fare_hareketleri(event):
#      print("kordinatları :  x =", event.x, "y =", event.y)
#
# w.bind("<Button-1>",fare_hareketleri)   # sağ fare tuşuna tıklama
# w.bind("<Button-2>",fare_hareketleri)   # scroll fare tuşuna tıklama
# w.bind("<Button-3>",fare_hareketleri)   # sol fare tuşuna tıklama
# w.bind("<Enter>",fare_hareketleri)      #fare pencere girdiğinde
# w.bind("<Leave>",fare_hareketleri)      #fare pencereden ayrıldığında
# w.bind("<Motion>",fare_hareketleri)     #fare nereye giderse gitsin
# w.bind("<ButtonRelease>",fare_hareketleri)  # fare tıklanmayı bıraktığında
#
# w.mainloop()




print("-------------------------------------------------------------------------------------------------------------------------------------------------")


# #                                                       (drop and drag:sürükle ve bırak)
# from tkinter import *
# #
# # 3 fonksiyon görevi:
# # start_drag işlevi sürükleme işlemine başlandığında başlangıç koordinatlarını kaydeder,
# # drag işlevi nesneyi sürükleyerek yeni konumuna yerleştirir ve end_drag işlevi sürükleme işlemi tamamlandığında başlangıç konumunu temizler.
# def start_drag(event):            # Bu fonksiyon,sürükleme işlemine başladığında Label'ın başlangıç konumunu kaydetmek için kullanılır.
#     label.start_drag_x = event.x   # label.start_drag_x ve label.start_drag_y adında iki değişken oluşturur ve bunlara event.x ve event.y ile fare imlecinin
#     label.start_drag_y = event.y   # x ve y başlangıç koordinatlarını atar. Bu, kullanıcının sürükleme işlemine başladığı noktanın konumunu saklamak için kullanılır.
#
#
# def drag(event):                        # Bu fonksiyon, sürükleme işlemi sırasında Label'ı yeni konumuna taşımak için kullanılır.
#     x, y = event.x, event.y             # Yeni x ve y konumları event.x ve event.y ile alınır.
#     label.place(x=x - label.start_drag_x + label.winfo_x(), y=y - label.start_drag_y + label.winfo_y())
# # Eski konumu (label.start_drag_x ve label.start_drag_y) ve nesnenin mevcut konumunu (label.winfo_x() ve label.winfo_y()) kullanarak, Label'ı yeni konumuna yerleştirir.
#
# def end_drag(event):            # Sürükleme işlemi tamamlandığında, label.start_drag_x ve label.start_drag_y değişkenlerini None olarak ayarlar.
#     label.start_drag_x = None   # Bu, sürükleme işleminin tamamlandığını belirtir ve başlangıç konumunun temizlendiği anlamına gelir.
#     label.start_drag_y = None
#
# root = Tk()
# root.geometry("400x400")
#
# label = Label(root, bg="red",width=10,height=5)
# label.place(x=0,y=0)
#
# # 3 kod satırı:
# # kullanıcının fareyi kullanarak bir Label'ı sürükleyip bırakmasını sağlayan temel sürükleme işlevselliğini uygular.
# label.bind("<ButtonPress-1>", start_drag) # bir Label'ı fare düğmesine tıklama olayıyla sürükleme işlemine başlamak için bir olay bağlar.
# label.bind("<B1-Motion>", drag)           # fareyi sürükleyerek Label'ı taşımak için kullanılan olayı tanımlar.
# label.bind("<ButtonRelease-1>", end_drag) # fare sol düğmesini bırakarak sürükleme işlemini sonlandırmak için kullanılan olayı tanımlar.
#
# root.mainloop()




#örnek2
# from tkinter import *
#
# window = Tk()
# window.geometry("500x400")
# def drag_strat(event):
#     label.stratX = event.x
#     label.stratY = event.y
# def drag_motion(event):
#     x = label.winfo_x() - label.stratX + event.x
#     y = label.winfo_y() - label.stratY + event.y
#     label.place(x=x,y=y)
#
# label = Label(window,bg="red",width=10,height=5)
# label.place(x=0,y=0)
#
# label.bind("<Button-1>",drag_strat)
# label.bind("<B1-Motion>",drag_motion)
#
# window.mainloop()



# ikili label
# from tkinter import *
#
# window = Tk()
# window.geometry("500x400")
# def drag_strat(event):
#     widget = event.widget
#     widget.stratX = event.x
#     widget.stratY = event.y
# def drag_motion(event):
#     widget = event.widget
#     x = widget.winfo_x() - widget.stratX + event.x
#     y = widget.winfo_y() - widget.stratY + event.y
#     widget.place(x=x,y=y)
#
# label = Label(window,bg="red",width=10,height=5)
# label.place(x=300,y=100)
# label2 = Label(window,bg="blue",width=10,height=5)
# label2.place(x=100,y=100)
#
# label.bind("<Button-1>",drag_strat)
# label.bind("<B1-Motion>",drag_motion)
# label2.bind("<Button-1>",drag_strat)
# label2.bind("<B1-Motion>",drag_motion)
#
# window.mainloop()


print("-------------------------------------------------------------------------------------------------------------------------------------------------")

#                                                                (filedialog)

# dosya açma

# from tkinter import *
# from tkinter import filedialog

# w = Tk()
# w.geometry("200x200")
# def open_file():
#     file_path = filedialog.askopenfilename(initialdir="C:\\Users\\90507\\OneDrive\\Masaüstü",title="Open File",filetypes=[("Metin Dosyası","*.Txt"),("Tüm Dosyalar","*.*")])
#     # print(file_path)                       # dosyanın yolunu ekranda yazdırır
#     file = open(file_path,"r")             # dosyayı açar ve için okur yani ekrana yazdırır.
#     print(file.read())
#     file.close()

# button = Button(w,text="Open",command=open_file)
# button.pack()

# w.mainloop()








# dosyaya kaydetme

# from tkinter import *
# from tkinter import filedialog
#
# w = Tk()
# w.geometry("400x400")
#
# def save_file():
#     file = filedialog.asksaveasfile(initialdir="C:\\Users\\90507\\yedek_kodlar\\PythonKonuları",filetypes=[("Metin Dosyası",".txt"),("Tüm Dosyalar","*.*")])
#     tex_al = text.get(1.0,END)
#     file.write(tex_al)
#     file.close()
#
# botun = Button(w,text="save",font=("Ink free",20),command=save_file)
# botun.pack()
#
# text = Text(w,font=("Ink free",20))
# text.pack()
#
# w.mainloop()





print("-------------------------------------------------------------------------------------------------------------------------------------------------")

#                                                              (tab:sekme)

# from tkinter import *
# from tkinter import ttk
#
# window = Tk()
# window.geometry("600x600")
#
# notebook = ttk.Notebook(window)
#
# sekme1 = Frame(notebook)
# sekme2 = Frame(notebook)
#
# notebook.add(sekme1,text="sekme bir ")
# notebook.add(sekme2,text="sekme iki ")
# notebook.pack(expand=True,fill="both")
#
# Label(sekme1,text="Merhaba sekme 1",width=50,height=25,background="blue").pack()
# Label(sekme2,text="Merhaba sekme 2",width=50,height=25,background="red").pack()
#
#
# window.mainloop()

