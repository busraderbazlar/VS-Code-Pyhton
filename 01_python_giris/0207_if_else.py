# if-else : evet döndüğünde bir şey yap, hayır döndüğünde başka bir şey yap
#region ornek_1
"""

havaDurumu= ("Yağmurlu")
if havaDurumu == "Yağmurlu" :
    print("şemsiye al lütfen")
else:
    print("şemsiye almana gerek yok")
"""
#endregion

#region ornek_2
engeleDegdiMi = False
#değişkenin eşitliğine göre çalışır True ise if , False ise else printini yazdırır.
can,skor =3,0
#ayrı ayrı değişkenleri yukarıdaki şekilde yazıldığında tek satırda birleştirir.
#inline değişken tanımlama denir.
#ifde otomatikman True olarak eşitleneceği için ==True yu yazmaya gerek yoktur.
if engeleDegdiMi:
    can-=1
    print(f"{can} canınız kaldı")
else:
    skor +=1
    print(f"{skor} anlık skorunuz")

#endregion

#region ornek_3

"""
"""
sayi = int(input("1. sayıyı giriniz\t :"))
if sayi %2 == 0:
    print(f"{sayi} sayı çifttir")
else:
    print(f"{sayi}sayı tektir")

#endregion
