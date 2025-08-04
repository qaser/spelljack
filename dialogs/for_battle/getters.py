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

    player_hand = battle["player_state"]["hand"]
    mob_hand = battle["mob_state"]["hand"]

    player_total = sum(card["power"] for card in player_hand)
    mob_total = sum(card["power"] for card in mob_hand)

    player_outfits = battle["player_state"].get("outfit_left", 6)
    mob_outfits = battle["mob_state"].get("outfit_left", 6)

    # 1. Определяем победителя
    if player_total > 21 and mob_total > 21:
        winner = "draw"
    elif player_total > 21:
        winner = "mob"
    elif mob_total > 21:
        winner = "player"
    elif player_total > mob_total:
        winner = "player"
    elif mob_total > player_total:
        winner = "mob"
    else:
        winner = "draw"

    # 2. Обновляем количество оставшейся одежды
    outfit_lost = 1  # по умолчанию теряется 1
    if winner == "player":
        mob_outfits = max(0, mob_outfits - outfit_lost)
    elif winner == "mob":
        player_outfits = max(0, player_outfits - outfit_lost)
    elif winner == "draw":
        player_outfits = max(0, player_outfits - outfit_lost)
        mob_outfits = max(0, mob_outfits - outfit_lost)

    # 3. Сильнейшие заклинания
    strongest_player_spell = max(player_hand, key=lambda c: c["power"]) if player_hand else None
    strongest_mob_spell = max(mob_hand, key=lambda c: c["power"]) if mob_hand else None

    # 4. Одежда, которую должен снять моб
    mob_outfit_removed = outfit_lost if winner in ("player", "draw") else 0

    # 5. Текст волшбы
    # mob_name = battle["mob_state"]["name"]
    mob_name = 'Моргана'
    if mob_outfit_removed > 0 and strongest_player_spell:
        outfit_index = battle["mob_state"].get("outfit_left", 6)  # до вычитания
        outfit_key = str(outfit_index)
        outfit_name = 'трусики'
        if outfit_name:
            undressing_text = generate_undressing_text(mob_name, str(outfit_index), outfit_name, strongest_player_spell["name"])
            print(undressing_text)
        else:
            undressing_text = f"{mob_name} потерял часть одежды."
    elif winner == "mob" and strongest_mob_spell:
        undressing_text = f"Заклинание {strongest_mob_spell['name']} выбило из тебя кусочек одежды..."
    else:
        undressing_text = "От заклинаний повеяло жаром, и вы оба чуть приоткрылись..."

    # Обновляем состояние битвы
    battles.update_one({"_id": battle["_id"]}, {"$set": {
        "player_state.outfit_left": player_outfits,
        "mob_state.outfit_left": mob_outfits,
        "round_result": {
            "winner": winner,
            "strongest_player_spell": strongest_player_spell,
            "strongest_mob_spell": strongest_mob_spell,
            "mob_outfit_removed": mob_outfit_removed,
            "text": undressing_text
        }
    }})

    result_data =  {
        "winner": winner,
        "player_outfits": player_outfits,
        "mob_outfits": mob_outfits,
        "strongest_player_spell": strongest_player_spell,
        "strongest_mob_spell": strongest_mob_spell,
        "mob_outfit_removed": mob_outfit_removed,
        "outfit_remove_text": undressing_text,
    }
    # print(result_data)
    return result_data
