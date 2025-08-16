from aiogram_dialog import Window
from aiogram_dialog.widgets.text import Format
from .states import Scene
from .getters import scene_getter
from .keyboards import make_scene_keyboard
from aiogram_dialog import Dialog


scene_window = Window(
    Format("{scene_text}"),
    make_scene_keyboard(),
    state=Scene.scene,
    getter=scene_getter,
)


scene_dialog = Dialog(scene_window)
