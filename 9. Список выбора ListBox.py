from tkinter import *

# Класс ListBox позволяет создавать объект, в котором можно выбирать элементы

root = Tk()

list_buy = ['milk', 'potato', 'bread', 'meat', 'apple']

# selectmode=EXTENDED -> можно выбирать сразу несколько элементов (с зажатым Ctrl или Shift)
# создаем объект - список покупок от класса ListBox
list_shop = Listbox(selectmode=EXTENDED)
list_shop.pack(side=LEFT)

#! Перед использованием объект класса ListBox необходимо заполнить
for item in list_buy:
    list_shop.insert(END, item)  # помещаем очередной элемент в конец списка выбора

cart = Listbox(selectmode=EXTENDED)
cart.pack(side=RIGHT)

# Может быть one - товар в списке покупок, а two - товар в корзине; а может быть наоборот
def change(one, two):
    current = one.curselection()  # тот товар, на котором мы сейчас находимся в конкретном списке выбора
    for i in current:  # создаем цикл, т.к. может быть выбран не один товар
        # помещаем данный товар в другой список выбор
        two.insert(END, one.get(i))

    current = list(current)  # преобразуем объект выбранных товаров в список
    current.reverse()  # делаем реверс, чтобы не было дублирования

    for i in current:
        one.delete(i)  # удаляем выбранный товар

frame = Frame()
frame.pack(side=LEFT)
# кнопки для добавления в корзину и удаления из корзины
# т.к. в command можно писать только имя функции, когда мы хотим передавать параметры вызываемой функции,
# нам необходимо использовать lambda
Button(frame, text='-->', command=lambda i=list_shop, j=cart: change(i, j)).pack()
Button(frame, text='<--', command=lambda i=cart, j=list_shop: change(i, j)).pack()

mainloop()