import Hesaplama

class BHesap(Hesaplama.Hesap):
   def __init__(self,s1=0,s2=0):
       Hesaplama.Hesap.__init__(self,s1,s2)

   def ustAl(self,sayi,ust):
      self.bSonuc=sayi**ust

nesne=BHesap()
nesne.ustAl(2,4)
print(str(2)+"üstü" + str(4)+"="+str(nesne.bSonuc))



class tHesap(Hesaplama.Hesap):
   def __init__(self,s1=0,s2=0):
       Hesaplama.Hesap.__init__(self,s1,s2)

   def toplam(self,sayi1,sayi2):
       self.tsonuc=sayi1+sayi2

nesne2=tHesap()
nesne2.toplam(2,4)
print(str(2)+"ile" + str(4)+"="+str(nesne2.tsonuc))
