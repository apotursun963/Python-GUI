from tkinter import *
from tkinter import ttk

window = Tk()
window.geometry("600x600")

notebook = ttk.Notebook(window)

sekme1 = Frame(notebook)
sekme2 = Frame(notebook)

notebook.add(sekme1,text="sekme bir ")
notebook.add(sekme2,text="sekme iki ")
notebook.pack(expand=True,fill="both")

Label(sekme1,text="Merhaba sekme 1",width=50,height=25,background="blue").pack()
Label(sekme2,text="Merhaba sekme 2",width=50,height=25,background="red").pack()

window.mainloop()