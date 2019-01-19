from tkinter import*

pencere=Tk()

yeniFrame=Frame()
yeniFrame.pack(side=BOTTOM)

uyariLabel=Label(pencere,text="Eminmisin lööö")
uyariLabel.pack()

evetButton=Button(yeniFrame,text="Evet",command=pencere.quit)
evetButton.pack(side=LEFT)

hayirButton=Button(yeniFrame,text="Hayır",command=pencere.quit)
hayirButton.pack(side=RIGHT)

pencere.mainloop()