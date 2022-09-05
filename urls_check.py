import asyncio

import requests
from bs4 import BeautifulSoup
from aiogram import *
from db import Database
db = Database("items.db")

async def url_parser(call:types.CallbackQuery, url):
    while True:
        request = requests.get(url)
        bs4 = BeautifulSoup(request.text, "lxml" )
        item = bs4.find("div", class_="card is-lazy")

        res = ""

        price = item.find("div", class_="card-price").text.strip().replace("\n", "").replace("        ", "")
        title = item.find("a", class_="card-title").text.strip()
        href = item.find('a', class_="card-images-wrapper")['href']
        city = item.find("div", class_="card-city").text.strip()
        if db.item_exists(title):
            await asyncio.sleep(1)
        else:
            db.add_item(title)
            res = f'{title}\n{price}\n{city}\n{href}'
            await call.message.answer(res)
