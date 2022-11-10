import requests
from pprint import pprint

try:
    txt = "http://ip-api.com/json/"
    ip_adr = input("Write IP adress: ")
    response = requests.get(txt + ip_adr)
    dct = response.json()
    print("Country: ", dct['country'])
except KeyError:
    print("Таĸого IP не существует")
