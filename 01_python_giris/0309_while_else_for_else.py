# region while-else
# WHILE döngüsü BREAK satırı ÇALIŞARAK biterse, else içerisine GİRMEZ
# WHILE döngüsü BREAK satırı ÇALIŞMADAN biterse, else içerisine GİRER
#break çalışırsa else çalışmaz, break çalışmazsa else çalışır.
"""
i = 1
x=int(input("Aradığınız Stok id:"))
while i <= 10:
    print(i, end=" ")
        if i == x:
            #break
        i += 1
else:
    print("şu an else içerisine girdim")
print("while döngüsü bitti")
"""
# endregion

# region for-else
# FOR döngüsü BREAK satırı ÇALIŞARAK biterse, else içerisine GİRMEZ
# FOR döngüsü BREAK satırı ÇALIŞMADAN biterse, else içerisine GİRER
"""
for i in range(5,15):
    if i==10:
        break
else:
    print("Evet else çalıştı")
"""
"""
cId=81
for i in range(1,92):
    if i == cId:
        print("Aradığınız Müşrteri id Bulundu")
        print("Müşteri toplam alışveriş tutarı")
        break
else:
    print("Aradığınız müşteri id bulunamadı.")
"""

