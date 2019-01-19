from tkinter import *

root=Tk()

etiket=Label(root,text="Aşağıdaki kutucuğa e-posta adresini yazınız!")
etiket.pack()

giris=Entry()
giris.pack()

cerceve=Frame(root,height=50,bd=1,relief=SUNKEN)
cerceve.pack(fill=X,padx=5,pady=5)

dugme=Button(root,text="Gönder",command=root.destroy)
dugme.pack()

def yeniPencere():
    p=Tk()
    p.mainloop()

def sayfa():
    sayfaa=Tk()
    cerceve = Frame(sayfaa,height=5, bd=1, relief=SUNKEN)
    cerceve.pack(fill=X, padx=5, pady=5)

    dugme44 = Button(sayfaa,text="logaritma", command=yeniPencere)
    dugme44.pack()

    dugme33 = Button(sayfaa,text="elektronik", command=yeniPencere)
    dugme33.pack()






sayfa()
root.mainloop()


# Üstteki uygulamayı sınıf içinde yazalım.

class Uygulama(object):
    def __init__(self):
        self.guiPencere()




    def guiPencere(self):
        self.etiket=Label(text="Aşağıdaki kutucuğa e-posta adresini yazınız! ")
        self.etiket.pack()

        self.giris.Entry()
        self.giris.pack()

        self.cerceve=Frame()
        self.cerceve.pack(side=BOTTOM,padx=5,pady=5)

        self.dugme=Button(self.cerceve,text="Gönder",width=5)
        self.dugme.pack(side=LEFT,padx=5)

        self.dugme2=Button(  self.cerceve,text="İptal",width=5)
        self.dugme2.pack()

        root=Tk()
        u=Uygulama()
        root.mainloop()


