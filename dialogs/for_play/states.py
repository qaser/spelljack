from aiogram.filters.state import State, StatesGroup


class Play(StatesGroup):
    player_info = State()
    # settings = State()
    # reg_confirm = State()
