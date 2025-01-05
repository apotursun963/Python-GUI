from tkinter import *

pencere = Tk()
pencere.title('arayüz')
pencere.geometry('500x400+500+200')

Button(pencere,text='tıkla!',font='times 15',bg='red',fg='white').pack()
Button(pencere,text='tıkla!',font='times 15',activebackground='blue',activeforeground='yellow').pack(pady=10)

cursor_list = [
 'arrow',
 'circle',
 'clock',
 'cross',
 'dotbox',
 'exchange'
]

for cursor_item in cursor_list:
    Button(pencere,text='tıkla',cursor=cursor_item).pack(pady=5)

Button(pencere,text='tıkla!',font='times 15',bg='red',fg='white',height=10,width=20,bd=6).pack()

def tıklanmak():
    print('tamam tıkladın yeter')
Button(pencere,text='tıkla!',font='times 15',bg='red',fg='white',command=tıklanmak).pack(pady=15)

Button(pencere,text='tıkla!',font='times 15',pady=15).pack(pady=5)
Button(pencere,text='tıkla!',font='times 15',padx=15).pack(pady=5)
Button(pencere,text='tıkla!',font='times 15',pady=15).pack(pady=5)

relief_list = [
    'groove',
    'sunken',
    'raised'
]

for relief_item in relief_list:
    Button(pencere,text='hadi buraya tıkla',relief=relief_item).pack(pady=3)

Button(pencere,text='tıkla!',state='normal').pack()
Button(pencere,text='tıkla!',state='disabled').pack()

pencere.mainloop()
