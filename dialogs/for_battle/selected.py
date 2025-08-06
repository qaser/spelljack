import datetime as dt
import random

from aiogram.filters.state import State, StatesGroup
from aiogram.types import CallbackQuery
from aiogram_dialog import Dialog, DialogManager, StartMode, Window
from aiogram_dialog.widgets.kbd import Button, Row
from aiogram_dialog.widgets.text import Const, Format
from bson import ObjectId

from config.mongo_config import battles, mobs, players
from config.telegram_config import MY_TELEGRAM_ID
from dialogs.for_battle.states import Battle
from text_constants.deck import FULL_DECK
from services.mob_ai import MobAI


def draw_initial_spell(deck: list) -> dict:
    return random.choice(deck)


def create_battle(player_id, mob_id):
    full_deck = FULL_DECK.copy()
    random.shuffle(full_deck)

    battle = {
        "player_id": player_id,
        "mob_id": mob_id,
        "deck": {
            "available": full_deck,
            "in_play": [],
            "discarded": []
        },
        "round_number": 1,
        "player_state": {
            "hand": [],
            "outfit_left": 6,
            "stop": False
        },
        "mob_state": {
            "hand": [],
            "outfit_left": 6,
            "stop": False
        },
        "battle_finished": False,
        "battle_winner": None,
        "created_at": dt.datetime.now(),
        "updated_at": dt.datetime.now()
    }
    return battles.insert_one(battle).inserted_id


async def on_generate_mob(callback, widget, manager: DialogManager):
    await manager.switch_to(Battle.show_enemy_info)


async def on_battle_start(callback, widget, manager: DialogManager):
    context = manager.current_context()
    user_id = callback.from_user.id
    # player = players.find_one({"user_id": user_id})
    mob_id = context.dialog_data['mob_id']
    battle_id = create_battle(user_id, ObjectId(mob_id))
    context.dialog_data.update(battle_id=str(battle_id))
    await manager.switch_to(Battle.battle_round)


def prepare_next_round(battle: dict) -> dict:
    player_outfit = battle["player_state"].get("outfit_left", 6)
    mob_outfit = battle["mob_state"].get("outfit_left", 6)
    # Проверка завершения боя
    if player_outfit == 0 and mob_outfit == 0:
        battle["battle_winner"] = "draw"
        battle["battle_finished"] = True
    elif player_outfit == 0:
        battle["battle_winner"] = "mob"
        battle["battle_finished"] = True
    elif mob_outfit == 0:
        battle["battle_winner"] = "player"
        battle["battle_finished"] = True
    else:
        # Бой продолжается
        battle["battle_finished"] = False
        # Увеличиваем номер раунда
        battle["round_number"] = battle.get("round_number", 1) + 1
        # Возвращаем все карты из in_play в available и перемешиваем
        deck = battle["deck"]
        deck["available"].extend(deck["in_play"])
        deck["in_play"] = []
        random.shuffle(deck["available"])
        battle["deck"] = deck
        # Сброс состояния игроков (кроме одежды)
        battle["player_state"]["hand"] = []
        battle["player_state"]["stop"] = False
        battle["mob_state"]["hand"] = []
        battle["mob_state"]["stop"] = False
    battle["updated_at"] = dt.datetime.now()
    return battle


def evaluate_round_result(battle: dict) -> dict:
    player_hand = battle["player_state"]["hand"]
    mob_hand = battle["mob_state"]["hand"]

    player_total = sum(card["power"] for card in player_hand)
    mob_total = sum(card["power"] for card in mob_hand)

    player_outfits = battle["player_state"].get("outfit_left", 6)
    mob_outfits = battle["mob_state"].get("outfit_left", 6)

    # 1. Определяем победителя раунда
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

    # 2. Сколько одежды теряется
    outfit_lost = 1
    mob_outfit_removed = 0
    player_outfit_removed = 0

    if winner == "player":
        mob_outfit_removed = min(outfit_lost, mob_outfits)
        mob_outfits -= mob_outfit_removed
    elif winner == "mob":
        player_outfit_removed = min(outfit_lost, player_outfits)
        player_outfits -= player_outfit_removed
    else:  # draw
        mob_outfit_removed = min(outfit_lost, mob_outfits)
        player_outfit_removed = min(outfit_lost, player_outfits)
        mob_outfits -= mob_outfit_removed
        player_outfits -= player_outfit_removed

    # 4. Сохраняем результаты текущего раунда
    round_number = battle.get("round_number", 1)
    if "rounds" not in battle:
        battle["rounds"] = {}

    battle["rounds"][str(round_number)] = {
        "winner": winner,
        "mob_outfit_removed": mob_outfit_removed,
        "player_outfit_removed": player_outfit_removed,
        # Текст будет добавлен позже
    }

    # 5. Обновляем состояние участников
    battle["player_state"]["outfit_left"] = player_outfits
    battle["mob_state"]["outfit_left"] = mob_outfits

    # 6. Также сохраняем это в поле round_result для текущего экрана
    battle["round_result"] = {
        "winner": winner,
        "mob_outfit_removed": mob_outfit_removed,
        "player_outfit_removed": player_outfit_removed,
    }

    # 7. Определяем финального победителя поединка
    if player_outfits == 0 and mob_outfits == 0:
        battle["battle_winner"] = "draw"
    elif player_outfits == 0:
        battle["battle_winner"] = "mob"
    elif mob_outfits == 0:
        battle["battle_winner"] = "player"
    else:
        battle["battle_winner"] = None  # Битва продолжается

    return battle


def auto_play_mob(battle: dict):
    """
    Моб тянет карты, пока не решит остановиться или не произойдёт перебор.
    Обновляет: battle["mob_state"], battle["deck"]
    """
    mob_total = sum(c["power"] for c in battle["mob_state"]["hand"])
    mob_ai = MobAI(battle["mob_state"].get("strategy", "balanced"))
    mob_ai.influence = battle["mob_state"].get("outfit_left", 6)
    mob_ai.energy = mob_total
    available = battle["deck"]["available"]
    in_play = battle["deck"]["in_play"]
    while not battle["mob_state"]["stop"]:
        decision = mob_ai.make_decision(battle["player_state"].get("outfit_left", 6))
        if decision == "draw" and available:
            mob_card = available.pop()
            battle["mob_state"]["hand"].append(mob_card)
            in_play.append(mob_card)
            mob_total += mob_card["power"]
            if mob_total > 21:
                battle["mob_state"]["stop"] = True
        else:
            battle["mob_state"]["stop"] = True
    battle["deck"]["available"] = available
    battle["deck"]["in_play"] = in_play


async def on_draw(callback: CallbackQuery, button: Button, manager: DialogManager):
    context = manager.current_context()
    battle_id = context.dialog_data["battle_id"]
    battle = battles.find_one({"_id": ObjectId(battle_id)})

    if battle["player_state"]["stop"]:
        await callback.answer("Вы уже остановили поглащение магии!")
        return

    deck = battle["deck"]
    available = deck["available"]
    in_play = deck["in_play"]

    if not available:
        await callback.answer("Источник магии иссяк!")
        return

    # --- Игрок тянет карту ---
    player_card = available.pop()
    battle["player_state"]["hand"].append(player_card)
    in_play.append(player_card)

    player_total = sum(c["power"] for c in battle["player_state"]["hand"])
    battle["deck"]["available"] = available
    battle["deck"]["in_play"] = in_play

    if player_total > 21:
        battle["player_state"]["stop"] = True
        await callback.answer(f"‼️ Магия перехлестнула Вас")
        # Моб доигрывает автоматически
        auto_play_mob(battle)
        battle_update = evaluate_round_result(battle)
        battles.update_one({"_id": battle["_id"]}, {"$set": {
            f"rounds.{battle['round_number']}": battle_update["round_result"],
            "player_state": battle_update["player_state"],
            "mob_state": battle_update["mob_state"],
            "deck": battle_update["deck"],
            "updated_at": dt.datetime.now()
        }})
        await manager.switch_to(Battle.round_result)
    else:
        await callback.answer(f"✨ Вы зачерпнули из магической сферы ⋆｡˚ {player_card['magic_type']} ⋆｡˚ ({player_card['power']})")

    # Ход моба, если он не остановился
    if not battle["mob_state"]["stop"]:
        auto_play_mob(battle)

    # Сохраняем изменения
    battles.update_one({"_id": battle["_id"]}, {"$set": {
        "deck": battle["deck"],
        "player_state": battle["player_state"],
        "mob_state": battle["mob_state"],
        "updated_at": dt.datetime.now()
    }})

    if battle["player_state"]["stop"] and battle["mob_state"]["stop"]:
        battle_update = evaluate_round_result(battle)
        battles.update_one({"_id": battle["_id"]}, {"$set": {
            f"rounds.{battle['round_number']}": battle_update["round_result"],
            "player_state": battle_update["player_state"],
            "mob_state": battle_update["mob_state"],
            "deck": battle_update["deck"],
            "updated_at": dt.datetime.now()
        }})
        await manager.switch_to(Battle.round_result)
    else:
        await manager.switch_to(Battle.battle_round)


async def on_stop(callback: CallbackQuery, button: Button, manager: DialogManager):
    context = manager.current_context()
    battle_id = context.dialog_data["battle_id"]
    battle = battles.find_one({"_id": ObjectId(battle_id)})

    battle["player_state"]["stop"] = True

    # Моб доигрывает автоматически
    auto_play_mob(battle)

    battle_update = evaluate_round_result(battle)
    battles.update_one({"_id": battle["_id"]}, {"$set": {
        f"rounds.{battle['round_number']}": battle_update["round_result"],
        "player_state": battle_update["player_state"],
        "mob_state": battle_update["mob_state"],
        "deck": battle_update["deck"],
        "updated_at": dt.datetime.now()
    }})

    await callback.answer("🫳 Ты произнёс заклинание.")
    await manager.switch_to(Battle.round_result)



async def on_escape(callback: CallbackQuery, button: Button, manager: DialogManager):
    context = manager.current_context()


async def on_next_round(callback: CallbackQuery, button: Button, manager: DialogManager):
    context = manager.current_context()
    battle_id = context.dialog_data["battle_id"]
    battle = battles.find_one({"_id": ObjectId(battle_id)})

    # Подготовка к новому раунду (или завершение боя)
    updated_battle = prepare_next_round(battle)

    # Сохраняем бой
    battles.update_one({"_id": battle["_id"]}, {"$set": {
        "round_number": updated_battle.get("round_number"),
        "deck": updated_battle["deck"],
        "player_state": updated_battle["player_state"],
        "mob_state": updated_battle["mob_state"],
        "battle_winner": updated_battle.get("battle_winner"),
        "battle_finished": updated_battle["battle_finished"],
        "updated_at": updated_battle["updated_at"]
    }})

    if updated_battle["battle_finished"]:
        await callback.answer("🏁 Битва завершена!")
        await manager.switch_to(Battle.battle_result)
    else:
        await callback.answer("✨ Новый раунд начинается!")
        await manager.switch_to(Battle.battle_round)



async def on_outfit(callback: CallbackQuery, button: Button, manager: DialogManager):
    context = manager.current_context()
