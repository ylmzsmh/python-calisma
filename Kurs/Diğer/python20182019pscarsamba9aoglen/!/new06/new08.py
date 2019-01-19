tekrar =0
s3=0.0
s1=input("Lütfen toplanacak sayıyı giriniz :")
s1=float(s1)
s4=s1
# s3=s1
s2=input("Lütfen tekrar sayısını giriniz :")
s2=int(s2)
while tekrar < s2:
    s1 = s3+s1
    tekrar +=1
    s3=s1
    print(tekrar,s1)
# 5
# if tekrar==s2:
 #   print("sonuc: ",s1,s2)