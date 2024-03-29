import datetime
import operator   # for time and datetime object
from functools import reduce
from tkinter import Frame, Button, Label, Tk

import config as cfg
from utils import HoursEntry, MinutesEntry


class Day(Frame):   # Input window creation widget (Entry)
    inputs = []

    def __init__(self, root, row, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = root
        self.row = row
        self.create_input()

    def create_input(self):  # Create inputs...
        self.inputs = [
            (HoursEntry(self.root)),
            (MinutesEntry(self.root)),
            (HoursEntry(self.root)),
            (MinutesEntry(self.root))
            ]

        for f, i in zip(self.inputs, [2, 3, 5, 6]):  # ...and place them on the grid
            f.grid(row=self.row, column=i)

    def get_fields(self):  # return entered data
        return [f.get() for f in self.inputs]


class MainWindow(Tk):
    days = []
    time = []
    delta_time = []
    result_days = ''
    cash = ''

    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('KARBAN CALC')
        self.geometry('800x600')
        self.create_days()
        self.mainloop()

    def accept_and_result(self):   # Method for calling functions when the "Accept" button is clicked
        self.get_time()
        self.calculate()
        self.show_result()

    def create_days(self):
        for row in range(cfg.days_cnt):  # count of days
            line = Day(self, row)
            line.grid(row=row)
            self.days.append(line)

        Label(text='Начало:').grid(row=0, column=0)
        Label(text='Конец:').grid(row=0, column=4)
        Button(text='Результат', font=20, command=self.accept_and_result).grid(column=8, row=21)

    def get_time(self):  # Collecting entered data in list...
        for i in self.days:
            self.time.append(i.get_fields())

    def calculate(self):  # ... and count the result
        for i in self.time:
            start = ':'.join(i[:2])
            end = ':'.join(i[2:])
            time_start = datetime.datetime.strptime(start, '%H:%M')  # Conversion format str("HH:MM")
            time_end = datetime.datetime.strptime(end, '%H:%M')
            self.delta_time.append(time_end - time_start)

        self.result_days = reduce(operator.add, self.delta_time)  # sum up the time from the list with objects
        self.cash = round((self.result_days.seconds / 3600) * cfg.tariff)

    def show_result(self):
        Label(text=f'Отработано часов: {self.result_days}').grid()
        Label(text=f'К выплате: {self.cash}р.').grid()
