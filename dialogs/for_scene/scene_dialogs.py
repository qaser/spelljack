from . import constants as const
import random


# заметки для победы моба:
# Face sitting,
# amazons pose,
# pyssy licking doggy,
# pyssy licking missionary
# pyssy licking standing
# on chair

DIALOGS = {
    "player": {
        "start": {
            "text": lambda: random.choice(const.MOB_ON_KNEES)
            + '\n\n<blockquote>'
            + random.choice(const.PLAYER_WISH)
            + '</blockquote>',
            "options": [
                {"id": "service", "label": "...услугу", "xp_req": 0, "next": "service"},
                {"id": "sex", "label": "...твоё тело", "xp_req": 5, "next": "sex"},
                {"id": "twins", "label": "...большего", "xp_req": 10, "next": "twins"},
            ],
        },
        "twins": {
            "text": lambda: random.choice(const.TWINS_SUMMONING),
            "options": [
                {
                    "id": "twins_handjob",
                    "label": "Поработайте ручками...",
                    "xp_req": 0,
                    "next": "twins_handjob_scene",
                },
            ],
        },
        "twins_handjob_scene": {
            "text": lambda: random.choice(const.TWINS_HANDJOB),
            "options": [
                {
                    "id": "twins_blowjob",
                    "label": "Пососите...",
                    "xp_req": 0,
                    "next": "twins_blowjob_scene",
                },
            ],
        },
        "twins_blowjob_scene": {
            "text": lambda: random.choice(const.TWINS_BLOWJOB),
            "options": [
                {
                    "id": "twins_blowjob_pre_climax",
                    "label": "Продолжайте...",
                    "xp_req": 0,
                    "next": "twins_blowjob_pre_climax",
                },
            ],
        },
        "twins_blowjob_pre_climax": {
            "text": lambda: random.choice(const.TWINS_BLOWJOB_PRE_CLIMAX)
            + '\n\n<blockquote>'
            + random.choice(const.PLAYER_TWINS_PRE_CLIMAX_REACTION)
            + '</blockquote>',
            "options": [
                {
                    "id": "twins_blowjob_cum_on_tits",
                    "label": "Кончить им на сиськи...",
                    "xp_req": 0,
                    "next": "twins_blowjob_cum_on_tits",
                },
                {
                    "id": "twins_blowjob_cum_on_faces",
                    "label": "Кончить им на лица...",
                    "xp_req": 0,
                    "next": "twins_blowjob_cum_on_faces",
                },
                {
                    "id": "twins_blowjob_cum_in_mounths",
                    "label": "Кончить им в ротики...",
                    "xp_req": 0,
                    "next": "twins_blowjob_cum_in_mouths",
                },
            ],
        },
        "twins_blowjob_cum_on_tits": {
            "text": lambda: random.choice(const.TWINS_BLOWJOB_CLIMAX_TITS)
            + '\n\n<blockquote>'
            + random.choice(const.PLAYER_CLIMAX_REACTION)
            + '</blockquote>',
            "options": [
                {
                    "id": "twins_end",
                    "label": "Завершить ритуал...",
                    "xp_req": 0,
                    "next": "twins_end",
                },
            ],
        },
        "twins_blowjob_cum_on_faces": {
            "text": lambda: random.choice(const.TWINS_BLOWJOB_CLIMAX_FACIAL)
            + '\n\n<blockquote>'
            + random.choice(const.PLAYER_CLIMAX_REACTION)
            + '</blockquote>',
            "options": [
                {
                    "id": "twins_end",
                    "label": "Завершить ритуал...",
                    "xp_req": 0,
                    "next": "twins_end",
                },
            ],
        },
        "twins_blowjob_cum_in_mouths": {
            "text": lambda: random.choice(const.TWINS_BLOWJOB_CLIMAX_ORAL)
            + '\n\n<blockquote>'
            + random.choice(const.PLAYER_CLIMAX_REACTION)
            + '</blockquote>',
            "options": [
                {
                    "id": "twins_cum_play",
                    "label": "Посмотреть на них...",
                    "xp_req": 0,
                    "next": "twins_blowjob_cum_play",
                },
                {
                    "id": "twins_end",
                    "label": "Завершить ритуал...",
                    "xp_req": 0,
                    "next": "twins_end",
                },
            ],
        },
        "twins_blowjob_cum_play": {
            "text": lambda: random.choice(const.TWINS_BLOWJOB_CUM_PLAY),
            "options": [
                {
                    "id": "twins_end",
                    "label": "Завершить ритуал...",
                    "xp_req": 0,
                    "next": "twins_end",
                },
            ],
        },
        "twins_end": {
            "text": lambda: random.choice(const.TWINS_RITUAL_ENDINGS)
            + '\n\n<blockquote>'
            + 'До скорой встречи...'
            + '</blockquote>',
        },
        "service": {
            "text": lambda: random.choice(const.MOB_SERVICE),
            "options": [
                {
                    "id": "handjob",
                    "label": "Поработай руками",
                    "xp_req": 0,
                    "next": "handjob_scene",
                },
                {
                    "id": "titsjob",
                    "label": "Поработай сиськами",
                    "xp_req": 5,
                    "next": "titsjob_scene",
                },
                {
                    "id": "blowjob",
                    "label": "Поработай ртом",
                    "xp_req": 10,
                    "next": "blowjob_scene",
                },
            ],
        },
        "handjob_scene": {
            "text": lambda: random.choice(const.HANDJOB_FIRST_CONTACT)
            + '\n\n<blockquote>'
            + random.choice(const.PLAYER_HANDJOB_REACTION)
            + '</blockquote>',
            "options": [
                {
                    "id": "testicles_play",
                    "label": "Поиграй с яичками...",
                    "xp_req": 0,
                    "next": "handjob_testicles_play",
                },
                {
                    "id": "slow",
                    "label": "Медленнее...",
                    "xp_req": 0,
                    "next": "handjob_slow",
                },
                {
                    "id": "fast",
                    "label": "Быстрее...",
                    "xp_req": 0,
                    "next": "handjob_fast",
                },
                {
                    "id": "continue",
                    "label": "Ещё...",
                    "xp_req": 0,
                    "next": "handjob_mid_stage",
                },
            ],
        },
        "handjob_testicles_play": {
            "text": lambda: random.choice(const.HANDJOB_TESTICLES_PLAY)
            + '\n\n<blockquote>'
            + random.choice(const.PLAYER_HANDJOB_REACTION)
            + '</blockquote>',
            "options": [
                {
                    "id": "handjob_mid",
                    "label": "Поработай рукой",
                    "xp_req": 0,
                    "next": "handjob_mid_stage",
                },
            ],
        },
        "handjob_mid_stage": {
            "text": lambda: random.choice(const.HANDJOB_MID_STAGE)
            + '\n\n<blockquote>'
            + random.choice(const.PLAYER_HANDJOB_REACTION)
            + '</blockquote>',
            "options": [
                {
                    "id": "testicles_play",
                    "label": "Поиграй с яичками...",
                    "xp_req": 0,
                    "next": "handjob_testicles_play",
                },
                {
                    "id": "slow",
                    "label": "Медленнее...",
                    "xp_req": 0,
                    "next": "handjob_slow",
                },
                {
                    "id": "fast",
                    "label": "Быстрее...",
                    "xp_req": 0,
                    "next": "handjob_fast",
                },
                {
                    "id": "continue",
                    "label": "Продолжай...",
                    "xp_req": 0,
                    "next": "handjob_pre_climax",
                },
            ],
        },
        "handjob_slow": {
            "text": lambda: random.choice(const.HANDJOB_SLOWDOWN)
            + '\n\n<blockquote>'
            + '</blockquote>',
            "options": [
                {
                    "id": "testicles_play",
                    "label": "Поиграй с яичками...",
                    "xp_req": 0,
                    "next": "handjob_testicles_play",
                },
                {
                    "id": "fast",
                    "label": "Быстрее...",
                    "xp_req": 0,
                    "next": "handjob_fast",
                },
                {
                    "id": "continue",
                    "label": "Продолжай...",
                    "xp_req": 0,
                    "next": "handjob_mid_stage",
                },
            ],
        },
        "handjob_fast": {
            "text": lambda: random.choice(const.HANDJOB_ACCELERATION)
            + '\n\n<blockquote>'
            + '</blockquote>',
            "options": [
                {
                    "id": "testicles_play",
                    "label": "Поиграй с яичками...",
                    "xp_req": 0,
                    "next": "handjob_testicles_play",
                },
                {
                    "id": "slow",
                    "label": "Медленнее...",
                    "xp_req": 0,
                    "next": "handjob_slow",
                },
                {
                    "id": "continue",
                    "label": "Продолжай...",
                    "xp_req": 0,
                    "next": "handjob_mid_stage",
                },
            ],
        },
        "handjob_pre_climax": {
            "text": lambda: random.choice(const.HANDJOB_PRE_CLIMAX)
            + '\n\n<blockquote>'
            + random.choice(const.PLAYER_SERVICE_PRE_CLIMAX_REACTION)
            + '</blockquote>',
            "options": [
                {
                    "id": "cum_on_tits",
                    "label": "Кончить на грудь...",
                    "xp_req": 0,
                    "next": "handjob_cum_on_tits",
                },
                {
                    "id": "cum_on_face",
                    "label": "Кончить на лицо...",
                    "xp_req": 0,
                    "next": "handjob_cum_on_face",
                },
                {
                    "id": "cum_in_mounth",
                    "label": "Кончить в ротик...",
                    "xp_req": 0,
                    "next": "handjob_cum_in_mouth",
                },
            ],
        },
        "handjob_cum_on_tits": {
            "text": lambda: random.choice(const.HANDJOB_CLIMAX_CHEST)
            + '\n\n<blockquote>'
            + random.choice(const.PLAYER_CLIMAX_REACTION)
            + '</blockquote>',
            "options": [
                {
                    "id": "end",
                    "label": "Завершить ритуал...",
                    "xp_req": 0,
                    "next": "end",
                },
            ],
        },
        "handjob_cum_on_face": {
            "text": lambda: random.choice(const.HANDJOB_CLIMAX_FACIAL)
            + '\n\n<blockquote>'
            + random.choice(const.PLAYER_CLIMAX_REACTION)
            + '</blockquote>',
            "options": [
                {
                    "id": "end",
                    "label": "Завершить ритуал...",
                    "xp_req": 0,
                    "next": "end",
                },
            ],
        },
        "handjob_cum_in_mouth": {
            "text": lambda: random.choice(const.HANDJOB_CLIMAX_ORAL)
            + '\n\n<blockquote>'
            + random.choice(const.PLAYER_CLIMAX_REACTION)
            + '</blockquote>',
            "options": [
                {
                    "id": "end",
                    "label": "Завершить ритуал...",
                    "xp_req": 0,
                    "next": "end",
                },
            ],
        },
        "titsjob_scene": {
            "text": lambda: random.choice(const.TITJOB_FIRST_CONTACT)
            + '\n\n<blockquote>'
            + random.choice(const.PLAYER_TITSJOB_REACTION)
            + '</blockquote>',
            "options": [
                {
                    "id": "slow",
                    "label": "Медленнее...",
                    "xp_req": 0,
                    "next": "titsjob_slow",
                },
                {
                    "id": "fast",
                    "label": "Быстрее...",
                    "xp_req": 0,
                    "next": "titsjob_fast",
                },
                {
                    "id": "continue",
                    "label": "Ещё...",
                    "xp_req": 0,
                    "next": "titsjob_mid_stage",
                },
            ],
        },
        "titsjob_mid_stage": {
            "text": lambda: random.choice(const.TITJOB_MID_STAGE)
            + '\n\n<blockquote>'
            + random.choice(const.PLAYER_TITSJOB_REACTION)
            + '</blockquote>',
            "options": [
                {
                    "id": "slow",
                    "label": "Медленнее...",
                    "xp_req": 0,
                    "next": "titsjob_slow",
                },
                {
                    "id": "fast",
                    "label": "Быстрее...",
                    "xp_req": 0,
                    "next": "titsjob_fast",
                },
                {
                    "id": "continue",
                    "label": "Продолжай...",
                    "xp_req": 0,
                    "next": "titsjob_pre_climax",
                },
            ],
        },
        "titsjob_slow": {
            "text": lambda: random.choice(const.TITJOB_SLOWDOWN)
            + '\n\n<blockquote>'
            + '</blockquote>',
            "options": [
                {
                    "id": "fast",
                    "label": "Быстрее...",
                    "xp_req": 0,
                    "next": "titsjob_fast",
                },
                {
                    "id": "continue",
                    "label": "Продолжай...",
                    "xp_req": 0,
                    "next": "titsjob_mid_stage",
                },
            ],
        },
        "titsjob_fast": {
            "text": lambda: random.choice(const.TITJOB_ACCELERATION)
            + '\n\n<blockquote>'
            + '</blockquote>',
            "options": [
                {
                    "id": "slow",
                    "label": "Медленнее...",
                    "xp_req": 0,
                    "next": "titsjob_slow",
                },
                {
                    "id": "continue",
                    "label": "Продолжай...",
                    "xp_req": 0,
                    "next": "titsjob_mid_stage",
                },
            ],
        },
        "titsjob_pre_climax": {
            "text": lambda: random.choice(const.TITJOB_PRE_CLIMAX)
            + '\n\n<blockquote>'
            + random.choice(const.PLAYER_SERVICE_PRE_CLIMAX_REACTION)
            + '</blockquote>',
            "options": [
                {
                    "id": "cum_on_tits",
                    "label": "Кончить на грудь...",
                    "xp_req": 0,
                    "next": "titsjob_cum_on_tits",
                },
                {
                    "id": "cum_on_face",
                    "label": "Кончить на лицо...",
                    "xp_req": 0,
                    "next": "titsjob_cum_on_face",
                },
                {
                    "id": "cum_in_mounth",
                    "label": "Кончить в ротик...",
                    "xp_req": 0,
                    "next": "titsjob_cum_in_mouth",
                },
            ],
        },
        "titsjob_cum_on_tits": {
            "text": lambda: random.choice(const.TITJOB_CLIMAX_TITS)
            + '\n\n<blockquote>'
            + random.choice(const.PLAYER_CLIMAX_REACTION)
            + '</blockquote>',
            "options": [
                {
                    "id": "end",
                    "label": "Завершить ритуал...",
                    "xp_req": 0,
                    "next": "end",
                },
            ],
        },
        "titsjob_cum_on_face": {
            "text": lambda: random.choice(const.TITJOB_CLIMAX_FACIAL)
            + '\n\n<blockquote>'
            + random.choice(const.PLAYER_CLIMAX_REACTION)
            + '</blockquote>',
            "options": [
                {
                    "id": "end",
                    "label": "Завершить ритуал...",
                    "xp_req": 0,
                    "next": "end",
                },
            ],
        },
        "titsjob_cum_in_mouth": {
            "text": lambda: random.choice(const.TITJOB_CLIMAX_ORAL)
            + '\n\n<blockquote>'
            + random.choice(const.PLAYER_CLIMAX_REACTION)
            + '</blockquote>',
            "options": [
                {
                    "id": "end",
                    "label": "Завершить ритуал...",
                    "xp_req": 0,
                    "next": "end",
                },
            ],
        },
        "blowjob_scene": {
            "text": lambda: random.choice(const.BLOWJOB_FIRST_CONTACT)
            + '\n\n<blockquote>'
            + random.choice(const.PLAYER_BLOWJOB_REACTION)
            + '</blockquote>',
            "options": [
                {
                    "id": "testicles_play",
                    "label": "Поиграй с яичками...",
                    "xp_req": 0,
                    "next": "blowjob_testicles_play",
                },
                {
                    "id": "testicles_oral_play",
                    "label": "Пососи яички...",
                    "xp_req": 0,
                    "next": "blowjob_testicles_oral",
                },
                {
                    "id": "slow",
                    "label": "Медленнее...",
                    "xp_req": 0,
                    "next": "blowjob_slow",
                },
                {
                    "id": "fast",
                    "label": "Быстрее...",
                    "xp_req": 0,
                    "next": "blowjob_fast",
                },
                {
                    "id": "continue",
                    "label": "Ещё...",
                    "xp_req": 0,
                    "next": "blowjob_mid_stage",
                },
            ],
        },
        "blowjob_testicles_play": {
            "text": lambda: random.choice(const.BLOWJOB_TESTICLES_HAND_PLAY)
            + '\n\n<blockquote>'
            + random.choice(const.PLAYER_HANDJOB_REACTION)
            + '</blockquote>',
            "options": [
                {
                    "id": "blowjob_mid",
                    "label": "Поработай рукой",
                    "xp_req": 0,
                    "next": "blowjob_mid_stage",
                },
            ],
        },
        "blowjob_testicles_oral": {
            "text": lambda: random.choice(const.BLOWJOB_TESTICLES_ORAL_PLAY)
            + '\n\n<blockquote>'
            + random.choice(const.PLAYER_HANDJOB_REACTION)
            + '</blockquote>',
            "options": [
                {
                    "id": "blowjob_mid",
                    "label": "Поработай рукой",
                    "xp_req": 0,
                    "next": "blowjob_mid_stage",
                },
            ],
        },
        "blowjob_mid_stage": {
            "text": lambda: random.choice(const.BLOWJOB_MID_STAGE)
            + '\n\n<blockquote>'
            + random.choice(const.PLAYER_HANDJOB_REACTION)
            + '</blockquote>',
            "options": [
                {
                    "id": "testicles_play",
                    "label": "Поиграй с яичками...",
                    "xp_req": 0,
                    "next": "blowjob_testicles_play",
                },
                {
                    "id": "testicles_oral_play",
                    "label": "Пососи яички...",
                    "xp_req": 0,
                    "next": "blowjob_testicles_oral",
                },
                {
                    "id": "slow",
                    "label": "Медленнее...",
                    "xp_req": 0,
                    "next": "blowjob_slow",
                },
                {
                    "id": "fast",
                    "label": "Быстрее...",
                    "xp_req": 0,
                    "next": "blowjob_fast",
                },
                {
                    "id": "continue",
                    "label": "Продолжай...",
                    "xp_req": 0,
                    "next": "blowjob_pre_climax",
                },
            ],
        },
        "blowjob_slow": {
            "text": lambda: random.choice(const.BLOWJOB_SLOWDOWN)
            + '\n\n<blockquote>'
            + '</blockquote>',
            "options": [
                {
                    "id": "testicles_play",
                    "label": "Поиграй с яичками...",
                    "xp_req": 0,
                    "next": "blowjob_testicles_play",
                },
                {
                    "id": "testicles_oral_play",
                    "label": "Пососи яички...",
                    "xp_req": 0,
                    "next": "blowjob_testicles_oral",
                },
                {
                    "id": "fast",
                    "label": "Быстрее...",
                    "xp_req": 0,
                    "next": "blowjob_fast",
                },
                {
                    "id": "continue",
                    "label": "Продолжай...",
                    "xp_req": 0,
                    "next": "blowjob_mid_stage",
                },
            ],
        },
        "blowjob_fast": {
            "text": lambda: random.choice(const.BLOWJOB_ACCELERATION)
            + '\n\n<blockquote>'
            + '</blockquote>',
            "options": [
                {
                    "id": "testicles_play",
                    "label": "Поиграй с яичками...",
                    "xp_req": 0,
                    "next": "blowjob_testicles_play",
                },
                {
                    "id": "testicles_oral_play",
                    "label": "Пососи яички...",
                    "xp_req": 0,
                    "next": "blowjob_testicles_oral",
                },
                {
                    "id": "slow",
                    "label": "Медленнее...",
                    "xp_req": 0,
                    "next": "blowjob_slow",
                },
                {
                    "id": "continue",
                    "label": "Продолжай...",
                    "xp_req": 0,
                    "next": "blowjob_mid_stage",
                },
            ],
        },
        "blowjob_pre_climax": {
            "text": lambda: random.choice(const.BLOWJOB_PRE_CLIMAX)
            + '\n\n<blockquote>'
            + random.choice(const.PLAYER_SERVICE_PRE_CLIMAX_REACTION)
            + '</blockquote>',
            "options": [
                {
                    "id": "cum_on_tits",
                    "label": "Кончить на грудь...",
                    "xp_req": 0,
                    "next": "blowjob_cum_on_tits",
                },
                {
                    "id": "cum_on_face",
                    "label": "Кончить на лицо...",
                    "xp_req": 0,
                    "next": "blowjob_cum_on_face",
                },
                {
                    "id": "cum_in_mounth",
                    "label": "Кончить в ротик...",
                    "xp_req": 0,
                    "next": "blowjob_cum_in_mouth",
                },
            ],
        },
        "blowjob_cum_on_tits": {
            "text": lambda: random.choice(const.BLOWJOB_CLIMAX_TITS)
            + '\n\n<blockquote>'
            + random.choice(const.PLAYER_CLIMAX_REACTION)
            + '</blockquote>',
            "options": [
                {
                    "id": "end",
                    "label": "Завершить ритуал...",
                    "xp_req": 0,
                    "next": "end",
                },
            ],
        },
        "blowjob_cum_on_face": {
            "text": lambda: random.choice(const.BLOWJOB_CLIMAX_FACIAL)
            + '\n\n<blockquote>'
            + random.choice(const.PLAYER_CLIMAX_REACTION)
            + '</blockquote>',
            "options": [
                {
                    "id": "end",
                    "label": "Завершить ритуал...",
                    "xp_req": 0,
                    "next": "end",
                },
            ],
        },
        "blowjob_cum_in_mouth": {
            "text": lambda: random.choice(const.BLOWJOB_CLIMAX_ORAL)
            + '\n\n<blockquote>'
            + random.choice(const.PLAYER_CLIMAX_REACTION)
            + '</blockquote>',
            "options": [
                {
                    "id": "end",
                    "label": "Завершить ритуал...",
                    "xp_req": 0,
                    "next": "end",
                },
            ],
        },
        "sex": {
            "text": lambda: random.choice(const.BED_SUMMONING),
            "options": [
                {
                    "id": "missionary",
                    "label": "Ложись на спину",
                    "xp_req": 0,
                    "next": "missionary"
                },
                {
                    "id": "lying",
                    "label": "Ложись на живот",
                    "xp_req": 0,
                    "next": "lying"
                },
                {
                    "id": "doggy",
                    "label": "Вставай на четвереньки",
                    "xp_req": 0,
                    "next": "doggy"
                },
            ],
        },
        "missionary": {
            "text": lambda: random.choice(const.MISSIONARY_PREPARE),
            "options": [
                {
                    "id": "missionary_vaginal",
                    "label": "Использовать её киску",
                    "xp_req": 0,
                    "next": "missionary_vaginal"
                },
                {
                    "id": "missionary_anal",
                    "label": "Использовать её попку",
                    "xp_req": 0,
                    "next": "missionary_anal"
                },
            ],
        },
        "missionary_vaginal": {
            "text": lambda: random.choice(const.MISSIONARY_VAGINAL_FIRST_CONTACT),
            "options": [
                {
                    "id": "missionary_vaginal_slowdown",
                    "label": "Снизить темп",
                    "xp_req": 0,
                    "next": "missionary_vaginal_slowdown"
                },
                {
                    "id": "missionary_vaginal_acceleration",
                    "label": "Увеличить темп",
                    "xp_req": 0,
                    "next": "missionary_vaginal_acceleration"
                },
                {
                    "id": "missionary_vaginal_continue",
                    "label": "Далее...",
                    "xp_req": 0,
                    "next": "missionary_vaginal_continue"
                },
            ],
        },
        "missionary_vaginal_slowdown": {
            "text": lambda: random.choice(const.MISSIONARY_VAGINAL_SLOWDOWN),
            "options": [
                {
                    "id": "missionary_vaginal_acceleration",
                    "label": "Увеличить темп",
                    "xp_req": 0,
                    "next": "missionary_vaginal_acceleration"
                },
                {
                    "id": "missionary_vaginal_continue",
                    "label": "Далее...",
                    "xp_req": 0,
                    "next": "missionary_vaginal_continue"
                },
            ],
        },
        "missionary_vaginal_acceleration": {
            "text": lambda: random.choice(const.MISSIONARY_VAGINAL_ACCELERATION),
            "options": [
                {
                    "id": "missionary_vaginal_slowdown",
                    "label": "Снизить темп",
                    "xp_req": 0,
                    "next": "missionary_vaginal_slowdown"
                },
                {
                    "id": "missionary_vaginal_continue",
                    "label": "Далее...",
                    "xp_req": 0,
                    "next": "missionary_vaginal_continue"
                },
            ],
        },
        "missionary_vaginal_continue": {
            "text": lambda: random.choice(const.MISSIONARY_VAGINAL_MID_STAGE),
            "options": [
                # {
                #     "id": "missionary_vaginal_slowdown",
                #     "label": "Снизить темп",
                #     "xp_req": 0,
                #     "next": "missionary_vaginal_slowdown"
                # },
                # {
                #     "id": "missionary_vaginal_acceleration",
                #     "label": "Увеличить темп",
                #     "xp_req": 0,
                #     "next": "missionary_vaginal_acceleration"
                # },
                {
                    "id": "missionary_vaginal_pre_climax",
                    "label": "Далее...",
                    "xp_req": 0,
                    "next": "missionary_vaginal_pre_climax"
                },
            ],
        },
        "missionary_vaginal_continue": {
            "text": lambda: random.choice(const.MISSIONARY_VAGINAL_MID_STAGE),
            "options": [
                # {
                #     "id": "missionary_vaginal_slowdown",
                #     "label": "Снизить темп",
                #     "xp_req": 0,
                #     "next": "missionary_vaginal_slowdown"
                # },
                # {
                #     "id": "missionary_vaginal_acceleration",
                #     "label": "Увеличить темп",
                #     "xp_req": 0,
                #     "next": "missionary_vaginal_acceleration"
                # },
                {
                    "id": "missionary_vaginal_pre_climax",
                    "label": "Далее...",
                    "xp_req": 0,
                    "next": "missionary_vaginal_pre_climax"
                },
            ],
        },

        "end": {
            "text": lambda: random.choice(const.RITUAL_ENDINGS)
            + '\n\n<blockquote>'
            + 'До скорой встречи...'
            + '</blockquote>',
        },
    },
    "mob": {
        "start": {
            "text": "Она схватила тебя за подбородок и заставила смотреть в глаза...",
            "options": [
                {
                    "id": "auto",
                    "label": None,
                    "xp_req": 0,
                    "next": ["mock_scene", "dominate_scene"],
                    "random": True,
                }
            ],
        },
        "mock_scene": {
            "text": "Она насмешливо хмыкает и отстраняется...",
            "options": [
                {"id": "continue", "label": "Далее", "xp_req": 0, "next": "end"}
            ],
        },
        "dominate_scene": {
            "text": "Она прижимает тебя к земле и шепчет...",
            "options": [
                {"id": "continue", "label": "Далее", "xp_req": 0, "next": "end"}
            ],
        },
        "end": {
            "text": lambda: random.choice(const.RITUAL_ENDINGS)
            + '\n\n<blockquote>'
            + 'До скорой встречи...'
            + '</blockquote>',
        },
    },
}
