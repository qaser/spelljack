from aiogram.filters.state import State, StatesGroup


class Battle(StatesGroup):
    select_enemy_type = State()
    show_enemy_info = State()
    battle_round = State()
    round_result = State()
    # round_finish = State()
    # battle_finish = State()
