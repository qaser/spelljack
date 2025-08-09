from aiogram_dialog.widgets.kbd import Button, Column, Select, Group
from aiogram_dialog.widgets.text import Const, Format

from . import selected


def magic_type_menu():
    return Column(
        Select(
            Format("{item}"),
            id="magic_type",
            item_id_getter=lambda x: x,
            items="magic_types",
            on_click=selected.on_select_magic_type
        )
    )


def enemy_menu():
    return Column(
        Button(Const('🔮 Случайный противник'), id='generate_mob', on_click=selected.on_generate_mob),
    )


def mob_info_menu():
    return Column(
        Button(Const('🔮 Новый противник'), id='generate_mob', on_click=selected.on_generate_mob),
        Button(Const('💞 Начать поединок'), id='battle_start', on_click=selected.on_battle_start),
    )


def battle_round_menu():
    return Group(
        Button(Const("❮❮ Сбежать"), id="escape", on_click=selected.on_escape),
        Button(
            Const("🌀 Больше!"),
            id="draw",
            on_click=selected.on_draw,
            when=lambda data, w, m: not data.get("player_stop", False) or data.get("player_extra_draw", False)
        ),
        Button(
            Const("⚡️ Хватит..."),
            id="stop",
            on_click=selected.on_stop,
            when=lambda data, w, m: not data.get("player_stop", False)
        ),
        width=2
    )


def round_result_menu():
    return Group(
        Button(Const("❮❮ Сбежать"), id="escape", on_click=selected.on_escape),
        # Button(Const("💃🏻 Обзор соперника"), id="outfit", on_click=selected.on_outfit_review),
        Button(Const("Продолжить ❯❯"), id="next_round", on_click=selected.on_next_round),
        width=2
    )
