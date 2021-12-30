import requests
nereye="Marseille"
nereden= input("ş:")
mainMapApiUrl="http://www.mapquestapi.com/directions/v2/route?key=yAApx2G1tnQAa3QSNsIU0CdvnB3ZfVoA&from="+nereden+"&to="+nereye+"\""""
mapApi=requests.get(mainMapApiUrl)
#print(mapApi.text)
mapApiorders= mapApi.json()
print(mapApiorders)
