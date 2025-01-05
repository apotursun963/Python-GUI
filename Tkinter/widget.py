from tkinter import *

pencere = Tk()
pencere.title('arayüz')
pencere.geometry('500x400+500+200')

lab1 = Label(pencere,text='merhabalar ben deneme 1')
lab1.grid(row=0,column=0)
lab2 = Label(pencere,text='merhabalar ben deneme 2')
lab2.grid(row=1,column=0)
lab3 = Label(pencere,text='merhabalar ben deneme 3')
lab3.grid(row=2,column=0,padx= 20,pady=20)

Label(pencere,text='merhabalar ben deneme 1').place(x=195,y=180)
lab2 = Label(pencere,text='merhabalar ben deneme 2')
lab2.place(x=300,y=250)

pencere.mainloop()
