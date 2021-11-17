#region if_aciklama
#if kullanımı
"""
1- önce if yazılır
2- sonra koşul yazılır
3- sonra da : iki nokta ile blok başlatılır
#if uName == "admin" : (gibi)
"""
#endregion

#region ornek_1
"""
havaDurumu = "yağmurlu"
print("a")
if havaDurumu == "yağmurlu":
    #print("Şemsiye alın Lütfen")
    print("b")
print("c")
"""
#endregion

#region ornek_2
"""
a = -10
if a < 0 :
    print(f"{a} sayısı negatiftir")
"""
#endregion

#region ornek_3
"""
sayi = int(input("Lütfen bir sayı giriniz \t:"))
if sayi  == 0 :
    print("Sıfır Giremezsiniz!")
"""
#endregion

#region ornek_4
uName = input("Lütfen Kullanıcı Adınız \t:")
if uName != "admin":
    print(f"{uName} admin paneline giriş yapamaz")

#endregion
#region ornek_5
"""
sayi1 = int(input("Lütfen Bir Rakam Giriniz \t:"))
if sayi1 > 9 :
    print("Bu bir rakam değildir!")
"""
#endregion




