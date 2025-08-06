import random
from typing import Dict, Optional


def apply_buff(participant: str, card: Dict, battle: Dict) -> Dict:
    """Применяет случайный баф, если тип карты совпадает со специализацией участника."""
    buffs = [
        {"name": "preserve_outfit", "description": "Одежда защищена от потери в этом раунде!"},
        {"name": "extra_draw", "description": "Можно взять ещё одну карту после остановки!"},
        {"name": "discard_card", "description": "Сброшена карта с заменой на новую!"},
        {"name": "block_mob", "description": "Противник пропускает ход!"}
    ]

    magic_type = battle.get("magic_type" if participant == "player" else "mob_state.magic_type")
    if card["magic_type"] != magic_type:
        return battle

    selected_buff = random.choice(buffs)
    battle[f"{participant}_state"]["buff"] = selected_buff["name"]
    battle[f"{participant}_state"]["buff_description"] = selected_buff["description"]

    # Для discard_card выполняем замену сразу
    if selected_buff["name"] == "discard_card" and battle["deck"]["available"]:
        battle[f"{participant}_state"]["hand"] = [
            c for c in battle[f"{participant}_state"]["hand"] if c != card
        ]
        new_card = battle["deck"]["available"].pop()
        battle[f"{participant}_state"]["hand"].append(new_card)
        battle["deck"]["in_play"] = [c for c in battle["deck"]["in_play"] if c != card]
        battle["deck"]["in_play"].append(new_card)

    return battle
