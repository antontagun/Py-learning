from tkinter import *
import random as r

# Класс ListBox позволяет создавать объект, в котором можно выбирать элементы

root = Tk()
root.geometry('700x400')

mix = []
capitals = ['Москва', 'Лондон', 'Вашингтон', 'Токио', 'Париж', 'Мадрид', 'Берлин', 'Сеул', 'Пекин', 'Рим']  # нужно дописать ещё 5 столиц
countries = ['Германия', 'Франция', 'Россия', 'Испания', 'США', 'Япония', 'Англия', 'Южная Корея', 'Китай', 'Испания']  # нужно дописать ещё 5 стран

# selectmode=EXTENDED -> можно выбирать сразу несколько элементов (с зажатым Ctrl или Shift)
# создаем объект - список покупок от класса ListBox
mix_box = Listbox(selectmode=EXTENDED)
mix_box.grid(row=1, column=2)

def get_mix():
    n = 5
    while n != 0:
        if r.randint(0, 1) % 2:
            a = r.choice(capitals)
            if a not in mix:
                mix.append(a)
            else:
                n += 1
        else:
            b = r.choice(countries)
            if b not in mix:
                mix.append(b)
            else:
                n += 1
        n -= 1
    # ! Перед использованием объект класса ListBox необходимо заполнить
    for item in mix:
        mix_box.insert(END, item)  # помещаем очередной элемент в конец списка выбора

get_mix()

count = 0
left_box = Listbox(selectmode=EXTENDED)
left_box.grid(row=1, column=0)
right_box = Listbox(selectmode=EXTENDED)
right_box.grid(row=1, column=4)
cart1 = []
cart2 = []
# Может быть one - товар в списке покупок, а two - товар в корзине; а может быть наоборот
def change_1(one, two):
    current_1 = one.curselection()  # тот товар, на котором мы сейчас находимся в конкретном списке выбора
    for i in current_1:  # создаем цикл, т.к. может быть выбран не один товар
        # помещаем данный товар в другой список выбор
        two.insert(END, one.get(i))
        cart1.append(i)

    current_1 = list(current_1)  # преобразуем объект выбранных товаров в список
    current_1.reverse()  # делаем реверс, чтобы не было дублирования

    for i in current_1:
        one.delete(i)
        cart1.remove(i)

def change_2(one, two):
    current_2 = one.curselection()  # тот товар, на котором мы сейчас находимся в конкретном списке выбора
    for i in current_2:  # создаем цикл, т.к. может быть выбран не один товар
        # помещаем данный товар в другой список выбор
        two.insert(END, one.get(i))
        cart2.append(i)

    current_2 = list(current_2)  # преобразуем объект выбранных товаров в список
    current_2.reverse()  # делаем реверс, чтобы не было дублирования

    for i in current_2:
        one.delete(i)
        cart2.remove(i)

def close_window():
    root.destroy()


def check():
    global count
    if mix_box.size() != 0:
        label_4.config(text='Еще не всё!', fg='red')
        return
    for capital in left_box.get(0, 4):
        if capital in countries:
            label_4.config(text='НЕ ВЕРНО', fg='red')
            return
    for country in right_box.get(0, 4):
        if country in capitals:
            label_4.config(text='НЕ ВЕРНО', fg='red')
            return
    count += 1
    label_4.config(text='ВЕРНО', fg='green')
    label_5.config(text=f'СЧЁТ: {count}')
    cart1.clear()
    cart2.clear()
    right_box.delete(0, right_box.size() - 1)
    left_box.delete(0, left_box.size() - 1)
    mix.clear()
    get_mix()




frame_1 = Frame()
frame_1.grid(row=1, column=1)
frame_2 = Frame()
frame_2.grid(row=1, column=3)
frame_3 = Frame()
frame_3.grid(row=3, column=2)
# кнопки для добавления в корзину и удаления из корзины
# т.к. в command можно писать только имя функции, когда мы хотим передавать параметры вызываемой функции,
# нам необходимо использовать lambda
label_1 = Label(text='Столицы', width=20, bg='lightblue')
label_1.grid(row=0, column=0)
label_2 = Label(text='Микс', width=20, bg='lightblue')
label_2.grid(row=0, column=2)
label_3 = Label(text='Страны', width=20, bg='lightblue')
label_3.grid(row=0, column=4)
label_4 = Label(frame_3, width=20, bg='white')
label_4.grid(row=1, column=3)
label_5 = Label(frame_3, width=20, bg='#D8FA89', text='СЧЁТ:')
label_5.grid(row=0, column=3)

bt_1 = Button(frame_1, text='<--', command=lambda i=mix_box, j=left_box: change_1(i, j))
bt_1.grid(row=2, column=1)
bt_2 = Button(frame_1, text='-->', command=lambda j=mix_box, i=left_box: change_1(i, j))
bt_2.grid(row=3, column=1)

bt_3 = Button(frame_2, text='-->', command=lambda i=mix_box, j=right_box: change_2(i, j))
bt_3.grid(row=0, column=3)
bt_4 = Button(frame_2, text='<--', command=lambda j=mix_box, i=right_box: change_2(i, j))
bt_4.grid(row=1, column=3)

bt_5 = Button(frame_3, bg='red', text='Выход', command=close_window)
bt_6 = Button(frame_3, bg='lightgreen', text='Проверить', command=check)
bt_5.grid(row=3, column=3)
bt_6.grid(row=2, column=3)

mainloop()