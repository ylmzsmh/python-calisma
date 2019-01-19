# gui checkbox kullanımı

from tkinter import *

pencere = Tk()
pencere.geometry("500x400+1000+100")

muzik=IntVar()
muzik.set(0)
check1 = Checkbutton(pencere,text="Müzik",variable=muzik)
# ? checked olma nasıl?
check1.pack()

pencere.mainloop()
