#!/usr/bin/python
# -*- coding: UTF-8 -*-
# netsupport school

from random import randint as r
harfler=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
sayilar =[0,1,2,3,4,5,6,7,8,9]
x = r(1,29)
y = r(1,10)
print(harfler[x],sayilar[y])

from random import randint as r
x=1
adet = int(input("Kaç Karakterli Şifre İsteniyor:"))
harfler=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
sayilar =[0,1,2,3,4,5,6,7,8,9]
sifre = ""
while x <= adet:
    sifre  += harfler(r(0,25))
    sifre += sayilar(r(0, 9))
    print (sifre)
    x += 1