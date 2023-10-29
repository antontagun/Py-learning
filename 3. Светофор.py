from tkinter import *

frame = Tk()
frame.geometry('200x100+700+300')  # .geometry('size_widthxsize_height+shift_width+shift_height')

# 1 кБ = 1024 байта
# 1 байт = 8 бит
# Сколько состояний может хранить 1 байт? Ответ: 2 ** 8 = 256
# Храним в байте 0: 00000000; Храним в байте 7dec: 00000111; Храним в байте 255dec: 11111111;
# Разложим десятичное число по степеням 10ки: 127 -> 1 ** 10 ** 2 + 2 * 10 ** 1 + 7 * 10 ** 0
# Преобразование bin -> dec: начиная с нулевого разряда справа налево по степеням двойки->
# 1*2**0 + 1*2**1 + 1*2**2 + 1*2**3 + 1*2**4 + 1*2**5 + 1*2**6 + 1*2**7 = 255
# RGB -> (R, G, B)dec от 0 до 255
# HEX -> '#rrggbb'hex -> 0-9 и a-f -> от 0dec до 15dec;
# '#ff0000' -> red; ff = 255dec -> 15 * 16 ** 0 + 15 * 16 ** 1 (16 -> основание системы счисления; 0, 1 - разряды)
clr = (('RED', '#ff0000'), ('YELLOW', '#ffff00'), ('GREEN', '#00ff00'))

print(clr[1])  # ('YELLOW', '#ffff00')
print(clr[1][1])  # #ffff00
print(clr[1][0][-1])  # W

def red():
    lbl['bg'] = clr[0][1]

def yellow():
    lbl['bg'] = clr[1][1]

def green():
    lbl['bg'] = clr[2][1]

lbl = Label(width=10, bg='#ffffff')
lbl.pack()
Button(width=10, text=clr[0][0], command=red).pack()
Button(width=10, text=clr[1][0], command=yellow).pack()
Button(width=10, text=clr[2][0], command=green).pack()

mainloop()






