import requests
from urllib.parse import urlparse
import json


data= "http://www.sedyt.org/centros-de-dialisis/centros-de-dialisis/27-centros-de-dialisis-en-espana/62-cataluna"
getData= requests.get(data)

newJsonData= getData.json()

print(newJsonData.text)
