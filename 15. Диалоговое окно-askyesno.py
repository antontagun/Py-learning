from tkinter import *
from tkinter import messagebox as mb

root = Tk()

def askyesno_():
    answer = mb.askyesno(title='Confirm', message='Вывести данные?')
    if answer:
        s = entry.get()
        entry.delete(0, END)
        label['text'] = s
    else:
        return entry.delete(0, END)

entry = Entry()
entry.pack()
Button(text='Вывести', command=askyesno_).pack()
label = Label(bg='white', height=3)
label.pack()

mainloop()
