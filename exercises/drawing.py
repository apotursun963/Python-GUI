
import tkinter as tk
from tkinter import colorchooser

class CizimUygulamasi:
    def __init__(self, root):
        self.root = root
        self.root.title("Gelişmiş Çizim Uygulaması")

        self.canvas = tk.Canvas(root, width=800, height=600, bg="white")
        self.canvas.pack()

        self.cizim_rengi = "black"

        self.canvas.bind("<Button-1>", self.baslat_cizim)
        self.canvas.bind("<B1-Motion>", self.cizim)

        self.rengi_sec = tk.Button(root, text="Rengi Seç", command=self.rengi_sec)
        self.rengi_sec.pack()

        self.temizle = tk.Button(root, text="Temizle", command=self.temizle_canvas)
        self.temizle.pack()

    def baslat_cizim(self, event):
        self.x1, self.y1 = event.x, event.y

    def cizim(self, event):
        x2, y2 = event.x, event.y
        self.canvas.create_line(self.x1, self.y1, x2, y2, fill=self.cizim_rengi, width=2)
        self.x1, self.y1 = x2, y2

    def rengi_sec(self):
        renk = tk.colorchooser.askcolor()[1]
        if renk:
            self.cizim_rengi = renk

    def temizle_canvas(self):
        self.canvas.delete("all")

if __name__ == "__main__":
    root = tk.Tk()
    uygulama = CizimUygulamasi(root)
    root.mainloop()
