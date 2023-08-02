from tkinter import Tk
from tkinter import Entry, Frame, Button, Toplevel, END


class Day(Frame):
    fields = []

    def __init__(self, row, *args, **kwargs):
        self.row = row
        super().__init__(*args, **kwargs)
        self.setup_ui()

    def setup_ui(self):
        # создаем наши инпутики
        self.fields = [Entry(width=4) for i in range(4)]

        # и раставляем на нашей сеткe
        for f, i in zip(self.fields, [0,1,2,3]):
            f.grid(column=i, row=self.row)

    def get(self):
        '''
        при этом вызове мы отдадим то что у нас написанно
        '''
        return [f.get() for f in self.fields]

# class Setting(Toplevel):
#     def __init__(self):
#         super().__init__()
#         self.open_window()
#
#     def open_window(self):
#         Button(text='TOTAL', font=20).grid(column=8, row=21)

class Window(Tk):
    days = []

    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):

        for row in range(5):
            line = Day(row)
            line.grid(row=row)
            self.days.append(line)

        Button(text='TOTAL', font=20, command=self.calculate).grid(column=8, row=21)

    def calculate(self):
        [print(l.get()) for l in self.days]


if __name__ == '__main__':
    root = Window()
    root.title('KARBAN CALC')
    root.geometry('390x380')

    root.mainloop()

