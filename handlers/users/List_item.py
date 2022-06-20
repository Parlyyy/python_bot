from aiogram import types

from keyboards.default.keyboard_menu_buy import kb_menu_buy, kb_menu_buy_eng
from loader import dp


@dp.message_handler(text='Список товаров📝',)
async def command_start(message: types.Message):
    await message.answer('Выполняется...', reply_markup=kb_menu_buy)


@dp.message_handler(text='Product list📝',)
async def command_start(message: types.Message):
    await message.answer('Performed...', reply_markup=kb_menu_buy_eng)