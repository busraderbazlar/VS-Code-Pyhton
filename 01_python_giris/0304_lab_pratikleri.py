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
    i+=1

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
#region
i=0
sayi= int(input("Lütfen bir sayı giriniz\t:"))
sayi2= int(input("Lütfen bir sayı giriniz\t:"))
while i:
    if sayi<sayi2
    print(i)
    i+1
"""
"""
ad= input("Kullanıcı adı giriniz\t:")
sifre= int(input("Şifre giriniz\t:"))
while ad=="admin":
    if sifre == 123:
        print("Hoşgeldiniz")
print("Hatalı Giriş")
"""
"""
i, j = 0, 0
while i<10:
    while j<10:
        if i%2 ==0:
            print(" * ", end= "")
        else:
            print(" & ", end= "")
        j += 1
    i +=1
    j = 0
    print()
"""
"""
#1→  [1-99] arası tek sayıları yan yana yazdıralım
#2→  Her bir 10 adet sayıda alt satıra alalım
i = 1
s = 0
while i < 100:
    if s % 10 == 0:
        print()
    print(i, end=" ")
    s += 1
    i += 2
"""
"""
adet, toplam = 0, 0
sayi = int(input("lütfen sayı giriniz, çıkmak için 0 giriniz... : "))
while sayi != 0:
    toplam += sayi
    adet += 1
    sayi = int(input("lütfen sayı giriniz, çıkmak için 0 giriniz... : "))
print(f"girdiğiniz sayıların ortalaması → {toplam/adet}")

"""
"""
i=1
while i<=4:
    print("*"*i, end=" ",)
    i+=1

"""
"""
i=0
j=7
while i<4:
    while j<8:
        if j%2 !=0:
            print(1, end="")
        else:
            print(0, end="")
        j-=1
    i+=1
    j=7
    print()
"""

#region artanlarda ve time kütüphanesi kullanımı
"""
import time as t #time kütüphanesini ekle
i=1
while i<11:
    print(i, end=" ")
    i+=1

    t.sleep(1)#time kütüphanesinde 1 saniye yavaş print yazdır.
"""
#endregion
#region azalanlarda
"""
i=10
while i>1:
    print(i)
    i-=1
#endregion
#region \r kullanımı

import time as t
i = 1
while i<11:
   print(f"\r{i}", end=" ")#\r satırı soldan seç, sil ,bir daha print yap çıktı ver sıradakini.
   i += 1
   t.sleep(1)

"""
#endregion

#region pratikler
"""
gizliKelime=input("Lütfen gizli bir kelime giriniz\t :")
while gizliKelime!= "susam":
    print("hahaha ne oldu bilemedin ama =)")
    gizliKelime=input("Lütfen gizli bir kelime giriniz\t :")
print("Başardın!")


Sayı Giriniz : 5
5 x 1 = 5
5 x 2 = 10
5 X 3 = 15
5 X 4 = 40
5 X 5 = 25
"""
"""
sayi= int(input("Lütfen Bir sayı Giriniz\t:"))
i=1
while i<=sayi:
    print(f"{sayi} x {i} = {sayi*i}")
    i+=1
"""
"""
i=0
x=0
while i<100:
    if i%2==1:
        print(f"{i}", end=" ")
        x+=1
    if x>10:
        print()
        x=1
    i+=1
"""
"""

i=0
toplam=0
while i<100:
    if i%2==1:
        toplam+=i
    i+=1
print(f"{toplam}")
"""
"""
i=1
toplam=0
while i<6:
    i+=1
    sayi=int(input("Bir sayı giriniz\t:"))
    toplam+=sayi
print(f"{toplam}")
"""
#girilen 5 adet sayının çift olanlarını topla
"""
i=1
toplam=0
while i<6:
    i+=1
    sayi=int(input("Bir sayı giriniz\t:"))
    if sayi%2==0:
        toplam+=sayi
print(f"{toplam}")
"""
"""
i=1
toplam=0
while i<6:
    sayi=int(input("Bir sayı giriniz\t:"))
    if sayi%2==0:
        i+=1
        toplam+=sayi
print(f"{toplam}")
"""
"""
i=0
j=0
while i<5:
    while j<=i:
        j+=1
        print(" * ", end=" ")
    i+=1
    j=0
    print()

"""
"""
* * * * * 
* * * * 
* * * 
* * 
*
"""
"""
i=0
j=5
while i<5:
    while j>0:
        j-=1
        print(" * ", end=" ")
    i+=1
    j=5-i
    print()
"""
"""
i=0
j=5
while i<5:
    while j>i:
        j-=1
        print(" * ", end=" ")
    i+=1
    j=5
    print()
"""
"""
i=0
j=0
b=0
while i<5:
    while j<5:
        if b<i:
            print("   ", end=" ")
        else:
            print(" * ", end=" ")
        j+=1
        b+=1
    i+=1
    j=0
    b=0
    print()
"""
"""
i=0
j=0
while i<10:
    while j<10:
        if i%2==0:
            print("*", end=" ")
        else:
            print("$", end=" ")
        j+=1
    i+=1
    j=0
    print()
"""
"""
i=0
j=0
while i<10:
    while j<10:
        if j%2==0:
            print("*", end=" ")
        else:
            print("$", end=" ")
        j+=1
    i+=1
    j=0
    print()
"""
"""
i = 0
j = 0
while i < 10:
    while j < 10:
        if i%2==1:
            if j%2==0:
                print(" # ", end=" ")
            else:
                print(" $ ", end=" ")
        else:
            if j%2==0:
                print(" $ ", end=" ")
            else:
                print(" # ", end=" ")
        j += 1 
    i += 1
    j = 0
    print ()

"""
"""
100-999
haneleri toplamı, hane sayısına eşit olanları ekrana yazalım
KOŞULU SAĞLAYAN SAYILAR:
102 (3 haneli, haneleri toplamı 3)
111 (3 haneli, haneleri toplamı 3)
120 (3 haneli, haneleri toplamı 3)
201 (3 haneli, haneleri toplamı 3)
210 (3 haneli, haneleri toplamı 3)
300 (3 haneli, haneleri toplamı 3)
i = 100
while i<1000:
    kalan = i % 10
    birler = kalan // 1
    kalan = i % 100
    onlar = kalan // 10
    kalan = i % 1000
    yuzler = kalan //100
    haneleriToplami = birler + onlar + yuzler
    if haneleriToplami == 3:
        print(f"{i} (3 haneli, haneleri toplamı 3)")
    i += 1
"""
#shift+delete tüm satırı silme
#ctrl+z

"""
sayi1=int(input("Lütfen Bir Sayı Giriniz\t:"))
sayi2=int(input("Lütfen Bir Sayı Giriniz\t:"))
i=0
if sayi1>sayi2:
    sayi1,sayi2=sayi2,sayi1
while sayi2>i:
        if i>sayi1:
            print(f"{i}",end=" ")
        i+=1
"""




"""
while sayi1>i :
    if sayi1<i:
        sayi1,i=i,sayi1
    elif sayi1<sayi2:
        sayi1,sayi2=sayi2,sayi1
    elif i<sayi2:
        i,sayi2=sayi2,i
    print(f"{i}")
    i+=1
"""





"""
while i :
    if sayi1<i:
        sayi1,i=i,sayi1
    elif sayi1<sayi2:
        sayi1,sayi2=sayi2,sayi1
    elif i<sayi2:
        i,sayi2=sayi2,i
        print(f"{sayi1}>{i}>{sayi2}")
    i+1
"""



"""
s1 = int(input("l. s1. giriniz : "))
s2 = int(input("l. s2. giriniz : "))
s3 = int(input("l. s3. giriniz : "))
if s1<s2:
    s1, s2 = s2, s1
if s1<s3:
    s1, s3 = s3, s1
if s2<s3:
    s2, s3 = s3, s2
print(f"{s1}>{s2}>{s3}")
"""

#endregion