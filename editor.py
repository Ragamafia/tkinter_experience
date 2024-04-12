from tkinter import Listbox, Button, Label, Entry, END, Tk
import uuid

import config as cfg
import utils


class Edit(Tk):
    # Вы можете добавлять или удалять сотрудников из списка
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.list_map = {}

        self.title('Редактирование')
        self.geometry('480x380')

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

        self.update()
        self.mainloop()

    def update(self):
        self.list_map.clear()
        self.listbox.delete(0, END)
        for n, id in enumerate(cfg.users):
            self.list_map[n] = id
            self.listbox.insert(END, cfg.users.get(id)['name'])

    def add_items(self):
        key = str(uuid.uuid4())
        cfg.users[key] = {
            'name': self.entry_name.get(),
            'id': key, 'tariff': int(self.entry_tariff.get())
        }
        utils.dump_users(cfg.users)
        self.update()

        self.entry_tariff.delete(0, END)
        self.entry_name.delete(0, END)

    def del_items(self):
        id = self.list_map[self.listbox.curselection()[0]]
        del cfg.users[id]
        utils.dump_users(cfg.users)
        self.update()
