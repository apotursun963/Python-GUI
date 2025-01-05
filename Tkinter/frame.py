from tkinter import *

pencere = Tk()
pencere.title('arayüz')
pencere.geometry('500x400+500+200')

Frame(pencere,height=120,width=150,bg='orange',highlightbackground='blue',highlightthickness=6,cursor='spider',).pack()

frame1 = Frame(pencere,height=120,width=150,bg='orange',highlightbackground='blue',highlightthickness=6,
               cursor='spider',padx=5,pady=5)
frame1.pack()

lab1 = Label(frame1,text='herkese salam ')
lab1.place(x=0,y=0)

pencere.mainloop()
