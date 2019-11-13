import random
import string
import csv
import webbrowser
import requests

urlsSh, urlsLo = {}, {}
with open('Urls.csv', 'r') as file:
    for entry in csv.reader(file, delimiter='\n'):
        short, long = entry[0].split(',')
        urlsSh[short] = long
        urlsLo[long] = short

url = ""
while url.lower() != 'quit':
    print("To quit program type Quit")
    print("Only full links. Example: https://mbl.is/")
    url = input("Url here. : ")

    if url[0:6] == 'sho.rt':
        try:
            print(f"Long link: {urlsSh[url]}")
            webbrowser.open(urlsSh[url], new=2)
        except:
            print("This is not a valid short link!")

    elif url == 'quit':
        print("Goodbye. Your short links are still stored for future purposes")

    else:
        try:
            print(f"Short link: {urlsLo[url]}")
        except KeyError:
            try:
                request = requests.get(url)

                shortLink = "sho.rt/" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
                print(f"New short link: {shortLink}")
                urlsSh[shortLink] = url
                urlsLo[url] = shortLink

            except:
                print("Sry, this is not a valid link!")


    with open('Urls.csv', 'w') as file:
        for short, long in urlsSh.items():
            file.write(f"{short},{long}\n")
