#adım sayısı belli olmadığında while kullanılır.
#region for
"""for i in range (5):
    print(f"Şu an {i}. for döngüsündeyim")
"""
#for'da 
#endregion
#region list
"""
sayiDizisi= list(range(20))
print(sayiDizisi)

#list(range) [1,20] sayıları arası

sayiDizisi2= list(range(5,20))
print(sayiDizisi2)

#list(range) 5 dahil 20'ye kadar sayıları arası

sayiDizisi3= list(range(5, 20, 2))
print(sayiDizisi3)
#5 dahil 20 sayı arası 2 şerli artan sayılar

#range(start,stop,step)
#range(20) = range(0,20,1) 
#range(0,20)=range(0,20,1) default olarak önceden belirlenmiş olanı çağırır.

sayiDizisi4= list(range(20,5,-1))
print(sayiDizisi4)

"""
#endregion

#region alistirma
"""
for i in range(1,11):
    print(f"{i}. öğrenci", end=" ")
"""
#endregion

#region iç içe for
"""
for i in range(1, 6):  #1,2,3,4,5
    for j in range (1, 6):  #1,2,3,4,5
        print(i, "x" , j, " = ", i*j,"\t" , end= " ")
    print()
"""

#endregion

#region for içinde pass
"""
for i in range(1, 6):  #1,2,3,4,5
    pass
print("Şu an for dışınadyım")
"""
#endergion

#regin for içinde if
"""
for i in range(1,6):
    for j in range (1,6):
        if i==3:
            if j==2:
                print(i, "x" , j, " = ", i*j,"\t" , end= " ")
"""
#endregion

#region pratikler
"""
lütfen sayı giriniz, çıkmak için -1 : -1
sayıların toplamı → ...


tekToplam=0
while True:
    sayi=int(input("Lütfen Bir sayı Giriniz, çıkamk için -1'e basınız:"))
    if sayi!=-1:
        if sayi%2!=0:
            tekToplam+=sayi
        else:
            print("Lütfen Tek sayı Giriniz\t:")
            continue
    else:
        break
print(tekToplam)
"""

"""
tekToplam=0
while True:
    sayi=int(input("Lütfen sayı giriniz\t:"))
    if sayi == -1:
        break
    if sayi%2==0:
        print("Lütfen tek sayı giriniz\t:")
        continue
    tekToplam+=sayi
print(tekToplam)
"""

#endregion

#region pratik_2
"""
lütfen sayı giriniz sayı giriniz: 30
1 2 3 5 6 10 15 30
"""

x= int(input("Lütfen sayı giriniz\t:"))
for i in range(1,x+1):
    if x%i==0:
        print(f"{i}", end=" ")

#endregion