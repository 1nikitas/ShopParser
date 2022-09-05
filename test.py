import requests as requests
from bs4 import BeautifulSoup
url = "https://xn---63-5cdesg4ei.xn--p1ai/catalog/telefony/sotovye-telefony/"
request = requests.get(url)
bs4 = BeautifulSoup(request.text, "lxml")
item = bs4.find("div", class_="card is-lazy")

res = ""

price = item.find("div", class_="card-price").text.strip().replace("\n", "").replace("        ", "")
title = item.find("a", class_="card-title").text.strip()
href = item.find('a', class_="card-images-wrapper")['href']
city = item.find("div", class_="card-city").text.strip()
print(city)