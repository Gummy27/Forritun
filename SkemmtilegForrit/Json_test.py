from flask import Flask, json
import urllib.request

with urllib.request.urlopen("http://apis.is/petrol") as url:
    data = json.loads(url.read().decode())

cheapestPrice, companies = 0, []
for index, entry in enumerate(data['results']):
    if index == 0 or cheapestPrice > entry['bensin95']:
        cheapestPrice = entry['bensin95']
        cheapestIndex = index

    if entry['company'] not in companies:
        companies.append(entry['company'])

print(companies)

