import random
from typing import Dict, Optional


MIRROR_THRESHOLD = 3
FOG_FULL_THRESHOLD = 4
FOG_PARTIAL_THRESHOLD = 3

def trigger_random_event(battle: Dict) -> Dict:
    """Определяет и активирует событие для раунда."""
    # Reset flags
    battle["mirror_event"] = False
    battle["fog_full"] = False
    battle["fog_partial"] = False
    battle["event_description"] = ""

    # Check for mirror event (deterministic)
    if battle.get("player_type_spell_count", 0) >= MIRROR_THRESHOLD:
        battle["mirror_event"] = True
        battle["event_description"] = "🌀 <b>Магическое зеркало активировано: магическая сила были инвертирована!</b>"
        battle["player_type_spell_count"] = 0
        return battle

    # Check for fog events based on consecutive wins
    consecutive_wins = battle.get("consecutive_player_wins", 0)
    if consecutive_wins == FOG_FULL_THRESHOLD:
        battle["fog_full"] = True
        battle["event_description"] = "<b>Твоё возбуждение достигло предела! Магический поток начинает иссякать и ты беспорядочно начинаешь хватать энергию.</b>"
    elif consecutive_wins == FOG_PARTIAL_THRESHOLD:
        battle["fog_partial"] = True
        battle["event_description"] = "<b>Твой разум затуманен возбуждением от вида полуобнаженного тела чародейки. Ты не можешь сконцентрироваться и читать магический поток.</b>"

    return battle
