import tkinter
import speechSpiders3

s = speechSpiders3.speechOne()

def suijishu(mytext):
    t.delete(0.0,'end')
    t.insert('end',mytext)
    t.after(10000, suijishu, s.get())

top = tkinter.Tk()

t = tkinter.Text(top,background='#e3f9ed')
t.pack(expand=1, fill='both')
suijishu(s.get())

top.mainloop()