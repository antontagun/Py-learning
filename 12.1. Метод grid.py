from tkinter import *

root = Tk()
root.geometry('300x300+500+500')

def hidden1():
    # все пустые типы возвращают False
    if not l1.grid_info():
        return l1.grid()
    l1.grid_remove()

def hidden2():
    # все пустые типы возвращают False
    if not l2.grid_info():
        return l2.grid()
    l2.grid_remove()

l1 = Label(width=10, height=5, bg='red')
l2 = Label(width=10, height=5, bg='green')
b1 = Button(bg='pink', command=hidden1)
b2 = Button(bg='lightgreen', command=hidden2)
l1.grid()
l2.grid(row=1)
b1.grid(row=2)
b2.grid(row=3)

mainloop()