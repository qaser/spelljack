from aiogram_dialog import DialogManager
from .states import Scene
from .scene_dialogs import DIALOGS


async def on_option_click(c, button, dialog_manager: DialogManager):
    option_id = button.widget_id
    branch = dialog_manager.start_data.get("branch")
    current_scene = dialog_manager.dialog_data.get("scene_id", "start")

    scene_data = DIALOGS[branch][current_scene]
    chosen_option = next(o for o in scene_data["options"] if o["id"] == option_id)

    dialog_manager.dialog_data["scene_id"] = chosen_option["next"]
    await dialog_manager.switch_to(Scene.scene)
