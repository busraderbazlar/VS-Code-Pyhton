import requests
from urllib.parse import urlparse
import datetime
import time
import json
#print(time.ctime(857344273))

urlCustomers = "https://northwind.netcore.io/customers.json"
rCustomers = requests.get(urlCustomers)
if not rCustomers.status_code == 200:
    raise Exception("API Bağlantı Sorunu. Status code: {}. Text: {}".format(
        rCustomers.status_code, rCustomers.text))
#print(rCustomers.text)


jsonCustomers = rCustomers.json()
#print(jsonCustomers)
#print(jsonCustomers.values)


urlOrders = "https://northwind.netcore.io/orders.json"
rOrders = requests.get(urlOrders)
if not rOrders.status_code == 200:
    raise Exception("API Bağlantı Sorunu. Status code: {}. Text: {}".format(
        rOrders.status_code, rOrders.text))
#print(rOrders.text)

jsonOrders = rOrders.json()
#print(jsonOrders)

mainMapApiUrl="https://www.mapquestapi.com/geocoding/v1/address?key=yAApx2G1tnQAa3QSNsIU0CdvnB3ZfVoA&location=istanbul"
mapApiKey="yAApx2G1tnQAa3QSNsIU0CdvnB3ZfVoA"

def metinKontrol(metin):
    if len(metin)>15:
        degisim = metin.replace(metin[16:],"...") 
        return f"{degisim}"
    else:
        return f"{metin}"

def musteriListele():
    print("Müşteri Listesi")
    print("+--------+-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+")
    print("|ID      |CompanyName            |ContactName            |Address                |Country                |City                   |")
    print("+--------+-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+")


"""for i in jsonCustomers["results"]:
    print(f"{i['id']}\t{i['companyName']}\t{i['contactName']}\t{i['address']}\t{i['country']}\t{i['city']}\t", end=" ")
    print("+--------+-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+")
"""
def musteriAra(musteriId):
    for i in jsonCustomers["results"]:
        if i['id']==musteriId:
            print(f"{musteriId} ID'li müşteri bulundu. Detay Listesi")
            print("==========================")
            metinKontrol(i)
            print(f"Şirketinin adı {i['companyName']}, ulaşılacak kişi adı {i['contactName']}, adresi {i['address']}, ülkesi {i['country']}, şehri {i['city']}")          
            break
        else:
            print(f"{musteriId} ID'li müşteri bulunamadı")


# 17 → Siparişleri listeleyelim
def siparisListele():  
    print("Sipariş Listesi")
    print("+--------+---------------+-------------------------------+-----------------------+-----------------------+-----------------------+")
    print("|ID      |CustomerId     |OrderDate                      |ShipAddress            |ShipCity               |ShipCountry            |")
    print("+--------+---------------+-------------------------------+-----------------------+-----------------------+-----------------------+")
"""siparisListele()
for i in jsonOrders["results"]:
    risetimeInEpochSeconds = int(i['order']["orderDate"][6:15])
    risetimeInFormattedString = time.ctime(risetimeInEpochSeconds)
print(f"{i['order']['id']}\t{i['order']['customerId']}\t{risetimeInFormattedString}\t{i['order']['shipAddress']}\t{i['order']['shipCity']}\t{i['order']['shipCountry']}\t", end=" ")
print("+--------+-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+")
"""
def siparisAra(siparisId):
    for i in jsonOrders["results"]:
        if i['order']['id']==siparisId:
            risetimeInEpochSeconds = int(i['order']["orderDate"][6:15])
            risetimeInFormattedString = time.ctime(risetimeInEpochSeconds)
            print(f"{siparisId} ID'li sipariş bulundu. Detay Listesi")
            print("==========================")
            print(f"Sipariş id : {i['order']['id']}\nMüşteri id : {i['order']['customerId']}\nSipariş tarihi : {i['order']['orderDate']}\nSipariş adresi : {i['order']['shipAddress']}\nŞehri : {i['order']['shipCity']}\nÜlkesi : {i['order']['shipCountry']}\n")
            nereye = i['order']['shipCity']          
            cevap = input(f"Kargo Rotasını {nereye.upper()} Şehri İçin Görmek İster misiniz? [e/E] :")
            if cevap.lower()=="e":
                while True:                    
                    print(f"Varış Noktası {nereye} için Rota Hesaplanacak")
                    nereden = input("Nereden Çıkacak: ")
                    mainMapApiUrl="https://www.mapquestapi.com/geocoding/v1/address?key=yAApx2G1tnQAa3QSNsIU0CdvnB3ZfVoA&location=istanbul"
                    break
            break
    else:
        print(f"{siparisId} ID'li sipariş bulunamadı")



# 19 → menu
while True:
    for i in range(5):
        print()
    secim = int(input("""
    Seçiminiz:
    [1]     → MÜŞTERİ LİSTELE
    [2]     → MÜŞTERİ ARA <MÜŞTERİ ID'E GÖRE>
    [3]     → SİPARİŞ LİSTELE
    [4]     → SİPARİŞ ARA <SİPARİŞ ID'E GÖRE>
    [5]     → ÇIK
    """))
    if secim==1:
        musteriListele()
        for i in jsonCustomers["results"]:
            print(f"{i['id']}\t{i['companyName']}\t{i['contactName']}\t{i['address']}\t{i['country']}\t{i['city']}\t", end=" ")
            print("+--------+-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+")
    elif secim==2:
        musteriAra(input("Müşteri id giriniz:"))
    elif secim==3:
        siparisListele()
        for i in jsonOrders["results"]:
            risetimeInEpochSeconds = int(i['order']["orderDate"][6:15])
            risetimeInFormattedString = time.ctime(risetimeInEpochSeconds)
            print(f"{i['order']['id']}\t{i['order']['customerId']}\t{risetimeInFormattedString}\t{i['order']['shipAddress']}\t{i['order']['shipCity']}\t{i['order']['shipCountry']}\t", end=" ")
            print("+--------+-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+")
    elif secim==4:
        siparisAra(int(input("Lütfen Sipariş id giriniz:")))
    elif secim==5:
        break
    else:
        pass


