import datetime as dt
import random
from typing import Dict
from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from bson import ObjectId

from config.mongo_config import battles, mobs, players
from dialogs.for_battle.states import Battle
from text_constants.deck import NEW_DECK_ALTER
from services.mob_ai import MobAI
from .events import trigger_random_event
from .buffs import apply_buff


def draw_initial_spell(deck: list) -> dict:
    return random.choice(deck)


def create_battle(player_id: int, mob_id: ObjectId, magic_type: str) -> ObjectId:
    full_deck = NEW_DECK_ALTER.copy()
    random.shuffle(full_deck)
    mob = mobs.find_one({"_id": mob_id})
    battle = {
        "player_id": player_id,
        "mob_id": mob_id,
        "magic_type": magic_type,
        "mob_state": {
            "hand": [],
            "outfit_left": 6,
            "stop": False,
            "magic_type": mob.get("magic_type", "Вожделение"),
            "buff": None,
            "buff_description": ""
        },
        "deck": {"available": full_deck, "in_play": [], "discarded": []},
        "round_number": 1,
        "player_state": {"hand": [], "outfit_left": 6, "stop": False, "buff": None, "buff_description": ""},
        "battle_finished": False,
        "battle_winner": None,
        "mirror_event": False,
        "fog_event": False,
        "event_description": "",
        "created_at": dt.datetime.now(),
        "updated_at": dt.datetime.now()
    }
    return battles.insert_one(battle).inserted_id


async def on_select_magic_type(callback: CallbackQuery, widget, manager: DialogManager, selected_magic: str):
    context = manager.current_context()
    context.dialog_data["magic_type"] = selected_magic
    await manager.switch_to(Battle.select_enemy_type)


async def on_generate_mob(callback: CallbackQuery, widget, manager: DialogManager):
    await manager.switch_to(Battle.show_enemy_info)


async def on_battle_start(callback: CallbackQuery, widget, manager: DialogManager):
    context = manager.current_context()
    user_id = callback.from_user.id
    mob_id = context.dialog_data['mob_id']
    magic_type = context.dialog_data.get('magic_type', 'Вожделение')
    battle_id = create_battle(user_id, ObjectId(mob_id), magic_type)
    context.dialog_data["battle_id"] = str(battle_id)
    await manager.switch_to(Battle.battle_round)


def evaluate_round_result(battle: Dict) -> Dict:
    player_total = sum(card["power"] for card in battle["player_state"]["hand"])
    mob_total = sum(card["power"] for card in battle["mob_state"]["hand"])
    if battle.get("mirror_event"):
        player_total, mob_total = mob_total, player_total

    player_outfits = battle["player_state"].get("outfit_left", 6)
    mob_outfits = battle["mob_state"].get("outfit_left", 6)
    player_buff = battle["player_state"].get("buff")
    mob_buff = battle["mob_state"].get("buff")

    winner = (
        "draw" if player_total > 21 and mob_total > 21 else
        "mob" if player_total > 21 else
        "player" if mob_total > 21 else
        "player" if player_total > mob_total else
        "mob" if mob_total > player_total else
        "draw"
    )

    outfit_lost = 1
    mob_outfit_removed = min(outfit_lost, mob_outfits) if winner in ["player", "draw"] and mob_buff != "preserve_outfit" else 0
    player_outfit_removed = min(outfit_lost, player_outfits) if winner in ["mob", "draw"] and player_buff != "preserve_outfit" else 0

    battle["player_state"]["outfit_left"] = player_outfits - player_outfit_removed
    battle["mob_state"]["outfit_left"] = mob_outfits - mob_outfit_removed
    battle["rounds"] = battle.get("rounds", {})
    battle["rounds"][str(battle.get("round_number", 1))] = {
        "winner": winner,
        "mob_outfit_removed": mob_outfit_removed,
        "player_outfit_removed": player_outfit_removed,
    }
    battle["round_result"] = {
        "winner": winner,
        "mob_outfit_removed": mob_outfit_removed,
        "player_outfit_removed": player_outfit_removed,
    }
    battle["battle_winner"] = (
        "draw" if battle["player_state"]["outfit_left"] == 0 and battle["mob_state"]["outfit_left"] == 0 else
        "mob" if battle["player_state"]["outfit_left"] == 0 else
        "player" if battle["mob_state"]["outfit_left"] == 0 else
        None
    )
    # Очистка бафов после раунда
    battle["player_state"]["buff"] = None
    battle["player_state"]["buff_description"] = ""
    battle["mob_state"]["buff"] = None
    battle["mob_state"]["buff_description"] = ""
    return battle


def prepare_next_round(battle: Dict) -> Dict:
    battle["battle_finished"] = battle["player_state"]["outfit_left"] == 0 or battle["mob_state"]["outfit_left"] == 0
    if not battle["battle_finished"]:
        battle = trigger_random_event(battle)
        battle["round_number"] = battle.get("round_number", 1) + 1
        battle["deck"]["available"].extend(battle["deck"]["in_play"])
        battle["deck"]["in_play"] = []
        random.shuffle(battle["deck"]["available"])
        battle["player_state"].update({"hand": [], "stop": False, "buff": None, "buff_description": ""})
        battle["mob_state"].update({"hand": [], "stop": False, "buff": None, "buff_description": ""})
    battle["updated_at"] = dt.datetime.now()
    return battle


def auto_play_mob(battle: Dict):
    mob_total = sum(c["power"] for c in battle["mob_state"]["hand"])
    mob_ai = MobAI(battle["mob_state"].get("strategy", "balanced"))
    mob_ai.influence = battle["mob_state"].get("outfit_left", 6)
    mob_ai.energy = mob_total
    available = battle["deck"]["available"]
    in_play = battle["deck"]["in_play"]

    if battle["player_state"].get("buff") == "block_mob":
        battle["mob_state"]["stop"] = True
        return

    while not battle["mob_state"]["stop"] and available:
        if mob_ai.make_decision(battle["player_state"].get("outfit_left", 6)) == "draw":
            mob_card = available.pop()
            battle = apply_buff("mob", mob_card, battle)
            battle["mob_state"]["hand"].append(mob_card)
            in_play.append(mob_card)
            mob_total += mob_card["power"]
            if mob_total > 21:
                battle["mob_state"]["stop"] = True
        else:
            battle["mob_state"]["stop"] = True
        if battle["mob_state"].get("buff") == "extra_draw" and battle["mob_state"]["stop"] and available:
            battle["mob_state"]["stop"] = False  # Позволяем взять ещё одну карту
    battle["deck"].update({"available": available, "in_play": in_play})


async def on_draw(callback: CallbackQuery, button, manager: DialogManager):
    context = manager.current_context()
    battle_id = context.dialog_data["battle_id"]
    battle = battles.find_one({"_id": ObjectId(battle_id)})

    if battle["player_state"]["stop"]:
        if battle["player_state"].get("buff") == "extra_draw" and battle["deck"]["available"]:
            battle["player_state"]["stop"] = False
        else:
            await callback.answer("Вы уже остановили поглащение магии!")
            return

    if not battle["deck"]["available"]:
        await callback.answer("Источник магии иссяк!")
        return

    player_card = battle["deck"]["available"].pop()
    battle = apply_buff("player", player_card, battle)
    battle["player_state"]["hand"].append(player_card)
    battle["deck"]["in_play"].append(player_card)
    player_total = sum(c["power"] for c in battle["player_state"]["hand"])

    buff_message = battle["player_state"].get("buff_description", "")
    if buff_message:
        await callback.answer(f"Вы зачерпнули из магической сферы ({player_card['power']})\n{buff_message}")
    else:
        await callback.answer(f"Вы зачерпнули из магической сферы ({player_card['power']})")

    if player_total > 21:
        battle["player_state"]["stop"] = True
        await callback.answer("‼️ Магия перехлестнула Вас")
        auto_play_mob(battle)
        battle = evaluate_round_result(battle)
        battles.update_one({"_id": battle["_id"]}, {"$set": battle})
        await manager.switch_to(Battle.round_result)
    else:
        if not battle["mob_state"]["stop"]:
            auto_play_mob(battle)
        battles.update_one({"_id": battle["_id"]}, {"$set": battle})
        if battle["player_state"]["stop"] and battle["mob_state"]["stop"]:
            battle = evaluate_round_result(battle)
            battles.update_one({"_id": battle["_id"]}, {"$set": battle})
            await manager.switch_to(Battle.round_result)
        else:
            await manager.switch_to(Battle.battle_round)


async def on_stop(callback: CallbackQuery, button, manager: DialogManager):
    context = manager.current_context()
    battle_id = context.dialog_data["battle_id"]
    battle = battles.find_one({"_id": ObjectId(battle_id)})
    battle["player_state"]["stop"] = True
    auto_play_mob(battle)
    battle = evaluate_round_result(battle)
    battles.update_one({"_id": battle["_id"]}, {"$set": battle})
    await callback.answer("Ты произнёс заклинание")
    await manager.switch_to(Battle.round_result)


async def on_escape(callback: CallbackQuery, button, manager: DialogManager):
    await manager.done()


async def on_next_round(callback: CallbackQuery, button, manager: DialogManager):
    context = manager.current_context()
    battle_id = context.dialog_data["battle_id"]
    battle = battles.find_one({"_id": ObjectId(battle_id)})
    battle = prepare_next_round(battle)
    battles.update_one({"_id": battle["_id"]}, {"$set": battle})
    if battle["battle_finished"]:
        await callback.answer("🏁 Битва завершена!")
        await manager.switch_to(Battle.battle_result)
    else:
        await callback.answer("✨ Новый раунд начинается!")
        await manager.switch_to(Battle.battle_round)


async def on_outfit(callback: CallbackQuery, button, manager: DialogManager):
    pass  # Placeholder for outfit overview logic
