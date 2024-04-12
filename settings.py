from tkinter import Button, Label, Radiobutton, Entry, StringVar, Tk

import config as cfg
import editor


class Setting(Tk):
    # Установка настроек
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.status = StringVar()  # Для выбора сотрудника
        self.status.set(cfg.default_user_id)
        self.title('Setting')
        self.geometry('540x380')

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
        Button(text='Редактирование', command=editor.Edit).grid(sticky='e')
