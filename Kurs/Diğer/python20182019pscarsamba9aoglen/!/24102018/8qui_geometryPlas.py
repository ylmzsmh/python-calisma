from  tkinter import*

pencere=Tk()

giris=Entry()
giris.place(relx=0.0,rely=0.0,relheight=0.15)

dugme1=Button(text="Düğme1")
dugme1.place(relx=0.5,rely=0.0,relheight=0.15)

dugme2=Button(text="Düğme2")
dugme2.place(relx=0.0,rely=0.2,relwidth=1,relheight=0.5)

giris2=Entry()
giris2.place(relx=0.0,rely=0.35)



pencere.mainloop()