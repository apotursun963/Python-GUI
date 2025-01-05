from tkinter import *

pencere = Tk()
pencere.title('arayüz')
pencere.geometry('500x400+500+200')

lb = Listbox(selectmode=EXTENDED)

lb.insert(0,"elma")
lb.insert(1,"nar")
lb.insert(2,"karpuz")
lb.insert(3,"kavun")
lb.insert(4,"muz")
lb.insert(0,"elma")
lb.insert(1,"nar")
lb.insert(2,"karpuz")
lb.insert(3,"kavun")
lb.insert(4,"muz")
lb.insert(2,"karpuz")

lb.pack()

pencere.mainloop()