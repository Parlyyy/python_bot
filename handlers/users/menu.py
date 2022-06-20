from loader import dp
from aiogram import types

from keyboards.default import kb_menu


@dp.message_handler(text='Меню(язык) ⬅️')
async def menu(message: types.Message):
    await message.answer('Список:', reply_markup=kb_menu)


@dp.message_handler(text='Menu(language) ⬅️')
async def menu_eng(message: types.Message):
    await message.answer('List:', reply_markup=kb_menu)








