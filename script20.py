import requests
import json
headers = {'API-Key':'e8c76f39-847e-41f0-a668-7d1e266f713b','Content-Type':'application/json'}
data = {"url": "https://foodies-siter.blogspot.com/2024/12/adcash.html", "visibility": "public", "country": "at"}
response = requests.post('https://urlscan.io/api/v1/scan/',headers=headers, data=json.dumps(data))
print(response)
print(response.json())
