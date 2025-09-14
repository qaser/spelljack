from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import (Back, Button, CurrentPage, NextPage,
                                        PrevPage, Row, Column)
from aiogram_dialog.widgets.text import Const, Format

from dialogs.for_play.states import Play
from . import getters, selected


async def exit_click(callback, button, dialog_manager):
    try:
        await dialog_manager.done()
        await callback.message.delete()
    except:
        pass


def player_info_window():
    return Window(
        Format(
            "<u><b>{name}</b> | {title}</u>\n\n"
            # "🏆 Уровень: {level}\n"
            "<b>Опыт:</b> {exp}\n"
            "<b>Глубина сновидений:</b> {dream_level}%\n"
            "<b>Баланс магии:</b> {magic_balance}\n\n"
            "<u>Статистика:</u>\n"
            "    Поединков: {battles}\n"
            "    ⭐ Побед: {wins}\n"
            "    💥 Поражений: {defeats}\n"
            "    ♥️ Ничьих: {draws}\n"
        ),
        Column(
            Button(
                Const('🌙  Начать поединок'),
                id='battle_start',
                on_click=selected.on_battle_start,
            ),
            Button(
                Const('❮❮ Выход'),
                id='exit',
                on_click=exit_click,
            ),
        ),
        state=Play.player_info,
        getter=getters.get_player_info,
    )
