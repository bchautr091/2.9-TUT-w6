
from tkinter import *
Window = Tk() # start the window
Window.title('my first caculator')

#define the function
def add(): #we add with this one
    num1 = eval(FirstNumber.get())
    num2 = eval(SecondNumber.get())
    sum = num1 +num2
    ThirdNumber.set("Sum: " +str(sum))

def sub():
    num1 = eval(FirstNumber.get())
    num2 = eval(SecondNumber.get())
    minus = num1 - num2
    ThirdNumber.set("Sub: " +str(minus))

def mul():
    num1 = eval(FirstNumber.get())
    num2 = eval(SecondNumber.get())
    Multiplication  = num1 - num2
    ThirdNumber.set("mul: " +str(Multiplication))
#adding the label
MyFirstLabel = Label(Window, text = "First \nNumber: ")
MyFirstLabel.grid(row=0,column=0)
MySecondLabel = Label(Window, text = "Second \nNumber: ")
MySecondLabel.grid( row = 0, column = 2)

#adding entry
FirstNumber = StringVar()
FirstEntry = Entry(Window, width = 5, textvariable = FirstNumber)
FirstEntry.grid(row = 1, column = 0)

SecondNumber = StringVar()
SecondEntry = Entry(Window, width = 5, textvariable = SecondNumber)
SecondEntry.grid(row = 1, column = 2)

#adding the entry that print the result
ThirdNumber = StringVar()
ThirdEntry = Entry(Window, state = "readonly", width = 20, textvariable = ThirdNumber)
ThirdEntry.grid(row = 3, column = 0, columnspan = 3, padx = 40, pady = 5)

#adding buttons
btnAdd = Button(Window, text = '+', width = 3, command=add)
btnAdd.grid(row = 0,column = 1, padx = 15)

btnSub = Button(Window, text = '-', width = 3, command=sub)
btnSub.grid(row = 1,column = 1, padx = 15)

btnMul = Button(Window, text = '*', width = 3, command=mul)
btnMul.grid(row = 2,column = 1, padx = 15)

