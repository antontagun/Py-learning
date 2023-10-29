from tkinter import *

frame = Tk()

#! Посмотри как выглядят размещение в минимальном окне и в полноэкранном режиме

#! В GUI, как правило, расположение каждого последующего элемента зависит от предыдущего

# expand=True -> виджет занимает все доступное пространство в пределах своих размеров
lbl1 = Label(text='label', height=10, bg='lightblue')
lbl1.pack(expand=False, fill=X)

mainloop()