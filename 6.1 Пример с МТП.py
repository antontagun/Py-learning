from tkinter import *

frame = Tk()

#wrap=WORD -> перенос текст, не разрывая слова
text = Text(width=25, height=10, bg='lightblue', fg='red', wrap=WORD)
text.pack(side=LEFT)

mainloop()