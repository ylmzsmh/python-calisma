#!/usr/bin/python
# -*- coding:UTF-8 -*-

import pprint
islem = input("Yapmak İstenilen İşlem: (görüntüle,ekle,çıkar,değiştir,Çıkış (q))")
personel = {"semih":("semih","yılmaz","1111111111","111","11"),"ali":("ali","yılmaz","22222222222","222","22")}
if islem == "q":
        print ("Çıkılıyor..")

elif islem == "görüntüle":
    isim = str(input("Bilgilerini İstediğiniz Personel Adını Giriniz:"))
    if isim == "hepsi":
        pprint.pprint(personel)
    else:
        pprint.pprint(personel[isim])

elif islem == "ekle":
        yeniad = input ("Ad Giriniz:")
        yenisoyad = input ("Soyad Giriniz:")
        yenitc = input ("Tc Giriniz:")
        yenioda = input ("Oda Giriniz:")
        yenidahili = input ("Dahili Giriniz:")
        personel.setdefault(yeniad,(yeniad,yenisoyad,yenitc,yenioda,yenidahili))
        print (personel)

elif islem == "değiştir":
        ad = input("Güncellenicek Kişiyi Giriniz:")
        yeniad = input("Ad Giriniz:")
        yenisoyad = input("Soyad Giriniz:")
        yenitc = input("Tc Giriniz:")
        yenioda = input("Oda Giriniz:")
        yenidahili = input("Dahili Giriniz:")
        personel.pop(ad)
        personel.setdefault(yeniad, (yeniad, yenisoyad, yenitc, yenioda, yenidahili))
        print(personel)

elif islem == "çıkar":
        ad = input("Çıkartmak İstenilen Kişi:")
        personel.pop(ad)
        print(personel)


