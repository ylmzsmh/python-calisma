from tkinter import *
from tkinter.messagebox import *
import sqlite3
from functools import partial

baglan=sqlite3.connect("adres_defteri.db")
if baglan==False:print("Bağlantı Hatası");exit();
baglan.row_factory=sqlite3.Row
db=baglan.cursor()

def kisiEkle():

    adSoyad=entryAdSoyad.get()
    telefon=entryTelefon.get()

    if adSoyad=="" or telefon=="":
        showwarning(("uyarı","Ad Soyad veya Telefon Gerekli..."))
    else:
        db.execute("insert into kisi(kisi_adsoyad,kisi_telefon)values('"+adSoyad+"','"+telefon+"')")
        baglan.commit()
        if db.lastrowid:
            showinfo("Başarılı", "Kişi Eklendi..")
        else:
            showerror("başarısız","kişi eklenemedi...")

    # showinfo("")


def kisileriListele():

   global pencereListele
   pencereListele=Toplevel()
   pencereListele.geometry("300x300+100+200")


   labelNo=Label(pencereListele,text="No").grid(row=0,column=1,sticky=W)
   labelAdSoyad = Label(pencereListele, text="Ad Soyad").grid(row=0, column=2, sticky=W)
   labelTelefon = Label(pencereListele, text="Telefon").grid(row=0, column=3, sticky=W)

   try:

        sorguTumKisiler=db.execute("select * from kisi")
        tumKisiler=sorguTumKisiler.fetchall()
        hata=False

   except:
       hata=True
       showerror("hata","Listelemede bir sorun oluştu..")

   if hata==False:
       no=2
       for kisi in tumKisiler:
           Label(pencereListele,text=no-1).grid(row=no,column=1,sticky=W)
           Label(pencereListele,text=kisi["kisi_adsoyad"]).grid(row=no,column=2,sticky=W)
           Label(pencereListele, text=kisi["kisi_telefon"]).grid(row=no, column=3, sticky=W)
           Button(pencereListele,text="Güncelle",command=partial(kisiGuncelle,kisi["kisi_id"])).grid(row=no,column=4,sticky=W)
           Button(pencereListele, text="Sil", command=partial(kisiSil, kisi["kisi_id"])).grid(row=no,column=5,sticky=W)
           no+=1


def kisiGuncelle(id):

    global entryAdSoyadGuncelle,entryTelefonGuncelle

    pencereGuncelle=Toplevel(pencereListele)
    sorguKisiBilgisi=db.execute("select * from kisi where kisi_id="+str(id))
    kisi=sorguKisiBilgisi.fetchone()

    labelAdSoyadGuncelle = Label(pencereGuncelle, text="Ad ve Soyad")
    labelAdSoyadGuncelle.grid(row=0, column=0, sticky=W)

    entryAdSoyadGuncelle = Entry(pencereGuncelle,justify='left')
    entryAdSoyadGuncelle.grid(row=0, column=1, sticky=W)

    entryAdSoyadGuncelle.insert(END,kisi["kisi_adsoyad"])

    labelTelefonGuncelle = Label(pencereGuncelle, text="Telefon")
    labelTelefonGuncelle.grid(row=1, column=0, sticky=W)

    entryTelefonGuncelle = Entry(pencereGuncelle)
    entryTelefonGuncelle.grid(row=1, column=1, sticky=W)

    entryTelefonGuncelle.insert(END,kisi["kisi_telefon"])

    butonGuncelle = Button(pencereGuncelle, text="Guncelle", command=partial(kisiGuncelleIslem,kisi["kisi_id"]))
    butonGuncelle.grid(row=2, column=1, sticky=W)

def kisiGuncelleIslem(id):

    adSoyad=entryAdSoyadGuncelle.get()
    telefon=entryTelefonGuncelle.get()

    # print(adSoyad+" - "+telefon)
    try:
        db.execute("update kisi set %s=?,%s=? where %s=?"%("kisi_adsoyad","kisi_telefon","kisi_id"),(adSoyad,telefon,id))
        baglan.commit()
        hata=False
    except:
        hata=True


    # if db.rowcount>0:
    #     showinfo("başarılı","Kişi Güncellendi..")
    # else:
    #     showerror("başarısız","Kişi Güncellenemedi.")

    if hata==False:
        showinfo("başarılı","Kişi Güncellendi..")
    else:
        showerror("başarısız","Kişi Güncellenemedi..")

def kisiSil(id):

    try:
        db.execute("delete from kisi where %s=?"%("kisi_id"),(id,))
        baglan.commit()
        showinfo("başarılı","Kişi Silindi..")
    except:
        showerror("başarısız.","Kişi silinemedi..")

    pencereListele.destroy()
    kisileriListele()
pencere=Tk()
pencere.title("Adres Defteri")
pencere.geometry("200x100+100+200")

labelAdSoyad=Label(pencere,text="Ad ve Soyad")
labelAdSoyad.grid(row=0,column=0,sticky=W)
entryAdSoyad=Entry(pencere)
entryAdSoyad.grid(row=0,column=1,sticky=W)

labelTelefon=Label(pencere,text="Telefon")
labelTelefon.grid(row=1,column=0,sticky=W)
entryTelefon=Entry(pencere)
entryTelefon.grid(row=1,column=1,sticky=W)

butonEkle=Button(pencere,text="Ekle",command=kisiEkle)
butonEkle.grid(row=2,column=1,sticky=W)
butonListele=Button(pencere,text="Kişileri Listele",command=kisileriListele)
butonListele.grid(row=3,column=1,sticky=W)


pencere.mainloop()