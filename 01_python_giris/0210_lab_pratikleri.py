#region ornek_1
"""
n1, n2 = int(input("lütfen 1. snv notunu giriniz \t : ")), int(input("lütfen 2. snv notunu giriniz \t : "))
ort = (n1+n2)/2
if ort>=85:
    print(f"yıl sonu notunuz {ort}, başarı durumu PEKİYİ")
elif ort>=70:
    print(f"yıl sonu notunuz {ort}, başarı durumu İYİ")
elif ort>=55:
    print(f"yıl sonu notunuz {ort}, başarı durumu ORTA")
elif ort>=45:
    print(f"yıl sonu notunuz {ort}, başarı durumu GEÇER")
else:
    print(f"yıl sonu notunuz {ort}, başarı durumu GEÇEMEZ")
"""
#endregion

#region ornek_2
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

#region ornek_3
"""
a = int(input("lütfen a kenarını giriniz \t : "))
b = int(input("lütfen b kenarını giriniz \t : "))
if a==b:
    print(f"karenin alanı {a*b}")
else:
    print(f"dikdörtgenin alanı {a*b}")
"""
#endregion

#region ornek_4
"""
kisaKenar = int(input("lütfen kısa kenarını giriniz \t : "))
uzunKenar = int(input("lütfen uzun kenarını giriniz \t : "))
if kisaKenar>uzunKenar:
    print("kısa kenar uzun girilemez")
else:
    print(f"dörtgenin çevresi {2*(kisaKenar + uzunKenar)}")
"""
#endregion

#region ornek_5
"""
a = int(input("lütfen 1. s giriniz \t : "))
b = int(input("lütfen 2. s giriniz \t : "))
if a%b==0:
    print(f"{a} sayısı {b} sayısına tam bölünür")
else:
    print(f"{a} sayısı {b} sayısına tam bölünemez")
"""
#endregion






#region odev_1
"""
sayi= int(input("Lütfen bir sayı giriniz\t: "))
if sayi > 0 :
    sayi**=2
    print(f"Sonuç {sayi} ")
elif sayi < 0:
    sayi**=0.5
    print(f"Sonuç {sayi} ")
else :
    sayi=0
    print(f"Sonuç {sayi} ")
"""
#endregion

#region odev_2
"""
fiyat1= int(input("Lütfen 1.ürünün fiyat bilgisini giriniz\t: "))
fiyat2= int(input("Lütfen 2.ürünün fiyat bilgisini giriniz\t: "))
ödenecekTutar= fiyat1+fiyat2
indirim=0
borc=fiyat1+fiyat2-indirim
if ödenecekTutar > 200 :
    indirim=fiyat2*0.25
    borc=fiyat1+fiyat2-indirim
    print(f"Ürünlerin fiyatı {fiyat1} TL ve {fiyat2} TL'dir. İkinci ürüne {indirim} TL indirim yapılmıştır. Borcunuz : {borc} TL'dir.")
else:
    borc=fiyat1+fiyat2
    print(f"Ürünlerin fiyatı {fiyat1} TL ve {fiyat2} TL'dir. İkinci ürüne {indirim} TL indirim yapılmıştır. Borcunuz : {borc} TL'dir.")
"""
#endregion
#region odev_3
"""
a= int(input("Lütfen a değerini giriniz\t:"))
b= int(input("Lütfen b değerini giriniz\t:"))
c= int(input("Lütfen c değerini giriniz\t:"))
delta=b**2-4*a*c
if delta > 0:
    kök1, kök2= round(((-b+delta**0.5)/2*a),2), round(((-b-delta**0.5)/2*a),2)
    print(f"1. kök {kök1}, 2. kök {kök2}\'dir")
elif delta==0 :
    ikikök=-b/2*a,-b/2*a
    print(f"Kökler birbirine eşit ve {ikikök} 'tür")
else:
    print("Kök yoktur")
"""
#endregion

#region odev_4
"""
vize= int(input("Lütfen vize notunu giriniz\t:"))
final= int(input("Lütfen final notunu giriniz\t:"))
ort= vize*0.4+final*0.6
if ort > 0 :
    if ort > 90 :
        print ("Sınav notunuz AA'dır.")
    elif ort >75 :
        print ("Sınav notunuz BB'dır.")
    elif ort >60 :
        print ("Sınav notunuz CC'dır.")
    elif ort >50 :
        print ("Sınav notunuz DD'dır.")
    else :
        print ("Sınav notunuz FF'dır.")
else:
    print("0-100 arasında değilse lütfen 0-100 arasında giriniz")
"""
#endregion

#region odev_5

yakit=int(input("Lütfen Yakıt Tipini giriniz\t:"))











