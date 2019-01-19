#! /usr/bin/pyton
# -*- coding: UTF-8 -*-

puan = int(input("Notunuzu Giriniz.."))
if puan >= 0 and puan <=44:
    print ("Kaldı")
elif puan >= 45 and puan <= 54:
    print("Geçer")
elif puan >= 55 and puan <= 69:
    print("Orta")
elif puan >= 70 and puan <= 84:
    print("İyi")
elif puan >= 85 and puan <= 100:
    print("Pekiyi")
else:
    print("Geçersiz Not!")



i = int(input())
j = int(input())

while i <=j:
    print (i)
    i = i+1


liste = ["can veysel", "semih","oğuz kaan", "arda", "ebru" , "esra", "ceren","gökhan", "emine", "sait", "selcen", "asude"]
x = len(liste)
i = 0
while i<x:
    print(liste[i])
    i = i+1


for x in range(1,10):
    print (x)
else:
    print("bitti")


i = int(input())
j = int(input())
while i<=j:
    if i%2==0:
    print (i)
    i = i + 1

i = int(input())
j = int(input())
k = 0
while i<=j:
    if i%3==0 and i%5==0:
        k = k+i
    i = i + 1
print(k)



i = int(input())
l = i
j = int(input())
if j>l:
    l=j
k = int(input())
if k>l:
    l=k
print (l)

# liste = []
# liste[0] = int(input())
# liste[1] = int(input())
# liste[2] = int(input())
# a = liste[0]
# for i in range(len(liste)):
#     if liste[i]>a:
#         a=liste[i]
#     print (liste[i])


# eleman sayısını bul
myListe = [1,3,5,6,4,2,9,7,5,20,8,28,34]



