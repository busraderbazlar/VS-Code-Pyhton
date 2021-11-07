#region
"""
rakam=int(input("Lütfen rakam giriniz\t:"))
sehir = "İstanbul"
print("Girdiğiniz rakamın 1 fazlası" + str(rakam+1) + sehir)
#rakam+1 printte int algılıyor ama strig olması lazım + birleştirmek için
#str() ile stringe dönüştürülür
"""
"""
rakam=int(input("Lütfen rakam giriniz\t:"))
#1.yöntem format
print(" {} Girdiğiniz rakamın 1 fazlası {} " .format (rakam, (rakam+1)))
#printanında dönüşüm kolaylığı format yöntemi
#{} formatlanacak yerler
#.format ile formatlıyor

#2.yöntem fstring
rakam=int(input("Lütfen rakam giriniz\t:"))
print(f"{rakam} rakamın 1 fazlası {rakam+1}")
"""
"""
Girilen 40, 60, 80 sayı değerinin ortalaması
"""
"""
s1 = int(input("1.sayıyı giriniz\t :"))
s2 = int(input("2.sayıyı giriniz\t :"))
s3 = int(input("3.sayıyı giriniz\t :"))
ort =(s1+s2+s3)


print(f" Girilen {s1}, {s2}, {s3} sayı değerinin ortalaması {ort}")
"""
"""
a= int(input("Lütfen Ağırlık Bilgisi Giriniz\t:"))
b= int(input("Lütfen Boy Bilgisi Giriniz (mt)\t:"))
vki = a/b**2
print(f"{a} kg ve {b} metre değerine göre VKİ sonucu : {vki}")

"""





"""
Lütfen Boy Bilgisi Giriniz (mt) : 178
75 kg. ve 1.78 metre değerine göre VKİ sonucu : 23

"""
#endregion

yariCap= int(input("Lütfen yarı çap giriniz\t :"))
cevre = 2*3.14*yariCap
alan = 3.14*yariCap**2
print(f"{yariCap},yarı çaplı dairenin çevresi {cevre} ve alanı {alan}")
#0129 ödev