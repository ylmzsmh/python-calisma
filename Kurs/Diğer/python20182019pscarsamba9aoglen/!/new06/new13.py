# recursive (kendikendisini çağıran) fonksiyonlar
#mliste=["meryem","hatice","muhammet","fatih"]
#for i in mliste:
#    print(i,end=" ")

mliste=["meryem","hatice","muhammet","fatih"]
def myRecursiveFonksiyon(fListe):
#    print(fliste)
    if len(fListe)==0:
        return ""
    else:

        yFListe=fListe[1:]
        return fListe[0] +" "+myRecursiveFonksiyon(yFListe)
print(myRecursiveFonksiyon(mliste))