#!/usr/bin/python
# -*- coding: UTF-8 -*-

notunuz = int(input("Not Giriniz : "))

if notunuz < 44:
    print("Notunuz 1")
elif (notunuz > 45 and notunuz < 54):
    print("Notunuz 2")
elif (notunuz >= 55 and notunuz < 69):
    print("Notunuz 3")
elif (notunuz >= 70 and notunuz < 84):
    print("Notunuz 4")
elif (notunuz >= 85):
    print("Notunuz 5")
else:
    print("Belirtilen aralığın dışında")