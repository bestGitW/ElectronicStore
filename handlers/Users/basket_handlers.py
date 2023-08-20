from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message

from keyboards import basket_keyboard, commands_keyboard, basket_callback
from loader import dp, db, bot
from states import BuyerState

from language import text_dit


@dp.message_handler(text='Корзина')
@dp.message_handler(commands=['basket'])
async def show_basket(message: Message):
    user_basket = db.select_user_basket(id=message.from_user.id)[1]
    if user_basket != '':
        user_basket = [item_data.split(':') for item_data in user_basket.split()]
        text = 'Корзина:'
        for item_id, item_count in user_basket:
            _, name, _, _ = db.select_items_info(id=item_id)[0]
            text += f'\n{name}: {item_count}'
        await message.answer(text=text,
                             reply_markup=basket_keyboard)
    else:
        text = 'В корзине нет товаров.'
        await message.answer(text=text)


@dp.callback_query_handler(basket_callback.filter(action='del_basket'))
async def del_basket(call: CallbackQuery):
    db.update_basket(id=call.from_user.id, user_basket='')
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    await bot.answer_callback_query(callback_query_id=call.id,
                                    text='Корзина успешно очищена.',
                                    show_alert=True)


@dp.callback_query_handler(basket_callback.filter(action='buy'))
async def start_buy(call: CallbackQuery):
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    await call.message.answer(text='Укажите дату доставки.')
    await BuyerState.wait_date.set()


@dp.message_handler(state=BuyerState.wait_date)
async def get_date(message: Message, state: FSMContext):
    # data = {}
    await state.update_data({'date': message.text})
    # data = {'date': '12:12:2022'}
    # await state.set_state() - полная очистка старых данных и запись новых
    await message.answer(text='Укажите время доставки.')
    await BuyerState.wait_time.set()


@dp.message_handler(state=BuyerState.wait_time)
async def get_time(message: Message, state: FSMContext):
    # data = {'date': '12:12:2022'}
    await state.update_data({'time': message.text})
    # data = {'date': '12:12:2022', 'time': '14:47'}
    await message.answer(text='Укажите Вашу имя.')
    await BuyerState.wait_name.set()


@dp.message_handler(state=BuyerState.wait_name)
async def get_name(message: Message, state: FSMContext):
    user_basket = db.select_user_basket(id=message.from_user.id)[1]
    user_basket = [item_data.split(':') for item_data in user_basket.split()]
    data = await state.get_data()
    text = f'Заявка' \
           f'\nВаше имя: {message.text}' \
           f'\nДата: {data["date"]}' \
           f'\nВремя: {data["time"]}' \
           f'\n\nТовар:'
    for item_id, item_count in user_basket:
        _, name, _, _ = db.select_items_info(id=item_id)[0]
        text += f'\n{name}: {item_count}'
    db.update_basket(id=message.from_user.id, user_basket='')
    await message.answer(text=text,
                         reply_markup=commands_keyboard)
    await state.reset_state()
