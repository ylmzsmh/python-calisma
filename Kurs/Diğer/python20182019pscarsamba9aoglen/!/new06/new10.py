def functionName(param):
    return param*param
sayilar = [1,2,3,4,5]
# print(type(sayilar[0]))
yeniSayilar= []
for i in sayilar:
    yeniI=functionName(i)
    yeniSayilar.append(yeniI)
#
print(yeniSayilar)
#
yeniSayilar2=list(map(functionName,sayilar))
print(yeniSayilar2)