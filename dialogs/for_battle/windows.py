from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Back, Button, Cancel, Select
from aiogram_dialog.widgets.text import Const, Format, Multi
from aiogram_dialog.widgets.media import DynamicMedia, MediaScroll, Media

from dialogs.for_battle.states import Battle
from . import getters, keyboards, selected


ROUND_TITLE = (
    'Обращайся к магическому потоку, черпай силу и произноси '
    'заклинания чтобы победить волшебницу и ... овладеть ею.\n'
)
FOG_TEXT = (
    '<b>Твой разум затуманен возбуждением от вида '
    'полуобнаженного тела чародейки. Ты не можешь '
    'сконцентрироваться и читать магический поток.</b>\n'
)
FULL_FOG_TEXT = (
    '<b>Твоё возбуждение достигло предела! Магический поток '
    'начинает иссякать и ты беспорядочно начинаешь хватать энергию.</b>\n'
)
TYPE_MAGIC_TEXT = ("<u>Выберите тип магии</u>\nВ <b>Мире Сновидений</b> это влияет на баланс магических сил.\n"
                   "Во время поединка это будет влиять на событие <b>Магическое Зеркало</b>.")


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
        Const(TYPE_MAGIC_TEXT),
        keyboards.magic_type_menu(),
        Cancel(Const('❮❮ Выход'), on_click=exit_click),
        state=Battle.select_magic_type,
        getter=getters.get_magic_types,
    )


def select_enemy_window():
    return Window(
        Const("Выберите вариант противника"),
        keyboards.enemy_menu(),
        Cancel(Const('❮❮ Выход'), on_click=exit_click),
        state=Battle.select_enemy_type,
    )


def show_enemy_window():
    return Window(
        DynamicMedia('image', when='has_image'),
        Format('{enemy_intro}'),
        keyboards.mob_info_menu(),
        Back(Const('❮❮ Назад')),
        state=Battle.show_battle_preview,
        getter=getters.get_mob_data,
    )


def battle_round_window():
    return Window(
        DynamicMedia('event_image', when='has_event_image'),
        Multi(
            Const(ROUND_TITLE),
            Const(FULL_FOG_TEXT, when=lambda data, w, m: data.get("fog_full", False)),
            Const(
                FOG_TEXT,
                when=lambda data, w, m: data.get("fog_partial", False)
                and not data.get("fog_full", False),
            ),
            Format('🧔🏻: {player_hitpoints}\n👸🏼: {mob_hitpoints}\n'),
            Const(
                '<u>Магическая сила</u>',
                when=lambda data, w, m: not (data.get("fog_full", False)),
            ),
            Format('{player_bar}'),
            Format(
                '{player_message}',
                when=lambda data, w, m: data.get("player_message", "")
                and not (data.get("fog_full", False) or data.get("fog_partial", False)),
            ),
        ),
        keyboards.battle_round_menu(),
        state=Battle.battle_round,
        getter=getters.get_battle_state,
    )


def round_result_window():
    return Window(
        Multi(
            Format('{hitpoints_remove_text}\n'),
            Format('<blockquote>{mob_phrase}</blockquote>\n'),
            Format('🧔🏻: {player_bar}\n👸🏼: {mob_bar}\n'),
            Format('{event_text}\n'),
            Format(
                '{player_message}',
                when=lambda data, w, m: data.get("player_message", ""),
            ),
        ),
        keyboards.round_result_menu(),
        state=Battle.round_result,
        getter=getters.round_result_getter,
    )


def battle_result_window():
    return Window(
        DynamicMedia('image', when='has_image'),
        Format("{result_text}"),
        Button(Const("Продолжить ❯❯❯"), id="scene", on_click=selected.on_scene),
        # Button(Const("🏃‍♂️ Выйти"), id="exit", on_click=exit_click),
        state=Battle.battle_result,
        getter=getters.get_battle_result,
    )
