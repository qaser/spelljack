from aiogram.filters.state import State, StatesGroup
from aiogram.types import Message
from aiogram_dialog import Dialog, DialogManager, StartMode, Window
from aiogram_dialog.widgets.kbd import Button, Cancel, Row
from aiogram_dialog.widgets.text import Const, Format
from bson import ObjectId

from config.mongo_config import mobs, players
from dialogs.battle_round import BattleRoundSG
from services.battle_factory import create_battle
from services.mob_factory import generate_random_mob, get_random_mob_for_player


class BattleSG(StatesGroup):
    CHOOSE = State()


async def on_start_battle(callback, button, manager: DialogManager):
    user_id = callback.from_user.id
    player = players.find_one({"user_id": user_id})

    mob_id = generate_random_mob()
    battle_id = create_battle(user_id, mob_id)

    await manager.start(
        BattleRoundSG.ROUND,
        mode=StartMode.RESET_STACK,
        data={
            "battle_id": str(battle_id),
        }
    )


async def get_mob_data(dialog_manager: DialogManager, **kwargs):
    mob_id = generate_random_mob()
    mob = mobs.find_one({"_id": ObjectId(mob_id)})
    if not mob:
        return {"desc": "Ошибка загрузки моба"}

    return {
        "desc": f"{mob['title']} {mob['name']} ({mob['persona']})\n" +
                f"💬 {mob['quotes']['entry'][0]}\n" +
                f"Уровень сложности: {mob['difficulty']}"
    }


battle_start_dialog = Dialog(
    Window(
        Format("{desc}"),
        Row(
            Button(Const("⚔ Начать бой"), id="start_fight", on_click=on_start_battle),
            Button(Const("🔁 Другой"), id="reroll", on_click=on_start_battle),
            Cancel(Const("❌ Выйти"))
        ),
        getter=get_mob_data,
        state=BattleSG.CHOOSE
    )
)
