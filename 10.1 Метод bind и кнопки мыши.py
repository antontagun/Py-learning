from tkinter import *

root = Tk()

# bind - это метод, который связывает виджет и функцию-обработчик через событие (event)

def left(event):  # event - обязательный параметр
    lbl['bg'] = 'blue'
    lbl['fg'] = 'purple'

def right(event):  # event - обязательный параметр
    lbl['bg'] = 'lightblue'
    lbl['fg'] = 'orange'

lbl = Label(text='Example', bg='red', fg='white')
lbl.pack()

lbl.bind('<Button-1>', left)  # '<Button-1>' - нажали ЛКМ
lbl.bind('<Button-3>', right)  # '<Button-3>' - нажали ПКМ

mainloop()