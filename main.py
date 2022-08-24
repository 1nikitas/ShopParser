from aiogram import Bot, executor, types, Dispatcher
from aiogram.dispatcher.filters import Command
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

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)