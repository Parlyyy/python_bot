from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_menu_register = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Оформить заказ...'),
            KeyboardButton(text='Назад ⬅'),
        ]
    ],
    resize_keyboard=True
)

kb_nomer_tel = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Поделиться номером', request_contact=True),
        ]
    ],
    resize_keyboard=True
)


kb_nomer_tel_eng = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Share number', request_contact=True),
        ]
    ],
    resize_keyboard=True
)


kb_menu_re_registration_confirmation = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Подтвердить заказ'),
            KeyboardButton(text='Переоформить...'),
        ],
        [
            KeyboardButton(text='Назад(список товаров) ⬅'),
        ]
    ],
    resize_keyboard=True
)


kb_menu_register_eng = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Checkout...'),
            KeyboardButton(text='Back ⬅'),
        ]
    ],
    resize_keyboard=True
)


kb_menu_re_registration_confirmation_eng = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Confirm the order'),
            KeyboardButton(text='Re-register'),
        ],
        [
            KeyboardButton(text='Back(list of products) ⬅')
    ]
    ],
    resize_keyboard=True
)