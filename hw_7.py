from tkinter import *

# Класс ListBox позволяет создавать объект, в котором можно выбирать элементы

root = Tk()
root.geometry('700x300')

list_buy = ['Москва', 'Германия', 'Франция', 'Лондон', 'Вашингтон']

# selectmode=EXTENDED -> можно выбирать сразу несколько элементов (с зажатым Ctrl или Shift)
# создаем объект - список покупок от класса ListBox
list_shop = Listbox(selectmode=EXTENDED)
list_shop.grid(row=1, column=2)

#! Перед использованием объект класса ListBox необходимо заполнить
for item in list_buy:
    list_shop.insert(END, item)  # помещаем очередной элемент в конец списка выбора

cart_1 = Listbox(selectmode=EXTENDED)
cart_1.grid(row=1, column=0)
cart_2 = Listbox(selectmode=EXTENDED)
cart_2.grid(row=1, column=4)
# Может быть one - товар в списке покупок, а two - товар в корзине; а может быть наоборот
def change_1(one, two):
    current_1 = one.curselection()  # тот товар, на котором мы сейчас находимся в конкретном списке выбора
    for i in current_1:  # создаем цикл, т.к. может быть выбран не один товар
        # помещаем данный товар в другой список выбор
        two.insert(END, one.get(i))

    current_1 = list(current_1)  # преобразуем объект выбранных товаров в список
    current_1.reverse()  # делаем реверс, чтобы не было дублирования


def change_2(one, two):
    current_2 = one.curselection()  # тот товар, на котором мы сейчас находимся в конкретном списке выбора
    for i in current_2:  # создаем цикл, т.к. может быть выбран не один товар
        # помещаем данный товар в другой список выбор
        two.insert(END, one.get(i))

    current_2 = list(current_2)  # преобразуем объект выбранных товаров в список
    current_2.reverse()  # делаем реверс, чтобы не было дублирования
def close_window(root):
    root.destroy()
frame_1 = Frame()
frame_1.grid(row=1, column=1)
frame_2 = Frame()
frame_2.grid(row=1, column=3)
frame_3 = Frame()
frame_3.grid(row=3, column=2)
# кнопки для добавления в корзину и удаления из корзины
# т.к. в command можно писать только имя функции, когда мы хотим передавать параметры вызываемой функции,
# нам необходимо использовать lambda
label_1 = Label(width=20, bg='lightblue')
label_1.grid(row=0, column=0)
label_2 = Label(width=20, bg='lightblue')
label_2.grid(row=0, column=2)
label_3 = Label(width=20, bg='lightblue')
label_3.grid(row=0, column=4)
label_4 = Label(width=20, bg='white')
label_4.grid(row=4, column=2)

bt_1 = Button(frame_1, text='<--', command=lambda i=list_shop, j=cart_1: change_1(i, j))
bt_1.grid(row=2, column=1)

bt_3 = Button(frame_2, text='-->', command=lambda i=list_shop, j=cart_2: change_2(i, j))
bt_3.grid(row=2, column=3)

bt_5 = Button(frame_3, bg='red', text='Выход', command=close_window)
bt_5.grid(row=10, column=10)
mainloop()