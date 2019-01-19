#def myfunc(param1,param2):
#    sonuc=param1+param2
#    return sonuc
#toplamaSonucu=myfunc(10,20)
#print(toplamaSonucu)

def topla(x,y):
    t=x+y
#    print(t)
    return t
def carp(x,y):
    ss=x*y
#   print(ss)
    return ss
s1=input("birinci sayı girin :")
s2=input("ikinci sayı girin :")
s1=int(s1)
s2=int(s2)
islem=input("bir işlem seçin (1-topla,2-çarpma) :")
if islem=="1":
    sonuc=topla(s1,s2)
    print("sonuc: ",sonuc)
elif islem=="2":
    sonuc=carp(s1,s2)
    print("sonuc: ",sonuc)
else:
    sonuc="geçersiz işlem seçildi"
    print(sonuc)
