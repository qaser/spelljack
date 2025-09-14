from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import (Back, Button, CurrentPage, NextPage,
                                        PrevPage, Row, Column)
from aiogram_dialog.widgets.text import Const, Format

import utils.constants as texts
from dialogs.for_registration.states import Registration

from . import getters, keyboards, selected

ID_SCROLL_PAGER = 'admins_pager'
AGE_CONFIRMATION_TEXT = ('Для доступа к игре вам должно быть не менее <u>18 лет</u>. '
                         'Подтвердите, что вы соответствуете этому требованию.')


async def exit_click(callback, button, dialog_manager):
    try:
        await dialog_manager.done()
        await callback.message.delete()
    except:
        pass


def age_confirmation_window():
    return Window(
        Const('‼️<b>ВНИМАНИЕ</b>‼️ <b>Вход ограничен по возрасту</b>'),
        Const(AGE_CONFIRMATION_TEXT),
        Column(
            Button(
                Const('🟥 Подтверждаю, что мне есть 18 лет'),
                id='age_confirm',
                on_click=selected.on_age_confirm,
            ),
            Button(
                Const('Мне нет 18 лет'),
                id='exit',
                on_click=exit_click,
            ),
        ),
        state=Registration.age_confirmation
        # getter=getters.get_admins,
    )


def select_name_window():
    return Window(
        Const('Выберите имя персонажа'),
        keyboards.name_menu(),
        Back(Const('❮❮ Назад')),
        state=Registration.select_name,
        getter=getters.get_names,
    )


def reg_confirm_window():
    return Window(
        Const('Подтвердите регистрацию'),
        Back(Const('❮❮ Назад')),
        Button(
            Const('✅ Подтверждаю'),
            id='reg_confirm',
            on_click=selected.on_reg_confirm,
        ),
        state=Registration.reg_confirm
    )
