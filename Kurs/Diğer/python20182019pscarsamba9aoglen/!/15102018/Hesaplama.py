class Hesap():

    '''Bu sınıf dört işlem hesap makinası yapar'''

    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2

    def topla(self):
         self.sonuc=self.s1 + self.s2

    def çıkar(self):
        self.sonuc = self.s1- self.s2

    def çarp(self):
        self.sonuc = self.s1 *self.s2

    def bol(self):
        self.sonuc = self.s1 / self.s2

