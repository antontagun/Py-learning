from tkinter import *

root = Tk()
root.geometry('300x300+500+500')

#! координаты размещения виджета - это координаты левого верхнего угла
Button(bg='red').place(x=250, y=150)  # абсолютные координаты
Button(bg='green').place(relx=0.3, rely=0.1)  # относительные координаты (в частях экрана)

mainloop()