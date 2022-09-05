import asyncio
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
        "22": "https://победа-63.рф/catalog/instrument/izmeritelnye-instrumenty/",
        "23": "https://победа-63.рф/catalog/instrument/specodejda/",
        "24": "https://победа-63.рф/catalog/instrument/elektroinstrument/",
        "25": "https://победа-63.рф/catalog/instrument/ruchnoi-instrument/",
        "26": "https://победа-63.рф/catalog/instrument/svarochnoe-oborudovanie/",
        "27": "https://победа-63.рф/catalog/instrument/benzoinstrument/",
        "28": "https://победа-63.рф/catalog/instrument/pnevmoinstrument/",
        "29": "https://победа-63.рф/catalog/instrument/svetotehnika/",
        "30": "https://победа-63.рф/catalog/instrument/tehnika-dlya-sada/",
        "31": "https://победа-63.рф/catalog/tovary-dlya-doma/multivarki/",
        "32": "https://победа-63.рф/catalog/tovary-dlya-doma/klimaticheskoe-oborudovanie/",
        "33": "https://победа-63.рф/catalog/tovary-dlya-doma/mebel-i-interer/",
        "34": "https://победа-63.рф/catalog/tovary-dlya-doma/mikrovolnovye-pechi/",
        "35": "https://победа-63.рф/catalog/tovary-dlya-doma/pylesosy/",
        "36": "https://победа-63.рф/catalog/tovary-dlya-doma/stiralnye-mashiny/",
        "37": "https://победа-63.рф/catalog/tovary-dlya-doma/tovary-dlya-krasoty-i-zdorovya/",
        "38": "https://победа-63.рф/catalog/tovary-dlya-doma/tovary-dlya-kuhni/",
        "39": "https://победа-63.рф/catalog/tovary-dlya-doma/utyugi-i-otparivateli/",
        "40": "https://победа-63.рф/catalog/tovary-dlya-doma/chainiki-i-kofevarki/",
        "41": "https://победа-63.рф/catalog/tovary-dlya-doma/elektricheskie-plity/",
        "45": "https://победа-63.рф/catalog/tovary-dlya-doma/shveinye-mashiny/",
        "46": "https://победа-63.рф/catalog/tovary-dlya-doma/britvy-i-mashinki-dlya-strijki/",
        "47": "https://победа-63.рф/catalog/tovary-dlya-doma/feny-i-ploiki/",
        "48": "https://победа-63.рф/catalog/tovary-dlya-doma/vesy/",
        "50": "https://победа-63.рф/catalog/igry-i-pristavki/igrovye-pristavki/",
        "51": "https://победа-63.рф/catalog/igry-i-pristavki/igry-dlya-pristavok/",
        "52": "https://победа-63.рф/catalog/igry-i-pristavki/aksessuary-dlya-igrovyh-pristavok/",
        "53": "https://победа-63.рф/catalog/igry-i-pristavki/nastolnye-igry/",
        "54": "https://победа-63.рф/catalog/avto/moiki-vysokogo-davleniya/",
        "55": "https://победа-63.рф/catalog/avto/nasosy-i-kompressory/",
        "56": "https://победа-63.рф/catalog/avto/avtomagnitoly/",
        "57": "https://победа-63.рф/catalog/avto/avtomobilnye-aksessuary-i-komplektuyucshie/",
        "58": "https://победа-63.рф/catalog/avto/avtomobilnye-kolonki/",
        "59": "https://победа-63.рф/catalog/avto/avtomobilnye-sabvufery/",
        "60": "https://победа-63.рф/catalog/avto/avtomobilnye-usiliteli/",
        "61": "https://победа-63.рф/catalog/avto/parktroniki-i-signalizaciya/",
        "62": "https://победа-63.рф/catalog/avto/videoregistratory/",
        "63": "https://победа-63.рф/catalog/avto/navigatory/",
        "64": "https://победа-63.рф/catalog/avto/radardetektory/",
        "65": "https://победа-63.рф/catalog/avto/shiny-i-diski/",
        "66": "https://победа-63.рф/catalog/foto-i-videotehnika/fotoramki/",
        "67": "https://победа-63.рф/catalog/foto-i-videotehnika/fotoapparaty/",
        "68": "https://победа-63.рф/catalog/foto-i-videotehnika/videokamery/",
        "69": "https://победа-63.рф/catalog/foto-i-videotehnika/aksessuary-dlya-foto-i-videokamer/",
        "70": "https://победа-63.рф/catalog/hobbi-i-otdyh/zimnii-sportivnyi-inventar/",
        "71": "https://победа-63.рф/catalog/hobbi-i-otdyh/mototehnika/",
        "72": "https://победа-63.рф/catalog/hobbi-i-otdyh/metalloiskateli/",
        "73": "https://победа-63.рф/catalog/hobbi-i-otdyh/binokli-i-optika/",
        "74": "https://победа-63.рф/catalog/hobbi-i-otdyh/vodnyi-inventar/",
        "75": "https://победа-63.рф/catalog/hobbi-i-otdyh/tatumashinki/",
        "76": "https://победа-63.рф/catalog/hobbi-i-otdyh/velosipedy-i-samokaty/",
        "77": "https://победа-63.рф/catalog/hobbi-i-otdyh/pnevmatika-i-elektroshokery/",
        "78": "https://победа-63.рф/catalog/hobbi-i-otdyh/sportivnyi-inventar/",
        "79": "https://победа-63.рф/catalog/hobbi-i-otdyh/tovary-dlya-jivotnyh/",
        "80": "https://победа-63.рф/catalog/hobbi-i-otdyh/trenajery/",
        "81": "https://победа-63.рф/catalog/hobbi-i-otdyh/rolikovye-i-ledovye-konki/",
        "82": "https://победа-63.рф/catalog/hobbi-i-otdyh/turizm/",
        "83": "https://победа-63.рф/catalog/hobbi-i-otdyh/kvadrokoptery/",
        "84": "https://победа-63.рф/catalog/hobbi-i-otdyh/kollekcionirovanie/",
        "85": "https://победа-63.рф/catalog/lichnye-vecshi/obuv/",
        "86": "https://победа-63.рф/catalog/lichnye-vecshi/kanctovary/",
        "87": "https://победа-63.рф/catalog/lichnye-vecshi/verhnyaya-odejda/",
        "88": "https://победа-63.рф/catalog/lichnye-vecshi/chasy/",
        "89": "https://победа-63.рф/catalog/lichnye-vecshi/koshelki-i-sumki/",
        "90": "https://победа-63.рф/catalog/audiotehnika/muzykalnye-instrumenty/",
        "91": "https://победа-63.рф/catalog/audiotehnika/mp3-pleery/",
        "92": "https://победа-63.рф/catalog/audiotehnika/kolonki/",
        "93": "https://победа-63.рф/catalog/audiotehnika/domashnie-kinoteatry/",
        "94": "https://победа-63.рф/catalog/audiotehnika/muzykalnye-centry/",
        "95": "https://победа-63.рф/catalog/audiotehnika/resivery/",
        "96": "https://победа-63.рф/catalog/tv-i-video/televizory/",
        "97": "https://победа-63.рф/catalog/tv-i-video/video/",
        "98": "https://победа-63.рф/catalog/tv-i-video/proektory/",
        "99": "https://победа-63.рф/catalog/tv-i-video/cifrovoe-televidenie/",
        "100": "https://победа-63.рф/catalog/tv-i-video/aksessuary-dlya-tv-i-video/",
        "101": "https://победа-63.рф/catalog/tovary-dlya-detei/detskie-avtokresla/",
        "102": "https://победа-63.рф/catalog/tovary-dlya-detei/detskie-igrushki/",
        "103": "https://победа-63.рф/catalog/tovary-dlya-detei/detskie-kolyaski/",
        "104": "https://победа-63.рф/catalog/tovary-dlya-detei/radio-i-video-nyani/",
        "105": "https://победа-63.рф/catalog/tovary-dlya-detei/tovary-dlya-mladencev/"
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

