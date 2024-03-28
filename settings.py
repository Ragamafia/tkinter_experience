from tkinter import Button, Label, Radiobutton, Entry, IntVar, Tk

import config as cfg


class Setting(Tk):   # Приветственное окно, настройки
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.status = IntVar()  # Для выбора сотрудника
        self.title('Setting')
        self.geometry('430x500')
        self.open_window()
        self.mainloop()

    def accept_and_close_window(self):   # Метод вызова функций для кнопки "Выбрать"
        cfg.days_cnt = int(self.work_days.get())
        cfg.tariff = cfg.users.get(self.status.get())['tariff']
        self.destroy()

    def open_window(self):
        text = '''
        КАЛЬКУЛЯТОР РАСЧЕТА ВРЕМЕНИ!
        В открывшемся окне введите время начала и конца рабочего дня.
        '''
        Label(text=text).grid(sticky='n')

        for id in sorted(cfg.users):
            user = cfg.users.get(id)['name']
            Radiobutton(text=user, variable=self.status, value=id).grid(sticky='w')

        Label(text='Введите количество отработанных дней').grid(sticky='w')
        self.work_days = Entry()
        self.work_days.grid()
        Button(text="Выбрать", command=self.accept_and_close_window).grid()
