from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_start_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Ru 🇷🇺'),
            KeyboardButton(text='Eng 🇺🇸')
        ]
    ],
    resize_keyboard=True
)