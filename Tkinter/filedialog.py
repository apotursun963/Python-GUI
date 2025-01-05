# dosya açma

from tkinter import *
from tkinter import filedialog

w = Tk()
w.geometry("200x200")
def open_file():
    file_path = filedialog.askopenfilename(initialdir="C:\\Users\\90507\\OneDrive\\Masaüstü",title="Open File",filetypes=[("Metin Dosyası","*.Txt"),("Tüm Dosyalar","*.*")])
    # print(file_path)                       # dosyanın yolunu ekranda yazdırır
    file = open(file_path,"r")             # dosyayı açar ve için okur yani ekrana yazdırır.
    print(file.read())
    file.close()

button = Button(w,text="Open",command=open_file)
button.pack()

w.mainloop()


# dosyaya kaydetme

from tkinter import *
from tkinter import filedialog

w = Tk()
w.geometry("400x400")

def save_file():
    file = filedialog.asksaveasfile(initialdir="C:\\Users\\90507\\yedek_kodlar\\PythonKonuları",filetypes=[("Metin Dosyası",".txt"),("Tüm Dosyalar","*.*")])
    tex_al = text.get(1.0,END)
    file.write(tex_al)
    file.close()

botun = Button(w,text="save",font=("Ink free",20),command=save_file)
botun.pack()

text = Text(w,font=("Ink free",20))
text.pack()

w.mainloop()