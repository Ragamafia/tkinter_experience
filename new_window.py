import tkinter
from tkinter import Tk
from tkinter import Frame, Button, Label, Radiobutton


class Marking(Tk):  # разметка и надписи в окнах

        def __init__(self):
                super().__init__()
                self.open_window()

        def accept_and_close_window(self):
                self.setup()
                self.destroy()

        def open_window(self):

                Label(text='ДОБРО ПОЖАЛОВАТЬ В КАЛЬКУЛЯТОР РАСЧЕТА ВРЕМЕНИ!').grid(sticky='n')
                Label(text='''Пожалуйста, выберите сотрудника и в следующем окне
        введите время начала и конца рабочего дня.''').grid()

                self.status = tkinter.IntVar()
                self.status.set(0)

                Radiobutton(text='Тати', variable=self.status, value=0).grid(sticky='w')
                Radiobutton(text='Аня', variable=self.status, value=1).grid(sticky='w')
                Radiobutton(text='Настя', variable=self.status, value=2).grid(sticky='w')

                Button(text="Принять", command=self.accept_and_close_window).grid()

        def setup(self):

                if self.status.get() == 0:
                        print('Выбрана Тати')
                elif self.status.get() == 1:
                        print('Выбрана Аня')
                elif self.status.get() == 2:
                        print('Выбрана Настя')


class Post(Frame):  # класс размещения Лейблов в главном окне

        def __init__(self, row):
                self.row = row
                super().__init__()

                Label(text='Начало:').grid(row=self.row, column=0, sticky='e')
                Label(text='Конец').grid(row=self.row, column=4, sticky='e')


root = Marking()
root.geometry('350x500')
root.title('Settings')

root.mainloop()
