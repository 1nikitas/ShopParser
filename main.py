from aiogram import Bot, executor, types, Dispatcher
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import State, StatesGroup
from dotenv import load_dotenv
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from keyboards import keyboard_menu, phone_keyboard, computers, tools, games, home, start_keyboard


load_dotenv()

memory = MemoryStorage()
bot = Bot(token=os.getenv("TOKEN"))
dp = Dispatcher(bot, storage=memory)


class Items(StatesGroup):
    item1 = State()
    item2 = State()
    item3 = State()


@dp.message_handler(Command('start'))
async def start(message: types.Message):
    await message.answer("Выберите категорию товара для отслеживания", reply_markup=start_keyboard)




@dp.callback_query_handler(text="Начать отслеживание")
async def PM(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Выберите категорию товара",
                         reply_markup=keyboard_menu)


@dp.message_handler(text="Телефоны")
async def phones(message: types.Message):
    await message.answer("Выберите подкатегорию для отслеживания", reply_markup=phone_keyboard)


@dp.message_handler(text="Компьютерная техника")
async def phones(message: types.Message):
    await message.answer("Выберите подкатегорию для отслеживания", reply_markup=computers)


@dp.message_handler(text="Инструменты")
async def phones(message: types.Message):
    await message.answer("Выберите подкатегорию для отслеживания", reply_markup=tools)


@dp.message_handler(text="Игры и приставки")
async def phones(message: types.Message):
    await message.answer("Выберите подкатегорию для отслеживания", reply_markup=games)


@dp.message_handler(text="Товары для дома")
async def phones(message: types.Message):
    await message.answer("Выберите подкатегорию для отслеживания", reply_markup=home)

@dp.message_handler(text="Авто")
async def phones(message: types.Message):
    await message.answer("Выберите подкатегорию для отслеживания", reply_markup=tools)


@dp.message_handler(text="Фото и видеотехника")
async def phones(message: types.Message):
    await message.answer("Выберите подкатегорию для отслеживания", reply_markup=tools)


@dp.message_handler(text="Хобби и отдых")
async def phones(message: types.Message):
    await message.answer("Выберите подкатегорию для отслеживания", reply_markup=tools)


@dp.message_handler(text="Личные вещи")
async def phones(message: types.Message):
    await message.answer("Выберите подкатегорию для отслеживания", reply_markup=tools)


@dp.message_handler(text="Аудиотехника")
async def phones(message: types.Message):
    await message.answer("Выберите подкатегорию для отслеживания", reply_markup=tools)

@dp.message_handler(text="Товары для дома")
async def phones(message: types.Message):
    await message.answer("Выберите подкатегорию для отслеживания", reply_markup=tools)


@dp.message_handler(text="ТВ и Видео")
async def phones(message: types.Message):
    await message.answer("Выберите подкатегорию для отслеживания", reply_markup=tools)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)