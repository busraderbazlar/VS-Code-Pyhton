# region cok_boyutlu_listeler_giris
"""
matris yapıları oluşturma
veri tabanı mimarisine benzer satırxsütun yapıları oluşturma
"""
# endregion

# region kurum_ici_veri_tabani_ornegi
"""
Örn. kurum içi bilgisayarların özelliklerini tutacağınız bir tablo
Bil.No  Cihaz Adı       CPU     PID
1       Desktop_Test    %56     chrome.exe
2       Guest101        %60     excel.exe
3       Kat-1_Laptop    %90     camtasia.exe, chrome.exe
"""
# endregion

# region tanimlama
"""
a = [[1, 2, 3, 4], [5, 6, 7, 8]] #liste içinde liste birden fazla listenin ortak değişkene sahip olması
1 2 3 4
5 6 7 8
ixj 2x4 #gibi çıkar
print(a)
print(a[0])#1.satır
print(a[1])
print(a[1][1])#1.satırın 1. elemeanı
a[1][1]=44
print(a[1][1])
"""
"""a = [[1, 2, 3, 4], [5, 6, 7, 8]] #liste içinde liste birden fazla listenin ortak değişkene sahip olması
for i in range (2):#0,1
    for j in range (4): #0,1,2,3
        print(a[i][j], end=" ")
    print()

for i in range (len(a)):#0,1
    for j in range (4): #0,1,2,3
        print(a[i][j], end=" ")
    print()"""

"""
a = [[1, 2, 3, 4], [5, 6, 7, 8, 9], [9,9,9,9,9]] #liste içinde liste birden fazla listenin ortak değişkene sahip olması
"""
# endregion

# region kurum_ici_veri_tabani_ornegi
"""
Örn. kurum içi bilgisayarların özelliklerini tutacağınız bir tablo
Bil.No  Cihaz Adı       CPU     PID
1       Desktop_Test    %56     chrome.exe
2       Guest101        %60     excel.exe
3       Kat-1_Laptop    %90     camtasia.exe, chrome.exe
"""
# endregion
"""
liste = [[1, "Desktop_Test", 56, "chrome.exe"],[2, "Guest101", 60, "excel.exe"],[3, "Kat-1_Laptop", 90, "camtasia.exe, chrome.exe" ]]
for i in range (len(liste)):
    for j in range (len(liste[i])):
        if j == 2:
            print(f"%{liste[i][j]}", end=" ")
        else:
            print(f"{liste[i][j]}", end=" ")
    print()"""
#print(a[1][1])
#işlemcinin %80'nin üzerinde olan Pc'nin kat bilgisi ve Host adı

"""liste = [[1, "Desktop_Test", 56, "chrome.exe"],[2, "Guest101", 60, "excel.exe"],[3, "Kat-1_Laptop", 90, "camtasia.exe, chrome.exe" ]]
for i in range (len(liste)):
    if liste [i][2]>80:
        print(f"Bilgisayar adı {liste[i][1]} olan {liste[i][0]}. kattaki host'un işlemcisi %{liste[i][2]}")
#print(a[1][1])
"""

# region for_ile_erisim_1
"""
1 2 3 4
5 6 7 8
a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
for  i in range(len(a)):
    for j in range(len(a[i])):
        print(f"{a[i][j]}", end= " ")
    print()
"""
# endregion

# region for_ile_erisim_2
"""
kurumBilgisayarlari=[
    [1, "Kat1-PCCCC", 45, "chrome.exe"], 
    [2, "Desktop-Lab1", 84, "chrome.exe, camtasia.exe"], 
    [3, "Misafir-PC", 25, "excel.exe"]
    ]
print(f"satır sayısı → {len(kurumBilgisayarlari)}")
print(f"sütun sayısı → {len(kurumBilgisayarlari[0])}")
for i in range(len(kurumBilgisayarlari)):    #0,1,2
    for j in range(len(kurumBilgisayarlari[i])):
        print(f"{kurumBilgisayarlari[i][j]}\t", end="" )
    print()
"""
# endregion