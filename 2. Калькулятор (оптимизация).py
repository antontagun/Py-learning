import tkinter as tk



class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Калькулятор")
        self.master.geometry("180x370")
        self.w_bt = 5
        self.c_bt = 'grey'
        self.h_bt = 5
        self.expression = ''
        self.number_entry = tk.Entry(self.master, width=20)
        self.number_entry.grid(row=0, column=0, columnspan=5, padx=5, pady=5)

        self.button_1 = tk.Button(self.master, text="1", width=self.w_bt, height=self.h_bt, bg=self.c_bt, command=lambda: self.button_click('1'))
        self.button_2 = tk.Button(self.master, text="2", width=self.w_bt, height=self.h_bt, bg=self.c_bt, command=lambda: self.button_click('2'))
        self.button_3 = tk.Button(self.master, text="3", width=self.w_bt, height=self.h_bt, bg=self.c_bt, command=lambda: self.button_click('3'))
        self.button_4 = tk.Button(self.master, text="4", width=self.w_bt, height=self.h_bt, bg=self.c_bt, command=lambda: self.button_click('4'))
        self.button_5 = tk.Button(self.master, text="5", width=self.w_bt, height=self.h_bt, bg=self.c_bt, command=lambda: self.button_click('5'))
        self.button_6 = tk.Button(self.master, text="6", width=self.w_bt, height=self.h_bt, bg=self.c_bt, command=lambda: self.button_click('6'))
        self.button_7 = tk.Button(self.master, text="7", width=self.w_bt, height=self.h_bt, bg=self.c_bt, command=lambda: self.button_click('7'))
        self.button_8 = tk.Button(self.master, text="8", width=self.w_bt, height=self.h_bt, bg=self.c_bt, command=lambda: self.button_click('8'))
        self.button_9 = tk.Button(self.master, text="9", width=self.w_bt, height=self.h_bt, bg=self.c_bt, command=lambda: self.button_click('9'))
        self.button_0 = tk.Button(self.master, text="0", width=self.w_bt, height=self.h_bt, bg=self.c_bt, command=lambda: self.button_click('0'))
        self.button_clear = tk.Button(self.master, text="C", width=self.w_bt, height=self.h_bt, bg=self.c_bt, command=lambda: self.button_click('C'))
        self.button_add = tk.Button(self.master, text="+", width=self.w_bt, height=self.h_bt, bg=self.c_bt, command=lambda: self.button_click('+'))
        self.button_equal = tk.Button(self.master, text="=", width=self.w_bt, height=self.h_bt, bg=self.c_bt, command=lambda: self.button_equal_click())
        self.button_subtract = tk.Button(self.master, text="-", width=self.w_bt, height=self.h_bt, bg=self.c_bt, command=lambda: self.button_click('-'))
        self.button_multiply = tk.Button(self.master, text="*", width=self.w_bt, height=self.h_bt, bg=self.c_bt, command=lambda: self.button_click('*'))
        self.button_divide = tk.Button(self.master, text="/", width=self.w_bt, height=self.h_bt, bg=self.c_bt, command=lambda: self.button_click('/'))

        self.button_1.grid(row=1, column=0)
        self.button_2.grid(row=1, column=1)
        self.button_3.grid(row=1, column=2)
        self.button_add.grid(row=1, column=3)

        self.button_4.grid(row=2, column=0)
        self.button_5.grid(row=2, column=1)
        self.button_6.grid(row=2, column=2)
        self.button_subtract.grid(row=2, column=3)

        self.button_7.grid(row=3, column=0)
        self.button_8.grid(row=3, column=1)
        self.button_9.grid(row=3, column=2)
        self.button_multiply.grid(row=3, column=3)

        self.button_clear.grid(row=4, column=0)
        self.button_0.grid(row=4, column=1)
        self.button_equal.grid(row=4, column=2)
        self.button_divide.grid(row=4, column=3)

        self.f_num = 0
        self.math = ""

    def button_click(self, item):
        current = self.number_entry.get()
        self.number_entry.delete(0, len(current))
        if item != 'C':
            self.number_entry.insert(0, current + item)
        pass
    def button_equal_click(self):
        current = self.number_entry.get()
        self.number_entry.delete(0, len(current))

        self.number_entry.insert(0, eval(current))
        pass


root = tk.Tk()
calc = Calculator(root)
root.mainloop()