from tkinter import *

pencere = Tk()
pencere.title('arayüz')
pencere.geometry('500x400+500+200')

def yazdir():
    print(spin1.get())

spin1 = Spinbox(pencere,from_=1,to=15,increment=2,justify= 'center',
                    width=25,font=('times 8 bold'),command=yazdir)
spin1.pack()

pencere.mainloop()
