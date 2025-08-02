import random
import datetime as dt
from config.mongo_config import mobs

def generate_random_mob():
    persona = random.choice(['застенчивая', 'дерзкая', 'доминирующая'])
    name = random.choice(['Амарилла', 'Шейла', 'Лира', 'Моргана'])
    title = random.choice(['Чародейка страсти', 'Иллюзионистка желания', 'Магесса искушения'])

    deck = [
        {"name": "Тепло дыхания", "power": 4, "type": "emotion"},
        {"name": "Танец призрачной кожи", "power": 2, "type": "illusion"},
        {"name": "Импульс истомы", "power": 11, "type": "energy"},
        {"name": "Пульсация вены желания", "power": 7, "type": "body"},
        # можно добавить больше
    ]
    mob_data = {
        "name": name,
        "title": title,
        "persona": persona,
        "level": 1,
        "base_avatar_id": "test_seed",
        "outfit": {
            "underwear": "Кружевной топ",
            "clothes": "Тонкая накидка",
            "accessories": ["ожерелье"],
            "colors": {"clothes": "#ffb6c1", "hair": "#9933cc"}
        },
        "logic_profile": "balanced",
        "quotes": {
            "entry": ["Ты хочешь сыграть со мной?"],
            "hurt": ["Ай! Ты слишком силён."],
            "cast": ["Моя очередь блистать!"],
            "lose_layer": ["Ох... это было неожиданно."],
            "defeat": ["Ты победил, но я не забуду этого."]
        },
        "deck": deck,
        "max_hp": 5,
        "difficulty": 1,
        "created_at": dt.datetime.now()
    }
    mob_id = mobs.insert_one(mob_data).inserted_id
    return mob_id


def get_random_mob_for_player(player_level: int):
    mobs_list = list(mobs.find({"level": {"$lte": player_level}}))
    if not mobs_list:
        raise Exception("No available mobs")
    return random.choice(mobs_list)
