###############################################################
# Bu program:
# - Customer tablosundan gelen json'u parse ederek listeler
# - Order tablosundan gelen json'u parse ederek listeler
# - Kullanıcıya "/customers" istegi için aramak istediği müşteri id'sorar.
# - Kullanıcıya "/orders" istegi için aramak istediği order id'sorar.
# - MapQuest API için kişisel Credential alır
# - GPS koordinatlarını MapQuest API'yı kullanarak "location" bilgisinden keşfeder.
# - MapQuest API'yı kullanarak kargo elemanına rota çizer.
# - Epoch time modülünü kullanarak ekrana zaman bilgisini formatlar.
# - Runtime'da hata vermemesi için Dictionary'de "key" olup olmadığını keşfederek kod yazar.
# - Dönen json'u konsepti "json beautifier" olan google araması ile daha okunaklı hale getirir
# - https://jsonformatter.curiousconcept.com/ sitesini referan alır
#
# Öğrenci:
# 1. API request", "URL parse", "epoch time conversion" için kütüphaneleri import edecek.
# 2. Customers API için gerekli URL'leri girecek
# 3. Customers API için GET request kullanacak
# 4. if  case, bu kısımda her hangi bir kod değişikliği yapmayacak, request status kontrol ediliyor
# 5. Response içeriği  referans amaçlı print edilecek
# 6. Response icerigi json data formatına encode edilecek
# 7. Orders API için gerekli URL'leri girecek
# 8. Orders API için GET request kullanacak
# 9. if  case, bu kısımda her hangi bir kod değişikliği yapmayacak, request status kontrol ediliyor
# 10. Response içeriği  referans amaçlı print edilecek
# 11. Response icerigi json data formatına encode edilecek
# 12. Mapquest API için gerekli URL'leri girecek
# 13. Mapquest Credential için; token, key... hazırlıkları yapılacak
# 14. UI manipulasyonu. Output anında 15 karakterden uzun metinler için manipulasyon yapılacak
# 15. Müşterileri listeleyecek
# 16. Müşterileri Id'ye göre arama yapılacak
# 17. Siparişleri listeleyecek
# 18. Sipariş Id'ye göre arama yapılacak
# 19. Menü hazırlıkları yapılacak
###############################################################
# 1 → Kütüphaneleri import edelim
# API request", 
# "URL parse", 
# "epoch time conversion"
import requests
from urllib.parse import urlparse
import datetime
import time
import json
from datetime import datetime, timedelta
import googlemaps
#print(time.ctime(857344273))

# 2 → Customers API için gerekli URL girelim
# 3 → Customers API için GET request
# 4 → if  case, bu kısımda her hangi bir kod değişikliği yapmayın lütfen
# 5 → Response içeriği print et referans amaçlı
urlCustomers = "https://northwind.netcore.io/customers.json"
rCustomers = requests.get(urlCustomers)
if not rCustomers.status_code == 200:
    raise Exception("API Bağlantı Sorunu. Status code: {}. Text: {}".format(
        rCustomers.status_code, rCustomers.text))
#print(rCustomers.text)

# 6 → Response icerigi json data formatına encode et
jsonCustomers = rCustomers.json()
#print(jsonCustomers)
#print(jsonCustomers.values)

# 7 → Orders API için gerekli URL'leri girelim
# 8 → Orders API için GET request
# 9 → if  case, bu kısımda her hangi bir kod değişikliği yapmayın lütfen
# 10 → Response içeriği print et referans amaçlı
urlOrders = "https://northwind.netcore.io/orders.json"
rOrders = requests.get(urlOrders)
if not rOrders.status_code == 200:
    raise Exception("API Bağlantı Sorunu. Status code: {}. Text: {}".format(
        rOrders.status_code, rOrders.text))
#print(rOrders.text)

# 11 → response icerigi json data formatına encode et
jsonOrders = rOrders.json()
#print(jsonOrders)

# 12 → Mapquest API için gerekli URL'leri girelim
# 13 → Mapquest Credential için; token, key... hazırlıkları yapalım
mainMapApiUrl="http://www.mapquestapi.com/directions/v2/route?key=yAApx2G1tnQAa3QSNsIU0CdvnB3ZfVoA&from=Paris&to=Marseille"
mapApiKey="yAApx2G1tnQAa3QSNsIU0CdvnB3ZfVoA"

# 14 → UI manipulasyonu. Output anında 15 karakterden uzun metinler için manipulasyon yapalım
def metinKontrol(metin):
    if len(metin)>15:
        degisim = metin.replace(metin[16:],"...") 
        return f"{degisim}"
    else:
        return f"{metin}"

# 15 → Müşterileri listeleyelim

def musteriListele():
    print("Müşteri Listesi")
    print("+--------+-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+")
    print("|ID      |CompanyName            |ContactName            |Address                |Country                |City                   |")
    print("+--------+-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+")
"""        
for i in jsonCustomers["results"]:
    print(f"{i['id']}\t{i['companyName']}\t{i['contactName']}\t{i['address']}\t{i['country']}\t{i['city']}\t", end=" ")
    print("+--------+-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+")"""

# 16 → Müşterileri Id'ye göre arama yapalım
def musteriAra(musteriId):
    for i in jsonCustomers["results"]:
        if i['id']==musteriId:
            print(f"{musteriId} ID'li müşteri bulundu. Detay Listesi")
            print("==========================")
            metinKontrol(i)
            print(f"Şirketinin adı: {i['companyName']}\nUlaşılacak kişi adı: {i['contactName']}\nAdresi: {i['address']}\nÜlkesi: {i['country']}\nŞehri: {i['city']}")          
            break
        else:
            print(f"{musteriId} ID'li müşteri bulunamadı")


# 17 → Siparişleri listeleyelim
def siparisListele():  
    print("Sipariş Listesi")
    print("+--------+---------------+-------------------------------+-----------------------+-----------------------+-----------------------+")
    print("|ID      |CustomerId     |OrderDate                      |ShipAddress            |ShipCity               |ShipCountry            |")
    print("+--------+---------------+-------------------------------+-----------------------+-----------------------+-----------------------+")
"""for i in jsonOrders["results"]:
    risetimeInEpochSeconds = int(i['order']["orderDate"][6:15])
    risetimeInFormattedString = time.ctime(risetimeInEpochSeconds)
print(f"{i['order']['id']}\t{i['order']['customerId']}\t{risetimeInFormattedString}\t{i['order']['shipAddress']}\t{i['order']['shipCity']}\t{i['order']['shipCountry']}\t", end=" ")
print("+--------+-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+")"""

# 18 → Sipariş Id'ye göre arama yapalım
def siparisAra(siparisId):
    for i in jsonOrders["results"]:
        if i['order']['id']==siparisId:
            risetimeInEpochSeconds = int(i['order']["orderDate"][6:15])
            risetimeInFormattedString = time.ctime(risetimeInEpochSeconds)
            print(f"{siparisId} ID'li sipariş bulundu. Detay Listesi")
            print("==========================")
            print(f"Sipariş id : {i['order']['id']}\nMüşteri id : {i['order']['customerId']}\nSipariş tarihi : {risetimeInFormattedString}\nSipariş adresi : {i['order']['shipAddress']}\nŞehri : {i['order']['shipCity']}\nÜlkesi : {i['order']['shipCountry']}\n")
            nereye = i['order']['shipCity']          
            cevap = input(f"Kargo Rotasını {nereye.upper()} Şehri İçin Görmek İster misiniz? [e/E] :")
            if cevap.lower()=="e":
                while True:                    
                    print(f"Varış Noktası {nereye} için Rota Hesaplanacak")
                    nereden = input("Nereden Çıkacak: ")
                    mainMapApiUrl="http://www.mapquestapi.com/directions/v2/route?key=yAApx2G1tnQAa3QSNsIU0CdvnB3ZfVoA&from="+nereden+"&to="+nereye+"\""""
                    mapApi=requests.get(mainMapApiUrl)
                    mapApiorders= mapApi.json()
                    print("==========================")
                    print(f"Toplam km: {mapApiorders['route']['distance']}")
                    print(f"Toplam süre : {mapApiorders['route']['time']}")
                    print("==========================")
                    for i in mapApiorders['route']['legs']:
                        print(i['destNarrative'])
                        print(i['origNarrative'])
                        for a in i['maneuvers']:
                            print(f"{a['narrative']}")
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
            metinKontrol(i['address'])
            print(f"|{i['id']}|\t|{i['companyName']}|\t|{i['contactName']}|\t|{i['address']}|\t|{i['country']}|\t|{i['city']}|\n",end="")
        print("+--------+-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+")
    elif secim==2:
        musteriAra(input("Müşteri id giriniz:"))
    elif secim==3:
        siparisListele()
        for i in jsonOrders["results"]:
            risetimeInEpochSeconds = int(i['order']["orderDate"][6:15])
            risetimeInFormattedString = time.ctime(risetimeInEpochSeconds)
            print(f"|{i['order']['id']}|\t|{i['order']['customerId']}|\t|{risetimeInFormattedString}|\t|{i['order']['shipAddress']}|\t|{i['order']['shipCity']}|\t|{i['order']['shipCountry']}|\n",end=" ")
        print("+--------+-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+")
    elif secim==4:
        siparisAra(int(input("Lütfen Sipariş id giriniz:")))
    elif secim==5:
        break
    else:
        pass