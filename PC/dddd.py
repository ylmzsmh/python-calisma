#!/usr/bin/python
# -*- coding: UTF-8 -*-


auto = {"opel": "alman", "bentley": "ingiliz", "honda": "japon",}
araba = auto.copy()
print(araba)

marka = {"opel", 'mercedes', 'bmw',}
mensei = ["alman"]
otomobil = dict.fromkeys(marka, mensei)
print(otomobil)

galeri = {"alman":("bmw","wolkswagen"),"amerikan":("ford","jeep","chevrolet")}
print(galeri)
galeri.setdefault("italyan",("alfa romeo","lamborghini"))
print(galeri)

motosikleteski = {"honda": "shadow vt600", "kawasaki": "en500", "hyosung": "gv250"}
motosikletyeni = {"honda": "shadow vt750", "kawasaki": "vn1500", "hyosung": "gv650"}
motosikleteski.update(motosikletyeni)
print(motosikleteski)