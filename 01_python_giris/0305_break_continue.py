# region break_continue_neden_kullanilir
"""
break     → döngüyü sonlandırır #beklenmedik bir hata olduğunda döngüyü kırmak için, aradığın bir şeyi bulduğun zaman aradığını devam etmemek kırmak için kullanılır.
continue  → tepeye geri döndürecek
"""
# endregion


#region ornek_1 break
"""
i=1
x= int(input("Aradığınız stok id: "))
while i<10:
    print(i, end=" ")
    if i==x:
        break
    i+=1
"""
#endregion

#region ornek_2 break
"""
i=1
x= int(input("Aradığınız stok id: "))
print(b)
while i<10:
    print("b", end=" ")
    if i==2:
        break
    i+=1
print(c)
"""
#endregion


#region ornek_3
"""
i=1
x= int(input("Aradığınız stok id: "))
while i<10:
    if i==x:
        i+=1
        continue
    print(i, end=" ")
    i+=1
"""
#endregion

#region ornek_4_continue
"""
i = 1
print("a")
while i<11:
    if i==15:
        print("b")
        break
    print(f"{i}. döngü")
    i += 1
print("c")
"""
"""
i = 1
print("a")
while i < 100:
    if i % 7 == 0:
        i += 1
        continue
    elif i % 15 == 0:
        break
    print(f"{i}. döngüdeyim")
    i += 1
print("b")
"""
#endregion

#region aliştirma
eb=0
while True:
    x=int(input("Lütfen bir sayı giriniz, çıkmak için -1'e basınız:"))
    if x==-1:
        break
    if x>eb:
        eb=x
if eb==0: #if eb==0 ve if eb: yani if==True olarak bilindiği için if eb: girilebilir
    print("Hiç Bir Sayı Girmediniz")
else:
    print(f"{eb}")

