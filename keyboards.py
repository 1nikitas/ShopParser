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


start_keyboard = InlineKeyboardMarkup(row_width=2,
                                       inline_keyboard=[

                                             [InlineKeyboardButton(text="Начать отслеживание", callback_data="Начать отслеживание")]


                                       ]
                                    )

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
                                             [InlineKeyboardButton(text="НАЗАД", callback_data="Где-то тут ссылка)")]


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
                                            InlineKeyboardButton(text="Электронные книги", callback_data="Где-то тут ссылка)")],
                                            [
                                            InlineKeyboardButton(text="НАЗАД", callback_data="Где-то тут ссылка)"),

                                            ],


                                       ]
                                    )


tools = InlineKeyboardMarkup(row_width=2,
                                       inline_keyboard=[
                                           [InlineKeyboardButton(text='Измерительные инструменты', callback_data='Сообщение'),
                                            InlineKeyboardButton(text="Спецодежда", callback_data="Где-то тут ссылка)")
                                            ],
                                           [InlineKeyboardButton(text='Электроинструменты', callback_data='Сообщение'),
                                            InlineKeyboardButton(text="Ручной инструмень", callback_data="Где-то тут ссылка)")
                                            ],
                                            [InlineKeyboardButton(text='Сварочное оборудование', callback_data='Сообщение'),
                                            InlineKeyboardButton(text="Бензоинструмент", callback_data="Где-то тут ссылка)")
                                            ],
                                            [
                                            InlineKeyboardButton(text="Пневмоинструмент", callback_data="Где-то тут ссылка)"),
                                            InlineKeyboardButton(text="Светотехника", callback_data="Где-то тут ссылка)")
                                            ],
                                           [
                                               InlineKeyboardButton(text="Перфоратор SALE",
                                                                    callback_data="Где-то тут ссылка)"),
                                               InlineKeyboardButton(text="Шуруповерт SALE",
                                                                    callback_data="Где-то тут ссылка)")
                                           ],
                                            [InlineKeyboardButton(text='Техника для сада', callback_data='Сообщение'),
                                            InlineKeyboardButton(text="НАЗАД", callback_data="Где-то тут ссылка)")
                                            ],


                                       ]
                                    )


games = InlineKeyboardMarkup(row_width=2,
                                       inline_keyboard=[
                                           [InlineKeyboardButton(text='Игровые приставки', callback_data='Сообщение'),
                                            InlineKeyboardButton(text="Игры для приставок", callback_data="Где-то тут ссылка)")
                                            ],
                                           [InlineKeyboardButton(text='Аксессуары для игровых приставок', callback_data='Сообщение'),
                                            InlineKeyboardButton(text="Настольные игры", callback_data="Где-то тут ссылка)")
                                            ],
                                            ]
                                    )


home = InlineKeyboardMarkup(row_width=2,
                                       inline_keyboard=[
                                           [InlineKeyboardButton(text='Мультиварки', callback_data='Сообщение'),
                                            InlineKeyboardButton(text="Климатическое оборудование", callback_data="Где-то тут ссылка)")
                                            ],
                                           [InlineKeyboardButton(text='Микроволновые печи', callback_data='Сообщение'),
                                            InlineKeyboardButton(text="Пылесосы", callback_data="Где-то тут ссылка)")
                                            ],
                                            [InlineKeyboardButton(text='Мебель и интерьер', callback_data='Сообщение'),
                                            InlineKeyboardButton(text="Стиральные машины", callback_data="Где-то тут ссылка)")
                                            ],
                                            [
                                            InlineKeyboardButton(text="Товары для красоты и здоровья", callback_data="Где-то тут ссылка)"),
                                            InlineKeyboardButton(text="Товары для кухни", callback_data="Где-то тут ссылка)")
                                            ],
                                           [
                                               InlineKeyboardButton(text="Утюги и отпариватели",
                                                                    callback_data="Где-то тут ссылка)"),
                                               InlineKeyboardButton(text="Чайники и кофеварки",
                                                                    callback_data="Где-то тут ссылка)")
                                           ],
                                            [InlineKeyboardButton(text='Холодильники и морозильники', callback_data='Сообщение'),
                                            InlineKeyboardButton(text="Швейные машины", callback_data="Где-то тут ссылка)")
                                            ],
                                            [InlineKeyboardButton(text='Бритвы и машинки для стрижки', callback_data='Сообщение'),
                                            InlineKeyboardButton(text="Фены и плойки", callback_data="Где-то тут ссылка)")
                                            ],
                                            [InlineKeyboardButton(text='Весы ', callback_data='Сообщение'),
                                            InlineKeyboardButton(text="Электрические плиты", callback_data="Где-то тут ссылка)")
                                            ],


                                       ]
                                    )