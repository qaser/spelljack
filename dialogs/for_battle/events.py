import random
from typing import Dict, Optional


def trigger_random_event(battle: Dict) -> Dict:
    """Определяет и активирует случайное событие для раунда."""
    events = [
        {"name": "mirror", "chance": 0.1, "description": "Зеркало активировано: очки были перевернуты!"},
        {"name": "fog_full", "chance": 0.05, "description": "Полный туман обмана: очки и прогресс скрыты!"},
        {"name": "fog_partial", "chance": 0.05, "description": "Туман обмана: очки скрыты, прогресс виден!"},
        {"name": None, "chance": 0.8, "description": ""}  # Без события
    ]

    # Выбор события на основе вероятностей
    total_chance = sum(event["chance"] for event in events)
    rand = random.random() * total_chance
    cumulative = 0
    selected_event = None

    for event in events:
        cumulative += event["chance"]
        if rand <= cumulative:
            selected_event = event
            break

    # Установка флагов событий
    battle["mirror_event"] = selected_event["name"] == "mirror"
    battle["fog_full"] = selected_event["name"] == "fog_full"
    battle["fog_partial"] = selected_event["name"] == "fog_partial"
    battle["event_description"] = selected_event["description"]

    return battle
