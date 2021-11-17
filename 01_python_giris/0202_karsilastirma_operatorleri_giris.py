#region karsilarstirma_operatorleri_giris
"""
Karşılaştırma Öperatörleri
1.  ==  eşittir
2.  !=  eşit değildir
3.  <   küçüktür
4.  >   büyüktür
5.  <=  küçük eşittir
6.  >=  büyük eşittir

"""
#endregion

# region ==
"""
print(10 == 10)
print(-5 == -5)
print(10 == 5)
#karşılaştırma öperatörlerinde sadece sayı olmaz.String değerleride olur.

print("meb" == "Meb")
print("istanbul" == "istanbul")
print("istanbul" == "İstanbul")
print("meb" == "MEB")
print(" " == " ")
#karakter olmamamsıda true false'u etkilemez.
print(10=10)
#bu yanlış olandır.
"""
# endregion

# region !=
"""
print(10 != 10)
#burada eşit değil midir sorduğu için false çıkar.
print(10 != 5)
print("meb" != "MEB")
"""
# endregion

# region <
"""
print(10 < 20)
print(10 < 10)
print(20 < 10)
print(5 < 9)
"""
# endregion

# region >
"""
print(10 > 20)
print(10 > 10)
print(20 > 10)
print(30 > 20)
print(20 > 20)
"""
# endregion

# region <=
"""
print(10 <= 20)
print(10 <= 10)
print(20 <= 10)
"""
# endregion

# region >=
"""
print(10 >= 20)
print(10 >= 10)
#eşit olmasaydı False eşit olduğu için True olur
print(20 >= 10)
"""
# endregion

# region ornek_1

ogrenciYas = int(input("Lütfen Öğrencinin Yaşını Giriniz: "))
print(ogrenciYas >= 18)

# endregion

# region ornek_2
"""
Kullanıcı Adını Giriniz : admin     → True 
Kullanıcı Adını Giriniz : user      → False 
"""
"""
uName = input("Lütfen K.A. Giriniz : ")
print(uName=="admin")
uName = input("Lütfen K.A. Giriniz : ")
print(uName!="user")
"""
# endregion