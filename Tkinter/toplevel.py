from tkinter import *

window = Tk()
window.title("Ana Pencere")
window.geometry("300x200")

def pencere_olustur():
    toplevel = Toplevel(window, bg="red",height=150,width=300)

button = Button(window,text="pencere oluştur",command=pencere_olustur)
button.pack()
window.mainloop()
