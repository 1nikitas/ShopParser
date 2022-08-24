from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard_menu = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='Телефоны'),
            KeyboardButton(text='Компьютерная техника')
        ],
        [
            KeyboardButton(text='Инструменты'),
            KeyboardButton(text="Игры и приставки")
        ],
        [
            KeyboardButton(text='Товары для дома'),
            KeyboardButton(text='Авто'),
        ],
        [
            KeyboardButton(text='Фото и видеотехника'),
            KeyboardButton(text='Хобби и отдых'),
        ],
        [
            KeyboardButton(text='Личные вещи'),
            KeyboardButton(text='Аудиотехника'),
        ],
        [
            KeyboardButton(text='ТВ и видео'),
            KeyboardButton(text='Товары для детей'),
        ]

    ], resize_keyboard=True, one_time_keyboard=True
)



from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

phone_keyboard = InlineKeyboardMarkup(row_width=2,
                                       inline_keyboard=[
                                           [InlineKeyboardButton(text='Телефоны', callback_data='Сообщение'),
                                            InlineKeyboardButton(text="Умные Часы", callback_data="Где-то тут ссылка)")
                                            ],
                                           [InlineKeyboardButton(text='Науники', callback_data='Сообщение'),
                                            InlineKeyboardButton(text="Телефоны для офиса", callback_data="Где-то тут ссылка)")
                                            ],
                                            [InlineKeyboardButton(text='Рации', callback_data='Сообщение'),
                                            InlineKeyboardButton(text="Зарядные устройства", callback_data="Где-то тут ссылка)")
                                            ],
                                            [
                                            InlineKeyboardButton(text="Зарядные устройства", callback_data="Где-то тут ссылка)"),
                                            InlineKeyboardButton(text="Iphone SALE", callback_data="Где-то тут ссылка)")
                                            ],
                                            [InlineKeyboardButton(text='Наушники SALE', callback_data='Сообщение'),
                                            InlineKeyboardButton(text="Телефоны SALE", callback_data="Где-то тут ссылка)")
                                            ],


                                       ]
                                    )

computers = InlineKeyboardMarkup(row_width=2,
                                       inline_keyboard=[
                                           [InlineKeyboardButton(text='Ноутбуку', callback_data='Сообщение'),
                                            InlineKeyboardButton(text="Системные блоки", callback_data="Где-то тут ссылка)")
                                            ],
                                           [InlineKeyboardButton(text='Мониторы', callback_data='Сообщение'),
                                            InlineKeyboardButton(text="Моноблоки", callback_data="Где-то тут ссылка)")
                                            ],
                                            [InlineKeyboardButton(text='Компьютерные мыши', callback_data='Сообщение'),
                                            InlineKeyboardButton(text="Клавиатуры", callback_data="Где-то тут ссылка)")
                                            ],
                                            [
                                            InlineKeyboardButton(text="Наушники", callback_data="Где-то тут ссылка)"),
                                            InlineKeyboardButton(text="WEB-камеры", callback_data="Где-то тут ссылка)")
                                            ],
                                            [InlineKeyboardButton(text='Планшеты', callback_data='Сообщение'),
                                            InlineKeyboardButton(text="Электронные книги", callback_data="Где-то тут ссылка)")
                                            ],


                                       ]
                                    )