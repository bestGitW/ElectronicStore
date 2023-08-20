from aiogram.utils.callback_data import CallbackData

navigation_items_callback = CallbackData('navigation_items_btm', 'for_data', 'id')
item_count_callback = CallbackData('item_count_btm', 'target', 'id', 'current_count')
basket_callback = CallbackData('change_btm', 'action')