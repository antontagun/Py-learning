class String:
    def __init__(self, string):
        # Преобразовываем  строку в список и делаем проверку для того чтобы в списке у нас были только строки
        self.lst_string = [x for x in string.split(', ') if x.isalpha()]

    def string_in_list(self):  # Создаем метод для сортировки эелементов списка
        if self.lst_string:
            self.lst_string.sort(key=str.lower)  # Сортируем по алфавиту
            print(self.lst_string)
        else:
            print(None)



string = input()
String(string).string_in_list()
