#def myfunk(param1,param2,param3):
#    print("param1 = "+param1)
#    print("param2 = "+param2)
#    print("param3 = "+param3)
#myfunk("eda","nadire","cemile")
#myfunk(param2="eda",param3="nadire",param1="cemile")
#
x=2
def myfunc():
    global y
    y=x+1
    print(y)
myfunc()
print(y)
