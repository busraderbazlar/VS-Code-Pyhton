# region break_continue_neden_kullanilir
"""
break     → döngüyü sonlandırır #beklenmedik bir hata olduğunda döngüyü kırmak için, aradığın bir şeyi bulduğun zaman aradığını devam etmemek kırmak için kullanılır.
continue  → tepeye geri döndürecek
"""
# endregion


#region ornek_1 break
"""
i=1
x= int(input("Aradığınız stok id: "))
while i<10:
    print(i, end=" ")
    if i==x:
        break
    i+=1
"""
#endregion

#region ornek_2 break

"""i=1
x= int(input("Aradığınız stok id: "))
print("b")
while i<10:
    print("b", end=" ")
    if i==2:
        break
    i+=1
print("c")"""

#endregion


#region ornek_3
"""
i=1
x= int(input("Aradığınız stok id: "))
while i<10:
    if i==x:
        i+=1
        continue
    print(i, end=" ")
    i+=1
"""
#endregion

#region ornek_4_continue
"""
i = 1
print("a")
while i<11:
    if i==15:
        print("b")
        break
    print(f"{i}. döngü")
    i += 1
print("c")
"""
"""
i = 1
print("a")
while i < 100:
    if i % 7 == 0:
        i += 1
        continue
    elif i % 15 == 0:
        break
    print(f"{i}. döngüdeyim")
    i += 1
print("b")
"""
#endregion

""""""
"""eb,say=0,0
while True:
    sayi = int(input("Lütfen bir sayı giriniz, çıkmak için - 1'e basınız\t:"))
    if sayi == -1:
        break
    say +=1
    if sayi>eb:
        eb=sayi
if say:
    print(f"Girdiğiniz en büyük sayı {eb}")
else:
    print("Hiç bir sayı girmediniz")"""


#region pratik_1
"""tekSayilarToplami=0
while True:
    a=int(input("Lütfen bir sayı giriniz,çıkmak için -1 basınız\t: "))
    if a==-1:
        break
    if a%2==0:
        print("Lütfen tek sayı giriniz\t:")
    else:
        tekSayilarToplami+=a
print(f"Listedeki tek sayıların toplamı {tekSayilarToplami}")"""
#endregion

#region pratik_2
"""while True:
    secim=int(input(
    [1] km-mil
    [2] mil-km
    [3] çık
        "))
    if secim ==1:
        km = float(input("Lütfen km bilgisi giriniz \t:"))
        mil = km*0.622137
        print(f"girilen {km} değerinin mil hesaplaması {mil}")
    elif secim ==2:
        mil = float(input("Lütfen mil bilgisi giriniz \t:"))
        km = mil*0.622137
        print(f"girilen {mil} değerinin km hesaplaması {km}")
    elif secim ==3:
        break
    else:
        print("hatalı seçim")"""
#endregion
