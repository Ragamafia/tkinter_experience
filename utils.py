from tkinter import messagebox
from tkinter import Entry


class ValidateEntry(Entry):
    arrange = []

    def __init__(self, root, *args, **kwargs):
        kwargs['validatecommand'] = root.register(self.validate), '%P'
        super().__init__(root, *args, **kwargs)

    def validate(self, value) -> bool:
        string = value.strip()
        if not string:
            return True

        if string.isnumeric():
            return min(self.arrange) <= int(string) <= max(self.arrange)

        else:
            messagebox.showwarning('Неверный ввод', 'Ожидаемый формат ввода "ЧЧ:ММ"!')
        return False


class HoursEntry(ValidateEntry):
    arrange = [00, 23]


class MinutesEntry(ValidateEntry):
    arrange = [00, 59]
