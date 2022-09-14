import asyncio

import requests
from bs4 import BeautifulSoup
from aiogram import *
from db import Database
db = Database("items.db")

async def url_parser(call:types.CallbackQuery, url):
    request = requests.get(url)
    bs4 = BeautifulSoup(request.text, "lxml")
    group =  bs4.find("div", "filter-header--title").find("h1").text
    await call.message.answer(f'Парсинг по категории {group} запущен!')
    while True:
        request = requests.get(url)
        bs4 = BeautifulSoup(request.text, "lxml" )
        items = bs4.find_all("div", class_="card is-lazy")
        for item in items:
            res = ""
            price = item.find("div", class_="card-price").text.strip().replace("\n", "").replace("        ", "")
            title = item.find("a", class_="card-title").text.strip()
            href = item.find('a', class_="card-images-wrapper")['href']
            city = item.find("div", class_="card-city").text.strip()
            if db.item_exists(href):
                await asyncio.sleep(1)
            else:
                db.add_item(href)
                res = f'{title}\n{price}\n{city}\n{href}'
                await call.message.answer(res)
