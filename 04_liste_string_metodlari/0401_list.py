"""
n1= 34
n2= 45
n3= 55

#listler kolleksiyon tipidir. Desğişkenleri tek bir listede toplar.
notlar= [ 34, 45, 55]
print(notlar)

renkler=["mavi","yeşil","kırmızı"]
print(renkler)

notlar1= [1,2,3,"A","B"]
print(notlar1)
print(type(notlar))
print(notlar[2])

#listte değişkenler boş olabilir, farklı olabilir, aynı değerden birden fazla olabilir.
#listte değerler 0,1,2,3 diye 0'dan başlayara sıralanır. Ve print(notlar[2]) gibi 0 değil 1 değil 2. değer print edilir.

isimler = ["ali","veli","ender"]
print(isimler[2])
isimler[1]= "aziz" #lisetdeki isim değiştirilebilir buna intellicense denir.
isimler= ["ali","veli","ender","ömer"]
print(f"son eleman {isimler[2]}")
#sondan başa okunursa liste -1,-2,-3 diye gider.
print(f"son eleman {isimler[-1]}") #ömer çıkar son ama sağdan sola ilk eleman.
"""

"""sayilar= [3,55,63,99,1,12,74] #indexable
sayilar[3]= sayilar[1]
print(sayilar)
del sayilar [3] #3.elemanı siler.
print(sayilar)
print(len(sayilar)) #liste uzunluğunu söyler."""

"""sayilar = [3,55,63,99,1,12,74]
del sayilar[len(sayilar)-1]
print(sayilar) #len li delete yöntemi
"""
#region list and for

"""sayilar=[3,55,63,99,1,12,74] #api #json #parsing
for i in sayilar:
    print(i)"""

#endregion

"""x=1
sayilar=[3,55,63,99,1,12,74] #api #json #parsing
for i in sayilar:
    if i>50:
        print(f"{x}. öğrencinin notu {i}")
        x+=1"""


"""sayilar=[3,55,63,99,1,12,74] #api #json #parsing
for i in range(len(sayilar)):
    if sayilar[i]>50:
        print(f"{i}. öğrencinin notu {sayilar[i]}")"""

