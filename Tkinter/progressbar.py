from tkinter import *
from tkinter.ttk import *
import time

def copy_file():
    for i in range(1, 101):
        time.sleep(0.1)
        progress_var.set(i)
        root.update_idletasks()  # İlerleme çubuğunu güncelle, ancak ana döngüyü bekletme

root = Tk()
root.title("Dosya Kopyalama İlerleme Çubuğu")

progress_var = IntVar()
progress_var.set(0)                # set() ile progress_var değişkenin değerini 0 olarak ayarladık

progress_bar = Progressbar(root, variable=progress_var, maximum=100)
progress_bar.pack(pady=10)

start_button = Button(root, text="Başlat", command=copy_file)
start_button.pack()

root.mainloop()


# örnek2:

from tkinter import *
from tkinter.ttk import *

window = Tk()
window.geometry("400x200")

progress_bar = Progressbar(window,orient=HORIZONTAL,length=300,mode="determinate")
progress_bar.pack(pady=15)

def ilerlet():
    yeni_deger = progress_bar["value"]
    if yeni_deger < 100:
        progress_bar["value"] = yeni_deger + 10
    else:
        progress_bar["value"] = 0

botun = Button(window,text="Tıkla",command=ilerlet)
botun.pack()

window.mainloop()