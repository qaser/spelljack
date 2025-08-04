from aiogram_dialog.widgets.kbd import Button, Column, Group, Row, Select
from aiogram_dialog.widgets.text import Const, Format

from . import selected

SCROLLING_HEIGHT = 6


def enemy_menu():
    return Column(
        Button(
            Const('🔮 Случайный противник'),
            id='generate_mob',
            on_click=selected.on_generate_mob
        ),
        # Button(
        #     Const('💞 Уникальные персонажи'),
        #     'unique_mobs',
        #     on_click=selected.on_unique_mobs,
        # ),
    )


def mob_info_menu():
    return Column(
        Button(
            Const('🔮 Новый противник'),
            id='generate_mob',
            on_click=selected.on_generate_mob
        ),
        Button(
            Const('💞 Начать поединок'),
            'battle_start',
            on_click=selected.on_battle_round,
        )
    )


def battle_round_menu():
    return Group(
        Button(
            Const("❮❮ Сбежать"),
            id="escape",
            on_click=selected.on_escape,
        ),
        Button(
            Const("🧙🏻‍♀️ Обзор"),
            id="outfit",
            on_click=selected.on_outfit,
        ),
        Button(
            Const("🌀 Больше!"),
            id="draw",
            on_click=selected.on_draw,
        ),
        Button(
            Const("⚡️ Хватит..."),
            id="stop",
            on_click=selected.on_stop,
        ),
        width=2,
    )


def round_result_menu():
    return Column(
        Button(
            Const("❮❮ Сбежать"),
            id="escape",
            on_click=selected.on_escape,
        ),
        Button(
            Const("Продолжить ❯❯"),
            id="outfit",
            on_click=selected.next_round,
        ),
    )
