from tkinter  import *

frame = Tk()
frame.geometry('300x300+700+300')

def err():
    try:
        num1 = float(ent1.get())
        num2 = float(ent2.get())
        return num1, num2  # в Python все перечисления по умолчанию имеют тип данных "кортеж"
    except ValueError:
        label['text'] = 'Ошибка ввода!'
        return False

def add():
    nums = err()
    # если nums = False, то условие не выполнится
    if nums:  # получаем из err() результат ее работы: 1) либо nums = (num1, num2) 2) либо False
        res = nums[0] + nums[1]
        label['text'] = res

def sub():
    nums = err()
    # если nums = False, то условие не выполнится
    if nums:  # получаем из err() результат ее работы: 1) либо nums = (num1, num2) 2) либо False
        res = nums[0] - nums[1]
        label['text'] = res

def multip():
    nums = err()
    # если nums = False, то условие не выполнится
    if nums:  # получаем из err() результат ее работы: 1) либо nums = (num1, num2) 2) либо False
        res = nums[0] * nums[1]
        label['text'] = res

def division():
    nums = err()
    # если nums = False, то условие не выполнится
    if nums:  # получаем из err() результат ее работы: 1) либо nums = (num1, num2) 2) либо False
        if nums[1] != 0:
            res = nums[0] / nums[1]
        else:
            res = "На ноль делить нельзя!"
        label['text'] = res

ent1 = Entry(width=20, bg='lightblue')
ent1.pack()
ent2 = Entry(width=20, bg='lightblue')
ent2.pack()

# master -> master object (владелец объекта) - можно не указывать, если мы хотим расположить виджет на главном фрейме
sum_ = Button(frame, width=20, text='+', bg='red', fg='blue')
sum_.pack()
min_ = Button(frame, width=20, text='-', bg='red', fg='blue')
min_.pack()
mult = Button(frame, width=20, text='x', bg='red', fg='blue')
mult.pack()
div = Button(frame, width=20, text='/', bg='red', fg='blue')
div.pack()

# связываем (линкуем) кнопки с их обработчиками (функциями)
#! Значением command является имя функции (без скобок вызова)
sum_['command'] = add
min_['command'] = sub
mult['command'] = multip
div['command'] = division

label = Label(width=20, bg='yellow')
label.pack()

mainloop()