import tkinter

from tkinter import Tk
from tkinter import Button, Label, Radiobutton


class Setting(Tk):   # Приветственное окно, настройки

    tariff = ''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title('Setting')
        self.geometry('430x500')

        self.open_window()
        self.mainloop()

    def accept_and_close_window(self):   # Метод вызова двух функций для кнопки "Выбрать"
        self.setup()
        self.destroy()

    def open_window(self):

        Label(text='КАЛЬКУЛЯТОР РАСЧЕТА ВРЕМЕНИ!').grid(sticky='n')
        Label(text='''Пожалуйста, выберите сотрудника.
         В открывшемся окне введите время начала и конца рабочего дня.''').grid()

        self.status = tkinter.IntVar()   # Выбор сотрудника
        self.status.set(0)

        Radiobutton(text='Тахмина', variable=self.status, value=0).grid(sticky='w')
        Radiobutton(text='Анна', variable=self.status, value=1).grid(sticky='w')
        Radiobutton(text='Анастасия', variable=self.status, value=2).grid(sticky='w')

        Button(text="Выбрать", command=self.accept_and_close_window).grid()

    def setup(self):   # Установка тарифа

        if self.status.get() == 0:
            Setting.tariff = 100
            print('Выбрана Тахмина')

        elif self.status.get() == 1:
            Setting.tariff = 120
            print('Выбрана Анна')

        elif self.status.get() == 2:
            Setting.tariff = 150
            print('Выбрана Анастасия')

