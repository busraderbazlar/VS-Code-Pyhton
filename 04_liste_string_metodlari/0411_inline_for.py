"""liste = []
for i in range (1,9): #geleneksel for
    liste.append(i)
print(i)

#in-line for

liste = [i for i in range(1,9)] #i 'ye rangedeki i değerleri atanır.
liste2= [i*i for i in range(1,9) if i >5] #if gibi koşullarda bağlanabilir.
print(liste2)"""


# region ornek

"""Haftanın 1. Günü Pazartesi  Haftanın 2. Günü Salı ...

haftaninGunleri = ["", "Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]
hafta = [ f" haftanın {a}. günü {haftaninGunleri[a]} " for a in range (1,8) ]
print(hafta)

liste = [f"haftanın {haftaninGunleri.index(a)}. günü {a}" for a in haftaninGunleri if haftaninGunleri.index(a)>0]
print(liste)"""
# endregion




# endregion

