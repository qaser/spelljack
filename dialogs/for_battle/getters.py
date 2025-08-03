import datetime as dt
import random

from aiogram_dialog import DialogManager
from bson import ObjectId
from dateutil.relativedelta import relativedelta

from config.mongo_config import battles, mobs, players
from services.mob_factory import generate_random_mob, get_random_mob_for_player
from utils import constants as const


def generate_enemy_introduction(mob_data):
    # Безопасное получение ключа для APPEARANCE
    appearance_key = None
    for key in const.APPEARANCE.keys():
        if key in mob_data['descriptors']['appearance'].lower():
            appearance_key = key
            break
    # Если ключ не найден, используем значение по умолчанию
    if not appearance_key:
        appearance_key = 'улыбка'
    # Сборка описания
    intro_parts = [
        f"Перед вами <b>{mob_data['name']}</b> - {mob_data['title']} {mob_data['sub_title']}.\n",
        f"<i>{random.choice(const.APPEARANCE[appearance_key])}.</i>",
        f"<i>{random.choice(const.BODY_DESCRIPTIONS)}.</i>"
    ]
    mob_entry_phrase = mob_data['quotes']['entry']
    intro_parts.append(f"\n<blockquote>{mob_entry_phrase}</blockquote>\n")
    # Добавление финального эротического акцента
    intro_parts.append(f'{random.choice(const.FINAL_TOUCH)} {random.choice(const.EPIGRAPH_PHRASES)}')
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


async def get_battle_state(dialog_manager: DialogManager, **kwargs):
    context = dialog_manager.current_context()
    battle_id = context.dialog_data["battle_id"]
    battle = battles.find_one({"_id": ObjectId(battle_id)})

    player_hand = battle["player_state"]["hand"]
    mob_hand = battle["mob_state"]["hand"]

    total = sum(card["power"] for card in player_hand)
    mob_total = sum(card["power"] for card in mob_hand)

    player_bar = "▓" * (total // 2) + "░" * ((21 - total) // 2)
    # mob_bar = "▓" * (mob_total // 2) + "░" * ((21 - mob_total) // 2)

    # spell_names = ", ".join(f"{c['name']} ({c['power']})" for c in player_hand)

    return {
        "player_bar": f"💖 Ты: {player_bar} ({total})",
        # "mob_bar": f"🖤 Она: {mob_bar} ({mob_total})",
        # "spells": spell_names,
        "battle_id": str(battle_id)
    }
