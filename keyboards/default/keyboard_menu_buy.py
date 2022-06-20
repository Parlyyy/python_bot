from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_menu_buy = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Худи'),
            KeyboardButton(text='Свитшот'),
            KeyboardButton(text='Футболка')
        ],
        [
            KeyboardButton(text='Назад ⬅️')
        ]
    ],
    resize_keyboard=True
)


kb_menu_buy_eng = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Hoodie'),
            KeyboardButton(text='Sweatshirt'),
            KeyboardButton(text='T shirt')
        ],
        [
            KeyboardButton(text='Back ⬅️')
        ]
    ],
    resize_keyboard=True
)