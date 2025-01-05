from tkinter import *
#
# 3 fonksiyon görevi:
# start_drag işlevi sürükleme işlemine başlandığında başlangıç koordinatlarını kaydeder,
# drag işlevi nesneyi sürükleyerek yeni konumuna yerleştirir ve end_drag işlevi sürükleme işlemi tamamlandığında başlangıç konumunu temizler.
def start_drag(event):            # Bu fonksiyon,sürükleme işlemine başladığında Label'ın başlangıç konumunu kaydetmek için kullanılır.
    label.start_drag_x = event.x   # label.start_drag_x ve label.start_drag_y adında iki değişken oluşturur ve bunlara event.x ve event.y ile fare imlecinin
    label.start_drag_y = event.y   # x ve y başlangıç koordinatlarını atar. Bu, kullanıcının sürükleme işlemine başladığı noktanın konumunu saklamak için kullanılır.


def drag(event):                        # Bu fonksiyon, sürükleme işlemi sırasında Label'ı yeni konumuna taşımak için kullanılır.
    x, y = event.x, event.y             # Yeni x ve y konumları event.x ve event.y ile alınır.
    label.place(x=x - label.start_drag_x + label.winfo_x(), y=y - label.start_drag_y + label.winfo_y())
# Eski konumu (label.start_drag_x ve label.start_drag_y) ve nesnenin mevcut konumunu (label.winfo_x() ve label.winfo_y()) kullanarak, Label'ı yeni konumuna yerleştirir.

def end_drag(event):            # Sürükleme işlemi tamamlandığında, label.start_drag_x ve label.start_drag_y değişkenlerini None olarak ayarlar.
    label.start_drag_x = None   # Bu, sürükleme işleminin tamamlandığını belirtir ve başlangıç konumunun temizlendiği anlamına gelir.
    label.start_drag_y = None

root = Tk()
root.geometry("400x400")

label = Label(root, bg="red",width=10,height=5)
label.place(x=0,y=0)

# 3 kod satırı:
# kullanıcının fareyi kullanarak bir Label'ı sürükleyip bırakmasını sağlayan temel sürükleme işlevselliğini uygular.
label.bind("<ButtonPress-1>", start_drag) # bir Label'ı fare düğmesine tıklama olayıyla sürükleme işlemine başlamak için bir olay bağlar.
label.bind("<B1-Motion>", drag)           # fareyi sürükleyerek Label'ı taşımak için kullanılan olayı tanımlar.
label.bind("<ButtonRelease-1>", end_drag) # fare sol düğmesini bırakarak sürükleme işlemini sonlandırmak için kullanılan olayı tanımlar.

root.mainloop()


# örnek2:

from tkinter import *

window = Tk()
window.geometry("500x400")
def drag_strat(event):
    widget = event.widget
    widget.stratX = event.x
    widget.stratY = event.y
def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.stratX + event.x
    y = widget.winfo_y() - widget.stratY + event.y
    widget.place(x=x,y=y)

label = Label(window,bg="red",width=10,height=5)
label.place(x=300,y=100)
label2 = Label(window,bg="blue",width=10,height=5)
label2.place(x=100,y=100)

label.bind("<Button-1>",drag_strat)
label.bind("<B1-Motion>",drag_motion)
label2.bind("<Button-1>",drag_strat)
label2.bind("<B1-Motion>",drag_motion)

window.mainloop()