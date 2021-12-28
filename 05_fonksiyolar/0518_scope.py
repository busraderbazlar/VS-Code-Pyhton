# region scope_kapsam_giris
"""
1→ python main fonksiyon ile yani main kısmı ile fonksiyon arasında değişken aktarımları, 
2→ main deki değişkeni fonksiyon görebilecek mi değiştirebilecek mi? 
3→ fonksiyondaki değişkene main kısmından erişim yapabilecek miyim?
4→ fonksiyondaki değişkenin içeriğini değiştirdiğimde, maindeki de değişecek mi? 
"""
# endregion

# region ornek_1
"""
def scopeTest():
    a = 34
    print("test")
    #while True:
        #pass
scopeTest()
print(a)
"""
# endregion

# region ornek_2
"""
not→ değişken adı aynı olsa da, fonksiyon scope’unda ATAMA YAPILDIĞI anda, o değişken, 
main bloktaki o değişken olmaktan çıkıyor
def scopeTest():
    a = 34
    print(a)
a = 19
scopeTest()
print(a)
"""
# endregion

# region ornek_3
"""      
not→ değişken adı aynı olan, fonksiyon scope’unda OKUMA YAPILDIĞI uygulamalarda, o değişken, 
main bloktaki o değişkendir
def scopeTest():
    #a = 34
    print(a)
a = 19
scopeTest()
print(a)
"""
# endregion

# region ornek_4
"""
not→ aynı örnekleri id özelliği ile ram hafıza adresini ekrana yazarak ta farkına varabiliriz
def scopeTest():
    a = 34
    print(id(a))
a = 19
scopeTest()
print(id(a))
"""
# endregion

# region ornek_5
"""
not→ değişken adı aynı olsa da, fonksiyon scope’unda ATAMA YAPILDIĞI anda, o değişken, 
main bloktaki o değişken olmaktan çıkıyor DEMİŞTİK. Olsun istiyor isek GLOBAL keyword kullanırız
def scopeTest():
    global a
    a = 34
    print(id(a))
a = 19
scopeTest()
print(id(a))
"""
# endregion

# region ornek_6
"""
not→ fonksiyona argüman gönderdiğimizde, fonksiyon scope’unda ATAMA YAPILIP DEĞİŞTİRMEK, 
main bloktaki o değişkeni DEĞİŞTİRMEZ
def scopeTest(a):
    print(a)
    a += 1
    print(a)
a = 19
scopeTest(a)
print(a)
"""
# endregion

# region ornek_7
"""
not→ fonksiyona argüman olarak LIST gönderdiğimizde, fonksiyon scope’unda ATAMA YAPMAK, 
main bloktaki o değişkeni DEĞİŞTİRMEZ demiştik, bu durum LIST içinde aynıdır
def scopeTest(arg):
    print(arg)
    arg = [19, 34, 35]
liste = [19, 34]
scopeTest(liste)
print(liste)
"""
# endregion

# region ornek_8
"""
not→ fonksiyona argüman olarak LIST gönderdiğimizde, fonksiyon scope’unda DEL ile LIST'i silmek, 
main bloktaki o listeyi DEĞİŞTİRİR.
"""
"""def scopeTest(arg):
    print(arg)
    del arg[0]



liste = [19, 34]
scopeTest(liste)
print(liste)"""

# endregion

# region Not
# Peki Neden?
"""
arg = [19, 34, 35] bu değişiklik listeyi değiştirmiyor, 
listenin elemanlarını değiştiriyor. 
Bu durumda liste elemanlarını değiştirmek main kısmındaki listeyi değiştirmez.
del arg[0] bu değişiklik 
listeyi değiştiriyor. 
Bu durumda listeyi değiştirmek main kısmındaki listenin de değişmesine neden olur.
"""
# endregion

#region_pratikler
"""def ciftSayiUret():
    global tekilListe
    while True:
        import random
        s = random.randint(1, 99)
        if s%2==1:
            continue
        else:
            if s in tekilListe:
                continue
            else:
                tekilListe.append(s)
                break
tekilListe=[]        
for i in range(1,30):
    ciftSayiUret()
print(tekilListe)"""



def fonk(arg):
    print(arg)
    del ar[0]

myList= [34,35]
fonk(myList)
print(myList)




#endregion