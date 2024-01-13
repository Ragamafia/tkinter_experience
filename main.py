import new_window
import datetime

from tkinter import Tk
from tkinter import Entry, Frame, Button


class Day(Frame):   # класс создания окон ввода
    fields = []

    def __init__(self, row, *args, **kwargs):
        self.row = row
        super().__init__(*args, **kwargs)
        self.create_input()

    def create_input(self):   # создаем инпуты...
        self.fields = [Entry(width=4) for i in range(4)]

        for f, i in zip(self.fields, [2, 3, 5, 6]):   # ...и размещаем их по сетке
            f.grid(row=self.row, column=i)

    def get(self):   # при этом вызове отдаём введенные данные
        return [f.get() for f in self.fields]


class Window(Tk):   # класс создания линий ввода
    days = []
    field = []

    def __init__(self):
        super().__init__()
        self.create_days()

    def create_days(self):

        for row in range(2):   # количество дней
            line = Day(row)
            line.grid(row=row)
            self.days.append(line)
            new_window.Post(row)

        Button(text='Принять', font=20, command=self.calculate).grid(column=8, row=21)

    def calculate(self):

        for i in self.days:
            self.field.append(i.get())
        Button(text='РАСЧЕТ', font=20, command=self.get_time).grid(column=8, row=22)

    def get_time(self):

        for i in self.field:
            start = ':'.join(i[:2])
            end = ':'.join(i[2:])
            time1 = datetime.datetime.strptime(start, '%H:%M')
            time2 = datetime.datetime.strptime(end, '%H:%M')
            time_delta = time2 - time1
            print(time_delta)


if __name__ == '__main__':

    root = Window()
    root.title('KARBAN CALC')
    root.geometry('800x600')

    root.mainloop()
