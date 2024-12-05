import requests
import json
headers = {'API-Key':'e8c76f39-847e-41f0-a668-7d1e266f713b','Content-Type':'application/json'}
data = {"url": "https://foodies-siter.blogspot.com/2024/11/apple-muffin.html", "visibility": "public", "country": "se", "useragent": "Mozilla/5.0 (Linux; Android 12; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36""Mozilla/5.0 (Linux; Android 12; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"}
response = requests.post('https://urlscan.io/api/v1/scan/',headers=headers, data=json.dumps(data))
print(response)
print(response.json())
