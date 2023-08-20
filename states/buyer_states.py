from aiogram.dispatcher.filters.state import State, StatesGroup


class BuyerState(StatesGroup):
    wait_date = State()
    wait_time = State()
    wait_name = State()
