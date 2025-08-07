import datetime as dt
import random

from config.mongo_config import mobs
from text_constants.outfit import OUTFIT_PARTS
from text_constants.mobs_personas import NAMES, TITLES, SUB_TITLES, PERSONAS
from utils.constants import MAGIC_TYPE


def generate_random_mob():
    # Определяем пол (позже можно сделать противоположным игроку)
    gender = 'female'
    # Выбираем персонализированные параметры
    persona = random.choice(list(PERSONAS.keys()))
    appearance = random.choice(['соблазнительная', 'загадочная', 'элегантная', 'опасная'])
    temperament = random.choice(PERSONAS[persona]['temperament'])
    magic_type = random.choice(MAGIC_TYPE)
    strategy = random.choice(['aggressive', 'careful', 'balanced'])

    # Генерируем одежду
    outfit = {
        part: random.choice(OUTFIT_PARTS[part])
        for part in OUTFIT_PARTS
    }

    mob_data = {
        'gender': gender,
        'name': random.choice(NAMES[gender]),
        'title': random.choice(TITLES[gender]),
        'sub_title': random.choice(SUB_TITLES),
        'persona': persona,
        'appearance': appearance,
        'temperament': temperament,
        'magic_type': magic_type,
        'level': 1,
        'strategy': strategy,
        'outfit': outfit,
        'max_hp': 6,
        'is_boss': False,
        'created_at': dt.datetime.now(),
    }

    mob_id = mobs.insert_one(mob_data).inserted_id
    return mob_id


def get_random_mob_for_player(player_level: int):
    mobs_list = list(mobs.find({"level": {"$lte": player_level}}))
    if not mobs_list:
        raise Exception("No available mobs")
    return random.choice(mobs_list)
