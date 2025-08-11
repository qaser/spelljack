from aiogram_dialog.widgets.kbd import Select, Column
from aiogram_dialog.widgets.text import Format
from .states import Scene


async def on_option_click(c, widget, manager, item_id: str):
    manager.dialog_data.update(selected_option=item_id)
    await manager.switch_to(Scene.scene)



def make_scene_keyboard():
    return Column(
        Select(
            Format("{item[label]}"),  # текст кнопки
            id="scene_option",        # статический id для группы кнопок
            item_id_getter=lambda x: x["id"],  # откуда брать item_id из списка
            items="options",          # ключ из геттера
            on_click=on_option_click
        )
    )
