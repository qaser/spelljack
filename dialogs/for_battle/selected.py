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

from . import states


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
        "status": "active",
        "winner": None,
        "created_at": dt.datetime.now(),
        "updated_at": dt.datetime.now()
    }
    return battles.insert_one(battle).inserted_id


async def on_generate_mob(callback, widget, manager: DialogManager):
    await manager.switch_to(states.Battle.show_enemy_info)


async def on_battle_start(callback, widget, manager: DialogManager):
    context = manager.current_context()
    user_id = callback.from_user.id
    # player = players.find_one({"user_id": user_id})
    mob_id = context.dialog_data['mob_id']
    battle_id = create_battle(user_id, ObjectId(mob_id))
    context.dialog_data.update(battle_id=str(battle_id))
    await manager.switch_to(states.Battle.battle_round)


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
        await callback.answer("Ты уже произнёс заклинание!")
        return

    deck = battle["deck"]
    available = deck["available"]
    in_play = deck["in_play"]

    if not available:
        await callback.answer("Колода закончилась!")
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
        await callback.answer(f"💥 Перебор! ({player_total})")

        # Моб доигрывает автоматически
        auto_play_mob(battle)

        # Обновление и переход к итогу раунда
        battles.update_one({"_id": battle["_id"]}, {"$set": {
            "deck": battle["deck"],
            "player_state": battle["player_state"],
            "mob_state": battle["mob_state"],
            "updated_at": dt.datetime.now()
        }})
        await manager.switch_to(Battle.round_result)
    else:
        await callback.answer(f"✨ Новое заклинание: {player_card['name']} ({player_card['power']})")

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
        await manager.switch_to(Battle.round_result)
    else:
        await manager.switch_to(states.Battle.battle_round)


async def on_stop(callback: CallbackQuery, button: Button, manager: DialogManager):
    context = manager.current_context()
    battle_id = context.dialog_data["battle_id"]
    battle = battles.find_one({"_id": ObjectId(battle_id)})

    battle["player_state"]["stop"] = True

    # Моб доигрывает автоматически
    auto_play_mob(battle)

    # Обновляем БД
    battles.update_one({"_id": battle["_id"]}, {"$set": {
        "player_state": battle["player_state"],
        "mob_state": battle["mob_state"],
        "deck": battle["deck"],
        "updated_at": dt.datetime.now()
    }})

    await callback.answer("🫳 Ты произнёс заклинание.")

    await manager.switch_to(Battle.round_result)



async def on_escape(callback: CallbackQuery, button: Button, manager: DialogManager):
    context = manager.current_context()


async def on_next_round(callback: CallbackQuery, button: Button, manager: DialogManager):
    context = manager.current_context()


async def on_outfit(callback: CallbackQuery, button: Button, manager: DialogManager):
    context = manager.current_context()
