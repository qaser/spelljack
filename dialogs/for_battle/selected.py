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

from . import states


from utils.constants import FULL_DECK


def draw_initial_spell(deck: list) -> dict:
    return random.choice(deck)


def create_battle(player_id, mob_id):
    from random import shuffle

    full_deck = [
        {"name": f"Чары {i}", "power": i, "type": t}
        for i in range(1, 12)
        for t in ["страсть", "нежность", "искушение", "соблазн"]
    ]
    shuffle(full_deck)

    battle = {
        "player_id": player_id,
        "mob_id": mob_id,
        "deck": full_deck,
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


async def on_battle_round(callback, widget, manager: DialogManager):
    user_id = callback.from_user.id
    player = players.find_one({"user_id": user_id})
    context = manager.current_context()
    mob_id = context.dialog_data['mob_id']
    battle_id = create_battle(user_id, ObjectId(mob_id))
    context.dialog_data.update(battle_id=str(battle_id))
    await manager.switch_to(states.Battle.battle_round)


async def on_cast(callback: CallbackQuery, button: Button, manager: DialogManager):
    context = manager.current_context()
    battle_id = context.dialog_data["battle_id"]
    battle = battles.find_one({"_id": ObjectId(battle_id)})

    # Проверка — не остановился ли игрок
    if battle["player_state"]["stop"]:
        await callback.answer("Ты уже произнёс заклинание!")
        return

    deck = battle["deck"]
    if not deck:
        await callback.answer("Колода закончилась!")
        return

    # Игрок тянет карту
    drawn_card = deck.pop()
    battle["player_state"]["hand"].append(drawn_card)

    # Проверка на перебор
    total = sum(c["power"] for c in battle["player_state"]["hand"])
    if total > 21:
        battle["player_state"]["stop"] = True  # Автостоп
        await callback.answer(f"💥 Перебор! ({total})")
    else:
        await callback.answer(f"✨ Новое заклинание: {drawn_card['name']} ({drawn_card['power']})")

    # Обновление колоды и состояния
    battles.update_one({"_id": battle["_id"]}, {"$set": {
        "deck": deck,
        "player_state": battle["player_state"],
        "updated_at": dt.datetime.now()
    }})

    await manager.dialog().switch_to(Battle.battle_round)



async def on_stop(callback: CallbackQuery, button: Button, manager: DialogManager):
    context = manager.current_context()
    battle_id = context.dialog_data["battle_id"]
    battle = battles.find_one({"_id": ObjectId(battle_id)})

    battle["player_state"]["stop"] = True
    battles.update_one({"_id": battle["_id"]}, {"$set": {
        "player_state.stop": True,
        "updated_at": dt.datetime.now()
    }})

    await callback.answer("🫳 Ты произнёс заклинание.")
    await manager.dialog().switch_to(Battle.round_step)
