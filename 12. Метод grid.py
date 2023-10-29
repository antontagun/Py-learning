from tkinter import *

root = Tk()
root.geometry('300x300+500+500')

# В pack() -> anchor, а в grid() -> sticky
Label(text="ФИО:").grid(sticky=W, padx=10, pady=10)  # если не написать координаты, это будет точка 0,0
Entry(width=35).grid(row=0, column=1, columnspan=3)

Button(text="Save").grid(row=1, padx=10, pady=10)
Button(text="Clear").grid(row=1, column=1, padx=10, pady=10)
Button(text="Close").grid(row=1, column=2, padx=10, pady=10)

mainloop()