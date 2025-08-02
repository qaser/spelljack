import pymongo

# Create the client
client = pymongo.MongoClient('localhost', 27017)
db = client['spelljack_db']

buffer = db['buffer']
admins = db['admins']

players = db['players']
mobs = db['mobs']
battles = db['battles']

'''
players = {
    "_id": ObjectId,
    "user_id": int,
    "username": str | None,
    "first_name": str | None,
    "state": str,  # "menu", "battle", "defeated", etc.
    "level": int,  # уровень игрока (влияет на доступных мобов)
    "current_battle_id": ObjectId | None,
    "created_at": datetime,
    "updated_at": datetime
}

mobs = {
    "_id": ObjectId,
    "name": str,
    "title": str,
    "persona": str,
    "level": int,   # сложность моба, доступен при >= игрока
    "base_avatar_id": str,
    "outfit": {
        "underwear": str,
        "clothes": str,
        "accessories": [str],
        "colors": {
            "clothes": str,
            "hair": str
        }
    },
    "logic_profile": str,  # "cautious", "aggressive", etc.
    "quotes": {
        "entry": [str],
        "hurt": [str],
        "cast": [str],
        "lose_layer": [str],
        "defeat": [str]
    },
    "deck": [
        {"name": str, "power": int, "type": str}
    ],
    "max_hp": int,
    "difficulty": int,
    "created_at": datetime
}

battles = {
    "_id": ObjectId,
    "player_id": int,
    "mob_id": ObjectId,
    "player_state": {
        "hp": int,
        "hand": [dict],
        "deck": [dict],
        "casted": bool,
        "is_turn": bool
    },
    "mob_state": {
        "hp": int,
        "hand": [dict],
        "deck": [dict],
        "casted": bool
    },
    "turn_number": int,
    "history": [
        {
            "actor": "player" | "npc",
            "action": "draw" | "cast" | "effect",
            "card": dict | None,
            "result": str | None,
            "timestamp": datetime
        }
    ],
    "status": "active" | "finished" | "interrupted",
    "winner": "player" | "mob" | None,
    "created_at": datetime,
    "updated_at": datetime
}
'''
