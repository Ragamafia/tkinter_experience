from tkinter import Listbox, Button, Label, Entry, END, Tk
import uuid

import config as cfg
import utils


class Edit(Tk):
    # Вы можете добавлять или удалять сотрудников из списка
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Редактирование')
        self.geometry('480x480+600+300')

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
        Button(self, text='Удалить', command=self.del_items).grid()

        self.current_items()
        self.mainloop()

    def current_items(self):
        for i in cfg.users:
            self.listbox.insert(END, cfg.users.get(i)['name'])

    def add_items(self):
        self.listbox.insert(END, self.entry_name.get())
        key = str(uuid.uuid4())
        new_users = {
            key: {
                'name': self.entry_name.get(),
                'id': key, 'tariff': int(self.entry_tariff.get())
            }
        }
        cfg.users.update(new_users)
        utils.dump_users(cfg.users)

        self.entry_tariff.delete(0, END)
        self.entry_name.delete(0, END)

    def del_items(self):
        select = self.listbox.curselection()
        key_delete = self.listbox.get(select)
        for key, value in list(cfg.users.items()):
            if value['name'] == key_delete:
                self.listbox.delete(select)
                del cfg.users[key]
                utils.dump_users(cfg.users)
