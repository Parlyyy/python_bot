from aiogram import types

from keyboards.default.keyboard_sart_menu import kb_start_menu
from loader import dp


@dp.message_handler(text='/start')
async def command_start(message: types.Message):
    await message.answer(f'Здравствуйте {message.from_user.first_name}, на каком языке вы предпочитаете продложить общение?')
    await message.answer(f'Hello  {message.from_user.first_name}, what language do you prefer to continue communication?', reply_markup=kb_start_menu)