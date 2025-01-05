from tkinter import *

w = Tk()

def fare_hareketleri(event):
     print("kordinatları :  x =", event.x, "y =", event.y)

w.bind("<Button-1>",fare_hareketleri)   # sağ fare tuşuna tıklama
w.bind("<Button-2>",fare_hareketleri)   # scroll fare tuşuna tıklama
w.bind("<Button-3>",fare_hareketleri)   # sol fare tuşuna tıklama
w.bind("<Enter>",fare_hareketleri)      #fare pencere girdiğinde
w.bind("<Leave>",fare_hareketleri)      #fare pencereden ayrıldığında
w.bind("<Motion>",fare_hareketleri)     #fare nereye giderse gitsin
w.bind("<ButtonRelease>",fare_hareketleri)  # fare tıklanmayı bıraktığında

w.mainloop()