from aiogram.filters.state import State, StatesGroup


class Battle(StatesGroup):
    select_magic_type = State()
    select_enemy_type = State()
    show_battle_preview = State()
    battle_round = State()
    round_result = State()
    battle_result = State()
