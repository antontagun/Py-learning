from tkinter import *
from tkinter import messagebox as mb

root = Tk()

def showerror_():
    s = entry.get()
    if not s.isdigit():
        mb.showerror('Error!', 'Нужно ввести число')
    else:
        entry.delete(0, END)
        label['text'] = s

entry = Entry()
entry.pack()
Button(text='Вывести', command=showerror_).pack()
label = Label(bg='white', height=3)
label.pack()

mainloop()
