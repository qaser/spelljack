from .constants import BATTLE_ENDING
import random


DIALOGS = {
    "player": {
        "start": {
            "text": random.choice(BATTLE_ENDING),
            "options": [
                {"id": "tease", "label": "Погладить её волосы", "xp_req": 0, "next": "tease_scene"},
                {"id": "mock", "label": "Издеваться", "xp_req": 5, "next": "mock_scene"},
                {"id": "dominate", "label": "Заставить поклониться", "xp_req": 10, "next": "dominate_scene"},
            ]
        },
        "tease_scene": {
            "text": "Ты проводишь пальцами по её щеке...",
            "options": [{"id": "continue", "label": "Далее", "xp_req": 0, "next": "end"}]
        },
        "mock_scene": {
            "text": "Ты смеёшься и глядишь на неё сверху вниз...",
            "options": [{"id": "continue", "label": "Далее", "xp_req": 0, "next": "end"}]
        },
        "dominate_scene": {
            "text": "Ты берёшь её за затылок и наклоняешь...",
            "options": [{"id": "continue", "label": "Далее", "xp_req": 0, "next": "end"}]
        },
        "end": {"text": "Сцена завершена.", "options": []}
    },

    "mob": {
        "start": {
            "text": "Она схватила тебя за подбородок и заставила смотреть в глаза...",
            "options": [
                {"id": "auto", "label": None, "xp_req": 0, "next": ["mock_scene", "dominate_scene"], "random": True}
            ]
        },
        "mock_scene": {
            "text": "Она насмешливо хмыкает и отстраняется...",
            "options": [{"id": "continue", "label": "Далее", "xp_req": 0, "next": "end"}]
        },
        "dominate_scene": {
            "text": "Она прижимает тебя к земле и шепчет...",
            "options": [{"id": "continue", "label": "Далее", "xp_req": 0, "next": "end"}]
        },
        "end": {"text": "Сцена завершена.", "options": []}
    }
}
