import tkinter

from tkinter import Tk
from tkinter import Button, Label, Radiobutton, Entry


class Setting(Tk):   # Приветственное окно, настройки
    tariff = ''
    work_days = ''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.status = tkinter.IntVar()  # Для выбора сотрудника
        self.status.set(0)

        self.title('Setting')
        self.geometry('430x500')

        self.open_window()

        self.mainloop()

    def accept_and_close_window(self):   # Метод вызова функций для кнопки "Выбрать"
        self.setup()
        self.destroy()

    def open_window(self):
        Label(text='КАЛЬКУЛЯТОР РАСЧЕТА ВРЕМЕНИ!').grid(sticky='n')
        Label(text='''Пожалуйста, выберите сотрудника.
         В открывшемся окне введите время начала и конца рабочего дня.''').grid()

        Radiobutton(text='Тахмина', variable=self.status, value=0).grid(sticky='w')
        Radiobutton(text='Анна', variable=self.status, value=1).grid(sticky='w')
        Radiobutton(text='Анастасия', variable=self.status, value=2).grid(sticky='w')

        Label(text='Введите количество отработанных дней').grid(sticky='w')
        self.work_days = Entry()
        self.work_days.grid()

        Button(text="Выбрать", command=self.accept_and_close_window).grid()

    def setup(self):   # Установка тарифа и количества линий
        result = self.work_days.get()
        Setting.work_days = int(result)

        if self.status.get() == 0:
            Setting.tariff = 100
            print('Выбрана Тахмина')

        elif self.status.get() == 1:
            Setting.tariff = 120
            print('Выбрана Анна')

        elif self.status.get() == 2:
            Setting.tariff = 150
            print('Выбрана Анастасия')


