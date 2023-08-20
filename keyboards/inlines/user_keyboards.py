from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inlines.callback_data import navigation_items_callback, item_count_callback, basket_callback
from loader import db


def get_item_inline_keyboard(id: int = 1, current_count: int = 1) -> InlineKeyboardMarkup:
    item_inline_keyboard = InlineKeyboardMarkup()
    left_id = id - 1
    right_id = id + 1
    if id == 1:
        btm = InlineKeyboardButton(text='>>>',
                                   callback_data=navigation_items_callback.new(
                                       for_data='items',
                                       id=right_id)
                                   )
        item_inline_keyboard.add(btm)
    elif id == db.get_items_count():
        btm = InlineKeyboardButton(text='<<<',
                                   callback_data=navigation_items_callback.new(
                                       for_data='items',
                                       id=left_id)
                                   )
        item_inline_keyboard.add(btm)
    else:
        btm_left = InlineKeyboardButton(text='<<<',
                                        callback_data=navigation_items_callback.new(
                                            for_data='items',
                                            id=left_id)
                                        )
        btm_right = InlineKeyboardButton(text='>>>',
                                         callback_data=navigation_items_callback.new(
                                             for_data='items',
                                             id=right_id)
                                         )
        item_inline_keyboard.row(btm_left, btm_right)
    item_inline_keyboard.row(InlineKeyboardButton(text='-',
                                                  callback_data=item_count_callback.new(
                                                      target='item_minus',
                                                      id=id,
                                                      current_count=f'{current_count}'
                                                  )),
                             InlineKeyboardButton(text=f'{current_count}',
                                                  callback_data=item_count_callback.new(
                                                      target='None',
                                                      id=id,
                                                      current_count=f'{current_count}'
                                                  )),
                             InlineKeyboardButton(text='+',
                                                  callback_data=item_count_callback.new(
                                                      target='item_plus',
                                                      id=id,
                                                      current_count=f'{current_count}'
                                                  )),
                             )
    item_inline_keyboard.row(InlineKeyboardButton(text='В корзину',
                                                  callback_data=item_count_callback.new(
                                                      target='basket',
                                                      id=id,
                                                      current_count=f'{current_count}')
                                                  ))
    return item_inline_keyboard


basket_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Очистить',
                                 callback_data=basket_callback.new(
                                     action='del_basket'
                                 ))
        ],
        [
            InlineKeyboardButton(text='Оформит заказ',
                                 callback_data=basket_callback.new(
                                     action='buy'
                                 ))
        ]
    ])
