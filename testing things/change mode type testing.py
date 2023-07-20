from tkinter import Tk, Button
variable = 1
def make_something(value):
    global variable
    variable = value
    print(variable)
root = Tk()
Button(root, text='Set value to four',command=lambda *args: make_something(4)).pack()
Button(root, text='Set value to eight',command=lambda *args: make_something(8)).pack()
Button(root, text='Set value to fifteen',command=lambda *args: make_something(15)).pack()


  