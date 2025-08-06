import datetime as dt
import random

from aiogram_dialog import DialogManager
from bson import ObjectId
from dateutil.relativedelta import relativedelta

from config.mongo_config import battles, mobs, players
from dialogs.for_battle.states import Battle
from services.mob_factory import generate_random_mob, get_random_mob_for_player
from text_generators.generate_mob_intro import generate_mob_intro
from text_generators.outfit_remove_generator import generate_undressing_text


def outfit_emoji(count: int, is_player=True) -> str:
    # Всего 6 уровней одежды, от нижнего к верхнему
    player_emojis = ['🩲', '🩱', '🧦', '👗', '🧥', '🎀']
    mob_emojis = ['🩳', '👚', '👖', '👔', '🧥', '📿']

    # Переворачиваем порядок, чтобы верхняя одежда шла слева
    outfit = player_emojis if is_player else mob_emojis
    return ''.join(outfit[-count:])  # последние count элементов слева направо


async def get_mob_data(dialog_manager: DialogManager, **kwargs):
    context = dialog_manager.current_context()
    mob_id = generate_random_mob()
    context.dialog_data.update(mob_id=str(mob_id))
    mob_data = mobs.find_one({"_id": mob_id})
    if not mob_data:
        return {"desc": "Ошибка загрузки информации о сопернике"}
    enemy_intro = generate_mob_intro(mob_data)
    return {"enemy_intro": enemy_intro}


def make_bar(total: int) -> str:
    MAX = 21
    SLOTS = 10
    if total > MAX:
        return "🟥" * SLOTS + f" ({total})"
    filled_ratio = total / MAX
    filled_slots = round(filled_ratio * SLOTS)
    empty_slots = SLOTS - filled_slots
    if total <= 12:
        filled = "🟨" * filled_slots
    elif 13 <= total <= 17:
        filled = "🟩" * filled_slots
    elif total == 21:
        filled = '🟪' * filled_slots
    else:
        filled = "🟧" * filled_slots
    bar = filled + "⬜" * empty_slots
    return f"{bar} ({total})"



def make_outfit_bar(outfits_left: int, total: int = 6) -> str:
    return "".join(["❤️"] * outfits_left + ["🤍"] * (total - outfits_left))


async def get_battle_state(dialog_manager: DialogManager, **kwargs):
    context = dialog_manager.current_context()
    battle_id = context.dialog_data["battle_id"]
    battle = battles.find_one({"_id": ObjectId(battle_id)})
    player_hand = battle["player_state"]["hand"]
    mob_hand = battle["mob_state"]["hand"]
    player_total = sum(card["power"] for card in player_hand)
    mob_total = sum(card["power"] for card in mob_hand)
    round_number = battle.get("round_number", 1)
    player_outfits = battle["player_state"].get("outfit_left", 6)
    mob_outfits = battle["mob_state"].get("outfit_left", 6)
    return {
        "player_bar": make_bar(player_total),
        "player_total": player_total,
        "mob_total": mob_total,
        "battle_id": str(battle_id),
        "round_number": round_number,
        "player_outfits": make_outfit_bar(player_outfits),
        "mob_outfits": make_outfit_bar(mob_outfits),
    }


async def round_result_getter(dialog_manager: DialogManager, **kwargs):
    context = dialog_manager.current_context()
    battle_id = context.dialog_data["battle_id"]
    battle = battles.find_one({"_id": ObjectId(battle_id)})

    round_number = str(battle.get("round_number", 1))
    round_data = battle.get("rounds", {}).get(round_number, {})

    winner = round_data.get("winner")
    mob_outfit_removed = round_data.get("mob_outfit_removed", 0)
    undressing_text = round_data.get("text", "Оба раздеваются")

    player_outfits = battle["player_state"].get("outfit_left", 6)
    mob_outfits = battle["mob_state"].get("outfit_left", 6)

    player_hand = battle["player_state"]["hand"]
    mob_hand = battle["mob_state"]["hand"]
    player_total = sum(card["power"] for card in player_hand)
    mob_total = sum(card["power"] for card in mob_hand)

    # Если текста всё ещё нет, можно сгенерировать и обновить
    if not round_data.get("text"):
        if winner == 'player':
            undressing_text = 'Моб раздевается'
        elif winner == "mob":
            undressing_text = 'Игрок раздевается'
        else:
            undressing_text = 'Оба раздеваются'

        # Обновим и в rounds, и в round_result
        battles.update_one({"_id": battle["_id"]}, {
            "$set": {
                f"rounds.{round_number}.text": undressing_text,
                "round_result.text": undressing_text  # Если нужно для совместимости
            }
        })

    return {
        "winner": winner,
        "player_outfits": player_outfits,
        "mob_outfits": mob_outfits,
        "mob_outfit_removed": mob_outfit_removed,
        "outfit_remove_text": undressing_text,
        "player_bar": make_bar(player_total),
        "mob_bar": make_bar(mob_total),
    }




async def get_battle_result_text(dialog_manager: DialogManager, **kwargs):
    context = dialog_manager.current_context()
    battle_id = context.dialog_data["battle_id"]
    battle = battles.find_one({"_id": ObjectId(battle_id)})

    winner = battle.get("battle_winner")
    mob_obj = mobs.find_one({"_id": battle["mob_id"]})
    mob_name = f"{mob_obj['title']} {mob_obj['name']}"

    if winner == "player":
        result_text = f"✨ Ты полностью победил {mob_name} — ни ниточки не осталось! Твоя волшба восторжествовала!"
    elif winner == "mob":
        result_text = f"💥 {mob_name} оказался слишком силён. Твоя одежда разлетелась клочьями. Битва проиграна..."
    else:
        result_text = f"⚖️ Оба мага остались без прикрытия. Что за дуэль такая — ничья!"

    return {"result_text": result_text}
