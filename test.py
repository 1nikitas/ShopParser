import requests
from bs4 import BeautifulSoup


request = requests.get("https://xn---63-5cdesg4ei.xn--p1ai/catalog/telefony/")
bs4 = BeautifulSoup(request.text, "lxml" )
items = bs4.find_all("div", class_="card is-lazy")

for item in items:
    print(item)