# mantıksal operatörler → logical operatörler
# koşul ifadelerini birleştirmek için kullanılır
"""
1→ ve       and (İkisininde true olması gerekir)
2→ veya     or (Birinden birinin True olması yeter)
3→ değil    not (değilse ifadesi )
"""


# region and
"""
print(5 == 5 and 15 > 5)
print(5 == 5 and 15 < 5)
print(5 == 15 and 15 > 5)
print(5 == 15 and 15 < 15)
"""
# endregion


# region or
"""
print(5 == 5 or 15 > 5)
print(5 == 5 or 15 < 5)
print(5 == 15 or 15 > 5)
print(5 == 15 or 15 < 15)
"""
# endregion


# region not
"""
print(not 5 == 5)
print(5 != 5)
"""
# endregion

#region ornek_1
"""
a= int(input("Lütfen a değerini giriniz\t:"))
if a >0 and a<100:
        print(f("{a} 100 den küçük ve pozitiftir"))
"""
"""
ay=int(input("Lütfen ay bilgisi alalım\t:"))
if ay>36 and ay<68:
    print("Okula Gidebilir")
else:
    print("Okula Gidemez")
"""
"""
kilo= int(input("Lütfen kilo bilgisi giriniz\t:"))
boy= float(input("Lğtfen boy bilgisi giriniz\t:"))
vki=kilo/boy**2
if vki<18.49:
    print("İdeal Kilonun altındasınız")
elif vki>18.50 and vki<24.99:
    print("ideal Kilodasınız")
elif vki>25 and vki<29.99:
    print("İdeal kilonun üzerindesiniz")
elif vki>30:
    print("İdeal kilonun çok üzerindesiniz")

#Ödev: İdeal kiloda olmayanlara öneri verilsin.
"""
"""
for i in range(2,19+1):
    for j in range (2,i):
        if i%j ==0:
            print(f"{i} asal değil")
            break
    else:
        print(f"{i} sayı asaldır")

s=int(input("Sayı giriniz:"))
for i in range(2,s+1):
    for j in range (2,i):
        if i%j ==0:
            print(f"{i} asal değil")
            break
    else:
        print(f"{i} sayı asaldır")

for i in range(2, 19+1):
    for j in range(2, i):
        if i % j == 0:
            print(f"{i} asal değil")
            break
        else:
            print(f"{i} sayı asaldır")
            break
"""