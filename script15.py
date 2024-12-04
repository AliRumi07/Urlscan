import requests
import json
headers = {'API-Key':'6699f474-9f04-4a37-b615-0542cd6a7022','Content-Type':'application/json'}
data = {"url": "https://foodies-siter.blogspot.com/2024/12/artificial-intelligence_3.html?m=1", "visibility": "public", "country": "au"}
response = requests.post('https://urlscan.io/api/v1/scan/',headers=headers, data=json.dumps(data))
print(response)
print(response.json())
