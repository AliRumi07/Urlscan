import requests
import json
headers = {'API-Key':'6699f474-9f04-4a37-b615-0542cd6a7022','Content-Type':'application/json'}
data = {"url": "https://foodies-siter.blogspot.com/2024/11/how-to-boil-eggs.html", "visibility": "public", "country": "pt", "useragent": "Mozilla/5.0 (Linux; Android 13; Motorola Edge 30) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"}
response = requests.post('https://urlscan.io/api/v1/scan/',headers=headers, data=json.dumps(data))
print(response)
print(response.json())
