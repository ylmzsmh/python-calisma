#   filter kullanımı

#sayılar=list(range(1,10))
#print(sayılar)

#bu listenin çift sayı olanları alalım
#yeniSayılar=list(filter(lambda p:p%2==0,sayılar))
#print(yeniSayılar)

#bir örnek
#kelimeler=["php","python","html","5","4"]
#
#yeniKelimeler=[]
#for i in kelimeler:
#    i=str(i)
#    if i.isnumeric():
#        yeniKelimeler.append(i)
#        print(yeniKelimeler)
kelimeler=["php","python","html","5","4"]
sayiOlanlar=list(filter(lambda p:p.isnumeric(),kelimeler))
print(sayiOlanlar)