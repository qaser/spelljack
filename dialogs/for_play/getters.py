import datetime as dt
from typing import Dict, Any
from bson import ObjectId
from aiogram_dialog import DialogManager
import random

from config.mongo_config import players


async def get_player_info(dialog_manager: DialogManager, **kwargs) -> Dict[str, list]:
    player_id = dialog_manager.event.from_user.id
    player_data = players.find_one({'_id': player_id})
    if player_data:
        return {
        'name': player_data['name'],
        'title': player_data['title'],
        'exp': player_data['exp'],
        'dream_level': player_data['dream_level'],
        'battles': player_data['stats']['battles'],
        'wins': player_data['stats']['wins'],
        'defeats': player_data['stats']['defeats'],
        'draws': player_data['stats']['draws'],
        'magic_balance': player_data['magic_balance'],
    }
