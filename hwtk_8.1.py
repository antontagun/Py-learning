from tkinter import *

root = Tk()
root.geometry('300x300+500+500')
canvas = Canvas(width=1000, height=1000)
canvas.pack()

def rectangle(e):
    x = e.x
    y = e.y
    lst.append(x)
    lst.append(y)
    if len(lst) == 4:
        canvas.create_rectangle(*lst, outline='blue', fill='orange', width=3)
        lst.clear()

root.bind('<Button-1>', rectangle)

lst = []

mainloop()