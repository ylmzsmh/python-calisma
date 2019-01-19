#!/usr/bin/pyton
# -*- coding: UTF8 -*-

# sayi=10
# while sayi>=0:
#     print(sayi)
#     sayi-=1


# sayi1 = int(input("Birinci Sayiyi Giriniz : "))
# sayi2 = int(input("İkinci Sayiyi Giriniz : "))
#
# if sayi1<sayi2:
#     while sayi1<=sayi2:
#         print(sayi1)
#         sayi1+=1
# elif sayi1>sayi2:
#     while sayi1>=sayi2:
#         print(sayi2)
#         sayi2+=1
#
# liste = ["Ali", "Ali2", "Ali3", "Ali4", "Ali5", "Ali6", "Ali7", "Ali8"]
# indis = 0
# i = len(liste)
# while i > 0:
#     print(liste[indis])
#     indis += 1

#
# i=1
# while i<10:
#     print(i)
#     if i==3:
#         break
#     i+=1




# basla = int(input("Birinci Sayiyi Giriniz : "))
# bitis = int(input("İkinci Sayiyi Giriniz : "))
#
# while basla<bitis:
#     basla += 1
#     if basla%2==1:
#         continue
#     print(basla)


#
# basla = int(input("Birinci Sayiyi Giriniz : "))
# bitis = int(input("İkinci Sayiyi Giriniz : "))
# toplam =int(0)
# while basla < bitis:
#     if basla % 15 == 0:
#         toplam = toplam+basla
#     basla += 1
# print(toplam)


sayi1 = int(input("Birinci Sayiyi Giriniz : "))
sayi2 = int(input("İkinci Sayiyi Giriniz : "))
sayi3 = int(input("İkinci Sayiyi Giriniz : "))

if sayi1>sayi2 and sayi1>sayi3:
    print(sayi1," En büyük sayıdır")
elif sayi2>sayi1 and sayi2>sayi3:
    print(sayi2," En büyük sayıdır")
elif sayi3 > sayi2 and sayi3 > sayi1:
    print(sayi3," En büyük sayıdır")
