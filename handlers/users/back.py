from aiogram import types

from keyboards.default.keyboard_back_menu import kb_back_menu, kb_back_menu_eng
from loader import dp


@dp.message_handler(text='Назад ⬅️',)
async def command_start(message: types.Message):
    await message.answer('Выполняется...', reply_markup=kb_back_menu)


@dp.message_handler(text='Back ⬅️')
async def command_start(message: types.Message):
    await message.answer('Performed...', reply_markup=kb_back_menu_eng)


