# gui label kullanımı

from tkinter import *

pencere=Tk()

pencere.geometry("400x400+500+100")

etiket1 = Label(text="trabzonspor",fg="#88001b",bg="#3ebef8",font="tahoma 28 bold")
etiket1.pack()

etiket2 = Label(text="türkiye",fg="#fff",bg="#f05",font="arial 28 bold")
etiket2.pack()

pencere.mainloop()