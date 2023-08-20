from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

commands_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Список товаров'),
            KeyboardButton(text='Корзина')
        ],
        [
            KeyboardButton(text='Помощь'),
            KeyboardButton(text='О нас')
        ],
        [
            KeyboardButton(text='Активация аккаунта',
                           request_contact=True)
        ],
        [
            KeyboardButton(text='Скрыть меню')
        ]
    ],
    resize_keyboard=True
)
