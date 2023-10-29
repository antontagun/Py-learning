from tkinter import *

frame = Tk()
frame.geometry('200x100+700+300')

class Crosslights:
    def __init__(self):
        self.lbl = Label(width=10, bg='#ffffff')
        self.lbl.pack()
        self.clr = (('RED', '#ff0000'), ('YELLOW', '#ffff00'), ('GREEN', '#00ff00'))

        for i in range(3):
            Button(width=10, text=self.clr[i][0], command=lambda s=self.clr[i][0]: self.color(s)).pack()

    def color(self,sing):
        if sing == 'RED':
            self.lbl['bg'] = self.clr[0][1]
        elif sing == 'YELLOW':
            self.lbl['bg'] = self.clr[1][1]
        elif sing == 'GREEN':
            self.lbl['bg'] = self.clr[2][1]


Crosslights()
mainloop()