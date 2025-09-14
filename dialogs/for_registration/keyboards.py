from aiogram_dialog.widgets.kbd import Button, Column, Select, Group
from aiogram_dialog.widgets.text import Const, Format

from . import selected


def name_menu():
    return Column(
        Select(
            Format("{item}"),
            id="name",
            item_id_getter=lambda x: x,
            items="names",
            on_click=selected.on_select_name,
        )
    )
