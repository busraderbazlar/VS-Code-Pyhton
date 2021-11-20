# region giris
# loop
# loop ne zaman kullanılır?
# loop → sürekli tekrarlayan işlemlerin yapılmasını sağlayan komutlardır


indirimOranı= 5
"""
print(f"Ekstra %{indirimOranı} İndirim Orani")
print(f"Ekstra %{indirimOranı} İndirim Orani")
print(f"Ekstra %{indirimOranı} İndirim Orani")
"""
#region prtik_1

indirimOrani= 5
i=0
while i<3:
    print(f"Ekstra %{indirimOranı} İndirim Orani")
    i +=1
#ctrl+c interrupt
#endregion
"""
1. Başlangıç
2. Bitiş
3. Artış Miktarı
"""
#region pratik_2
"""
i=1

while i<=3:
    #bitiş samanı while, i 3 ten küçük olduğu sürece true
    print(f"Ekstra %{indirimOranı} İndirim Orani") #buna baktık koşulu sağlıyor print yap. i=2 üzerinde ilerlendi tekrardan print yapıldı.
    i +=1 #i=2 oldu artık tekrar while koşula atandı. Artış miktarı olmazsa sonsuz döngü olur.
print(f"c")
"""
#endregion

#region ornek_2
"""
i=5
while i != 0 :
    print(f"{i}")
    i-=1

i=5
while i:
    print(f"{i}")
    i-=1

#integerda default sıfırdır. Tam sayı sıfır olduğunda false döner döngü kırılır. Boleanda True defaulttur.
#tam sayı olduğunda sıdır döner.
"""
#endregion

#region pratik_1
"""
yas= int(input("Lütfen yaş bilgisi giriniz: "))
if yas : #yas!=0 = yas: 
    print (yas)
else:
    print("yaş değeri sıfır olamaz.")
"""
#endregion


