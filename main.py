from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.ttk import Checkbutton
import datetime

class MyFrame:
    '''Описание параметров размещения окон'''
    def __init__(self, day, line):

        date = day
        column_lab = 1
        column_come = 2
        column_min = 3
        column_gone = 4
        column_hour = 5
        column_gone_min = 6
        column_check = 7
        column_one = 8
        row = line

        self.date = date
        self.column_lab = column_lab
        self.column_come = column_come
        self.column_min = column_min
        self.column_gone = column_gone
        self.column_hour = column_hour
        self.column_gone_min = column_gone_min
        self.column_check = column_check
        self.column_one = column_one
        self.row = row

class InputInfo(MyFrame):

    def draw(self):
        '''Отрисовка окон для ввода'''
        self.label = Label(window, text=f'{self.date}. Пришла:')
        self.label.grid(column=self.column_lab, row=self.row)
        self.come_hours = Entry(window, width=6, )
        self.come_hours.grid(column=self.column_come, row=self.row)
        self.come_minutes = Entry(window, width=6, )
        self.come_minutes.grid(column=self.column_min, row=self.row)
        self.label_gone = Label(window, text='Ушла:')
        self.label_gone.grid(column=self.column_gone, row=self.row)
        self.gone_hours = Entry(window, width=6, )
        self.gone_hours.grid(column=self.column_hour, row=self.row)
        self.gone_minutes = Entry(window, width=6, )
        self.gone_minutes.grid(column=self.column_gone_min, row=self.row)

        self.check_state = BooleanVar()
        self.check_state.set(False)
        self.check = Checkbutton(window, text='Чек-лист', variable=self.check_state)
        self.check.grid(column=self.column_check, row=self.row)
        self.one_state = BooleanVar()
        self.one_state.set(False)
        self.one = Checkbutton(window, text='Одна    ', variable=self.one_state)
        self.one.grid(column=self.column_one, row=self.row)

class App(Tk, InputInfo):
    '''Главное окно'''
    def __init__(self):
        super().__init__()

        self.title("Karban cash calculator")
        self.geometry('1200x600')

        self.label = Label(self, text='Дата:', font=30)
        self.label.grid(column=0, row=1)
        self.button = Button(self, text='TOTAL', font=20, command=self.button_result)
        self.button.grid(column=0, row=0)

    def button_result(self):

        start = [int(self.come_hours.get()), int(self.come_minutes.get())]
        end = [int(self.gone_hours.get()), int(self.gone_minutes.get())]
        t1 = datetime.datetime(2022, 1, 1, *start)
        t0 = datetime.datetime(2022, 1, 1, *end)
        delta = t0 - t1
        print(delta)
        seconds = delta.total_seconds()
        cash = round(delta.total_seconds() * 0.0277777777777)
        print(cash)
        print('hui!')

    def button_clicked(self):
        showinfo(title='Result', message='TO DO')

if __name__ == "__main__":
    window = App()
    day, line = 0, 1

    for i in range(1):
        day += 1
        line += 1
        start = InputInfo(day, line)
        start.draw()


    window.mainloop()
