#region aritmetik-operatorler
# aritmetik operatörler
"""
1→  +   toplama
2→  -   çıkarma
3→  *   çarpma
4→  /   bölme
5→  //  tam bölme
6→  **  üst alma
7→  %   mod alma
mod alma bir şeyin bölümünden kalan alma
"""
#endregion
"""
print(2+4)
print(3-3)
print(4+2.8)
#unary sayının işareti
#eksi işareti olarak algılar, çıkarma olarak değil.
print(-9)
# toplama,çıkarma binarydir.
"""

print(6*5)
print(type(5*6))
#aynı 
print(5*6.0)
print(5*6.)
#aynı

print(10/5)
print(type(10/5))
#bölmede her türlü tip float çıkar
print(10/2.0)


print(2**3)
print(2**3.)
print(type(2*3.2))

#karekök alma

print(16**0.5)

#floor division

print(12/7)
print(12//7)
print(-12/7)
print(-12//7)

#tam bölme her zaman bir küçük sayıya yuvarlar.
#tam bölme //

print(12%5)
print(12%2)
#mod almada bölümden kalanlar gösterilir.%
#region
"""
1. +,- unary baştaki işaret, tüm işaretlerin ötesinde ilk yapılan process
2. **  üst alma
3. *, /, % çarpma, bölme, mod alma
4. +, -
kullanım sırası birden fazla ise yukarıdan aşağı doğrudur.
"""
print(5*2+3)
print(17/5%2) 
#yukarıdaki printte
#formülde aynı önceliğe sahip işaretler varsa soldan sağa işlem yapar.
#left-side binding
print(15%4%2) 
#soldan sağa işlem yapılır

print(2**3**2)
print(2*3*(3-2)/2)
print(2+4/2-5*2+10/(2+3))
print((10/(3+3))**0.5)
print(((1+2**3)**0.5)-((1/(3+2**2))**0.5))

#endregion







