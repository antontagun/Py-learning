from tkinter import *

root = Tk()
root.geometry('300x300+500+500')

def left(e):
    root.title('ЛКМ')

def right(e):
    root.title('ПКМ')

def focus(e):
    print(e)

def move(e):
    x = e.x
    y = e.y
    root.title(f'{x}x{y}')

root.bind('<Button-1>', left)
root.bind('<Button-3>', right)
root.bind('<Motion>', move)  # движение мыши
root.bind('<Return>', focus)

mainloop()