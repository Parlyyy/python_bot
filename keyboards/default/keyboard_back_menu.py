from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_back_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Меню(язык) ⬅️'),
            KeyboardButton(text='Помощь 📙')
        ],
        [
            KeyboardButton(text='Список товаров📝'),
        ]
    ],
    resize_keyboard=True
)

kb_back_menu_eng = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Menu(language) ⬅️'),
            KeyboardButton(text='Help 📙')
        ],
        [
            KeyboardButton(text='Product list📝')
        ]
    ],
    resize_keyboard=True
)


