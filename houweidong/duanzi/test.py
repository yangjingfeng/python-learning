import tkinter
import random


def suijishu(a, b):
    t.delete(0.0, 'end')
    t.insert('end', random.randint(a, b))
    t.after(500, suijishu, a, b)


top = tkinter.Tk()

t = tkinter.Text(top)
t.pack(expand=1, fill='both')
suijishu(51, 100)

top.mainloop()