import datetime as dt
import random

from config.mongo_config import mobs
from utils.constants import (NAMES, OUTFIT_PARTS, PERSONAS, QUOTES, SUB_TITLES,
                             TITLES)


def generate_random_mob():
    # Определяем пол (позже можно сделать противоположным игроку)
    gender = 'female'
    # Выбираем персонализированные параметры
    persona = random.choice(list(PERSONAS.keys()))
    persona_desc = random.choice(PERSONAS[persona]['descriptors'])
    magic_type = random.choice(['Флирт', 'Соблазн', 'Вожделение', 'Искушение'])
    ai_style = random.choice(['aggressive', 'careful', 'balanced'])

    # Генерируем одежду
    outfit = {
        part: random.choice(OUTFIT_PARTS[part])
        for part in OUTFIT_PARTS
    }

    # Генерируем цитаты в соответствии с персонажем
    quotes = {
        quote_type: random.choice(QUOTES[quote_type][persona])
        for quote_type in QUOTES
    }

    mob_data = {
        'gender': gender,
        'name': random.choice(NAMES[gender]),
        'title': random.choice(TITLES[gender]),
        'sub_title': random.choice(SUB_TITLES),
        'persona': persona,
        'magic_type': magic_type,
        'level': 1,
        'ai_style': ai_style,
        'outfit': outfit,
        'quotes': quotes,
        'max_hp': 6,
        'difficulty': 1,
        'created_at': dt.datetime.now(),
        'descriptors': {
            'appearance': f"{random.choice(['соблазнительная', 'загадочная', 'элегантная', 'опасная'])} {random.choice(['улыбка', 'походка', 'аура', 'манера держаться'])}"
        }
    }

    mob_id = mobs.insert_one(mob_data).inserted_id
    return mob_id


def get_random_mob_for_player(player_level: int):
    mobs_list = list(mobs.find({"level": {"$lte": player_level}}))
    if not mobs_list:
        raise Exception("No available mobs")
    return random.choice(mobs_list)
