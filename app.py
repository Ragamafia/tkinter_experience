import settings

from utils import HoursEntry, MinutesEntry

import datetime   # Для работы со временем,
import operator   # и объектами datetime

from tkinter import Tk
from tkinter import Frame, Button, Label
from functools import reduce


class Day(Frame):   # класс создания окон ввода (Entry)
    inputs = []

    def __init__(self, root, row, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = root
        self.row = row
        self.create_input()

    def create_input(self):  # создаем инпуты...
        self.inputs = [
            (HoursEntry(self.root)), (MinutesEntry(self.root)), (HoursEntry(self.root)), (MinutesEntry(self.root))
            ]

        for f, i in zip(self.inputs, [2, 3, 5, 6]):  # ...и размещаем их по сетке
            f.grid(row=self.row, column=i)

    def get_fields(self):  # При этом вызове отдаём введенные данные
        return [f.get() for f in self.inputs]


class MainWindow(Tk):   # Создание главного окна
    days = []
    time = []
    delta_time = []
    result_days = ''
    cash = ''

    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tariff = settings.Setting.tariff
        self.work_day = settings.Setting.work_days

        self.title('KARBAN CALC')
        self.geometry('800x600')
        self.create_days()
        self.mainloop()

    def accept_and_result(self):   # Метод вызова двух функций нажатием одной кнопки "Принять"
        self.get_time()
        self.calculate()
        self.show_result()

    def create_days(self):
        for row in range(self.work_day):  # Количество дней
            line = Day(self, row)
            line.grid(row=row)
            self.days.append(line)

        Label(text='Начало:').grid(row=0, column=0, sticky='e')
        Label(text='Конец:').grid(row=0, column=4, sticky='e')
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
            self.delta_time.append(time_end - time_start)

        result = reduce(operator.add, self.delta_time)  # суммируем время из списка с объектами datetime
        self.result_days = result
        cash = (result.seconds / 3600) * self.tariff
        self.cash = round(cash)

    def show_result(self):
        Label(text=f'Отработано часов: {self.result_days}').grid()
        Label(text=f'К выплате: {self.cash}р.').grid()


