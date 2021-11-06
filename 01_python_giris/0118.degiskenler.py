#region degisken_isimlendirme_kurallari
"""
Değişken İsimlendirme Kuralları
1- harf veya alt çizgi ile başlamalıdır
2- rakam ile başlayamaz
3- ilk harf dışındakiler, harf, sayı, alt çizgi olabilir
4- alt çizgi dışında alfa sayısal karakterlerimiz (%, #, $...) kullanılamaz
5- case sensitive
6- anahtar kelimeler if, pass, while, def bunlar kullanılamaz
7- türkçe karakter kullanmamaya özen gösterelim
"""
#endregion
"""
name= "John"
surname= "Mercedes"
age= 45

print(name)
print(surname)
print(name, surname, age)
okulNo = "1065"
ad = "Ender"
soyad = "Barış"

print(ad, soyad, okulNo)
#deverostasyonu camelcasing birdenfazlakelimevarsadeğişkendeilkkelime sonrası büyükharflebaşlarkelimeler
"""

okul_no = "1065"
ad = "Ender"
soyad = "Barış"

print(ad, soyad, okul_no)
#birdenfazlakelime varsa kelilemeler arası alt tre yani alt çizgi
# underscorecasing 
#ingilizce kelime ve harf içermeli

_1nciOgrenci = "Buse"
print(_1nciOgrenci)
#başlangıç sayı olamaz alt çizgi olabilir

plaka_35 = "İzmir"
print(plaka_35)

import keyword
print(keyword.kwlist)
#keywordlar bu şekilde tanımlanır ve değişken olarak kullanılamaz.

