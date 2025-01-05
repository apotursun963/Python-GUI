from PIL import Image, ImageTk
import tkinter as tk
import time

w = tk.Tk()

WIDTH = 600
HEIGHT = 500

X_hizi = 4
Y_hizi = 3

canvas = tk.Canvas(w,width=WIDTH,height=HEIGHT)
canvas.pack()

background_photo = tk.PhotoImage(file="C:\\Users\\90507\\OneDrive\\Masaüstü\\Python-GUI\\images\\space.png")
background = canvas.create_image(0,0,image=background_photo,anchor=tk.NW)

image = Image.open("C:\\Users\\90507\\OneDrive\\Masaüstü\\Python-GUI\\images\\ball.png")
photo_image = ImageTk.PhotoImage(image)
my_image = canvas.create_image(0,0,image=photo_image,anchor=tk.NW)

image_width = photo_image.width()
image_height = photo_image.height()

while True:
    kordinatlar = canvas.coords(my_image)
    print(kordinatlar)

    if kordinatlar[0] >= WIDTH - image_width or kordinatlar[0] < 0:
        X_hizi = - X_hizi

    if kordinatlar[1] >= HEIGHT - image_height or kordinatlar[1] < 0:
        Y_hizi = - Y_hizi

    canvas.move(my_image,X_hizi,Y_hizi)
    w.update()
    time.sleep(0.01)

w.mainloop()
