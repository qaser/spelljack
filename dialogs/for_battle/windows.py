from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Back, Button, Cancel, Select
from aiogram_dialog.widgets.text import Const, Format, Multi

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


def select_magic_window():
    return Window(
        Const("Выберите тип магии:"),
        keyboards.magic_type_menu(),
        Cancel(Const('👣 Выход'), on_click=exit_click),
        state=Battle.select_magic_type,
        getter=getters.get_magic_types
    )


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
        Back(Const('❮❮ Отказаться от поединка')),
        state=Battle.show_enemy_info,
        getter=getters.get_mob_data
    )


def battle_round_window():
    return Window(
        Multi(
            Const("<b>Потоки магии сошлись - протяни руку и возьми своё!</b>\n"),
            Const('🌫️ Полный туман обмана скрывает магию!\n', when=lambda data, w, m: data.get("fog_full", False)),
            Const('🌫️ Туман обмана скрывает очки!\n', when=lambda data, w, m: data.get("fog_partial", False) and not data.get("fog_full", False)),
            Format('🧔🏻: {player_outfits}\n👸🏼: {mob_outfits}\n<u>Накопленная магия</u>\n{player_bar}'),
            Format('{player_buff_description}', when=lambda data, w, m: data.get("player_buff_description", "")),
            Format('{mob_buff_description}', when=lambda data, w, m: data.get("mob_buff_description", "")),
            Format('{player_message}', when=lambda data, w, m: data.get("player_message", "") and not (data.get("fog_full", False) or data.get("fog_partial", False))),
        ),
        keyboards.battle_round_menu(),
        state=Battle.battle_round,
        getter=getters.get_battle_state
    )


def round_result_window():
    return Window(
        Multi(
            Format('{outfit_remove_text}\n🧔🏻: {player_bar}\n👸🏼: {mob_bar}'),
            Format('{player_message}', when=lambda data, w, m: data.get("player_message", "")),
        ),
        keyboards.round_result_menu(),
        state=Battle.round_result,
        getter=getters.round_result_getter
    )


def battle_result_window():
    return Window(
        Format("{result_text}"),
        Button(Const("🔁 Сыграть снова"), id="restart", on_click=selected.on_battle_start),
        Button(Const("🏃‍♂️ Выйти"), id="exit", on_click=exit_click),
        state=Battle.battle_result,
        getter=getters.get_battle_result_text
    )
