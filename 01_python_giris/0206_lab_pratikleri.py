#region ornek_1
"""
bavulAgirligi = 20
biletFiyat = float(input("Lütfen Bilet Fiyatını Giriniz \t:"))
if bavulAgirligi > 15 :
    fark = bavulAgirligi-15
    biletFiyat += fark*5
    pass
print(f"Güncel Bilet Fiyatı {round(biletFiyat*1.18,2)} 'TL dir.")
"""
#endregion

#region ornek_2
"""
biletFiyati = float(input("Lütfen Bilet Fiyatını Giriniz\t:"))
bavulAgirligi = float(input("Lütfen Bavul Ağırlığını Giriniz\t:"))
ekUcret =0
if bavulAgirligi > 15 :
    ekUcret = (bavulAgirligi-15)*5
print(f"Toplam Ücret : {(biletFiyati) + (biletFiyati*1.8) + (ekUcret)}")
print(f"Kdv Ücreti {biletFiyati*1.8}")
print(f"Ekstra Bagaj Ücreti {ekUcret}")
"""
#endregion

#region ornek_3
""" 
biletFiyati=int(input("Bilet fiyatını giriniz : "))
bavulAgirligi=float(input("Lütfen bavul ağırlığını giriniz : "))
if bavulAgirligi>15:
    fark=((bavulAgirligi-15)*5)
    biletFiyati+=fark
    print(f"{bavulAgirligi-15} ekstra ağırlık için {fark} TL ödediniz.")
print("Ödenecek olan tutar : ",biletFiyati*1.18,"TL")
"""
#endregion

# region ornek_4
"""
sayi = int(input("lütfen sayı giriniz "))
if sayi<0:
    sayi *= -1
print(f"sayının mutlak değeri {sayi}")
"""
# endregion

# region ornek_5
"""
bakiye = 5000
bankaKodu = 101
eftBankaKodu = 101
kesinti = 0
transfer = float(input("lütfen eft tutarını giriniz : "))
if bankaKodu != eftBankaKodu:
    kesinti = transfer*0.05
print(f"güncel bakiyeniz {bakiye - transfer - kesinti} TL.")
"""
# endregion

# region ornek_6
# 3 sayı girilecek en büyük ekrana yazılacak
"""
eb = 0
s = int(input("Lütfen Sayı Giriniz \t : "))
if s > eb:
    eb = s
s = int(input("Lütfen Sayı Giriniz \t : "))
if s > eb:
    eb = s
s = int(input("Lütfen Sayı Giriniz \t : "))
if s > eb:
    eb = s
print(f"Girilen Sayıların En Büyüğü {eb}")
"""
# endregion

# region ornek_7
"""
s1 = int(input("Lütfen 1. Sayı Giriniz \t : "))
s2 = int(input("Lütfen 2. Sayı Giriniz \t : "))
if s1>s2:
    print(f"{s1}>{s2}")
"""
#endregion

# region ornek_7
"""
s1 = int(input("Lütfen 1. Sayı Giriniz \t : "))
s2 = int(input("Lütfen 2. Sayı Giriniz \t : "))
s3 = int(input("Lütfen 3. Sayı Giriniz \t : "))
ort = (s1+s2+s3) / 3
if ort >= 50:
    print(f"GEÇTİNİZ, ORTALAMANIZ {round(ort,2)}")

"""
#endregion

#region odev_1
""""
kargoBedeli = 7.5
satinAlinanToplamFiyat = float(input("Lütfen Satın Alınan Ürünlerin Toplam Fiyatını Giriniz\t:"))
if satinAlinanToplamFiyat < 250:
    satinAlinanToplamFiyat +=kargoBedeli
print(f"Satın Alınan Ürünlerin Toplam Fiyatı {satinAlinanToplamFiyat}")
"""
#endregion

#region odev_2
"""
Bakiye = int(input("Lütfen Bakiyeyi Giriniz\t :"))
a = input("Lütfen hesabın bulunduğu bankayı giriniz\t :")
b = input("Lütfen hesabın gönderileceği bankayı giriniz\t :")
c = int(input("Lütfen transfer edilecek tutarı giriniz\t :"))
eftKesinti=0
if a!=b :
    eftKesinti=c*0.10
kalanTutar = (Bakiye-c)-eftKesinti
print(f"Hesapta Kalan Tutar {kalanTutar}")
"""
#endregion


#region pratik_1
"""
sayi = int(input("Lütfen bir sayı giriniz\t:"))
if sayi == 0 :
    print("Bu sayı ne pozitif ne de negatiftir")
if sayi < 0 :
    print("Bu sayı negatiftir")
if sayi > 0 :
    print("Bu sayı pozitiftir")
"""
#endregion







