from aiogram.filters.state import State, StatesGroup


class Registration(StatesGroup):
    age_confirmation = State()
    select_name = State()
    reg_confirm = State()
