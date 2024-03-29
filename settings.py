from tkinter import Listbox, Button, Label, Radiobutton, Entry, StringVar, END, Tk

import config as cfg
import utils


class Setting(Tk):   # Установка настроек
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.status = StringVar()  # Для выбора сотрудника
        self.status.set(cfg.default_user_id)
        self.title('Setting')
        self.geometry('430x500')

        self.open_window()
        self.mainloop()

    def accept_and_close_window(self):   # Забираем установки
        cfg.days_cnt = int(self.work_days.get())
        cfg.tariff = cfg.users.get(self.status.get())['tariff']
        self.destroy()

    def open_window(self):
        text = '''
        КАЛЬКУЛЯТОР РАСЧЕТА ВРЕМЕНИ!
        
        Пожалуйста, выберите сотрудника.
        В откроющемся окне введите время начала и конца рабочего дня.
        '''
        Label(text=text).grid(sticky='n')

        for id in sorted(cfg.users):   # Radiobutton по юзерам из файла json
            user = cfg.users.get(id)['name']
            Radiobutton(text=user, variable=self.status, value=id).grid(sticky='w')

        Label(text='Введите количество отработанных дней').grid(sticky='w')
        self.work_days = Entry()
        self.work_days.grid(sticky='w')
        Button(text='Принять', command=self.accept_and_close_window).grid(sticky='w')
        Button(text='Редактирование', command=Edit).grid(sticky='e')


class Edit(Tk):   # Вы можете добавлять или удалять сотрудников из списка
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Редактирование')
        self.geometry('400x400')

        Label(self, text='Текущие сотрудники').grid()
        self.listbox = Listbox(self, width=30, height=10)
        self.listbox.grid()
        Label(self, text='Добавление нового сотрудника').grid(row=2)
        Label(self, text='Введите имя').grid(row=3)
        Label(self, text='Введите тариф').grid(row=4)
        self.entry_name = Entry(self)
        self.entry_name.grid(row=3, column=1)
        self.entry_tariff = Entry(self)
        self.entry_tariff.grid(row=4, column=1)
        Button(self, text='Добавить', command=self.add_items).grid()

        self.current_items()
        self.mainloop()

    def current_items(self):   # Показывает зарегестрированных сотрудников
        for i in cfg.list_users:
            self.listbox.insert(END, i)

    def add_items(self):
        self.listbox.insert(END, self.entry_name.get())
        key = int(len(cfg.list_users)) + 1
        cfg.users[key] = {'name': self.entry_name.get(), 'id': key,'tariff': int(self.entry_tariff.get())}
        self.entry_tariff.delete(0, END)
        self.entry_name.delete(0, END)

        utils.add_users_json(cfg.users)   # Перезапись списка сотрудников