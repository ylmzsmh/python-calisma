class Hesap():
    def __init__(self,s1,s2):
        self.s1=s1
        self.s2=s2

    def topla(self):
        self.sonuc=self.s1+self.s2

    def cikar(self):
        self.sonuc=self.s1-self.s2

    def carp(self):
        self.sonuc=self.s1*self.s2

    def Bol(self):
        self.sonuc = self.s1/self.s2


hm=Hesap(10,20)
hm.topla()
print("Toplam= "+str(hm.sonuc))

print("----------")

class BHesap(Hesap):
    def  __init__(self,s1,s2):
        Hesap.__init__(self,s1,s2)

    def ustAl(self,sayi,ust):
        self.bilimselSonuc=sayi**ust

bhm=BHesap(10,20)
bhm.topla()
print("Toplam="+str(bhm.sonuc))

bhm.ustAl(10,2)
print("Üst="+str(bhm.bilimselSonuc))

