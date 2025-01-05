from tkinter import *

# Ana pencereyi oluştur
root = Tk()
root.title("Dikey ve Yatay Scrollbar Örneği")

# Dikey scrollbar oluştur
y_scrollbar = Scrollbar(root, orient=VERTICAL)
y_scrollbar.pack(side=RIGHT, fill=Y)

# Yatay scrollbar oluştur
x_scrollbar = Scrollbar(root, orient=HORIZONTAL)
x_scrollbar.pack(side=BOTTOM, fill=X)

# Listbox oluştur ve scrollbar'lar ile bağla
my_listbox = Listbox(root, yscrollcommand=y_scrollbar.set, xscrollcommand=x_scrollbar.set)
my_listbox.pack(fill=BOTH)

# Scrollbar'ları Listbox ile bağla(scrollo listbox'a yerleştirmek)
y_scrollbar.config(command=my_listbox.yview)    # (y_scrollbar) listbox'ın y eksenine yerlştir demek.
x_scrollbar.config(command=my_listbox.xview)    # (x_scrollbar) listbox'ın x eksenine yerlştir demek.

# Listbox'a örnek veri ekle
for i in range(50):
    my_listbox.insert(END, f"Merhabalr hoş geldiniz 0'dan 49'a kadar olan sayıları göstericem {i}")

# Ana döngüyü başlat
root.mainloop()
