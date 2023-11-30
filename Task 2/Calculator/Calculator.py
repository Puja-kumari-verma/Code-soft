from tkinter import *
import math

def click(value):
    ex = entryField.get()
    answer = ''
    try:
        if value == 'C':
            ex = ex[:-1]
            entryField.delete(0, END)
            entryField.insert(0, ex)
            return
        elif value == 'CE':
            entryField.delete(0, END)
        elif value == '√':
            answer = math.sqrt(eval(ex))
        elif value == 'π':
            answer = math.pi
        elif value == 'cosθ':
            answer = math.cos(math.radians(eval(ex)))
        elif value == 'tanθ':
            answer = math.tan(math.radians(eval(ex)))
        elif value == 'sinθ':
            answer = math.sin(math.radians(eval(ex)))
        elif value == '2π':
            answer = 2*math.pi
        elif value == 'cosh':
            answer = math.cosh(eval(ex))
        elif value == 'tanh':
            answer = math.tanh(eval(ex))
        elif value == 'sinh':
            answer = math.sinh(eval(ex))
        elif value == chr(8731):
            answer = eval(ex) ** (1/3)
        elif value == 'x\u02b8':
            entryField.insert(END, '**')
            return
        elif value == 'x\u00b3':
            answer = eval(ex) ** 3
        elif value == 'ln':
            answer = math.log(eval(ex))
        elif value == 'deg':
            answer = math.degrees(eval(ex))
        elif value == "rad":
            answer = math.radians(eval(ex))
        elif value == 'e':
            answer = math.e
        elif value == 'log10':
            answer = math.log10(eval(ex))
        elif value == 'x!':
            answer = math.factorial(int(eval(ex)))
        elif value == chr(247):
            entryField.insert(END, "/")
            return
        elif value == '=':
            answer = eval(ex)
        else:
            entryField.insert(END, value)
            return

        entryField.delete(0, END)
        entryField.insert(0, answer)

    except Exception as e:
        entryField.delete(0, END)
        entryField.insert(0, "Error")

root = Tk()
root.title('Smart Calculator')
root.config(bg='dodgerblue3')
root.geometry('680x486+100+100')

entryField = Entry(root, font=('arial', 20, 'bold'), bg='dodgerblue3', fg='white')
entryField.grid(row=0, column=0, columnspan=8)

buttonTextList = (
    "C", "CE", "√", "+", "π", "cosθ", "tanθ", "sinθ",
    "1", "2", "3", "-", "2π", "cosh", "tanh", "sinh",
    "4", "5", "6", "*", chr(8731), "x\u02b8", "x\u00b3", "x\u00b2",
    "7", "8", "9", chr(247), "ln", "deg", "rad", "e",
    "0", ".", "%", "=", "log10", "(", ")", "x!"
)

rowValue = 1
columnValue = 0

for i in buttonTextList:
    button = Button(root, width=5, height=2, bd=2, relief=SUNKEN, text=i, bg='dodgerblue3', fg='white',
                    font=('arial', 18, 'bold'), activebackground='dodgerblue3',
                    command=lambda button=i: click(button))
    button.grid(row=rowValue, column=columnValue, pady=1)
    columnValue += 1
    if columnValue > 7:
        rowValue += 1
        columnValue = 0

root.mainloop()









