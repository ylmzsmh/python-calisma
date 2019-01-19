
isimler = ["phyton", "php", "html"]
for i in isimler:
    print(i, end=" ")
    uzunluk = len(i)
    adet = 1

    for m in i:
        if uzunluk == adet:
            print(m, end="")
        else:
            print(m, end="-")