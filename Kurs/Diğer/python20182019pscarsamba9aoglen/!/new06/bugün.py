# class Hesap:
#     sonuc=0
#     def topla(self,s1,s2):
#         self.sonuc=s1+s2
#     def publicsonuc(self):
#         return self.sonuc
# nesne=Hesap()
# nesne.topla(10,20)
# print(nesne.publicsonuc())
# print(nesne.sonuc)
# class Hesap:
#     sonuc=0
#     def topla(self,s1,s2):
#         self.sonuc=s1+s2
#     def publicSonuc(self):
#         return self.sonuc
#     def __privateSonuc(self):
#         return self.sonuc
#     def privateUlas(self):
#         return self.__privateSonuc()
# nesne=Hesap()
# nesne.topla(10,20)
# print(nesne.publicSonuc())
# print(nesne.sonuc)
# print(nesne.privateUlas())
# from sympy import *
# from sympy.abc import x,y
#
# print(latex(x**(7)))
# print(latex((x/4)*y**3, mode='equation'))
# print(latex(x**2, mode='inline'))
# print(latex(Integral(x**2,x), mode='inline'))
# print(latex((x+1)/y))
# class Hesap:
#     sonuc=0
#     def topla(self,s1,s2):
#         self.sonuc=s1+s2
#     def publicsonuc(self):
#         return self.sonuc
# nesne=Hesap()
# nesne.topla(10,20)
# print(nesne.publicsonuc())
# print(nesne.sonuc)
# class Hesap:
#     sonuc=0
#     def topla(self,s1,s2):
#         self.sonuc=s1+s2
#     def publicSonuc(self):
#         return self.sonuc
#     def __privateSonuc(self):
#         return self.sonuc
#     def privateUlas(self):
#         return self.__privateSonuc()
#     def _protectedSonuc(self):
#         return self.sonuc
#     def protectedUlas(self):
#         return self._protectedSonuc()
# nesne=Hesap()
# nesne.topla(10,20)
# print(nesne.publicSonuc())
# print(nesne.sonuc)
# print(nesne.privateUlas())
# print(nesne.protectedUlas())
# class bilimselhesap(Hesap):
#     def ustsiniftakipubliccsonuc(self):
#         return self.publicSonuc()
#     # def üstsınıftakiprotectedcsonuc(self):
#     #     return self._protectedSonuc()
# nesne=bilimselhesap()
# nesne.topla(10,20)
# print(nesne.publicSonuc())
for i in range(20):
    print("*".center(20))

