# while döngüsü
# print(1)
# print(2)
# ...
# print(x)

# kullanımı
#
# baslangicDegiskeni=""
# while sart:
#     işlemler
#      artırma yada azalatma

adet=1
print("döngü öncesi")
while adet<=10:
    print(adet)
    adet=adet+1
print("döngü sonrası")




# döngüler
# 2 tür döngü vardır
# birincisi while
# ikincisi for



# diğer kullanım türleri

# a=30
# b=20
# if a>b: print("a büyük b")

# diğer bir kullanım

# a=10
# b=20
#
# print("a büyük b") if a>b else print("b büyük a")

# and ve or kullanımı

# dil="ingilizce"
# yas=29
# if dil=="ingilizce" and yas>=30:
#     print("mülakat")
# else:
#     print("red")

sinavNotu = 101
# if sinavNotu>=0 and sinavNotu<=44:
#     print("kaldı - 1")
# elif sinavNotu>=45 and sinavNotu<=54:
#     print("geçti - 2")
# elif sinavNotu>=55 and sinavNotu<=69:
#     print("orta - 3")
# elif sinavNotu>=70 and sinavNotu<=84:
#     print("iyi - 4")
# elif sinavNotu>=85 and sinavNotu<=100:
#     print("pekiyi - 5")
# else:
#     print("geçersiz")

# ikinci çözüm
if sinavNotu<0:
    print("geçersiz")
elif sinavNotu<45:
    print("kaldı - 1")
elif sinavNotu<55:
    print("geçti - 2")
elif sinavNotu<70:
    print("orta - 3")
elif sinavNotu<85:
    print("iyi - 4")
elif sinavNotu<101:
    print("pekiyi - 5")
else:
    print("geçersiz")




# pythonda koşullar (if - eğer)

# yas=18
#
# print("if öncesi")
#
# if yas==18:
#     print("yaşınız 18 dir")
#
# print("if sonrası")

# yas=20
# print("if öncesi")
#
# if yas==18:
#     print("yaşınız 18dir")
# else:
#     print("yaşınız 18değildir")
#
# print("if sonrası")

# yas=17
# mesaj="yaşınız 18 değildir."
#
# if yas==18:
#     mesaj="yaşınız 18 dir"
#
# print(mesaj)

# a=30
# b=30
#
# if a>b:
#     print("a büyüktür b")
# elif b>a:
#     print("b büyüktür a")
# else:
#     print("a eşittir b")

