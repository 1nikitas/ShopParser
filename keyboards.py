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
                                           [InlineKeyboardButton(text='Телефоны', callback_data='1'),
                                            InlineKeyboardButton(text="Умные Часы", callback_data="2")
                                            ],
                                           [InlineKeyboardButton(text='Науники', callback_data='3'),
                                            InlineKeyboardButton(text="Телефоны для офиса", callback_data="4")
                                            ],
                                            [InlineKeyboardButton(text='Рации', callback_data='5'),
                                            InlineKeyboardButton(text="Зарядные устройства", callback_data="6")
                                            ],
                                            [
                                            InlineKeyboardButton(text="Зарядные устройства", callback_data="7"),
                                            InlineKeyboardButton(text="Iphone SALE", callback_data="8")
                                            ],
                                            [InlineKeyboardButton(text='Наушники SALE', callback_data='9'),
                                            InlineKeyboardButton(text="Телефоны SALE", callback_data="10")
                                            ],


                                       ]
                                    )

computers = InlineKeyboardMarkup(row_width=2,
                                       inline_keyboard=[
                                           [InlineKeyboardButton(text='Ноутбуку', callback_data='11'),
                                            InlineKeyboardButton(text="Системные блоки", callback_data="12")
                                            ],
                                           [InlineKeyboardButton(text='Мониторы', callback_data='13'),
                                            InlineKeyboardButton(text="Моноблоки", callback_data="14")
                                            ],
                                            [InlineKeyboardButton(text='Компьютерные мыши', callback_data='15'),
                                            InlineKeyboardButton(text="Клавиатуры", callback_data="16")
                                            ],
                                            [
                                            InlineKeyboardButton(text="Наушники", callback_data="17"),
                                            InlineKeyboardButton(text="WEB-камеры", callback_data="18")
                                            ],
                                            [InlineKeyboardButton(text='Планшеты', callback_data='19'),
                                            InlineKeyboardButton(text="Электронные книги", callback_data="20")
                                            ],


                                       ]
                                    )


tools = InlineKeyboardMarkup(row_width=2,
                                       inline_keyboard=[
                                           [InlineKeyboardButton(text='Измерительные инструменты', callback_data='11'),
                                            InlineKeyboardButton(text="Спецодежда", callback_data="12")
                                            ],
                                           [InlineKeyboardButton(text='Электроинструмент', callback_data='13'),
                                            InlineKeyboardButton(text="Ручной инструмент", callback_data="14")
                                            ],
                                            [InlineKeyboardButton(text='Сварочное оборудование ', callback_data='15'),
                                            InlineKeyboardButton(text="Клавиатуры", callback_data="16")
                                            ],
                                            [
                                            InlineKeyboardButton(text="Наушники", callback_data="17"),
                                            InlineKeyboardButton(text="WEB-камеры", callback_data="18")
                                            ],
                                            [InlineKeyboardButton(text='Планшеты', callback_data='19'),
                                            InlineKeyboardButton(text="Электронные книги", callback_data="20")
                                            ],


                                       ]
                                    )