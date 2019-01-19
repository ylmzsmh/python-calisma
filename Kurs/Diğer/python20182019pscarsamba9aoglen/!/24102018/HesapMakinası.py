from tkinter import *


pencere=Tk()

yeniFrame=Frame()
yeniFrame.pack(side=BOTTOM)


pencere=("200x500+500+100")

dugme1=Button(yeniFrame,text="Toplama",width=8,height=2,padx=1,pady=2)
dugme1.grid(row=0,column=0)

# label=Label(text="\t")
# label.grid(row=0,column=1)

dugme2=Button(yeniFrame,text="Çıkarma", width=8,height=2,padx=1,pady=2)
dugme2.grid(row=0,column=2)

dugme3=Button(yeniFrame,text="Çıkarma", width=8,height=2,padx=1,pady=2)
dugme3.grid(row=0,column=2)

dugme4=Button(yeniFrame,text="Çıkarma", width=8,height=2,padx=1,pady=2)
dugme4.grid(row=0,column=2)

dugme5=Button(yeniFrame,text="Çıkarma", width=8,height=2,padx=1,pady=2)
dugme5.grid(row=0,column=2)


dugme6=Button(yeniFrame,text="Hakkımda",width=8,height=2,padx=1,pady=2)
dugme6.grid(row=1,column=0)

dugme7=Button(yeniFrame,text="Ulaşım",width=8,height=2,padx=1,pady=2)
dugme7.grid(row=1,column=2)

pencere.mainloop()