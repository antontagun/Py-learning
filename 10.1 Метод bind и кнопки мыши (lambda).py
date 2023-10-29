from tkinter import *

root = Tk()

# bind - это метод, который связывает виджет и функцию-обработчик через событие (event)

def change(bg, fg):
    lbl['bg'] = bg
    lbl['fg'] = fg

lbl = Label(text='Example', bg='red', fg='white')
lbl.pack()

# event - обязательный параметр передаем сразу здесь в lambda
lbl.bind('<Button-1>', lambda e, bg='blue', fg='purple': change(bg=bg, fg=fg))  # '<Button-1>' - нажали ЛКМ
lbl.bind('<Button-3>', lambda e, bg='lightblue', fg='orange': change(bg=bg, fg=fg))  # '<Button-3>' - нажали ПКМ

# Другие события: '<Double-Button-1>' - двойной ЛКМ, '<Key-space>' - пробел и т.п.
#! Все события можно посмотреть в документации tkinter

mainloop()