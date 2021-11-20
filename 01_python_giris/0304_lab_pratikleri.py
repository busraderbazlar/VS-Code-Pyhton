"""
a= input("Metin giriniz:")
x=0
while x<5:
    print(a)
    x+=1
"""
"""
a=input("Metin Giriniz:")
x=0
i = int(input("Kaç kez tekrar etmeli"))
while x<i:
    print(a)
    x+=1
"""
"""
i=0
j=0
while i <1:
    while j<10:
        j+=1
    i+=1
    j=0
    print()

"""
"""
#* * * * * * * * * *  
i=1
while i<=10:
    i+=1
    print("*", end=" " )
"""
"""
i=0
while i<10:
    i+=1
    if i%2 ==0:
        print("$", end=" ")
    else:
        print("*", end=" ")
"""
"""
#* * * * * * * * * *  
i=1
while i<=10:
    i+=1
    print("*", end=" " )
"""
"""
i=1
j=1
while i<=10:
    while j<=10:
        print(f"{i}.K {j}.Oda'dır.", end=("") )
        j+=1
    i+=1
    j=1
    print()

"""

# region ornek_6

#1.  [1-99] arası tek sayıların toplamını yazdıralım
i = 1
toplam = 0
while i < 100:
    toplam += i
    i += 2
print(f"[1-99] arası tek sayıların toplamı → {toplam}")

# endregion
