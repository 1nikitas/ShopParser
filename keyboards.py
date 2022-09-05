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
                                           [
                                            InlineKeyboardButton(text="НАЗАД", callback_data="21")
                                           ]


                                       ]
                                    )



tools = InlineKeyboardMarkup(row_width=2,
                                       inline_keyboard=[
                                           [InlineKeyboardButton(text='Измерительные инструменты', callback_data='22'),
                                            InlineKeyboardButton(text="Спецодежда", callback_data="23")
                                            ],
                                           [InlineKeyboardButton(text='Электроинструмент', callback_data='24'),
                                            InlineKeyboardButton(text="Ручной инструмент", callback_data="25")
                                            ],
                                            [InlineKeyboardButton(text='Сварочное оборудование ', callback_data='26'),
                                            InlineKeyboardButton(text="Бензоинструмент", callback_data="27")
                                            ],
                                            [
                                            InlineKeyboardButton(text="Пневмоинструмент", callback_data="28"),
                                            InlineKeyboardButton(text="Светотехника", callback_data="29")
                                            ],
                                            [InlineKeyboardButton(text='Техника для сада', callback_data='30'),
                                            InlineKeyboardButton(text="НАЗАД", callback_data="21")
                                            ],


                                       ]
                                    )




for_home = InlineKeyboardMarkup(row_width=2,
                                       inline_keyboard=[
                                           [InlineKeyboardButton(text='Мультиварки', callback_data='31'),
                                            InlineKeyboardButton(text="Климатическое оборудование", callback_data="32")
                                            ],
                                           [InlineKeyboardButton(text='Мебель и интерьер', callback_data='33'),
                                            InlineKeyboardButton(text="Микроволновые печи", callback_data="34")
                                            ],
                                            [InlineKeyboardButton(text='Пылесосы ', callback_data='35'),
                                            InlineKeyboardButton(text="Стиральные машины", callback_data="36")
                                            ],
                                            [
                                            InlineKeyboardButton(text="Товары для красоты и здоровья", callback_data="37"),
                                            InlineKeyboardButton(text="Товары для кухни", callback_data="38")
                                            ],
                                            [InlineKeyboardButton(text='Утюги и отпариватели', callback_data='39'),
                                            InlineKeyboardButton(text="Чайники и кофеварки", callback_data="40")
                                            ],
                                               [InlineKeyboardButton(text="Электрические плиты", callback_data="41"),
                                            InlineKeyboardButton(text="Холодильники и морозильники", callback_data="44")
                                             ],
                                            [InlineKeyboardButton(text="Швейные машины", callback_data="45"),
                                            InlineKeyboardButton(text="Бритвы и машинки", callback_data="46")
                                            ],
                                            [InlineKeyboardButton(text="Фены и плойки", callback_data="47"),
                                            InlineKeyboardButton(text="Весы", callback_data="48")
                                            ],[
                                            InlineKeyboardButton(text="НАЗАД", callback_data="21")
                                            ]
                                       ]
                                    )


gamess = InlineKeyboardMarkup(row_width=2,
                                       inline_keyboard=[
                                           [InlineKeyboardButton(text='Игровые приставки', callback_data='50'),
                                            InlineKeyboardButton(text="Игры", callback_data="51")
                                            ],
                                           [InlineKeyboardButton(text='Аксессуары', callback_data='52'),
                                            InlineKeyboardButton(text="Настольные игры", callback_data="53")
                                            ],
                                            [
                                            InlineKeyboardButton(text="НАЗАД", callback_data="21")
                                            ]
                                       ]
                                    )



auto = InlineKeyboardMarkup(row_width=2,
                                       inline_keyboard=[
                                           [InlineKeyboardButton(text='Мойки высокого давления', callback_data='54'),
                                            InlineKeyboardButton(text="Насосы и компрессоры", callback_data="55")
                                            ],
                                           [InlineKeyboardButton(text='Автомагнитолы', callback_data='56'),
                                            InlineKeyboardButton(text="Автомобильные аксессуары и комплектующие", callback_data="57")
                                            ],
                                           [InlineKeyboardButton(text='Автомобильные колонки', callback_data='58'),
                                            InlineKeyboardButton(text="Автомобильные сабвуферы", callback_data="59")
                                            ],
                                           [InlineKeyboardButton(text='Автомобильные усилители', callback_data='60'),
                                            InlineKeyboardButton(text="Парктроники и сигнализация", callback_data="61")
                                            ],

                                           [InlineKeyboardButton(text='Видеорегистраторы', callback_data='62'),
                                            InlineKeyboardButton(text="Навигаторы",
                                                                 callback_data="63")
                                            ],
                                           [InlineKeyboardButton(text='Радар-детекторы', callback_data='64'),
                                            InlineKeyboardButton(text="Шины и диски",
                                                                 callback_data="65")
                                            ],
                                            [
                                            InlineKeyboardButton(text="НАЗАД", callback_data="21")
                                            ]
                                       ]
                            )

photo = InlineKeyboardMarkup(row_width=2,
                                       inline_keyboard=[
                                           [InlineKeyboardButton(text='Фоторамки', callback_data='66'),
                                            InlineKeyboardButton(text="Фотоаппараты", callback_data="67")
                                            ],
                                           [InlineKeyboardButton(text='Видеокамеры', callback_data='68'),
                                            InlineKeyboardButton(text="Аксессуары для фото и видеокамер", callback_data="69")
                                            ],
                                            [
                                            InlineKeyboardButton(text="НАЗАД", callback_data="21")
                                            ]
                                       ]
                                    )

hobby = InlineKeyboardMarkup(row_width=2,
                                       inline_keyboard=[
                                           [InlineKeyboardButton(text='Зимний спортивный инвентарь', callback_data='70'),
                                            InlineKeyboardButton(text="Мототехника", callback_data="71")
                                            ],
                                           [InlineKeyboardButton(text='Металлоискатели', callback_data='72'),
                                            InlineKeyboardButton(text="Бинокли и оптика", callback_data="73")
                                            ],
                                           [InlineKeyboardButton(text='Водный инвентарь', callback_data='74'),
                                            InlineKeyboardButton(text="Тату-машинки", callback_data="75")
                                            ],
                                           [InlineKeyboardButton(text='Велосипеды и самокаты', callback_data='76'),
                                            InlineKeyboardButton(text="Пневматика и электрошокеры", callback_data="77")
                                            ],
                                           [InlineKeyboardButton(text='Спортивный инвентарь', callback_data='78'),
                                            InlineKeyboardButton(text="Товары для животных", callback_data="79")
                                            ],
                                           [InlineKeyboardButton(text='Тренажеры', callback_data='50'),
                                            InlineKeyboardButton(text="Роликовые и ледовые коньки", callback_data="80")
                                            ],
                                           [InlineKeyboardButton(text='Туризм', callback_data='81'),
                                            InlineKeyboardButton(text="Квадрокоптеры", callback_data="82")
                                            ],
                                           [InlineKeyboardButton(text='Квадрокоптеры', callback_data='83'),
                                            InlineKeyboardButton(text="Коллекционирование", callback_data="84")
                                            ],
                                            [
                                            InlineKeyboardButton(text="НАЗАД", callback_data="21")
                                            ]
                                       ]
                             )


clothers = InlineKeyboardMarkup(row_width=2,
                                       inline_keyboard=[
                                           [InlineKeyboardButton(text='Обувь', callback_data='85'),
                                            InlineKeyboardButton(text="Канцтовары", callback_data="86")
                                            ],
                                           [InlineKeyboardButton(text='Верхняя одежда', callback_data='87'),
                                            InlineKeyboardButton(text="Часы", callback_data="88")
                                            ],
                                           [InlineKeyboardButton(text='Кошельки и сумки', callback_data='89'),
                                            InlineKeyboardButton(text="НАЗАД", callback_data="21")
                                            ]
                                       ]
                                    )

audio = InlineKeyboardMarkup(row_width=2,
                                       inline_keyboard=[
                                           [InlineKeyboardButton(text='Музыкальные инструменты', callback_data='90'),
                                            InlineKeyboardButton(text="MP3 плееры", callback_data="91")
                                            ],
                                           [InlineKeyboardButton(text='Колонки', callback_data='92'),
                                            InlineKeyboardButton(text="Домашние кинотеатры", callback_data="93")
                                            ],
                                           [InlineKeyboardButton(text='Музыкальные центры', callback_data='94'),
                                            InlineKeyboardButton(text="Ресиверы", callback_data="95")],
                                            [
                                            InlineKeyboardButton(text="НАЗАД", callback_data="21")
                                            ]
                                       ]
                                    )

TV = InlineKeyboardMarkup(row_width=2,
                                       inline_keyboard=[
                                           [InlineKeyboardButton(text='Телевизоры', callback_data='96'),
                                            InlineKeyboardButton(text="Видео", callback_data="97")
                                            ],
                                           [InlineKeyboardButton(text='Проекторы', callback_data='98'),
                                            InlineKeyboardButton(text="Цифровое телевидение", callback_data="99")
                                            ],
                                           [InlineKeyboardButton(text='Аксессуары для ТВ и видео', callback_data='100'),
                                            InlineKeyboardButton(text="НАЗАД", callback_data="21")
                                            ]
                                       ]
                                    )


baby = InlineKeyboardMarkup(row_width=2,
                                       inline_keyboard=[
                                           [InlineKeyboardButton(text='Детские автокресла', callback_data='101'),
                                            InlineKeyboardButton(text="Детские игрушки", callback_data="102")
                                            ],
                                           [InlineKeyboardButton(text='Детские коляски', callback_data='103'),
                                            InlineKeyboardButton(text="Радио и видео няни", callback_data="104")
                                            ],
                                           [InlineKeyboardButton(text='Товары для младенцев', callback_data='105'),
                                            InlineKeyboardButton(text="НАЗАД", callback_data="21")
                                            ]
                                       ]
                                    )