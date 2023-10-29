from tkinter import *

root = Tk()
root.geometry('+500+500')
def change(e):
    print(e)  # смотрим на e как на объект
    if ent1.get().isdigit():
        txt['width'] = ent1.get()
    if ent2.get().isdigit():
        txt['height'] = ent2.get()

def red(e):
    print(e)  # смотрим на e как на объект
    txt['bg'] = 'red'

def green(e):
    print(e)  # смотрим на e как на объект
    txt['bg'] = 'green'

#! Даже если мы не используем event явно, tkinter его использует "под капотом"

frame = Frame()
frame.pack()

frame1 = Frame(frame)
frame1.pack(side=LEFT)

ent1 = Entry(frame1, width=5)
ent1.pack()
ent2 = Entry(frame1, width=5)
ent2.pack()

but = Button(frame, text='CHANGE')
but.pack(side=LEFT)
but.bind('<Button-1>', change)  # нажали на ЛКМ
but.bind('<Return>', change)   # нажали на ENTER

frame2 = Frame()
frame2.pack()

txt = Text(frame2, width=25, height=10, bg='orange')
txt.pack()
txt.bind('<FocusIn>', red)  # сфокусированный объект
txt.bind('<FocusOut>', green)  # расфокусированный объект


mainloop()