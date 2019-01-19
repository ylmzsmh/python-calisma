from tkinter import *
# import tkinter
# Tk sınıfından örnek al
# pencere = tkinter.Tk()
pencere=Tk()

# pencerenin konumu ve boyutu
# width,height,left,top
# genişlik, yükseklik, sol, üst
# ? pencere nasıl tam ekran açılır.
pencere.geometry("400x300+500+100")
# ? pencere nasıl taşınmaz.
pencere.resizable(width=FALSE,height=FALSE)

# pencerenin ekranda sabit durması
pencere.mainloop()
