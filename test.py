import asyncio
import signal

from urls_check import url_parser
from aiogram import Bot, executor, types, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import StatesGroup, State
from dotenv import load_dotenv
import os
from keyboards import keyboard_menu, phone_keyboard, computers, tools, for_home, audio, auto, TV, baby, hobby, clothers, photo, gamess
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

@dp.message_handler(text="Инструменты")
async def phones(message: types.Message):
    await message.answer("Выберите подкатегорию для поиска", reply_markup=tools)

@dp.message_handler(text="Товары для дома")
async def phones(message: types.Message):
    await message.answer("Выберите подкатегорию для поиска", reply_markup=for_home)

@dp.message_handler(text="Игры и приставки")
async def games(message: types.Message):
    await message.answer("Выберите подкатегорию для поиска", reply_markup=gamess)

@dp.message_handler(text="Авто")
async def games(message: types.Message):
    await message.answer("Выберите подкатегорию для поиска", reply_markup=auto)

@dp.message_handler(text="Фото и видеотехника")
async def games(message: types.Message):
    await message.answer("Выберите подкатегорию для поиска", reply_markup=photo)

@dp.message_handler(text="Хобби и отдых")
async def games(message: types.Message):
    await message.answer("Выберите подкатегорию для поиска", reply_markup=hobby)

@dp.message_handler(text="Личные вещи")
async def games(message: types.Message):
    await message.answer("Выберите подкатегорию для поиска", reply_markup=clothers)

@dp.message_handler(text="Аудиотехника")
async def games(message: types.Message):
    await message.answer("Выберите подкатегорию для поиска", reply_markup=audio)

@dp.message_handler(text="ТВ и Видео")
async def games(message: types.Message):
    await message.answer("Выберите подкатегорию для поиска", reply_markup=TV)

@dp.message_handler(text="Товары для детей")
async def games(message: types.Message):
    await message.answer("Выберите подкатегорию для поиска", reply_markup=baby)

@dp.callback_query_handler(text="21")
async def start(call: types.CallbackQuery):
    await call.message.answer("Выберите категорию товара для отслеживания", reply_markup=keyboard_menu)

@dp.callback_query_handler(text=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
                                "11","12","13","14","15","16","17","18","19","20",
                                 "21","22","23","24","25","26","27","28","29","30",
                                 "31","32","33","34","35","36","37","38","39","40",
                                 "41","42","43","44","45","46","47","48","49","50","51",
                                 "52","53","54","55","56","57","58","59","60",
                                 "61","62","63","64","65","66","67","68","69","70",
                                 "71","72","73","74","75","76","77","78","79","80",
                                 "81","82","83","84","85","86","87","88","89","90",
                                 "91","92","93","94","95","96","97","98","99","100",
                                 "101","102","103","104","105"])

#def stop():
#    for task in listeners:
#        task.cancel()
#    loop.stop()

async def first(call: types.CallbackQuery):
    await call.answer("Парсинг запущен!")
    urls = {
        "1": ["https://победа-63.рф/catalog/telefony/sotovye-telefony/", 0]

    }
    urls[call.data[1]] += 1
    if urls[call.data[1]] % 2 == 0:
        await asyncio.get_event_loop().add_signal_handler(signal.SIGINT, stop)
    await asyncio.create_task(url_parser(call, urls[call.data[0]]))
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

