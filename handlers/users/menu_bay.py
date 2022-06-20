from aiogram import types

from keyboards.default.keyboard_menu_buy import kb_menu_buy, kb_menu_buy_eng
from keyboards.default.keyboard_register_info import kb_menu_register_eng, kb_menu_register
from loader import dp


@dp.message_handler(text='Ru 🇷🇺')
async def command_start(message: types.Message):
    await message.answer(f'<b>Здравствуйте, что вы хочете заказать?</b>', reply_markup=kb_menu_buy)


@dp.message_handler(text='Худи')
async def command_start(message: types.Message):
    await message.answer('Вы хочете оформить заказ?(Худи)',reply_markup=kb_menu_register)


@dp.message_handler(text='Свитшот')
async def command_start(message: types.Message):
    await message.answer('Вы хочете оформить заказ?(Свитшот)',reply_markup=kb_menu_register)


@dp.message_handler(text='Футболка')
async def command_start(message: types.Message):
    await message.answer('Вы хочете оформить заказ?(Футболка)',reply_markup=kb_menu_register)


@dp.message_handler(text='Eng 🇺🇸')
async def command_start(message: types.Message):
    await message.answer(f'<b>What are you want to order?</b>', reply_markup=kb_menu_buy_eng)


@dp.message_handler(text='Hoodie')
async def command_start(message: types.Message):
    await message.answer('Do you want to place an order?(Hoodie)',reply_markup=kb_menu_register_eng)


@dp.message_handler(text='Sweatshirt')
async def command_start(message: types.Message):
    await message.answer('Do you want to place an order?(Sweatshirt)',reply_markup=kb_menu_register_eng)


@dp.message_handler(text='T shirt')
async def command_start(message: types.Message):
    await message.answer('Do you want to place an order?(T shirt    )',reply_markup=kb_menu_register_eng)