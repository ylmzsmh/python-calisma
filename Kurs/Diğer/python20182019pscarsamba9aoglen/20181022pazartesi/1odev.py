class sesli_harf():

    def kontrol(self,data):
        self.harfler=["a","e","i","o","u"]
        self.deg=0
        for i in data:
            if i in self.harfler:
                self.deg=self.deg+1
        return self.deg

a=sesli_harf()

kelime=input("kelime giriniz")

sayi=a.kontrol(kelime)

print("Girilen Kelimedeki Sesli Harf Sayisi= ",sayi)