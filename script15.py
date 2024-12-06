import requests
import json
headers = {'API-Key':'6699f474-9f04-4a37-b615-0542cd6a7022','Content-Type':'application/json'}
data = {"url": "https://foodies-siter.blogspot.com/2024/11/dunkin-donuts-french-cruller.html", "visibility": "public", "country": "au", "useragent": "Mozilla/5.0 (Linux; Android 13; Sony Xperia 1 IV) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"}
response = requests.post('https://urlscan.io/api/v1/scan/',headers=headers, data=json.dumps(data))
print(response)
print(response.json())
