import requests
import json
headers = {'API-Key':'e8c76f39-847e-41f0-a668-7d1e266f713b','Content-Type':'application/json'}
data = {"url": "https://entertainment-era.onrender.com/", "visibility": "public", "country": "at", "useragent": "Mozilla/5.0 (Linux; Android 14; Asus ROG Phone 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"}
response = requests.post('https://urlscan.io/api/v1/scan/',headers=headers, data=json.dumps(data))
print(response)
print(response.json())
