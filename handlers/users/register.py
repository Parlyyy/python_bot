from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.default.keyboard_register_info import kb_menu_re_registration_confirmation_eng, kb_menu_re_registration_confirmation, \
    kb_nomer_tel,kb_nomer_tel_eng

from keyboards.default.keyboard_menu_buy import kb_menu_buy, kb_menu_buy_eng

from states import register, register_eng


@dp.message_handler(text=f'Переоформить...')
async def reregister_(message: types.Message):
    await register_(message)


@dp.message_handler(text=f'Назад(список товаров) ⬅')
async def list_all(message: types.Message):
    await message.answer('Список товаров:', reply_markup=kb_menu_buy)


@dp.message_handler(text=f'Назад ⬅')
async def list(message: types.Message):
    await message.answer('Список товаров:', reply_markup=kb_menu_buy)


@dp.message_handler(text=f'Оформить заказ...')
async def register_(message: types.Message):
    await message.answer('Здравствуйте это стадия оформления заказа... \nВведите количество:')
    await register.test1.set()


@dp.message_handler(state=register.test1)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(test1=answer)
    await message.answer('Номер телефона:')
    await register.test2.set()


@dp.message_handler(state=register.test2)
async def state2(message: types.Message, state: FSMContext):
    answer = message.answer_contact

    await state.update_data(test2=answer)
    await message.answer('Введите Имя:')
    await register.test3.set()


@dp.message_handler(state=register.test3)
async def state3(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(test3=answer)
    await message.answer('Введите Фамилию:')
    await register.test4.set()


@dp.message_handler(state=register.test4)
async def state4(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(test4=answer)
    await message.answer('Введите размер:')
    await register.test5.set()


@dp.message_handler(state=register.test5)
async def state5(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(test5=answer)
    await message.answer('Введите адресс(Страна, город, отделение почты. Все через запятую):')
    await register.test6.set()


@dp.message_handler(state=register.test6)
async def state6(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(test6=answer)
    data = await state.get_data()
    amount = data.get('test1')
    phone_nuber = data.get('test2')
    name = data.get('test3')
    surname = data.get('test4')
    size = data.get('test5')
    address = data.get('test6')
    await message.answer('Заказ успешно оформлен\n'
                         f'Количество: {amount}\n'
                         f'Ваш телефон: {phone_nuber}\n'
                         f'Ваше имя: {name}\n'
                         f'Ваша фамилия: {surname}\n'
                         f'Ваш размер: {size}\n'
                         f'Ваш адресс: {address}\n',
                         reply_markup=kb_menu_re_registration_confirmation
                         )
    await state.finish()


@dp.message_handler(text=f'Re-register')
async def re_register_(message: types.Message):
    await register_engg(message)


@dp.message_handler(text=f'Back ⬅')
async def back_list(message: types.Message):
    await message.answer('Product List:', reply_markup=kb_menu_buy_eng)


@dp.message_handler(text=f'Back(list of products) ⬅')
async def back(message: types.Message):
    await message.answer('Product List:', reply_markup=kb_menu_buy_eng)


@dp.message_handler(text=f'Checkout...')
async def register_engg(message: types.Message):
    await message.answer('Hello, this is the checkout stage.... \nEnter Quantity:')
    await register_eng.test1_eng.set()


@dp.message_handler(state=register_eng.test1_eng)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(test1=answer)
    await message.answer('Phone number:')
    await register_eng.test2_eng.set()


@dp.message_handler(state=register_eng.test2_eng)
async def state2(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(test2=answer)
    await message.answer('Enter your name:')
    await register_eng.test3_eng.set()


@dp.message_handler(state=register_eng.test3_eng)
async def state3(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(test3=answer)
    await message.answer('Enter Last Name:')
    await register_eng.test4_eng.set()


@dp.message_handler(state=register_eng.test4_eng)
async def state4(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(test4=answer)
    await message.answer('Enter size:')
    await register_eng.test5_eng.set()


@dp.message_handler(state=register_eng.test5_eng)
async def state5(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(test5=answer)
    await message.answer('Enter the address (Country, city, post office. All separated by commas):')
    await register_eng.test6_eng.set()


@dp.message_handler(state=register_eng.test6_eng)
async def state6(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(test6=answer)
    data = await state.get_data()
    amount = data.get('test1')
    phone_nuber = data.get('test2')
    name = data.get('test3')
    surname = data.get('test4')
    size = data.get('test5')
    address = data.get('test6')
    await message.answer('Order successfully completed\n'
                         f'Quantity: {amount}\n'
                         f'Your phone number: {phone_nuber}\n'
                         f'Your name: {name}\n'
                         f'Your last name: {surname}\n'
                         f'Your size: {size}\n'
                         f'Your address: {address}\n',
                         reply_markup=kb_menu_re_registration_confirmation_eng
                         )
    await state.finish()