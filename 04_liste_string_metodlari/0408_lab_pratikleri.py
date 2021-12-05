"""# region siralama
# orjinal liste     9, 7, 5, 1, 3, 4, 2, 6, 8
# 1. Sıralamada     7, 5, 1, 3, 4, 2, 6, 8, 9
# 2. Sıralamada     5, 1, 3, 4, 2, 6, 7, 8, 9
# 3. Sıralamada     1, 3, 4, 2, 5, 6, 7, 8, 9
# ...
"""
"""
listem = [9, 7, 5, 1, 3, 4, 2, 6, 8]
while True:
    siraliMi = True
    for i in range(len(listem)-1):
        if listem[i]>listem[i+1]:
            listem[i], listem[i+1]= listem[i+1], listem[i]
            siraliMi = False
    if siraliMi:
        break
print(listem)
# endregion"""

dersListesi = []
print("""
    Çıkış [0]
    Ekle [1]
    Sil [2]
    Listele [3]
""")

while True:
    secim = int(input("lütfen menüden seçim yapınız? \t: "))
    if secim == 0:
        break
    elif secim == 1:
        eklenecekDers = input("lütfen eklenecek dersi giriniz : ")
        varMi = dersListesi.count(eklenecekDers)
        if varMi==0:
            dersListesi.append(eklenecekDers)
        else:
            print("Ders Zaten Listede Vardır!!!")
    elif secim == 2:
        silinecekDers = input("lütfen silinecek dersi giriniz : ")
        varMi = dersListesi.count(silinecekDers)
        if varMi==0:
            print("böyle bir ders yok")
            continue
        dersListesi.remove(silinecekDers)
        print(f"{silinecekDers} dersi silindi!")
    elif secim == 3:
        if len(dersListesi)==0:
            print("ders listesi boş")
            continue
        print("Derslerimiz")
        print("-"*25)
        for i in dersListesi:
            print(i)
    else:
        print("lütfen geçerli seçim yapın")




# ödev →
"""
Lütfen Bir Sayı Giriniz: 183
Yüz Seksen Üç
"""


# ödev →
"""
ecodation
1 adet e
2 adet o
1 adet a
1 adet i
"""