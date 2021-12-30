# region list_arguments_giris
"""
Argüman olarak → int, float, string, gönderebiliyorum, peki
Argüman olarak → list gönderebilir miyim? Cevabı, Evet
"""
# endregion

# region ornek
"""
def ortalama(liste):
    print(type(liste))
    for i in liste:
        print(i)
    print(f"tüm listenin elemanları toplamı → {sum(liste)}")
ortalama([3, 5, 9, 15, 16])
"""

"""def ortalama (liste):
    tekAded, tekOlanlarToplami = 0,0
    for i in liste:
        if i%2 ==1:
            tekAded+=1
            tekOlanlarToplami+=i
        print(tekAded)
        print(tekOlanlarToplami)

ortalama([3, 5, 9, 15, 16])
"""

import time
from datetime import datetime
cTime = time.time()
print(cTime)
print(datetime.now())
#print(datetime.now().time.timestamp()) #time.time ile aynı
#print(datetime.fromisoformat("2000-30-12").timestamp()) #stringi tarihe çevirdik sonra, tarihi times tampa çevirdirk.

#epoch time
#1/1/1970 - unix-linux- macos-win 1970 tariihnden geçen saniye"""


"""import time
from datetime import datetime

def urunTarihKontrol(liste):
    for i in liste:
        cTime=time.time()
        pTime=datetime.fromisoformat(i).timestamp()
        if round((cTime-pTime)/86400)>60:
            print(i)



urunTarihleri = [
"2021-10-18",
"2021-10-19",
"2021-10-20",
"2021-10-21",

]

urunTarihKontrol(urunTarihleri)"""

# endregion