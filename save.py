from tkinter import Tk, Listbox

root = Tk()

window = Listbox(root, width=60, height=15)
window.grid()

for i in ('One', 'Two', 'Three'):
    window.insert(0, i)

root.mainloop()


