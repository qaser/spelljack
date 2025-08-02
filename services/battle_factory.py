import datetime as dt
import random
from bson import ObjectId
from config.mongo_config import mobs, battles, players
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
