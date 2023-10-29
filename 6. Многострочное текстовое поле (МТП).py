from tkinter import *

frame = Tk()

#wrap=WORD -> перенос текст, не разрывая слова
text = Text(width=25, height=10, bg='lightblue', fg='red', wrap=WORD)
text.pack(side=LEFT)

# Скроллинг
scroll = Scrollbar(command=text.yview)
scroll.pack(side=LEFT, fill=Y)
# связка скроллинга с текстом
text.config(yscrollcommand=scroll.set)

mainloop()