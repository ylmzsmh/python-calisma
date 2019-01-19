from tkinter import *


pencere=Tk()

yeniFrame=Frame()
yeniFrame.pack(side=BOTTOM)




dugme1=Button(yeniFrame,text="ürünler",width=8,height=2,padx=1,pady=2)
dugme1.grid(row=0,column=0)

# label=Label(text="\t")
# label.grid(row=0,column=1)

dugme2=Button(yeniFrame,text="Hizmetler", width=8,height=2,padx=1,pady=2)
dugme2.grid(row=0,column=2)

dugme3=Button(yeniFrame,text="Hakkımda",width=8,height=2,padx=1,pady=2)
dugme3.grid(row=1,column=0)

dugme4=Button(yeniFrame,text="Ulaşım",width=8,height=2,padx=1,pady=2)
dugme4.grid(row=1,column=2)

pencere.mainloop()