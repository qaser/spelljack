import datetime as dt
import random

from aiogram_dialog import DialogManager
from bson import ObjectId
from dateutil.relativedelta import relativedelta

from config.mongo_config import battles, mobs, players
from services.mob_factory import generate_random_mob, get_random_mob_for_player
from utils import constants as const
from dialogs.for_battle.states import Battle


def generate_enemy_introduction(mob_data):
    appearance_key = None
    for key in const.APPEARANCE.keys():
        if key in mob_data['descriptors']['appearance'].lower():
            appearance_key = key
            break
    if not appearance_key:
        appearance_key = 'улыбка'
    # outfit_text = generate_outfit_description(mob_data['outfit'])
    intro_parts = [
        f"Перед вами <b>{mob_data['name']}</b> — {mob_data['title']} {mob_data['sub_title']}.\n",
        f"<i>{random.choice(const.APPEARANCE[appearance_key])}.</i>",
        f"<i>{random.choice(const.BODY_DESCRIPTIONS)}.</i>\n",
        f"<blockquote>{mob_data['quotes']['entry']}</blockquote>\n",
        f"{random.choice(const.FINAL_TOUCH)} {random.choice(const.EPIGRAPH_PHRASES)}"
    ]
    return "\n".join(intro_parts)


async def get_mob_data(dialog_manager: DialogManager, **kwargs):
    context = dialog_manager.current_context()
    mob_id = generate_random_mob()
    context.dialog_data.update(mob_id=str(mob_id))
    mob_data = mobs.find_one({"_id": ObjectId(mob_id)})
    if not mob_data:
        return {"desc": "Ошибка загрузки информации о сопернике"}
    enemy_intro = generate_enemy_introduction(mob_data)
    return {"enemy_intro": enemy_intro}


def make_bar(total: int) -> str:
    MAX = 21
    FILLED = total if total <= MAX else MAX
    empty_slots = (MAX - FILLED) // 2
    filled_slots = FILLED // 2
    if total > 21:
        return "🟥" * 10 + f" ({total})"
    elif total <= 12:
        return "🟨" * filled_slots + "⬜" * empty_slots + f" ({total})"
    elif 13 <= total <= 17:
        return "🟩" * filled_slots + "⬜" * empty_slots + f" ({total})"
    else:
        return "🟧" * filled_slots + "⬜" * empty_slots + f" ({total})"


async def get_battle_state(dialog_manager: DialogManager, **kwargs):
    context = dialog_manager.current_context()
    battle_id = context.dialog_data["battle_id"]

    battle = battles.find_one({"_id": ObjectId(battle_id)})
    player_hand = battle["player_state"]["hand"]
    mob_hand = battle["mob_state"]["hand"]
    player_total = sum(card["power"] for card in player_hand)
    mob_total = sum(card["power"] for card in mob_hand)
    round_number = battle.get("round_number", 1)

    return {
        "player_bar": f"<u>Накопленная магия</u>\n{make_bar(player_total)}",
        "player_total": player_total,
        "mob_total": mob_total,
        "battle_id": str(battle_id),
        "round_number": round_number,
        "player_outfit": battle["player_state"].get("outfit_left", 6),
        "mob_outfit": battle["mob_state"].get("outfit_left", 6),
    }



async def round_step_getter(dialog_manager: DialogManager, **kwargs):
    context = dialog_manager.current_context()
    battle_id = context.dialog_data["battle_id"]
    battle = battles.find_one({"_id": ObjectId(battle_id)})

    # if battle["player_state"]["stop"] and battle["mob_state"]["stop"]:
    #     # Оба завершили — сравнение результатов
    #     await dialog_manager.dialog().switch_to(Battle.round_finish)
    # return {}
