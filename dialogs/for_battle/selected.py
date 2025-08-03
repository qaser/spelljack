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


def create_battle(player_id: int, mob_id: ObjectId) -> ObjectId:
    shuffled_deck = random.sample(FULL_DECK, len(FULL_DECK))

    battle = {
        "player_id": player_id,
        "mob_id": mob_id,
        "player_state": {
            "hp": 5,
            "hand": [],
            "casted": False,
            "is_turn": True
        },
        "mob_state": {
            "hp": 5,
            "hand": [],
            "casted": False
        },
        "shared_deck": shuffled_deck,
        "turn_number": 1,
        "status": "active",
        "winner": None,
        "history": [],
        "created_at": dt.datetime.now(),
        "updated_at": dt.datetime.now()
    }

    result = battles.insert_one(battle)
    return result.inserted_id


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
    user_id = callback.from_user.id
    context = manager.current_context()
    battle_id = ObjectId(context.dialog_data["battle_id"])
    battle = battles.find_one({"_id": battle_id})

    player_state = battle["player_state"]
    hand = player_state["hand"]
    shared_deck = battle.get("shared_deck", [])

    if not shared_deck:
        await callback.answer("❗ Общая колода пуста!")
        return

    # Вытянуть верхнюю карту
    new_card = shared_deck.pop(0)
    hand.append(new_card)

    total = sum(card["power"] for card in hand)

    update = {
        "player_state.hand": hand,
        "shared_deck": shared_deck
    }

    history_entry = {
        "actor": "player",
        "action": "draw",
        "card": new_card,
        "result": None,
        "timestamp": callback.message.date
    }

    if total > 21:
        update["status"] = "finished"
        update["winner"] = "mob"
        history_entry["result"] = "overload"

        battles.update_one({"_id": battle_id}, {
            "$set": update,
            "$push": {"history": history_entry}
        })

        await callback.answer("💥 Ты перегрузился чарами!")
        # Здесь позже переход к сцене поражения
        return

    # Обновление БД
    battles.update_one({"_id": battle_id}, {
        "$set": update,
        "$push": {"history": history_entry}
    })

    await callback.answer("✨ Ты вплёл новое заклинание!")
    await manager.switch_to(Battle.battle_round)


async def on_stop(callback: CallbackQuery, button: Button, manager: DialogManager):
    await callback.answer("🧘 Пока не реализовано: стоп")
