#!/usr/bin/pyton
# -*- coding: UTF8 -*-
tutulansayi = 3
print("1-", tutulansayi, "tutulan sayı arası bir sayı tahmin ediniz, 3 hakkınız var!")
i=1
while i<=3:
    print(i,". hakkınız, tahmininiz=")
    girilen = int(input())
    if girilen == tutulansayi:
        print("Doğru tahmin ettiniz")
        break;
    i += 1
else:
    print("3 hakkınızda tahmin edemediniz")