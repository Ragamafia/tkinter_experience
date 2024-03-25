from tkinter import Button, Label, Radiobutton, Entry, IntVar, StringVar, Tk

import config as cfg


class Setting(Tk):   # Приветственное окно, настройки
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.status = IntVar()  # Для выбора сотрудника
        self.status.set(cfg.current_user)
        self.title('Setting')
        self.geometry('430x500')
        self.open_window()
        self.mainloop()

    def accept_and_close_window(self):   # Метод вызова функций для кнопки "Выбрать"
        self.setup()
        self.destroy()

    def open_window(self):
        Label(text='''КАЛЬКУЛЯТОР РАСЧЕТА ВРЕМЕНИ!
        В открывшемся окне введите время начала и конца рабочего дня.''').grid(sticky='n')

        Radiobutton(text='Тахмина', variable=self.status, value=0).grid(sticky='w')
        Radiobutton(text='Анна', variable=self.status, value=1).grid(sticky='w')
        Radiobutton(text='Анастасия', variable=self.status, value=2).grid(sticky='w')
        Label(text='Введите количество отработанных дней').grid(sticky='w')

        days = StringVar()
        days.set(cfg.current_user)

        self.work_days = Entry(textvariable=days)
        self.work_days.grid()
        Button(text="Выбрать", command=self.accept_and_close_window).grid()

    def setup(self):   # Установка тарифа и количества линий
        cfg.days_cnt = int(self.work_days.get())

        if self.status.get() == 0:
            cfg.tariff = 100

        elif self.status.get() == 1:
            cfg.tariff = 120

        elif self.status.get() == 2:
            cfg.tariff = 150
