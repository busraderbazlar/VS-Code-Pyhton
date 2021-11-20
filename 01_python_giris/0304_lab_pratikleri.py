"""
a= input("Metin giriniz:")
x=0
while x<5:
    print(a)
    x+=1
"""
"""
a=input("Metin Giriniz:")
x=0
i = int(input("Kaç kez tekrar etmeli"))
while x<i:
    print(a)
    x+=1
"""
"""
i=0
j=0
while i <1:
    while j<10:
        j+=1
    i+=1
    j=0
    print()

"""
"""
#* * * * * * * * * *  
i=1
while i<=10:
    i+=1
    print("*", end=" " )
"""
"""
i=0
while i<10:
    i+=1
    if i%2 ==0:
        print("$", end=" ")
    else:
        print("*", end=" ")
"""
"""
#* * * * * * * * * *  
i=1
while i<=10:
    i+=1
    print("*", end=" " )
"""
"""
i=1
j=1
while i<=10:
    while j<=10:
        print(f"{i}.K {j}.Oda'dır.", end=("") )
        j+=1
    i+=1
    j=1
    print()

"""

# region ornek_6
"""
#1.  [1-99] arası tek sayıların toplamını yazdıralım
i = 1
toplam = 0
while i < 100:
    toplam += i
    i += 2
print(f"[1-99] arası tek sayıların toplamı → {toplam}")
"""
# endregion

# region ornek_7
"""
Lütfen Sayı Giriniz:    5
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
...
i = 1
sayi = int(input("Lütfen Sayı Giriniz: "))
while i <= 10:
    print(f"{sayi } x {i} = {sayi*i}")
    i += 1
"""
# endregion
"""
gizliKelime=input("Lütfen gizli bir kelime giriniz\t :")
while gizliKelime!= "susam":
    print("hahaha ne oldu bilemedin ama =)")
    gizliKelime=input("Lütfen gizli bir kelime giriniz\t :")
print("Başardın!")
"""
#endregion

#region
"""
sayi=int(input("Lütfen bir sayı giriniz, 0 girildiğinde çıkış yapılacaktır\t:"))
adet,toplam= 0,0
while sayi!=0:
    toplam+=sayi
    adet+=1
    sayi=int(input("Lütfen bir sayı giriniz, 0 girildiğinde çıkış yapılacaktır\t:"))
print(f"girdiğiniz sayıların ortalaması → {toplam/adet}")
"""
#endregion

#region odev_1
"""
rakam=int(input("Lütfen [1-9] arası bir rakam giriniz\t:"))
i=1
while i<6:
    print(f"{rakam * i}", end=" ")
    i+=1
"""
#endregion

"""
sayi= int(input("Lütfen bir sayı giriniz\t:"))
i=0
while i<sayi:
    if i%5 == 0 and i %7 != 0:
        print(i)
    i4+=1

"""
"""
sayi= int(input("Lütfen bir sayı giriniz\t:"))
i=0
adet=0
while i<sayi:
    if i%5 ==0 and i%3 == 0:
        adet+=1
    i+=1
print(adet)

"""
"""
!#region
i=0
sayi= int(input("Lütfen bir sayı giriniz\t:"))
sayi2= int(input("Lütfen bir sayı giriniz\t:"))
while sayi<i<sayi2:
    print(i)
    i+1
!"""
"""
ad= input("Kullanıcı adı giriniz\t:")
sifre= int(input("Şifre giriniz\t:"))
while ad=="admin":
    if sifre == 123:
        print("Hoşgeldiniz")
print("Hatalı Giriş")
"""




