# region min_max→minimum_maksimum_degeri_dondurme
"""
listeRakamlar = [2, 5, 6, 1, 9, 7]
print(f"listenin en küçük değeri {min(listeRakamlar)}")
print(f"listenin en küçük değeri {max(listeRakamlar)}")
print(min(3, 9))
"""
"""
x= int(input("Lütfen Başlangıç değeri giriniz:"))
y= int(input("Lütfen Bitiş değeri giriniz:"))
for i in range (min(x,y), max(x,y)+1):
    print(i)"""

#manuel olarakta algoritma yazabiliriz
"""
listeRakamlar = [2, 5, 6, 1, 9, 7]
eb = 0
for i in listeRakamlar:
    if i > eb:
        eb = i
print(eb)
"""
# endregion