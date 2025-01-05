from tkinter import *
from tkinter import messagebox

pencere = Tk()
pencere.title('arayüz')
pencere.geometry('500x400+500+200')

def tıklanmak():

    messagebox.showinfo('bilgi göster','işleminiz başarıyla gerçekleşti')
    messagebox.showwarning('Uyarı göster','işleminiz uyarı gösteriyor')
    err = messagebox.showerror('hata göster', 'işleminiz hatalı oldu')
    print(err)
    yes_no = messagebox.askyesno('yes or no ','are you sure ? ')
    print(yes_no)
    ok_cancel = messagebox.askokcancel('okey or cancel','do you want to countinue')
    print(ok_cancel)
    retry_cancel = messagebox.askretrycancel('retry or cancel', '482789373')
    print(retry_cancel)
    ques = messagebox.askquestion('nice', '482789373')
    print(ques)
    yes_no_cancel = messagebox.askyesnocancel('yes or no or cancel', 'devammmı etmek istiyorsun')
    print(yes_no_cancel)

Button(pencere,text='tıkla!',command=tıklanmak).pack()

pencere.mainloop()
