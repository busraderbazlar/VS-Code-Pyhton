"""rakamlar = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
kHarfler = ["a","b","c","ç","d","e","f","g","ğ","h","i","ı","j","k","l","m","n","o","ö","p","r","s","ş","t","u","ü","v","y","z"]
bHarfler = ["A","B","C","Ç","D","E","F","G","Ğ","H","I","İ","J","K","L","M","N","O","Ö","P","R","S","Ş","T","U","Ü","V","Y","Z"]
import random
parola = ""
def parolaUret():
    global parola
    sec = random.randint(1,3)
    if sec==1:
        parola += str(random.choice(rakamlar))
    elif sec==2:
        parola += random.choice(kHarfler)
    else:
        parola += random.choice(bHarfler)
while True:
    for i in range(10):
        parolaUret()
    print(parola)
    parola = ""
    print()"""


    # region ornek_4
"""
def kartBilgiVer(k):
    return f"{k['ad']} {k['soyad']} {k['bankaAdi']} {k['para']}"
def atmBilgiVer(a):
    return f"{a['ad']} {a['para']}"
def ayniMi(k, a):
    if k['bankaAdi'] == a['ad']:
        return True
    else: 
        return False
def paraYatir(k, a, miktar):
    k['para'] += miktar
    a['para'] += miktar
    if not ayniMi(k, a):
        k['para'] -= miktar*0.03
        a['para'] += miktar*0.03
    print(f"{miktar} para yatırıldı. ATM'de {a['para']} TL. oldu")
def paraCek(k, a, miktar):
    if a['para']>=miktar:
        if k['para']>=miktar:
            k['para'] -= miktar
            a['para'] -= miktar
            if not ayniMi(k, a):
                k['para'] -= miktar*0.03
                a['para'] += miktar*0.03
                print(f"kartınızdan {miktar*0.03} TL. ücret alındı")
            print(f"{miktar} TL. Çekildi. Atm'de {a['para']} kaldı. Hesabınızda da {k['para']} kaldı.")
        else:
            print(f"Bakiyenizde bu kadar para yok. En fazla {k['para']} TL. çekebilirsiniz")
    else:
        print(f"ATM'de Bu KAdar PAra Yok {a['para']} miktar çekebilirsiniz...")
kart = {
    "ad": "ali",
    "soyad" : "kemal",
    "bankaAdi": "zirat",
    "para": 100
}
atm = {
    "ad":"halk",
    "para":350
}
print(kartBilgiVer(kart))
print(atmBilgiVer(atm))
paraYatir(kart, atm, 100)
print("-"*50)
print(kartBilgiVer(kart))
print(atmBilgiVer(atm))
paraCek(kart, atm, 50)
print("-"*50)
print(kartBilgiVer(kart))
print(atmBilgiVer(atm))
"""
# endregion

"""
import requests
from bs4 import BeautifulSoup
url = "https://www.worldometers.info/coronavirus/?utm_campaign=homeAdvegas1?"
response = requests.get(url)
source = BeautifulSoup(response.content, "html.parser")
innerContent = source.find_all("div", attrs={"class": "maincounter-number"})
for i in range(len(innerContent)):
    print(innerContent[i].get_text().strip("\n"))
    print()
    print()

print("vaka → ", innerContent[0].get_text().strip('\n'))
print("vefat → ", innerContent[1].get_text().strip('\n'))
print("iyileşen hasta → ", innerContent[2].get_text().strip('\n'))

"""
