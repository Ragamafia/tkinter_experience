from tkinter import *
import datetime


class Block:   # Блок с окнами для заполнения времени

    def __init__(self, root, row):

        self.label = Label(text=f'Дата: {row}', font=30).grid(column=0, row=row)
        self.label = Label(text='Пришла:').grid(column=1, row=row)
        self.a = Entry(root, width=6)
        self.a.grid(column=2, row=row)
        self.b = Entry(root, width=6)
        self.b.grid(column=3, row=row)
        self.label = Label(text='Ушла:').grid(column=4, row=row)
        self.c = Entry(root, width=6)
        self.c.grid(column=5, row=row)
        self.d = Entry(root, width=6)
        self.d.grid(column=6, row=row)

        self.button = Button(text='TOTAL', font=20, command=self.click_button).grid(column=7, row=0)

    def click_button(self):   # Расчет результата нажатия кнопки TOTAL

        start = [int(self.a.get()), int(self.b.get())]
        end = [int(self.c.get()), int(self.d.get())]
        t1 = datetime.datetime(2022, 1, 1, *start)
        t0 = datetime.datetime(2022, 1, 1, *end)
        delta = t0 - t1
        print(delta)
        minutes = delta.total_seconds() / 60
        print(minutes)
        cash = round(minutes * 1.6666666666)
        print(cash)


if __name__ == "__main__":

    root = Tk()
    root.title("Karban cash calculator")
    root.geometry('1200x600')
    row = 0

    for i in range(2):
        row += 1

        Block(root, row)

    root.mainloop()