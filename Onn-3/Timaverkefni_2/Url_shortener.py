import random
import string
import csv

urls = {}

with open('Urls.csv', 'r') as file:
    for entry in list(csv.reader(file, delimiter='\n'))[0]:
        short, long = entry.split(',')
        urls[short] = long

url = input()
if url[0:6] == 'sho.rt':
    print(urls[url])
else:
    try:
        print(urls[url])
    except KeyError:
        urls["sho.rt/"+''.join(random.choices(string.ascii_lowercase + string.digits, k=6))] = url
        print(urls)

with open('Urls.csv', 'w') as file:
    for short, long in urls.items():
        file.write(f"{short},{long}\n")