from tkinter import *

root = Tk()

# bind - это метод, который связывает виджет и функцию-обработчик через событие (event)

def change_mouse(event):  # event - обязательный параметр
    but['bg'] = 'blue'

def change_key(e):  # имя параметра значения не имеет
   but['bg'] = 'red'

but = Button(bg='green', width=12, height=5)
but.pack()
but.bind('<Button-1>', change_mouse)  # '<Button-1>' - нажали ЛКМ
# для того, чтобы элемент управления "клавиша клавиатуры" стал активным, нужно нажать TAB (сфокусировать)
but.bind('<Return>', change_key)  # '<Return>' - нажали на Enter

mainloop()