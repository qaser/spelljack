import random
from aiogram_dialog import DialogManager
from .scene_dialogs import DIALOGS


async def scene_getter(dialog_manager: DialogManager, **kwargs):
    # branch — "player" или "mob"
    branch = dialog_manager.start_data.get("branch")
    current_scene = dialog_manager.dialog_data.get("scene_id", "start")
    player_xp = dialog_manager.start_data.get("xp", 0)

    scene_data = DIALOGS[branch][current_scene]

    # Фильтрация кнопок по опыту
    available_options = [
        opt
        for opt in scene_data.get("options", [])
        if player_xp >= opt.get("xp_req", 0)
    ]

    # Автоматический выбор для моба
    if branch == "mob" and available_options:
        if available_options[0].get("random"):
            next_scene = random.choice(available_options[0]["next"])
            dialog_manager.dialog_data["scene_id"] = next_scene
            return await scene_getter(
                dialog_manager
            )  # Рекурсивно грузим следующую сцену

    return {
        "scene_text": (
            scene_data["text"]() if callable(scene_data["text"]) else scene_data["text"]
        ),
        "options": available_options,
    }
