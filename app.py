import settings

import datetime   # Для работы со временем,
import operator   # и объектами datetime
from datetime import datetime

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


class Main_window(Tk):   # Класс создания линий ввода

    days = []
    time = []
    delta_time = []

    def __init__(self,  *args, **kwargs):

        settings.Setting()   # Вызов окна настроек поверх главного окна

        super().__init__(*args, **kwargs)

        self.title('KARBAN CALC')
        self.geometry('800x600')

        self.create_days()
        self.mainloop()

    def accept_and_result(self):   # Метод вызова двух функций нажатием одной кнопки "Принять"

        self.get_time()
        self.calculate()

    def create_days(self):

        for row in range(1):  # Количество дней
            line = Day(row)
            line.grid(row=row)
            self.days.append(line)

        Label(text='Начало:').grid(row=0, column=0, sticky='e')
        Label(text='Конец:').grid(row=0, column=4, sticky='e')

        Button(text='Принять данные', font=20, command=self.accept_and_result).grid(column=8, row=21)

    def get_time(self):  # Cобираем введенные данные в список...

        for i in self.days:
            self.time.append(i.get_fields())

    def calculate(self):  # ...и считаем результат

        self.tariff = settings.Setting.tariff

        for i in self.time:
            start = ':'.join(i[:2])
            end = ':'.join(i[2:])
            time_start = datetime.datetime.strptime(start, '%H:%M')  # приведение к формату str("ЧЧ:ММ")
            time_end = datetime.datetime.strptime(end, '%H:%M')

            self.delta_time.append(time_end - time_start)

        result = reduce(operator.add, self.delta_time)  # суммируем время из списка с объектами datetime
        print(f'Отработано времени: {result}')   # пока что печать в консоль
        cash = (result.seconds / 3600) * self.tariff
        print(f'К выплате: {cash}')
