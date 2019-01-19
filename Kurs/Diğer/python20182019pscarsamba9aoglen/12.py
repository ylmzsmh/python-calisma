import re
a=["28GRS","GRS34","283406","10AB20","ABCDEF0","?*??--+","A5C","C6T?","3A7","5B8*","A3A7B"]
for i in a:
    if (re.match("[0-9]",i)):
        print(i)
print("-")
a=["28GRS","GRS34","283406","10AB20","ABCDEF0","?*??--+","A5C","C6T?","3A7","5B8*","A3A7B"]
for i in a:
    if(re.search("[0-9]",i)):
        print(i)
print("-")
for i in a:
    if(re.search("[0-9],[A-Z],[0-9]",i)):
        print(i)
ifadeler = ["elma","armut","kiraz","fındık","Ceviz","fişne","*2a","*28gi"]
import re
import os
dizin=os.listdir("C:\\Users\\Lab08\\Dowloads")
toplamadet=0
jpgadet=0
for i in dizin:
    toplamadet+=1
    if re.match(".*jpg",i):
        print(i)
        jpgadet+=1
print("Toplam %s Adet öge bulundu"%toplamadet)
print("toplam %s adet öge bulundu"%jpgadet)