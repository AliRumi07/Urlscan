import requests
import json
headers = {'API-Key':'e8c76f39-847e-41f0-a668-7d1e266f713b','Content-Type':'application/json'}
data = {"url": "https://link-target.net/1249104/entertainment", "visibility": "public", "country": "au", "useragent": "Mozilla/5.0 (Linux; Android 13; Sony Xperia 1 IV) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"}
response = requests.post('https://urlscan.io/api/v1/scan/',headers=headers, data=json.dumps(data))
print(response)
print(response.json())
