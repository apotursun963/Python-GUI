from tkinter import *

w = Tk()
w.geometry("250x100")

firs_name_label = Label(w,text="First Name : ",font="Times 10 bold").grid(row=0,column=0)
firs_name_entry = Entry(w,font="Times 10 bold").grid(row=0,column=1)

last_name_label = Label(w,text="last Name : ",font="Times 10 bold").grid(row=1,column=0)
last_name_entry = Entry(w,font="Times 10 bold").grid(row=1,column=1)

email_label = Label(w,text="Email : ",font="Times 10 bold").grid(row=2,column=0)
email_entry = Entry(w,font="Times 10 bold").grid(row=2,column=1)

botun = Button(w,text="Kaydet",font="Times 10 bold",).grid(row=3,column=0,columnspan=2)

w.mainloop()
