import requests
import json

# 22 Şubat 2022 tarihinde 92410 madde içeriyordu
url = 'https://sozluk.gov.tr/gts_id'

sozluk = []

for i in range(92410):
    response = requests.get(url, {'id': i + 1})
    sozluk.append(response.json()[0])
    print(f"{i / 924.10:.3f}% {response.json()[0]['madde']}")

with open('gtk.json', 'w') as outfile: # gtk.json dosyasına yazdır
    json.dump(sozluk, outfile, indent=4)
