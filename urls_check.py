import requests
from bs4 import BeautifulSoup
from aiogram import *


async def url_parser(call:types.CallbackQuery, url):
    while True:
        request = requests.get(url)
        bs4 = BeautifulSoup(request.text, "lxml" )
        item = bs4.find("div", class_="card is-lazy")

        res = ""

        price = item.find("div", class_="card-price").text.strip().replace("\n", "").replace("        ", "")
        title = item.find("a", class_="card-title").text.strip()

        res = f'{title}\n{price}'

        await call.message.answer(res)