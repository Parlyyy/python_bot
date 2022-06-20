from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_help = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Как заказать'),
            KeyboardButton(text='Назад ⬅️')
        ]
    ],
    resize_keyboard=True
)


kb_help_eng = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='How to order'),
            KeyboardButton(text='Back ⬅️')
        ]
    ],
    resize_keyboard=True
)




