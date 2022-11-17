from tkinter import *
from tkinter.ttk import Checkbutton
import datetime

class App(Tk):
    def __init__(self, day):   #   характеристики размещения элементов для ввода времени
        super(App, self).__init__()

        self.title("Karban cash calculator")
        self.geometry('1200x600')

        date = 1
        column_lab = 1
        column_come = 2
        column_min = 3
        column_gone = 4
        column_hour = 5
        column_gone_min = 6
        column_check = 7
        column_one = 8
        row = day

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


    def draw(self):   #   отрисовка элементов для ввода

        self.label = Label(text='Дата:', font=30).grid(column=0, row=1)
        self.button = Button(text='TOTAL', font=20, command=self.click_button).grid(column=0, row=0)

        self.label = Label( text=f'{self.date}. Пришла:').grid(column=self.column_lab, row=self.row)
        self.a = Entry(window, width=6)
        self.a.grid(column=self.column_come, row=self.row)
        self.b = Entry(window, width=6)
        self.b.grid(column=self.column_min, row=self.row)
        self.label = Label( text='Ушла:').grid(column=self.column_gone, row=self.row)
        self.c = Entry(window, width=6)
        self.c.grid(column=self.column_hour, row=self.row)
        self.d = Entry(window, width=6)
        self.d.grid(column=self.column_gone_min, row=self.row)

    def click_button(self):   #   расчет результата нажатия кнопки TOTAL

        self.start = [int(self.a.get()), int(self.b.get())]
        self.end = [int(self.c.get()), int(self.d.get())]
        self.t1 = datetime.datetime(2022, 1, 1, *self.start)
        self.t0 = datetime.datetime(2022, 1, 1, *self.end)
        self.delta = self.t0 - self.t1
        print(self.delta)
        minutes = self.delta.total_seconds() / 60
        print(minutes)
        self.cash = round(minutes * 1.6666666666)
        print(self.cash)

        # '''Чекбоксы'''
        # self.check_state = BooleanVar()
        # self.check_state.set(False)
        # self.check = Checkbutton(window, text='Чек-лист', variable=self.check_state)
        # self.check.grid(column=self.column_check, row=self.row)
        # self.one_state = BooleanVar()
        # self.one_state.set(False)
        # self.one = Checkbutton(window, text='Одна    ', variable=self.one_state)
        # self.one.grid(column=self.column_one, row=self.row)

if __name__ == "__main__":
    day = 1
    window = App(day)


    for i in range(3):
        day += 1


        window.draw()


    window.mainloop()

