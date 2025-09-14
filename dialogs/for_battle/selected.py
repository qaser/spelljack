import datetime as dt
import random
from typing import Dict
from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from bson import ObjectId
from aiogram_dialog.api.entities import MediaAttachment, MediaId
from aiogram.enums import ContentType

from config.mongo_config import battles, mobs, players, mob_meta
from dialogs.for_battle.states import Battle
from dialogs.for_battle.utils import update_player_after_battle
from dialogs.for_scene.states import Scene
from .constants import DECK, MAGIC_TYPE
from services.mob_ai import MobAI
from .events import trigger_random_event, FOG_FULL_THRESHOLD, FOG_PARTIAL_THRESHOLD

def draw_initial_spell(deck: list) -> dict:
    return random.choice(deck)

def create_battle(player_id: int, mob_id: ObjectId, magic_type: str) -> ObjectId:
    full_deck = DECK.copy()
    random.shuffle(full_deck)
    mob = mobs.find_one({"_id": mob_id})
    battle = {
        "player_id": player_id,
        "mob_id": mob_id,
        "magic_type": magic_type,
        "mob_state": {
            "hand": [],
            "hitpoints_left": 6,
            "stop": False,
            "magic_type": mob.get("magic_type", "Вожделение"),
            "message": "",
        },
        "deck": {"available": full_deck, "in_play": [], "discarded": []},
        "round_number": 1,
        "player_state": {
            "hand": [],
            "hitpoints_left": 6,
            "stop": False,
            "message": "",
        },
        "battle_finished": False,
        "battle_winner": None,
        "mirror_event": False,
        "fog_full": False,
        "fog_partial": False,
        "event_description": "",
        "player_type_spell_count": 0,
        "consecutive_player_wins": 0,
        "created_at": dt.datetime.now(),
        "updated_at": dt.datetime.now(),
    }
    return battles.insert_one(battle).inserted_id

async def on_select_magic_type(callback, widget, manager, selected_magic):
    context = manager.current_context()
    context.dialog_data["magic_type"] = selected_magic
    await manager.switch_to(Battle.select_enemy_type)

async def on_generate_mob(callback, widget, manager):
    await manager.switch_to(Battle.show_battle_preview)

async def on_battle_start(callback: CallbackQuery, widget, manager: DialogManager):
    context = manager.current_context()
    user_id = callback.from_user.id
    mob_id = context.dialog_data['mob_id']
    magic_type = context.dialog_data.get('magic_type')
    if magic_type in MAGIC_TYPE:
        players.update_one(
            {"_id": user_id},
            {"$inc": {f"magic.{magic_type}": 1}}
        )
    battle_id = create_battle(user_id, ObjectId(mob_id), magic_type)
    context.dialog_data["battle_id"] = str(battle_id)
    await manager.switch_to(Battle.battle_round)

def evaluate_round_result(battle: Dict) -> Dict:
    player_total = sum(card["power"] for card in battle["player_state"]["hand"])
    mob_total = sum(card["power"] for card in battle["mob_state"]["hand"])
    if battle.get("mirror_event"):
        player_total, mob_total = mob_total, player_total

    player_hitpoints = battle["player_state"].get("hitpoints_left", 6)
    mob_hitpoints = battle["mob_state"].get("hitpoints_left", 6)

    winner = (
        "draw"
        if player_total > 21 and mob_total > 21
        else (
            "mob"
            if player_total > 21
            else (
                "player"
                if mob_total > 21
                else (
                    "player"
                    if player_total > mob_total
                    else "mob" if mob_total > player_total else "draw"
                )
            )
        )
    )

    # Update consecutive wins
    if winner == "player" and battle["consecutive_player_wins"] <= FOG_FULL_THRESHOLD:
        battle["consecutive_player_wins"] = battle.get("consecutive_player_wins", 0) + 1
    else:
        battle["consecutive_player_wins"] = 0

    hitpoints_lost = 1
    mob_hitpoints_removed = min(hitpoints_lost, mob_hitpoints) if winner in ["player", "draw"] else 0
    player_hitpoints_removed = min(hitpoints_lost, player_hitpoints) if winner in ["mob", "draw"] else 0

    battle["player_state"]["hitpoints_left"] = player_hitpoints - player_hitpoints_removed
    battle["mob_state"]["hitpoints_left"] = mob_hitpoints - mob_hitpoints_removed
    battle["rounds"] = battle.get("rounds", {})
    battle["rounds"][str(battle.get("round_number", 1))] = {
        "winner": winner,
        "mob_hitpoints_removed": mob_hitpoints_removed,
        "player_hitpoints_removed": player_hitpoints_removed,
    }
    battle["round_result"] = {
        "winner": winner,
        "mob_hitpoints_removed": mob_hitpoints_removed,
        "player_hitpoints_removed": player_hitpoints_removed,
    }
    battle["battle_winner"] = (
        "draw"
        if battle["player_state"]["hitpoints_left"] == 0
        and battle["mob_state"]["hitpoints_left"] == 0
        else (
            "mob"
            if battle["player_state"]["hitpoints_left"] == 0
            else "player" if battle["mob_state"]["hitpoints_left"] == 0 else None
        )
    )
    # Clear messages after round
    battle["player_state"]["message"] = ""
    battle["mob_state"]["message"] = ""
    return battle

def prepare_next_round(battle: Dict) -> Dict:
    battle["battle_finished"] = (
        battle["player_state"]["hitpoints_left"] == 0
        or battle["mob_state"]["hitpoints_left"] == 0
    )
    if not battle["battle_finished"]:
        battle = trigger_random_event(battle)
        battle["round_number"] = battle.get("round_number", 1) + 1
        battle["deck"]["available"].extend(battle["deck"]["in_play"])
        battle["deck"]["in_play"] = []
        random.shuffle(battle["deck"]["available"])
        battle["player_state"].update(
            {
                "hand": [],
                "stop": False,
                "message": "",
            }
        )
        battle["mob_state"].update(
            {
                "hand": [],
                "stop": False,
                "message": "",
            }
        )
    battle["updated_at"] = dt.datetime.now()
    return battle

def get_stage_image(stage, meta_id):
    try:
        meta_data = mob_meta.find_one({'_id': meta_id})
        images_list = meta_data['images']['actions'][stage]
        image_random = random.choice(images_list)
        image = MediaAttachment(ContentType.PHOTO, file_id=MediaId(image_random['telegram_file_id']))
        return (image, True)
    except:
        return ('', False)

def auto_play_mob(battle: Dict):
    mob_total = sum(c["power"] for c in battle["mob_state"]["hand"])
    mob_ai = MobAI(battle["mob_state"].get("strategy", "balanced"))
    mob_ai.influence = battle["mob_state"].get("hitpoints_left", 6)
    mob_ai.energy = mob_total
    available = battle["deck"]["available"]
    in_play = battle["deck"]["in_play"]

    while not battle["mob_state"]["stop"] and available:
        if (
            mob_ai.make_decision(
                battle["player_state"].get("hitpoints_left", 6),
                battle.get("mirror_event", False),
                battle.get("fog_full", False) or battle.get("fog_partial", False),
            )
            == "draw"
        ):
            mob_card = available.pop()
            battle["mob_state"]["hand"].append(mob_card)
            in_play.append(mob_card)
            mob_total += mob_card["power"]
            mob_ai.energy = mob_total
            if not (battle.get("fog_full", False) or battle.get("fog_partial", False)):
                battle["mob_state"]["message"] = f"Противник зачерпнул магию ({mob_card['power']})"
            if mob_total > 21:
                battle["mob_state"]["stop"] = True
                battle["mob_state"]["message"] = "‼️ Магия перехлестнула противника!"
        else:
            battle["mob_state"]["stop"] = True
    battle["deck"].update({"available": available, "in_play": in_play})

async def on_draw(callback: CallbackQuery, button, manager: DialogManager):
    context = manager.current_context()
    battle_id = context.dialog_data["battle_id"]
    battle = battles.find_one({"_id": ObjectId(battle_id)})

    if battle["player_state"]["stop"]:
        battle["player_state"]["message"] = "Ты уже остановил поглащение магии!"
        battles.update_one({"_id": battle["_id"]}, {"$set": battle})
        await manager.switch_to(Battle.battle_round)
        return

    if not battle["deck"]["available"]:
        battle["player_state"]["message"] = "Источник магии иссяк!"
        battles.update_one({"_id": battle["_id"]}, {"$set": battle})
        await manager.switch_to(Battle.battle_round)
        return

    player_card = battle["deck"]["available"].pop()
    battle["player_state"]["hand"].append(player_card)
    battle["deck"]["in_play"].append(player_card)
    player_total = sum(c["power"] for c in battle["player_state"]["hand"])

    # Increment mirror event counter if card matches player's chosen magic type
    if player_card["magic_type"] == battle["magic_type"]:
        battle["player_type_spell_count"] += 1

    if not (battle.get("fog_full", False) or battle.get("fog_partial", False)):
        battle["player_state"]["message"] = (
            f"\n<i>Ты произнёс заклинание <b>{player_card['name']}</b> ({player_card['power']})</i>"
        )

    if player_total > 21:
        battle["player_state"]["stop"] = True
        battle["player_state"]["message"] = "‼️ Магия перехлестнула тебя"
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
    battle["player_state"]["message"] = "Ты произнёс заклинание"
    auto_play_mob(battle)
    battle = evaluate_round_result(battle)
    battles.update_one({"_id": battle["_id"]}, {"$set": battle})
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
        player_id = battle["player_id"]
        inc = {"stats.battles": 1}
        if battle["battle_winner"] == "player":
            inc["stats.wins"] = 1
        elif battle["battle_winner"] == "mob":
            inc["stats.defeats"] = 1
        else:
            inc["stats.draws"] = 1
        players.update_one({"_id": player_id}, {"$inc": inc})
        battles.update_one(
            {"_id": battle["_id"]},
            {"$unset": {
                "deck": '',
                "round_result": '',
                'round_number': '',
                'event_description': '',
                'mob_state': '',
                'player_state': '',
                'mirror_event': '',
                'fog_full': '',
                'fog_partial': '',
                'player_type_spell_count': '',
                'consecutive_player_wins': '',
                'rounds': '',
            }}
        )
        update_player_after_battle(player_id, battle)
        await manager.switch_to(Battle.battle_result)
    else:
        await manager.switch_to(Battle.battle_round)

async def on_scene(callback: CallbackQuery, button, manager: DialogManager):
    context = manager.current_context()
    battle_id = context.dialog_data["battle_id"]
    battle = battles.find_one({"_id": ObjectId(battle_id)})
    scene_branch = battle['battle_winner']
    await manager.done()
    await manager.start(Scene.scene, data={"branch": scene_branch, "xp": 1000})
