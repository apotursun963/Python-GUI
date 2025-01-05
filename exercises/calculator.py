from tkinter import *

w = Tk()
w.title("Hesap Makinesi")
w.geometry("300x360+600+100")

def clear():
    entry.delete(0, END)

def show(value=None):
    current_text = entry_var.get()
    if value == "=":
        evaluate()
    else:
        entry_var.set(current_text + value)

def enter_key(event):
    if event.keysym == "Return":
        show("=")

def evaluate():
    expression = entry_var.get()
    try:
        result = calculate(expression)
        entry_var.set(int(result))
    except:
        entry_var.set("Hata")

def calculate(expression):
    operators = "+-*/"
    stack = []
    postfix = []
    number = ""
    for char in expression:
        if char.isnumeric() or char == ".":
            number += char
        elif char in operators:
            if number:
                postfix.append(number)
                number = ""
            while (stack and stack[-1] in operators and operators.index(char) <= operators.index(stack[-1])):
                postfix.append(stack.pop())
            stack.append(char)
    if number:
        postfix.append(number)
    while stack:
        postfix.append(stack.pop())
    stack = []
    for char in postfix:
        if char.isnumeric() or char.replace(".", "").isnumeric():
            stack.append(float(char))
        elif char in operators:
            b = stack.pop()
            a = stack.pop()
            if char == '+':
                stack.append(a + b)
            elif char == '-':
                stack.append(a - b)
            elif char == '*':
                stack.append(a * b)
            elif char == '/':
                stack.append(a / b)
    return stack[0]

entry_var = StringVar()
entry = Entry(w, font="Times 25 bold", width=29, justify="left", textvariable=entry_var)
entry.place(x=1, y=25)

botun1 = Button(w, width=5, height=2, relief="ridge", text="7", font="Times 15 bold", border=3, command=lambda: show("7"))
botun1.place(x=3, y=80)
botun2 = Button(w, width=5, height=2, relief="ridge", text="4", font="Times 15 bold", border=3, command=lambda: show("4"))
botun2.place(x=3, y=150)
botun3 = Button(w, width=5, height=2, relief="ridge", text="1", font="Times 15 bold", border=3, command=lambda: show("1"))
botun3.place(x=3, y=220)
botun4 = Button(w, width=5, height=2, relief="ridge", text="C", font="Times 15 bold", bg="gray", fg="white", border=3, command=clear)
botun4.place(x=3, y=290)

botun5 = Button(w, width=5, height=2, relief="ridge", text="8", font="Times 15 bold", border=3, command=lambda: show("8"))
botun5.place(x=77, y=80)
botun6 = Button(w, width=5, height=2, relief="ridge", text="5", font="Times 15 bold", border=3, command=lambda: show("5"))
botun6.place(x=77, y=150)
botun7 = Button(w, width=5, height=2, relief="ridge", text="2", font="Times 15 bold", border=3, command=lambda: show("2"))
botun7.place(x=77, y=220)
botun8 = Button(w, width=5, height=2, relief="ridge", text="0", font="Times 15 bold", border=3, command=lambda: show("0"))
botun8.place(x=77, y=290)

botun9 = Button(w, width=5, height=2, relief="ridge", text="9", font="Times 15 bold", border=3, command=lambda: show("9"))
botun9.place(x=150, y=80)
botun10 = Button(w, width=5, height=2, relief="ridge", text="6", font="Times 15 bold", border=3, command=lambda: show("6"))
botun10.place(x=150, y=150)
botun11 = Button(w, width=5, height=2, relief="ridge", text="3", font="Times 15 bold", border=3, command=lambda: show("3"))
botun11.place(x=150, y=220)
botun12 = Button(w, width=5, height=2, relief="ridge", text="=", font="Times 15 bold", bg="gray", fg="white", border=3, command=lambda: show("="))
botun12.place(x=150, y=290)

w.bind('<Return>', enter_key)

botun13 = Button(w, width=5, height=2, relief="ridge", text="/", font="Times 15 bold", bg="gray", fg="white", border=3, command=lambda: show("/"))
botun13.place(x=225, y=80)
botun14 = Button(w, width=5, height=2, relief="ridge", text="x", font="Times 15 bold", bg="gray", fg="white", border=3, command=lambda: show("*"))
botun14.place(x=225, y=150)
botun15 = Button(w, width=5, height=2, relief="ridge", text="-", font="Times 15 bold", bg="gray", fg="white", border=3, command=lambda: show("-"))
botun15.place(x=225, y=220)
botun16 = Button(w, width=5, height=2, relief="ridge", text="+", font="Times 15 bold", bg="gray", fg="white", border=3, command=lambda: show("+"))
botun16.place(x=225, y=290)

w.mainloop()