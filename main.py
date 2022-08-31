import asyncio
from urls_check import url_parser
from aiogram import Bot, executor, types, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import StatesGroup, State
from dotenv import load_dotenv
import os
from keyboards import keyboard_menu, phone_keyboard, computers

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

@dp.callback_query_handler(text=["1", "2"])
async def first(call: types.CallbackQuery):
    await call.answer("Парсинг запущен!")
    urls = {
        "1": "https://победа-63.рф/catalog/telefony/sotovye-telefony/",
        "2": "https://победа-63.рф/catalog/telefony/umnye-chasy-i-braslety/",
        "3": ""

    }
    await url_parser(call, urls[call.data])





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

