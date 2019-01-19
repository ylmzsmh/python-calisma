from tkinter import*
import sympy
x,y=sympy.Symbol("x"),sympy.Symbol("y")
ifade=""

def fonk(deger):
    global ifade
    ifade = ifade + str(deger)

    esitlik.set(ifade)


def sil():
    global ifade
    ifade = ""
    esitlik.set("")


def integ():
    global ifade
    for i in ifade:
        ifade=i[0]
        a=i[4]
        b=i[5]
        deg=i[3]
        sonuc = sympy.integrate(ifade, (deg, a, b))
        esitlik.set(sonuc)
        ifade=""
        break
        # ifade = ""
        # esitlik.set()


def teksilme():
    global ifade
    ifade = ekran.get()[:-1]
    ekran.delete(0, END)
    ekran.insert(0, ifade)


def teksilme():
    global ifade
    ifade = ekran.get()[:-1]
    ekran.delete(0, END)
    ekran.insert(0, ifade)


def esittir():

    global ifade
    try:

        sonuc = eval(ifade)

        esitlik.set(sonuc)
        ifade = ''
    except:

        esitlik.set(" hatalı işlem ")
        ifade = ""
    else:


        sonuc = sympy.integrate(ifade)
        esitlik.set(sonuc)
        ifade = ""
if __name__ == "__main__":
    pencere = Tk()
    esitlik = StringVar()
    pencere.configure(background="white")

    pencere.geometry("200x200")
    ekran = Entry(pencere, textvariable=esitlik)

    ekran.grid(columnspan=6, ipady=10, ipadx=40)

    esitlik.set("Değer Giriniz: ")

    button1 = Button(pencere, text=' 1 ', fg='black', bg='#97aba9', command=lambda: fonk(1)
                         , width=3)

    button1.grid(row=2, column=0, sticky=S + E + W + N)

    button2 = Button(pencere, text=' 2 ', fg='black', bg='#97aba9', command=lambda: fonk(2)
                         , width=3)

    button2.grid(row=2, column=1, sticky=E + W + N + S)
    button3 = Button(pencere, text=' 3 ', fg='black', bg='#97aba9', command=lambda: fonk(3)
                         , width=3)

    button3.grid(row=2, column=2, sticky=E + W + N + S)

    button4 = Button(pencere, text=' 4 ', fg='black', bg='#97aba9', command=lambda: fonk(4)
                         , width=3)

    button4.grid(row=3, column=0, sticky=E + W + N + S)

    button5 = Button(pencere, text=' 5 ', fg='black', bg='#97aba9', command=lambda: fonk(5)
                         , width=3)

    button5.grid(row=3, column=1, sticky=E + W + N + S)
    button6 = Button(pencere, text=' 6 ', fg='black', bg='#97aba9', command=lambda: fonk(6)
                         , width=3)

    button6.grid(row=3, column=2, sticky=E + W + N + S)

    button7 = Button(pencere, text=' 7 ', fg='black', bg='#97aba9', command=lambda: fonk(7)
                         , width=3)

    button7.grid(row=4, column=0, sticky=E + W + N + S)

    button8 = Button(pencere, text=' 8 ', fg='black', bg='#97aba9', command=lambda: fonk(8)
                         , width=3)

    button8.grid(row=4, column=1, sticky=E + W + N + S)

    button9 = Button(pencere, text=' 9 ', fg='black', bg='#97aba9', command=lambda: fonk(9)
                         , width=3)

    button9.grid(row=4, column=2, sticky=E + W + N + S)

    button0 = Button(pencere, text=' 0 ', fg='black', bg='#97aba9', command=lambda: fonk(0)
                         , width=3)

    button0.grid(row=5, column=1, sticky=E + W + N + S)
    Button(pencere, text="(", width=3, fg='black', bg='#97aba9', command=lambda: fonk('(')).grid(row=2, column=3,
                                                                                                     sticky=E + W + N + S)
    Button(pencere, text=")", width=3, fg='black', bg='#97aba9', command=lambda: fonk(')')).grid(row=3, column=3,
                                                                                                     sticky=E + W + N + S)

    plus = Button(pencere, text=' + ', fg='black', bg='#97aba9', command=lambda: fonk("+"), width=3).grid(row=4,
                                                                                                              column=4,
                                                                                                              sticky=E + W + N + S)

    minus = Button(pencere, text=' - ', fg='black', bg='#97aba9', command=lambda: fonk("-")
                       , width=3)

    minus.grid(row=5, column=4, sticky=E + W + N + S)

    multiply = Button(pencere, text=' * ', fg='black', bg='#97aba9', command=lambda: fonk("*")
                          , width=3)

    multiply.grid(row=4, column=3, sticky=E + W + N + S)

    divide = Button(pencere, text=' / ', fg='black', bg='#97aba9', command=lambda: fonk("/")
                        , width=3)

    divide.grid(row=6, column=3, sticky=E + W + N + S)

    equal = Button(pencere, text=' = ', fg='black', bg='#97aba9', command=esittir
                       , width=4)

    equal.grid(row=5, column=2, columnspan=2, sticky=E + W + N + S)
    karekok = Button(pencere, text=' √ ', fg='black', bg='#97aba9', command=lambda: fonk("**(1/2)")
                         , width=3)

    karekok.grid(row=6, column=2, sticky=E + W + N + S)
    kare = Button(pencere, text=' x² ', fg='black', bg='#97aba9', command=lambda: fonk("**2")
                      , width=3)

    kare.grid(row=6, column=4, sticky=E + W + N + S)
    sil = Button(pencere, text=' tamsil', fg='black', bg='#97aba9', command=sil
                     , width=3)

    sil.grid(row=3, column=4, sticky=E + W + N + S)
    teksil = Button(pencere, text='sil', fg='black', bg='#97aba9', command=teksilme
                        , width=3)

    teksil.grid(row=2, column=4, sticky=E + W + N + S)
    nokta = Button(pencere, text=' . ', fg='black', bg='#97aba9', command=lambda: fonk("."), width=3)

    nokta.grid(row=5, column=0, sticky=E + W + N + S)
    # ekbutton = Button(pencere, text=' Diğer işlemler ', fg='black', bg='#97aba9', width=10, command=denklem)

    # ekbutton.grid(row=6, column=0, columnspan=2, sticky=E + W + N + S)
    xbut = Button(pencere, text=' x ', fg='black', bg='#97aba9', command=lambda: fonk(x), width=3)

    xbut.grid(row=7, column=0, sticky=E + W + N + S)
    ybut = Button(pencere, text=' y ', fg='black', bg='#97aba9', command=lambda: fonk(y), width=3)

    ybut.grid(row=7, column=1, sticky=E + W + N + S)
    # zbut = Button(pencere, text=' z ', fg='black', bg='#97aba9', command=lambda: fonk(z), width=3)

    # zbut.grid(row=7, column=2, sticky=E + W + N + S)
    virgul = Button(pencere, text=' , ', fg='black', bg='#97aba9', command=lambda: fonk(","), width=3)

    virgul.grid(row=7, column=3, sticky=E + W + N + S)
    # integral = Button(pencere, text=' ∫ ', fg='black', bg='#97aba9', command=integ, width=3)

    # integral.grid(row=7, column=4, sticky=E + W + N + S)
    pencere.mainloop()


