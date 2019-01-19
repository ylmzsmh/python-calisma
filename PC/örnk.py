#!/usr/bin/python
# -*- coding: UTF-8 -*-

# eleman silme
liste = ["abc","bca","cab"]
print (liste)
liste.pop(2)
print (liste)

#eleman silme
liste = ["abc","bca","cab"]
print(liste)
del liste[0]
print(liste)

#liste silme/temizleme/içini boşaltma
liste = ["abc","bca","cab"]
print(liste)
liste.clear()
print(liste)

#listeye demetten eleman alma
demet = ("abc","bca","cab")
liste = [demet[0],"bbb",]
liste1 = [demet,"bbb",]
print(liste)
print(liste1)
liste[0] = "hhh"
print (liste)

#inputlu sözlük oluşturma
ad1 = input("AD1= ")
soyad1= input("SOYAD1= ")
yas1 = input("YAS1= ")
ad2 = input("AD2= ")
soyad2= input("SOYAD2= ")
yas2 = input("YAS2= ")
ad3 = input("AD3= ")
soyad3= input("SOYAD3= ")
yas3 = input("YAS3= ")
sozluk = {
1:{
"ad =": ad1,
"soyad =": soyad1,
"yas =": yas1
},
2:{
"ad =": ad2,
"soyad =": soyad2,
"yas =": yas2
},
3:{
"ad =": ad3,
"soyad =": soyad3,
"yas =": yas3
}
}
print(sozluk)


#

# isimler = {
# 1:{
# "ad": "Mustafa",
# "soyad":"Yılmaz",
# "yas":35
# },
# 2:{
# "ad": "Can Veysel",
# "soyad":"Şoroğlu",
# "yas=": 27
# },
# 3:{
# "ad": "Semih",
# "soyad": "Yılmaz",
# "yas=": 25
# },
# }
# # x = input("1 ile 3 Arasında Bir Değer Giriniz..")
# # print(isimler[int(x)][1],isimler[int(x)][2],isimler[int(x)][3])
# print(isimler[1],isimler[1],isimler[1])

#

isimler = ("Mustafa Yılmaz 35","Can Veysel 27", "Semih Yılmaz 25")
x = input("1 ile 3 Arasında Bir Değer Giriniz..")
print(isimler[int(x)-1])

#

notunuz = int(input("Not Giriniz : "))
if notunuz < 44:
    print("Notunuz 1")
elif (notunuz > 45 and notunuz < 54):
    print("Notunuz 2")
elif (notunuz >= 55 and notunuz < 69):
    print("Notunuz 3")
elif (notunuz >= 70 and notunuz < 84):
    print("Notunuz 4")
elif (notunuz >= 85 and notunuz <= 100 ):
    print("Notunuz 5")
else:
    print("Belirtilen aralığın dışında")

#sözlükten eleman silme popitem, del
# sözlüğü temizleme/boşaltma sozlük.clear()

#

a = int(input("Bir Sayı Giriniz.."))
b = int(input("Bir Sayı Giriniz.."))

if a>b:
    print("a"+"("+str(a)+")","büyüktür","b"+"("+str(b)+")")
elif a==b:
    print("a"+"("+str(a)+")","eşittir", "b"+"("+str(b)+")")
else:
    print("a"+"("+str(a)+")","küçüktür", "b"+"("+str(b)+")")

#

a = 6
b = 8

if a>b:
    print("a"+"("+str(a)+")","büyüktür","b"+"("+str(b)+")")
elif a==b:
    print("a"+"("+str(a)+")","eşittir", "b"+"("+str(b)+")")
else:
    print("a"+"("+str(a)+")","küçüktür", "b"+"("+str(b)+")")


marka = {"opel", 'mercedes', 'bmw',}
mensei = ["alman"]
otomobil = dict.fromkeys(marka, mensei)
print(otomobil)

auto = {"opel": "alman", "bentley": "ingiliz", "honda": "japon",}
araba = auto.copy()
print(araba)
