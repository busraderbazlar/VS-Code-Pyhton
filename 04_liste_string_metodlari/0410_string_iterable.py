
# region string_iterable_giris
"""
ad = "BATUHAN"
print(ad[0])
meyveler = ["elma", "armut", "muz", "ayva", "üzüm", "elma"]
print(meyveler[1])
kurum = "ecodation"
print(kurum[3])
"""
# endregion

# region ornek
"""
ad = "BATUHAN"
print(ad[1])
print(len(ad))
if "U" in ad:
    print(f"{ad} ifadesinde U karakteri var")
meyveler = ["elma", "armut", "muz", "ayva", "üzüm", "elma"]
print(len(meyveler))
"""
# endregion

# region ismi_tersten_yazma_ornegi
"""
ad = "BATUHAN"
NAHUTAB
ad = "BATUHAN"
for i in range(len(ad)-1, -1, -1):
    print(ad[i], end= " ")
"""
# endregion

"""kurumAdi ="ecodatiton"
print(kurumAdi)
print(type(kurumAdi))
#print (list(kurumAdi)) str - iterable
print (kurumAdi[2])
for i in kurumAdi:
    print(i)"""

"""kurumAdi ="ecodation"
sesliHarfler = ["a", "e", "i ", " o ", "u","ü"]
ara = input ("aranan karakter:")
if ara in kurumAdi:
    print (f"{kurumAdi.count(ara)} adet bulundu")
else:
    print("karakter bulunamadı")"""

"""kurumAdi ="ecodation"
sesliHarfler = ["a", "e", "i ", " o ", "u","ü"]
for i in kurumAdi:
    if i in sesliHarfler:
        print(f"{i} sesli harfinden {kurumAdi.count(i)} var")"""

"""kurumAdi ="ecodation"
sesliHarfler = ["a", "e", "i ", " o ", "u","ü"]
yenListe = []
for i in kurumAdi:
    if i in sesliHarfler:
        yenListe.append(i)
yenListe.sort()
print(yenListe)"""

"""kurumAdi = "ecodation"
sesliHarfler = ["a", "e", "ı", "i", "o", "ö", "u", "ü"]
yeniListe = []
for i in kurumAdi:
    if i in sesliHarfler and not i in yeniListe:
        yeniListe.append(i)
print(yeniListe)"""
