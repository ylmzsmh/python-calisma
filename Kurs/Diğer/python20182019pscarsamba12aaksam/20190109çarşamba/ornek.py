#!/usr/bin/pyton
# -*- coding: UTF8 -*-
def topla(x,y):
    return x+y
def carp(x,y):
    return x*y
s1= input("birinci sayı =")
s2= input("ikinci sayı=")
s1= int(s1)
s2= int(s2)
islem=input("bir işlem seçin(1-topla, 2- çarpma")
if islem=="1":
    sonuc=topla(s1,s2)
elif islem=="2":
    sonuc==carp(s1,s2)
else:
    sonuc="geçersiz işlem"
print(sonuc)