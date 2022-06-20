from aiogram import types

from keyboards.default.keyboard_help import kb_help, kb_help_eng
from keyboards.default.keyboard_back_menu import kb_back_menu_eng, kb_back_menu
from loader import dp


@dp.message_handler(text='Помощь 📙',)
async def command_start(message: types.Message):
    await message.answer('Ответы на ваши вопросы, находятся здесь:', reply_markup=kb_help)


@dp.message_handler(text='Назад ⬅️',)
async def command_start(message: types.Message):
    await message.answer('Список:', reply_markup=kb_back_menu)


@dp.message_handler(text='Help 📙')
async def command_start(message: types.Message):
    await message.answer('The answers to your questions are here:', reply_markup=kb_help_eng)


@dp.message_handler(text='Back ⬅️')
async def command_start(message: types.Message):
    await message.answer('List:', reply_markup=kb_back_menu_eng)


