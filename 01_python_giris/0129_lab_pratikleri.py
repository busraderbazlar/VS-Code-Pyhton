
print("""
    Leylek Uygulamasına Hoş Geldiniz!!!
    Sürüş Ücreti → 0.59/dk
""")
"""
s = int(input("sürüş için geçen süre (saat)\t : "))
d = int(input("sürüş için geçen süre (dakika)\t : "))
toplamDakika = s*60
toplamDakika += d
toplamTutar = 0.59 * toplamDakika
print(f"Sürüş için geçen süre (saat)\t: {s}")
print(f"Sürüş için geçen süre (dakika)\t: {d}")
print(f"sürüşün toplam süresi {s}:{d} - {toplamDakika} dakika da bitmiştir")
print(f"kartınızdan çekilen toplam tutar {round(toplamTutar,2)}")
"""
#region ödev1
"""
km = int(input("Km bilginizi giriniz\t :"))
mil = km/1.609344
print(f"{km} km, {mil} mil'e eşittir.")
"""
#endregion 

#region ödev2
"""
kenar1 = int(input("Lütfen Üçgenin A Kenarı Açısını Giriniz\t :"))
kenar2 = int(input("Lütfen Üçgenin B Kenarı Açısını Giriniz\t :"))
kenar3 = 180-(kenar1+kenar2)
print(f"C Kenarı {kenar3} Derecedir.")
"""
#endregion

#region ödev3
"""
deger1= int(input("X1 Değerini Giriniz\t :"))
deger2= int(input("X2 Değerini Giriniz\t :"))
deger3= int(input("Y1 Değerini Giriniz\t :"))
deger4= int(input("Y2 Değerini Giriniz\t :"))
uzaklik= ((((deger1-deger2)*2)+(deger3-deger4)*2)**1/2)
print(f"(x1,x2) ve (y1,y2) noktaları arasındaki uzaklık {uzaklik} birimdir")
"""
#endregion

#region ödev4
"""
at= int(input("Aylık Tüketim Giriniz [khw]\t : "))
aeb= at*0.39736
db = aeb*0.2475
teb= aeb+db
tp= 3.97
ef= 1.39
etv= 9.92
kdv=((teb+tp+ef+etv)*0.18)
vt= tp+ef+etv+kdv
toplamFatura= vt+teb
print(f"Elektrik faturanız {round(toplamFatura)} TL\'dir.")
"""
#endregion


#region ödev5
"""
endex= float(input("Güncel Benzin Endeksini Giriniz\t :"))
yakit= float(input("Yakıt Tüketimini Giriniz [100 km. başına]\t :"))
km = int(input("Kaç Kilometre Yol Aldığınızı Giriniz\t :"))
toplamYakit= ((km*yakit)/100)*endex
print(f"Toplam Yakıt Tüketimi {toplamYakit}")
"""
#endregion

#region ödev6
ürün= input("Lütfen Ürün Adı Giriniz\t :")
adet= int(input("Satın Alınacak Adeti Giriniz\t :"))
fiyat= float(input("Lütfen Ürün Fiyatı Giriniz [KDV-Dahil]\t :"))
indirim= int(input("Lütfen İndirim Oranını Giriniz [%]\t :"))
toplam= (fiyat-((fiyat*indirim)/100))*adet
print(f"Ürünlerin Toplam Tutarı {toplam} Tl.")
#endregion








