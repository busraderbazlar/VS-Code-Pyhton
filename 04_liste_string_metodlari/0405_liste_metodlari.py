"""notlar=[10,55,90,77,85,45,77]
ek=101
for i in notlar:
    if i<ek:
        ek=i
print(ek)
print(min(notlar))"""

#kısa yol toplam = sum()
#kısa yol minimum = min()

#append
"""derslerim = ["programlama", "seriler", "DA"]
#listeye yeni bir eleman eklemek için append kullanılır. Otomatik sona eklenir.
derslerim.append("Jscript")
for ders in derslerim:
    print(ders)"""
#insert
"""derslerim.insert(3,"Jscript") #insert ile yeni eleman 3.sıraya eklenmiş olur(eklenme yeri,eklenilen şey)
for ders in derslerim:
    print(ders)"""

#remove
"""meyveler = ["elma", "armut", "muz", "ayva", "üzüm"]
print(f"listemizin ilk hali → {meyveler}")
# meyveler.remove("muz")
meyveler.remove("muzz")
print(f"listemizin son hali → {meyveler}")"""

#pop
"""meyveler = ["elma", "armut", "muz", "ayva", "üzüm"]
print(f"listemizin ilk hali → {meyveler}")
#print(meyveler.pop()) son elemanı
print(meyveler.pop(2)) #o indeksli elemanı siler #pop parametresiz kullanabilir. Kullanıldığında son elemanı siler. 
print(f"listemizin son hali → {meyveler}")
sebzeler = []
sebzeler.pop() #kod sonunda şunu söyler ben şu elemenı sildim."""

"""ogrenciler = ["buse", "büşra", "ömer", "kaçak", "ender", "selin"]
print(ogrenciler.pop(2))
for i in ogrenciler:
    print(i)"""

# region clear→listeyi_temizler
"""
meyveler = ["elma", "armut", "muz", "ayva", "üzüm"]
print(f"listemizin ilk hali → {meyveler}")
meyveler.clear()
print(meyveler)
del meyveler #tamamen siler
print(f"listemizin son hali → {meyveler}")
"""
#endregion

# region copy→listeyi_kopyalar
"""
meyveler = ["elma", "armut", "muz", "ayva", "üzüm"]
print(f"listemizin ilk hali → {meyveler}")
meyveTabagi = meyveler.copy()
print(f"listemizin son hali → {meyveTabagi}")
"""
# endregion

# region count→elaman_sayisi
"""
listeRakamlar = [2, 5, 6, 1, 9, 7, 5, 9]
arananEleman = 9
elemanAdedi = listeRakamlar.count(arananEleman)
print(f"listemizdeki {arananEleman} elemanı adedi→ {elemanAdedi}")
meyveler = ["elma", "armut", "muz", "ayva", "muz", "üzüm"]
print(meyveler.count("muzz")) #bulunmadığında kızmaz. Count saymak için kullanılır raramak içinde kullanılabilir.
"""
# endregion

# region ornek_1
"""
meyveler = ["elma", "armut", "muz", "ayva", "üzüm"] 
arananMeyve = input("aramak istediğiniz meyve? : ")
elemanAdedi = meyveler.count(arananMeyve)
if elemanAdedi:   # elemanAdedi!=0
    print(f"aradığınız {arananMeyve} listede yer almaktadır.")
else:
    print(f"Aradığınız {arananMeyve} listede yer almamaktadır.")
"""
# endregion

# region sort_reverse→sirala_tersten_sirala
"""
listeRakamlar = [2, 5, 6, 1, 4, 9, 3, 8, 7]
print(f"listemizin ilk hali → {listeRakamlar}")
listeRakamlar.sort()#içini hiç bir şey yapmağında artarak yazar. sor()=(reverse=False)
print(f"listemizin son hali → {listeRakamlar}")
listeRakamlar.reverse() #reverse()=(reverse=True)
print(f"listemizin son hali → {listeRakamlar}")
"""
# endregion

# region index→arama_indeks_dondurme
"""
listeRakamlar = [2, 5, 6, 1, 9, 7]
print(listeRakamlar.index(10)) #index aramak için kullanılır counttan farkı count kaç adet olduğunu sayar. Indexte ilk bulduğunu sayar birden fazla olursa.
kaciciIndex =miniMiniBirler.index("ömer",1,4) #başlangı. bitişde aranabilir.
"""
# endregion
