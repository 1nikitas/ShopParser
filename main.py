import asyncio
from urls_check import url_parser
from aiogram import Bot, executor, types, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import StatesGroup, State
from dotenv import load_dotenv
import os
from keyboards import keyboard_menu, phone_keyboard, computers
from db import Database
load_dotenv()


bot = Bot(token=os.getenv("TOKEN"))
dp = Dispatcher(bot)



@dp.message_handler(Command('start'))
async def start(message: types.Message):
    await message.answer("Выберите категорию товара для отслеживания", reply_markup=keyboard_menu)


@dp.message_handler(text="Телефоны")
async def phones(message: types.Message):
    await message.answer("Выберите подкатегорию для поиска", reply_markup=phone_keyboard)


@dp.message_handler(text="Компьютерная техника")
async def phones(message: types.Message):
    await message.answer("Выберите подкатегорию для поиска", reply_markup=computers)

@dp.callback_query_handler(text=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])
async def first(call: types.CallbackQuery):
    await call.answer("Парсинг запущен!")
    urls = {
        "1": "https://победа-63.рф/catalog/telefony/sotovye-telefony/",
        "2": "https://победа-63.рф/catalog/telefony/umnye-chasy-i-braslety/",
        "3": "https://победа-63.рф/catalog/telefony/naushniki-dlya-telefonov/",
        "4": "https://победа-63.рф/catalog/telefony/telefony-dlya-doma-i-ofisa/",
        "5": "https://победа-63.рф/catalog/telefony/racii/",
        "6": "https://победа-63.рф/catalog/telefony/zaryadnye-ustroistva/",
        "7": "https://победа-63.рф/catalog/telefony/aksessuary-dlya-telefonov/",
        "8": "https://победа-63.рф/catalog/telefony/sotovye-telefony/?q=20&s=new&c=0&cg=143&a=0&p_0[]=1&b[]=81&",
        "9": "https://победа-63.рф/catalog/telefony/naushniki-dlya-telefonov/?q=20&s=new&c=0&cg=585&a=0&p_0[]=1&",
        "10": "https://победа-63.рф/catalog/telefony/sotovye-telefony/?q=20&s=new&c=0&cg=143&a=0&p_0[]=1&",
        "11": "https://победа-63.рф/catalog/kompyuternaya-tehnika/noutbuki/",
        "12": "https://победа-63.рф/catalog/kompyuternaya-tehnika/sistemnye-bloki//",
        "13": "https://победа-63.рф/catalog/kompyuternaya-tehnika/monitory/",
        "14": "https://победа-63.рф/catalog/kompyuternaya-tehnika/monobloki/",
        "15": "https://победа-63.рф/catalog/kompyuternaya-tehnika/kompyuternye-myshi/",
        "16": "https://победа-63.рф/catalog/kompyuternaya-tehnika/klaviatury/",
        "17": "https://победа-63.рф/catalog/kompyuternaya-tehnika/kompyuternye-garnitury-i-naushniki/",
        "18": "https://победа-63.рф/catalog/kompyuternaya-tehnika/webkamery/",
        "19": "https://победа-63.рф/catalog/kompyuternaya-tehnika/planshetnye-pk/",
        "20": "https://победа-63.рф/catalog/kompyuternaya-tehnika/elektronnye-knigi/",
        "21": "https://победа-63.рф/catalog/kompyuternaya-tehnika/printery-i-mfu/",
        "22": "https://победа-63.рф/catalog/kompyuternaya-tehnika/routery-i-modemy/",
        "23": "https://победа-63.рф/catalog/kompyuternaya-tehnika/jestkie-diski/",
        "24": "https://победа-63.рф/catalog/kompyuternaya-tehnika/prochaya-orgtehnika/",
        "25": "https://победа-63.рф/catalog/kompyuternaya-tehnika/setevye-filtry-i-udliniteli/",
        "26": "https://победа-63.рф/catalog/kompyuternaya-tehnika/aksessuary-dlya-kompyuterov/",



    }
    await asyncio.create_task(url_parser(call, urls[call.data]))
    await asyncio.sleep(1)





async def main1():
    await dp.start_polling()

async def main2():
    while True:
        await asyncio.sleep(1)

async def main_task():
    await asyncio.gather(
        main1(),
        main2()
    )


while True:
    asyncio.get_event_loop().run_until_complete(main_task())

