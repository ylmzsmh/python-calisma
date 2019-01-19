class HesapMakinesi:

    s1,s2,t,f,c,b=0,0,0,0,0,0

    def __init__(self,p1,p2):
        self.s1=p1
        self.s2=p2

    def hesapla(self):
        self.t=self.s1+self.s2
        self.f=self.s1-self.s2
        self.c=self.s1*self.s2
        self.b=self.s1/self.s2

islem=HesapMakinesi(2,3)
islem.hesapla()
print("Toplam",islem.t)
print("Fark",islem.f)
print("Çarpım",islem.c)
print("Bölüm",islem.b)

