from tkinter import *

root = Tk()
root.geometry('300x300+500+500')

def start(e):
    global x1, y1
    x1 = e.x
    y1 = e.y
    canvas.bind('<B1-Motion>', rectangle)

def rectangle(e):
    x2 = e.x
    y2 = e.y
    canvas.create_rectangle(x1, y1, x2, y2)
    canvas.bind('<B1-Motion>', clear)

def clear(e):
    canvas.delete('all')
    rectangle(e)

canvas = Canvas(width=1000, height=1000)
canvas.pack()

canvas.bind('<Button-1>', start)

mainloop()