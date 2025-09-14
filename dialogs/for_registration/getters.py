import datetime as dt
from typing import Dict, Any
from bson import ObjectId
from aiogram_dialog import DialogManager
import random


PLAYERS_NAMES = ['Люциан', 'Винсент', 'Лоренцо', 'Рафаэль', 'Феликс', 'Орион', 'Осирис']


async def get_names(dialog_manager: DialogManager, **kwargs) -> Dict[str, list]:
    return {"names": PLAYERS_NAMES}
