from tkinter import *

"""
Entry:
kullanıcıdan tek satırlık metin girişi almak için kullanılan bir widget'tır. 
Örneğin, kullanıcı bir isim, parola veya sayı yazabilir.
"""

pencere = Tk()
pencere.title('arayüz')
pencere.geometry('500x400+500+200')

Entry(pencere).pack()
Entry(pencere,font=('Arial 15 bold '),bg='yellow',fg='red',border=6,width=25,cursor='pirate').pack()

Entry(pencere,relief='raised').pack(pady= 15)
Entry(pencere,relief='groove').pack(pady= 15)
Entry(pencere,relief='sunken').pack(pady= 15)

Entry(pencere,show='*').pack()

Entry(pencere,justify='right').pack()

Entry(pencere,selectbackground='blue',selectforeground='white').pack()

Entry(pencere).pack()
Entry(pencere,state='disabled').pack()
Entry(pencere,state='normal').pack()

ent1 = Entry(pencere)
ent1.pack()
def click_button():
    # print(ent1.get())
    ent1.insert(5,'/')

Button(pencere,text='cick here',command=click_button).pack()

pencere.mainloop()