from tkinter import *

w = Tk()
w.geometry("400x300")
w.title("Text area")

label = Label(w,text="Metin Gir:",font="Times 12 bold")
label.place(x=150,y=10)

entry = Entry(w,font="Times 15 bold")
entry.place(x=90,y=35)

text = Text(w,bg="black",wrap="word",padx=10,pady=10,fg="white",font=("Ink free",20),height=7,width=26)
text.place(x=0,y=65)
def donustur():
    cumleyi_al = entry.get()
    text.insert(END,cumleyi_al)
def metin_sil():
    text.delete("1.0",END)

botun = Button(w,text="Yazdır",font="Times 12 bold",bg="pink",command=donustur)
botun.place(x=310,y=25)

botun2 = Button(w,text="Text Sil",font="Times 12 bold",bg="pink",command=metin_sil)
botun2.place(x=10,y=25)

w.mainloop()
