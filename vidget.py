import welcome

import datetime   # Для работы со временем,
import operator   # и объектами datetime

from tkinter import Tk
from tkinter import Entry, Frame, Button, Label
from functools import reduce


class Day(Frame):   # класс создания окон ввода (Entry)

    inputs = []

    def __init__(self, row, *args, **kwargs):
        self.row = row
        super().__init__(*args, **kwargs)

        self.create_input()

    def create_input(self):  # создаем инпуты...

        self.inputs = [Entry(width=4) for i in range(4)]

        for f, i in zip(self.inputs, [2, 3, 5, 6]):  # ...и размещаем их по сетке
            f.grid(row=self.row, column=i)

    def get_fields(self):  # При этом вызове отдаём введенные данные
        return [f.get() for f in self.inputs]


class Window(Tk):   # Класс создания линий ввода

    days = []
    time = []
    result_time = []

    def __init__(self, tariff, *args, **kwargs):
        self.tariff = tariff
        super().__init__(*args, **kwargs)

        self.create_days()

    def accept_and_result(self):   # Метод вызова двух функций нажатием одной кнопки "Принять"

        self.get_time()
        self.calculate()

    def create_days(self):


        for row in range(1):  # Количество дней
            line = Day(row)
            line.grid(row=row)
            self.days.append(line)

        Label(text='Начало:').grid(row=0, column=0, sticky='e')
        Label(text='Конец').grid(row=0, column=4, sticky='e')

        Button(text='Принять данные', font=20, command=self.accept_and_result).grid(column=8, row=21)

    def get_time(self):  # Cобираем введенные данные в список...

        for i in self.days:
            self.time.append(i.get_fields())

    def calculate(self):  # ...и считаем результат

        for i in self.time:
            start = ':'.join(i[:2])
            end = ':'.join(i[2:])
            time_start = datetime.datetime.strptime(start, '%H:%M')  # приведение к формату str("ЧЧ:ММ")
            time_end = datetime.datetime.strptime(end, '%H:%M')

            self.result_time.append(time_end - time_start)

        result = reduce(operator.add, self.result_time)  # суммируем время из списка с объектами datetime
        print(f'Отработано времени: {result}')   # пока что печать в консоль
        cash = (result.seconds / 3600) * self.tariff
        print(f'К выплате: {cash}')

tariff = welcome.Setting.tariff

root = Window(tariff)
root.title('KARBAN CALC')
root.geometry('800x600')

root.mainloop()