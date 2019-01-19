from tkinter import *

p=Tk()
p.geometry("500x400+500+100")

labelAd = Label(text="Adınızı Girin")
labelAd.pack()

entryAd = Entry(p)
entryAd.pack()

def entryOku():
    girilenAd = entryAd.get()
    labelSonuc =Label(text="Merhaba "+ girilenAd)
    labelSonuc.pack()

butonTikla = Button(text="Tıkla",command=entryOku)
butonTikla.pack()

p.mainloop()