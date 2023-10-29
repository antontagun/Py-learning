class Count_points:
    def __init__(self, uchastniki):
        self.coin = uchastniki
        self.median = 0

    def get_median(self):  # Создаем метод
        self.coin.sort()  # Сортируем список
        if len(self.coin) % 2 == 0:  # Если длинна списка четная:
            # Находим разность 2х центральных элементов
            self.median = ((self.coin[(len(self.coin) - 1) // 2]) + self.coin[len(self.coin) // 2]) / 2
        else:  # Если длинна списка нечетная:
            # Находим центральный элемент
            self.median = (self.coin[(len(self.coin)) // 2])
            # Выводим его
        print(self.median)

uchastniki = [10]  # Создаем список
num = int(input())
while num != 10:  # Вводим значения, пока не введется 10
    uchastniki += [num]  # Добавляем в список
    num = int(input())

Count_points(uchastniki).get_median()  # Вызываем класс с методом
