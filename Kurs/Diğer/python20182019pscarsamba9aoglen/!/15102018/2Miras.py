# Sınıflarda miras alma
# Bir sınıfın özelliklerinin başka bir sınıfa devredilmesidir.

class Imza():
    def __init__(self,ad,soyad,telefon):
        self.ad=ad
        self.soyad=soyad
        self.telefon=telefon

    def yaz(self):
        print(self.ad+" "+ self.soyad+"-"+self.telefon)

nesne=Imza("Hamide","Atakul","45636363")
nesne.yaz()

class MirasImza(Imza):
    def yaz2(self):
        self.yaz()

class MirasImza(Imza):
    def yaz2(self):
        self.yaz()
nesne2=Imza("Nuran","Erken","45636363")
nesne2.yaz()

