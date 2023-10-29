class Examples:  # Создаем класс
    def __init__(self, num, exe):
        self.num = num
        self.exe = exe
        if self.exe == 'Квадрат числа':  # Делаеи проверку, если строчка ровна 'Квадрат числа'
            self.square()
        elif self.exe == 'Куб числа':  # Делаеи проверку, если строчка ровна 'Куб числа'
            self.cube()
        elif self.exe == 'Модуль числа':  # Делаеи проверку, если строчка ровна 'Модуль числа'
            self.absolute()
        else:
            return print(None)  # Иначе выводим None

    def square(self):  # Создаем метот который возводит числа в квадрат
        print(self.num ** 2)

    def cube(self):  # Создаем метот который возводит числа в куб
        print(self.num ** 3)

    def absolute(self):  # Создаем метот который печатает модуль числа
        print(abs(self.num))

num = int(input('Введи число '))
exe = input('Выбери функцию ')
Examples(num, exe)  # Вызываем класс
