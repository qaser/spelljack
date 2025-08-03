from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Back, Button, Cancel, Row
from aiogram_dialog.widgets.text import Const, Format, Multi

import utils.constants as texts
from dialogs.for_battle.states import Battle

from . import getters, keyboards, selected


async def exit_click(callback, button, dialog_manager):
    try:
        await dialog_manager.done()
        await callback.message.delete()
    except:
        pass


async def return_main_menu(callback, button, dialog_manager):
    await dialog_manager.switch_to(Battle.select_enemy_type)


def select_enemy_window():
    return Window(
        Const("Выберите вариант противника"),
        keyboards.enemy_menu(),
        Cancel(Const('👣 Выход'), on_click=exit_click),
        state=Battle.select_enemy_type
    )


def show_enemy_window():
    return Window(
        Format('{enemy_intro}'),
        keyboards.mob_info_menu(),
        Back(Const('🏃💨 Отказаться от поединка')),
        state=Battle.show_enemy_info,
        getter=getters.get_mob_data
    )


def battle_round_window():
    return Window(
        Const("💫 <b>Потоки магии сошлись - протяни руку и возьми своё!</b>\n"),
        Format("{player_bar}"),
        Row(
            Button(
                Const("🌀 Поглотить ещё"),
                id="cast",
                on_click=selected.on_cast
            ),
            Button(
                Const("🫳 Произнести заклинание"),
                id="stop",
                on_click=selected.on_stop
            ),
        ),
        state=Battle.battle_round,
        getter=getters.get_battle_state
    )


def round_step_window():
    return Window(
        Const("🔮 Ожидание... магия накапливается..."),
        state=Battle.round_step,
        getter=getters.round_step_getter
    )
