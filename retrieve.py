import requests
import json

# 22 Şubat 2022 tarihinde 92410 madde içeriyordu
url = 'https://sozluk.gov.tr/gts_id'

SIZE = 92410

file = open('gtk.json', 'a')
file.write("[")

for i in range(SIZE):
    response = requests.get(url, {'id': i + 1})
    json.dump(response.json()[0], file)

    if i % 100 == 0:
        print(f"{i / SIZE * 100:.2f}% {response.json()[0]['madde']}")
        
        if i % 1000:
            file.close()
            file = open('gtk.json', 'a')

    if i != SIZE - 1:
        file.write(',')

file.write("]")