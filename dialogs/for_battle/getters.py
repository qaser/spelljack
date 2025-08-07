import datetime as dt
from typing import Dict, Any
from bson import ObjectId
from aiogram_dialog import DialogManager

from config.mongo_config import battles, mobs
from services.mob_factory import generate_random_mob
from generators.generate_mob_intro import generate_mob_intro
from utils.constants import MAGIC_TYPE
from generators.outfit_review_generator import outfit_review_generator


async def get_mob_data(dialog_manager: DialogManager, **kwargs) -> Dict[str, str]:
    context = dialog_manager.current_context()
    mob_id = generate_random_mob()
    context.dialog_data["mob_id"] = str(mob_id)
    mob_data = mobs.find_one({"_id": mob_id})
    if not mob_data:
        return {"desc": "Ошибка загрузки информации о сопернике"}
    return {"enemy_intro": generate_mob_intro(mob_data)}


def make_bar(total: int, max_value: int = 21, slots: int = 10, show_total: bool = True) -> str:
    if total > max_value:
        bar = "🟥" * slots
    else:
        filled_ratio = total / max_value
        filled_slots = round(filled_ratio * slots)
        empty_slots = slots - filled_slots
        filled = (
            "🟪" if total == max_value else
            "🟩" if 13 <= total <= 17 else
            "🟧" if total > 17 else
            "🟨"
        ) * filled_slots
        bar = f"{filled}{'⬜' * empty_slots}"
    return f"{bar} ({total})" if show_total else bar


def make_outfit_bar(outfits_left: int, total: int = 6) -> str:
    return "❤️" * outfits_left + "🤍" * (total - outfits_left)


async def get_battle_state(dialog_manager: DialogManager, **kwargs) -> Dict[str, Any]:
    context = dialog_manager.current_context()
    battle_id = context.dialog_data["battle_id"]
    battle = battles.find_one({"_id": ObjectId(battle_id)})
    player_hand = battle["player_state"]["hand"]
    mob_hand = battle["mob_state"]["hand"]

    player_bar = (
        "🌫️ Туман скрывает магию!" if battle.get("fog_full", False) else
        make_bar(sum(card["power"] for card in player_hand), show_total=not battle.get("fog_partial", False))
    )

    return {
        "player_bar": player_bar,
        "player_total": sum(card["power"] for card in player_hand),
        "mob_total": sum(card["power"] for card in mob_hand),
        "battle_id": str(battle_id),
        "round_number": battle.get("round_number", 1),
        "player_outfits": make_outfit_bar(battle["player_state"].get("outfit_left", 6)),
        "mob_outfits": make_outfit_bar(battle["mob_state"].get("outfit_left", 6)),
        "mirror_event": battle.get("mirror_event", False),
        "fog_full": battle.get("fog_full", False),
        "fog_partial": battle.get("fog_partial", False),
        "player_buff_description": battle["player_state"].get("buff_description", ""),
        "mob_buff_description": battle["mob_state"].get("buff_description", ""),
        "player_message": battle["player_state"].get("message", ""),
        "player_stop": battle["player_state"].get("stop", False),
        "player_extra_draw": battle["player_state"].get("buff") == "extra_draw",
    }


async def round_result_getter(dialog_manager: DialogManager, **kwargs) -> Dict[str, Any]:
    context = dialog_manager.current_context()
    battle_id = context.dialog_data["battle_id"]
    battle = battles.find_one({"_id": ObjectId(battle_id)})
    round_number = str(battle.get("round_number", 1))
    round_data = battle.get("rounds", {}).get(round_number, {})

    winner = round_data.get("winner")
    mob_outfit_removed = round_data.get("mob_outfit_removed", 0)
    player_outfit_removed = round_data.get("player_outfit_removed", 0)
    undressing_text = (
        'Моб раздевается' if winner == 'player' else
        'Игрок раздевается' if winner == 'mob' else
        'Оба раздеваются'
    )
    event_text = battle.get("event_description", "")
    buff_text = "\n".join(
        [desc for desc in [battle["player_state"].get("buff_description", ""),
                          battle["mob_state"].get("buff_description", "")] if desc]
    )

    player_total = sum(card["power"] for card in battle["player_state"]["hand"])
    mob_total = sum(card["power"] for card in battle["mob_state"]["hand"])
    if battle.get("mirror_event", False):
        player_total, mob_total = mob_total, player_total

    if not round_data.get("text"):
        battles.update_one(
            {"_id": battle["_id"]},
            {"$set": {f"rounds.{round_number}.text": undressing_text}}
        )

    return {
        "winner": winner,
        "player_outfits": battle["player_state"].get("outfit_left", 6),
        "mob_outfits": battle["mob_state"].get("outfit_left", 6),
        "mob_outfit_removed": mob_outfit_removed,
        "player_outfit_removed": player_outfit_removed,
        "outfit_remove_text": f"{undressing_text}\n{event_text}\n{buff_text}".strip(),
        "player_bar": make_bar(player_total, show_total=not (battle.get("fog_full", False) or battle.get("fog_partial", False))),
        "mob_bar": make_bar(mob_total, show_total=not (battle.get("fog_full", False) or battle.get("fog_partial", False))),
        "player_message": battle["player_state"].get("message", ""),
    }


async def get_battle_result_text(dialog_manager: DialogManager, **kwargs) -> Dict[str, str]:
    context = dialog_manager.current_context()
    battle_id = context.dialog_data["battle_id"]
    battle = battles.find_one({"_id": ObjectId(battle_id)})
    winner = battle.get("battle_winner")
    result_text = (
        "Твоя волшба восторжествовала!" if winner == "player" else
        "Битва проиграна..." if winner == "mob" else
        "Ничья!"
    )
    return {"result_text": result_text}


async def get_magic_types(dialog_manager: DialogManager, **kwargs) -> Dict[str, list]:
    return {"magic_types": MAGIC_TYPE}


async def get_mob_outfit(dialog_manager: DialogManager, **kwargs):
    context = dialog_manager.current_context()
    mob_id = context.dialog_data["mob_id"]
    battle_id = context.dialog_data["battle_id"]
    mob_data = mobs.find_one({"_id": ObjectId(mob_id)})
    outfits = mob_data['outfit']  # словаь с ключами-числами от 1 до 6
    battle = battles.find_one({"_id": ObjectId(battle_id)})
    mob_outfit_left = battle['mob_state']['outfit_left']  # число от 6 до 0
    review_text = outfit_review_generator(mob_data['name'], outfits, mob_outfit_left)
    return {'review_text': review_text}
