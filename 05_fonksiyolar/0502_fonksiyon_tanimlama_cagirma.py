# region fonksiyon_tanimlama
"""
1→ def ile başlar
2→ fonksiyonun adı yazılır
3→ aç kapa parantez
4→ : iki nokta üst üste

def mesaj():
    print("lütfen bir sayı giriniz: ")
mesaj()
s1 = int(input())
mesaj()
s2 = int(input())
mesaj()
s3 = int(input())
print(f"{(s1+s2+s3)/3}")
"""
# endregion

#def ornek
"""def kullanıcı():
   ka= input("Lütfen kullanıcı adı giriniz:")
   print(f" Hoşgeldin {ka}")
kullanıcı()"""

def toplam():
    s1=(input("Lütfen s1 griniz:"))
    s2=(input("Lütfen s2 griniz:"))
    if s1.isdigit() and s2.isdigit():
        s1,s2 = int(s1), int(s2)
        print(s1+s2)
    else: 
        print("Lütfen sayı değeri girin")
    print(f"{s1}+{s2} iki sayının toplamıdır")

toplam()


# region fonksiyon_cagirma
"""
print("a")
def welcome():
    print("b")
print("c")
welcome()
print("d")
"""
# endregion

#region
"""def mesaj():
    print("lütfen bir sayı giriniz: ")
    print("Çıkmak için ç:")"""
#endregion

# region fonksiyon_duplicate
"""
def welcome():
    print("ilk f.")
def welcome():
    print("ikinci f.")
welcome()
"""
# endregion


# region fonksiyon_pass
"""
#pass???
def welcome():
    pass
"""
# endregion


# region fonksiyon_turleri
"""
1→ Parametre Almayan, Değer Döndürmeyen
2→ Parametre Alan, Değer Döndürmeyen
3→ Parametre Almayan, Değer Döndüren
4→ Parametre Alan, Değer Döndüren
"""
# endregion