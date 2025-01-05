from tkinter import *

"""
Label:
Bir pencere veya uygulama arayüzünde metin veya görüntü göstermek için kullanılan temel bir bileşendir. 
"""

pencere = Tk()
pencere.title('tkinter öğreniyorum')
pencere.geometry('500x400+500+200')

Label(pencere,text='hoşgeldiniz').pack()
Label(pencere,text='hoşgeldiniz',font=('times',15,'underline')).pack()
Label(pencere,text='hoşgeldiniz',font=('times',20),bg='red',fg='yellow').pack()
Label(pencere,text='hoşgeldiniz',font=('times',20),bg='blue',fg='pink',width=18,height=6).pack()
Label(pencere,text='hoşgeldiniz',font=('times',20),bg='green',fg='purple',width=24,height=12,anchor='nw').pack()
Label(pencere,font=('times',15,),bitmap='warning',).pack()

Label(pencere,text='hoşgeldiniz',font=('times',15),bg='red',fg='yellow').pack()
Label(pencere,text='hoşgeldiniz',font=('times',15),bg='red',fg='yellow',padx=20).pack()
Label(pencere,text='hoşgeldiniz',font=('times',15),bg='red',fg='yellow',pady=15).pack()

Label(pencere,text='hoşgeldiniz',font=('times',15),relief='raised').pack()

pencere.mainloop()
