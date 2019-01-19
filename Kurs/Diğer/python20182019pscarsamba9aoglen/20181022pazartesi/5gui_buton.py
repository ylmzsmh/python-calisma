# gui buton kullanımı

from tkinter import *

def yaz():
    print("yazdım")

pencere = Tk()

pencere.geometry("400x400+500+100")

buton1 = Button(text="YAZ",command=yaz)
buton1.pack()

buton2 = Button(text="PENCEREYİ KAPAT",command=pencere.quit)
buton2.pack()

pencere.mainloop()