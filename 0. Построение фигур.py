from tkinter import *

root = Tk()

# создаем холст (область для рисования)
canvas = Canvas(width=500, height=500)
canvas.pack()

# Линии
canvas.create_line(0, 0, 100, 150, fill='red', width=2)

# Прямоугольники: координаты л.в.у. (левого верхнего угла) и п.н.у. (правого нижнего угла)
canvas.create_rectangle(100, 150, 300, 400, outline='blue', fill='orange', width=3)

# Квадраты
canvas.create_rectangle(350, 150, 450, 250, outline='purple', fill='yellow', width=4)

# Эллипсы, окружности
#canvas.create_oval()

# Дуги
#canvas.create_arc()

# Многоугольники
#canvas.create_polygon()

mainloop()