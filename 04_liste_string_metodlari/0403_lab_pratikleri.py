"""sayilar = [11, 5, 36, 78, 99, 2]
aradığınız eleman : 99
aradığınız 99 elemanı listestenin 4. indisli elemanıdır
"""
"""
x=0
sayilar = [11, 5, 36, 78, 99, 2]
aradiginizEleman=int(input("Lütfen aradığınız elemanı giriniz\t:"))
for i in sayilar:
    if i==aradiginizEleman:
        print(f"{aradiginizEleman} elemanı listenin {x+1}. elemandır ")
        break
    x+=1
else:
    print("Bulamadım")
"""
"""
sayilar = [11, 5, 36, 78, 99, 2]
aradiginizEleman=int(input("Lütfen aradığınız elemanı giriniz\t:"))
for i in sayilar:
    if i == aradiginizEleman:
        print(f"{aradiginizEleman} elemanı Listenin {i+1}. elemanıdır.") #yada range(len(sayilar)). elemandır 
"""

"""isim=str(input("Lütfen isminizi giriniz\t:"))#stringlerde bir listedir. Her bir kelimenin harflerini eleman olarak algılar.
print(isim[0])
print(isim[1])
print(isim[2])
print(isim[3])
for i in range(len(isim)):
    print(isim[i])"""

"""isim = "EGE BARTU"
print(isim[len(isim)-1])
print(isim[len(isim)-2])
print(isim[len(isim)-3])
#forlu hali
for i in range((len(isim)-1),-1,-1):
    print(isim[i], end=" ")
"""


"""meyveler= str(input("Lütfen bir meyve giriniz\t:"))
for i in meyveler:
    if meyveler[0] == "E":
        print(i, end=" ")
    else:
        print("Yazdığınız Eleman E harfi ile başlamamaktadır. ")"""


"""while True:
    ogrenciAdi = input("Aradığınız Öğrenci Giriniz, çıkmak için ç :")
    if ogrenciAdi=="ç":
        break
    for i in range (len(ogrenciListesi)):
        if ogrenciListesi[i] == ogrenciAdi:
            print(f"{ogrenciAdi} listenin {i+1}. sırasındaki öğrencidir.")
            break
    else:
        print(f"{ogrenciAdi} listede yoktur)"""