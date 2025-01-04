from PIL import Image, ImageTk
from tkinter import *
import time

w = Tk()

WIDTH = 400
HEIGHT = 400

X_hizi = 4
Y_hizi = 3

canvas = Canvas(w,width=WIDTH,height=HEIGHT)
canvas.pack()

background_photo = PhotoImage(file="Ekran görüntüsü 2024-04-16 163751.png")
background = canvas.create_image(0,0,image=background_photo,anchor=NW)

image = Image.open("apo.jpg")
photo_image = ImageTk.PhotoImage(image)
my_image = canvas.create_image(0,0,image=photo_image,anchor=NW)

image_width = photo_image.width()
image_height = photo_image.height()

while True:
    kordinatlar = canvas.coords(my_image)
    print(kordinatlar)

    if kordinatlar[0]>=WIDTH-image_width or kordinatlar[0]<0:
        X_hizi = -X_hizi

    if kordinatlar[1]>=HEIGHT-image_height or kordinatlar[1]<0:
        Y_hizi = -Y_hizi

    canvas.move(my_image,X_hizi,Y_hizi)
    w.update()
    time.sleep(0.01)

w.mainloop()
