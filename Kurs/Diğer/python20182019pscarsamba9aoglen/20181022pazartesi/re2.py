# a="python güçlü dil"
# if "python" in a:
#     print("var")

import re
a="python güçlü dil"
# if re.match("di",a)!=None:
#     print("var")
# sonuc=re.match("di",a)
# print(sonuc)
# print(sonuc.group())

# print("a=",a)
# sonuc=a.split()
# if sonuc[0]=="python":
#     print("a baslangıcında python var")
#     print(a.startswith("python"))

# print(re.search("lü",a))

liste=["elma","armut","kiraz","fındık","armut"]
for i in liste:
    bulunan=re.search("armut",i)
    if bulunan:
        print(bulunan.group())
