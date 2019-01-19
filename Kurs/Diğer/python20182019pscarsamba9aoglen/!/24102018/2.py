# pack

# expand(yes,no)
#
# fill(x,y,both)
#
# side=(top,bottom,left,rigt)
# >hepsi büyük harf olacak

from tkinter import*

root=Tk()
root.geometry("200x300+500+100")

lira=Label(root,text="Lira",fg="white",bg="blue",font="verdana 13 bold")
lira.pack(expand=YES,fill=Y)

euro=Label(root,text="Euro",fg="white",bg="blue",font="verdana 13 bold")
euro.pack(expand=YES,fill=Y)

dolar=Label(root,text="Dolar",fg="white",bg="blue",font="verdana 13 bold")
dolar.pack(expand=YES,fill=Y)

root.mainloop()