import new_window
import datetime

from functools import reduce
import operator

from tkinter import Tk
from tkinter import Entry, Frame, Button


class Day(Frame):  # класс создания окон ввода
    inputs = []

    def __init__(self, row, *args, **kwargs):
        self.row = row
        super().__init__(*args, **kwargs)
        self.create_input()

    def create_input(self):  # создаем инпуты...
        self.inputs = [Entry(width=4) for i in range(4)]

        for f, i in zip(self.inputs, [2, 3, 5, 6]):  # ...и размещаем их по сетке
            f.grid(row=self.row, column=i)

    def get_fields(self):  # при этом вызове отдаём введенные данные
        return [f.get() for f in self.inputs]


class Window(Tk):  # класс создания линий ввода
    days = []
    time_obj = []
    result_time = []

    def __init__(self):
        super().__init__()
        self.create_days()

    def accept_and_result(self):   # метод вызова двух функций нажатием одной кнопки "Принять"

        self.get_time()
        self.calculate()

    def create_days(self):

        for row in range(1):  # количество дней
            line = Day(row)
            line.grid(row=row)
            self.days.append(line)
            new_window.Post(row)  # Вызываем окно настроек

        Button(text='Принять', font=20, command=self.accept_and_result).grid(column=8, row=21)

    def get_time(self):  # собираем введенные данные в список...

        for i in self.days:
            self.time_obj.append(i.get_fields())

    def calculate(self):  # ...и считаем результат

        for i in self.time_obj:
            start = ':'.join(i[:2])
            end = ':'.join(i[2:])
            time_start = datetime.datetime.strptime(start, '%H:%M')  # приведение к формату str("ЧЧ:ММ")
            time_end = datetime.datetime.strptime(end, '%H:%M')
            time_delta = time_end - time_start

            self.result_time.append(time_delta)

        result = reduce(operator.add, self.result_time)   # суммируем время из объектов datetime
        print(result)

        cash = (result.seconds / 3600) * 100
        print(cash)


if __name__ == '__main__':
    root = Window()
    root.title('KARBAN CALC')
    root.geometry('800x600')

    root.mainloop()
