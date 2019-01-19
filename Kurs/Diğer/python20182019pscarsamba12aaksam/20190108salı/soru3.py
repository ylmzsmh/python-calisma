#!/usr/bin/pyton
# -*- coding: UTF8 -*-

from random import randint

# sadece randint modülünü kullanacağımız için
# bütün random paketini yüklememiz gerekmiyor

# kaç adet tahmin yaptığımızı takip edecek
tahminSayisi = 0
# bulmamız gereken sayı.
sayi = randint(1, 100)
print('Merhaba, 1 ile 100 arasında bir sayı tuttum, 3 denemede bu sayıyı bulabilir misin?')
print('İlk tahminini nedir: ')
while tahminSayisi < 3:
    # input() methodu ile tahmin kosuldan bir veri istediğimizi belirtiyoruz
    # ve bu veriyi alana kadar kodumuz duruyor
    tahmin = input()
    try:
        # girilen veriyi int yani bir tam sayıya çeviriyoruz
        tahmin = int(tahmin)
    except ValueError:
        # tam sayıya çeviremediğimiz durumlarda try except yardımı ile bu bloğumuz çalışacak
        print("Lütfen bir tam sayı giriniz.")
        continue

    tahminSayisi = tahminSayisi + 1
    if tahmin < sayi:
        print('Yukarı')
    if tahmin > sayi:
        print('Aşağı')
    if tahmin == sayi:
        # tahminimiz sayi ile aynı olduğunda while döngüsünden çıkabiliriz
        break

if tahmin == sayi:
    print('Tebrikler, doğru tahmin ettin!')
if tahmin != sayi:
    print('Maalesef doğru tahmin edemedin' )