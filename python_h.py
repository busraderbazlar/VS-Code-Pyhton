import requests
from urllib.parse import urlparse
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
"""
def musteriListele():
    print("Müşteri Listesi")
    print("+--------+-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+")
    print("|ID      |CompanyName            |ContactName            |Address                |Country                |City                   |")
    print("+--------+-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+")
musteriListele()

for i in jsonCustomers["results"]:
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
musteriAra("PRINI")

