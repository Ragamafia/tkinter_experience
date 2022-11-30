import tkinter as tk
import datetime

result = []

class Line:   # Отрисовка окон для заполнения времени

    def __init__(self, row, root):

        #self.result_in_line = []

        for i in range(row):
            row += 1

            #self.label = tk.Label(text=f'Дата: {}', font=30).grid(column=0, row=row)
            self.label = tk.Label(text='Пришла:').grid(column=1, row=row)
            self.label = tk.Label(text='Ушла:').grid(column=4, row=row)

            self.a = tk.Entry(root, width=6)   # пришла (часов)
            self.a.grid(column=2, row=row)
            self.b = tk.Entry(root, width=6)   # пришла (минут)
            self.b.grid(column=3, row=row)
            self.c = tk.Entry(root, width=6)   # ушла (часов)
            self.c.grid(column=5, row=row)
            self.d = tk.Entry(root, width=6)   # ушла (минут)
            self.d.grid(column=6, row=row)

            result.append(self.a)#.get())
            result.append(self.b)#.get())
            result.append(self.c)#.get())
            result.append(self.d)#.get())

            # self.result_in_line.append(self.a)
            # self.result_in_line.append(self.b)
            # self.result_in_line.append(self.c)
            # self.result_in_line.append(self.d)

        print(f'Объекты result: {result}')
        #print(f'Объекты result_in_line: {self.result_in_line}')

    def calculating(self):
        for i in result:
            print(i)
        print(f'Объекты result: {result}')
        #print(f'Объекты result_in_line: {self.result_in_line}')

        # for i in result:
        #     print(f'Объект {i}')

            # start = [int(self.a.get()), int(self.b.get())]
            # end = [int(self.c.get()), int(self.d.get())]
            # t1 = datetime.datetime(2022, 1, 1, *start)
            # t0 = datetime.datetime(2022, 1, 1, *end)
            # delta = t0 - t1
            # print(delta)
            # minutes = delta.total_seconds() / 60
            # print(minutes)
            # cash = round(minutes * 1.6666666666)
            # #result.append(cash)
            # print(cash)
            # print(i)
            # print(result)

if __name__ == "__main__":

    root = tk.Tk()   # окно приложения
    root.title('KARBAN')
    root.geometry('800x600')

    row = 2   # количество отработанных дней
    run = Line(row, root)

    tk.Button(root, text='TOTAL', font=20, command=run.calculating).grid(column=7, row=0)

    root.mainloop()










