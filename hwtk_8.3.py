from tkinter import *

root = Tk()
root.geometry('300x300+500+500')
canvas = Canvas(width=1000, height=1000)
canvas.pack()
def move(e):

    x = e.x
    y = e.y
    canvas.create_line(x - 1, y - 1, x, y, fill='black', width=2)

root.bind('<B1-Motion>', move)


mainloop()