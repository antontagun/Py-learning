class String:
    def __init__(self, string):
        self.lst_string = [x for x in string.split(', ') if x.isalpha()]

    def string_in_list(self):
        if self.lst_string:
            self.lst_string.sort(key=str.lower)
            print(self.lst_string)
        else:
            print(None)



string = input()
String(string).string_in_list()
