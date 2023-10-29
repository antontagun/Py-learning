class Examples:
    def __init__(self, num, exe):
        self.num = num
        self.exe = exe
        if self.exe == 'Квадрат числа':
            self.square()
        elif self.exe == 'Куб числа':
            self.cube()
        elif self.exe == 'Модуль числа':
            self.absolute()
        else:
            return print(None)

    def square(self):
        print(self.num ** 2)

    def cube(self):
        print(self.num ** 3)

    def absolute(self):
        print(abs(self.num))

num = int(input('Введи число '))
exe = input('Выбери функцию ')
Examples(num, exe)
