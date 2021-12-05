"""ogrenci1 = ["Alp", "Besi", 90,	90]
ogrenci2 = ["Batu", "Koçhan", 10, 90]
ogrenci3 = ["Emir", "Besi", 100,	90]
ogrenci4 = ["Umut", "Ahmet", 95, 80]
ogrenci5 = ["Aziz", "Bektaş", 15, 10]
ogrenciler = [ogrenci1, ogrenci2, ogrenci3, ogrenci4, ogrenci5]

for i in ogrenciler:
    print(f"{i[0]} adlı {i[0][1]} soyadlı öğrencinin  notları {i[2]} ve {i[2]}'dir.")


for i in ogrenciler:
    ort = i[1]+[3]/2
    if ort < 50:
        print(f"{i[0]} adlı {i[0][1]} soyadlı öğrencinin  notları {i[2]} ve {i[3]}'dir. Kaldı.")
    else:
        print(f"{i[0]} adlı {i[0][1]} soyadlı öğrencinin  notları {i[2]} ve {i[3]}'dir.Geçti.")

"""

"""liste = [["piyon" for j in range (8)] for i in range (8)]
yeniListe = [[ for j in range] for i in range ] #j içerdeki döngü i dışardaki döngü
"""

"""yeniListe =[[i*j for j in range (1,9)] for i in range (1,9)]
print(yeniListe)"""

import random
"""
x= random.randrange(30,40)
print(x)
"""
"""haftaninKacinciGunu = int(input("Hangi Gün [1...7]:"))
liste = [[ random.randrange(30,40) for j in range (24)] for i in range (7)]
for sicaklik in liste:
    print (sicaklik[haftaninKacinciGunu-1], end=" ")"""


"""liste = [[random.randrange(30,40) for j in range(24)] for i in range(7)]
gununHangiSaati = int(input("Hangi Gün [0..24] "))
yeniSicaklik = []
for sicaklik in liste:
    yeniSicaklik.append(sicaklik[gununHangiSaati])
print(f"tüm haftada {gununHangiSaati} saatteki ortalama sıcaklık {sum(yeniSicaklik)/len(yeniSicaklik)} ")
"""