from aiogram_dialog import DialogManager
from .states import Scene
from .scene_dialogs import DIALOGS


async def on_option_click(c, widget, manager, item_id: str):
    branch = manager.start_data.get("branch")
    current_scene = manager.dialog_data.get("scene_id", "start")
    scene_data = DIALOGS[branch][current_scene]
    chosen_option = next(o for o in scene_data["options"] if o["id"] == item_id)
    # Сохраняем именно next-сцену
    manager.dialog_data["scene_id"] = chosen_option["next"]
    await manager.switch_to(Scene.scene)
