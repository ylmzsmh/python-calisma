#
# basla=(int(input("Başlangıç sayısını giriniz:")))
# bitis=(int(input("Bitiş sayısını giriniz:")))
#
# for x in range(basla,bitis,2):
#     print(x)
#

# basla=int(input("Başlangıç sayısını giriniz:"))
# bitis=int(input("Bitiş sayısını giriniz:"))
#
# while basla<=bitis:
#     bolmedenKalan=basla%2
#     if bolmedenKalan==0:
#         print(basla)
#     basla+=1
#
# basla = int(input("Başlangıç sayısını giriniz:"))
# bitis = int(input("Bitiş sayısını giriniz:"))
#
# while basla <= bitis:
#         UcbolmedenKalan = basla % 3
#         if UcbolmedenKalan == 0:
#             BesBolmedenKalan=basla%5
#             if BesBolmedenKalan == 0:
#                 print(basla)
#         basla += 1
#


# basla = int(input("Başlangıç sayısını giriniz:"))
# bitis = int(input("Bitiş sayısını giriniz:"))
# toplam=0
# while basla <= bitis:
#     if basla%3==0 and basla%5==0:
#         toplam=toplam+basla
#
#     basla+=1
#
# print("3'e ve 5'e bölünen toplamı="+str(toplam))
#
sayi1 = int(input("İlk sayıyı giriniz:"))
sayi2= int(input("İkinci sayıyı giriniz:"))
sayi3= int(input("Üçüncü sayıyı giriniz:"))



if sayi1>sayi2:
    if sayi1>sayi3:
        print("Birinci sayı en büyüktür=",sayi1)
if sayi2>sayi1:
    if sayi2>sayi3:
        print("İkinci sayı en büyüktür=",sayi2)
if sayi3 > sayi2:
    if sayi3 > sayi1:
        print("Üçüncü sayı  en büyüktür.=",sayi3)




