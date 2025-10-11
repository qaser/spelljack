import datetime as dt
from typing import Dict, Any
from bson import ObjectId
from aiogram_dialog import DialogManager
import random

from config.mongo_config import battles, mobs, mob_meta
from services.mob_factory import generate_random_mob
from .utils import generate_mob_intro, QUOTES
from .constants import MAGIC_TYPE, DECK, DRAW_TEXTS, WIN_TEXTS, LOSE_TEXTS, DRAW_EFFECTS
from text_constants.battle_stories import SPELL_CAST_TEXT
from aiogram_dialog.api.entities import MediaAttachment, MediaId
from aiogram.enums import ContentType

WIN_TEXT = random.choice(WIN_TEXTS)
LOSE_TEXT = random.choice(LOSE_TEXTS)
DRAW_TEXT = random.choice(DRAW_TEXTS)

def cast_spell(spell_name: str, caster: str, is_mob: bool, is_player: bool) -> str:
    """Генератор описаний заклинаний"""
    if is_player:
        templates = [
            f"Ты произнёс заклинание <b>«{spell_name}»</b> — и оно",
            f"Словно в танце, ты вызвал заклинание <b>«{spell_name}»</b>. Оно",
            f"Взмах твоей руки — и ты соткал заклинание <b>«{spell_name}»</b>. Оно",
            f"Заклинание <b>«{spell_name}»</b> ожило в твоих устах, и оно",
            f"Ты сконцентрировал волю на заклинании <b>«{spell_name}»</b> — это",
            f"Слова силы сорвались с твоих губ: <b>«{spell_name}»</b>! Оно",
            f"Ты направил магию в заклинании <b>«{spell_name}»</b>, и оно",
            f"С жестом могущества ты призвал заклинание <b>«{spell_name}»</b> — оно"
        ]
    else:
        templates = [
            f"<b>{caster}</b> произнесла заклинание <b>«{spell_name}»</b> — и",
            f"Словно в танце, <b>{caster}</b> вызвала заклинание <b>«{spell_name}»</b> и",
            f"Взмах руки — и <b>{caster}</b> соткала заклинание <b>«{spell_name}»</b>. В тот миг",
            f"<b>{caster}</b> сконцентрировала волю на заклинании <b>«{spell_name}»</b> —",
            f"<b>{caster}</b> направила магию в заклинании <b>«{spell_name}»</b>, и",
            f"С жестом могущества <b>{caster}</b> призвала заклинание <b>«{spell_name}»</b> —"
        ]
    base_sentence = random.choice(templates)
    if is_player and not is_mob:
        base_sentence += " помогло тебе выиграть раунд."
    elif is_mob and not is_player:
        base_sentence += " магия склонила исход раунда в её пользу."
    else:
        base_sentence += " энергия заклинания растворилась, оставив лишь жар в воздухе."
    return base_sentence

def get_stage_media(stage, meta_id):
    media_list = [
        {"type": "photo", "file_id": "https://picsum.photos/400/200?1"},
        {"type": "photo", "file_id": "https://picsum.photos/400/200?2"},
        {"type": "photo", "file_id": "https://picsum.photos/400/200?3"},
    ]
    try:
        meta_data = mob_meta.find_one({'_id': meta_id})
        images_list = meta_data['images']['actions'][stage]
        image_random = random.choice(images_list)
        image = MediaAttachment(ContentType.PHOTO, file_id=MediaId(image_random['telegram_file_id']))
        return (image, True)
    except:
        return ('', False)

def get_stage_image(stage, meta_id):
    try:
        meta_data = mob_meta.find_one({'_id': meta_id})
        images_list = meta_data['images'][stage]
        image_random = random.choice(images_list)
        image = MediaAttachment(ContentType.PHOTO, file_id=MediaId(image_random['telegram_file_id']))
        return (image, True)
    except:
        return ('', False)

async def get_mob_data(dialog_manager: DialogManager, **kwargs) -> Dict[str, str]:
    context = dialog_manager.current_context()
    mob_id = generate_random_mob()
    context.dialog_data["mob_id"] = str(mob_id)
    mob_data = mobs.find_one({"_id": mob_id})
    # image, has_image = get_stage_image('presentation', mob_data.get('meta_id'))
    return {
        "enemy_intro": generate_mob_intro(mob_data),
        # 'image': image,
        # 'has_image': has_image
    }

def make_bar(
    total: int, max_value: int = 21, slots: int = 10, show_total: bool = True
) -> str:
    if total > max_value:
        bar = "🟥" * slots
    else:
        filled_ratio = total / max_value
        filled_slots = round(filled_ratio * slots)
        empty_slots = slots - filled_slots
        filled = (
            "🟪"
            if total == max_value
            else "🟩" if 13 <= total <= 17 else "🟧" if total > 17 else "🟨"
        ) * filled_slots
        bar = f"{filled}{'⬜' * empty_slots}"
    return f"{bar} ({total})" if show_total else bar

def make_hitpoints_bar(hitpoints_left: int, total: int = 6) -> str:
    return "❤️" * hitpoints_left + "🤍" * (total - hitpoints_left)

async def get_battle_state(dialog_manager: DialogManager, **kwargs) -> Dict[str, Any]:
    context = dialog_manager.current_context()
    battle_id = context.dialog_data["battle_id"]
    mob_id = context.dialog_data["mob_id"]
    battle = battles.find_one({"_id": ObjectId(battle_id)})
    player_hand = battle["player_state"]["hand"]
    mob_hand = battle["mob_state"]["hand"]
    mob_data = mobs.find_one({"_id": ObjectId(mob_id)})
    spell_cast_name = f'<b>{mob_data["name"]}</b> {random.choice(SPELL_CAST_TEXT)}'
    spell_cast_title = f'{mob_data["title"]} {random.choice(SPELL_CAST_TEXT)}'
    spell_cast = random.choice([spell_cast_name, spell_cast_title])
    player_bar = (
        "‼️<b>Уровень магической силы скрыт. Тебе придётся колдовать вслепую. Будь осторожен!</b>"
        if battle.get("fog_full", False)
        else make_bar(
            sum(card["power"] for card in player_hand),
            show_total=not battle.get("fog_partial", False),
        )
    )
    # Set image based on fog event
    meta_id = mob_data.get("meta_id")
    event_image, has_event_image = ('', False)
    # if battle.get("fog_full", False):
    #     event_image, has_event_image = get_stage_image("demonstration_ass", meta_id)
    # elif battle.get("fog_partial", False):
    #     event_image, has_event_image = get_stage_image("demonstration_breasts", meta_id)
    return {
        "player_bar": player_bar,
        "player_total": sum(card["power"] for card in player_hand),
        "mob_total": sum(card["power"] for card in mob_hand),
        "battle_id": str(battle_id),
        'spell_cast': spell_cast,
        "round_number": battle.get("round_number", 1),
        "player_hitpoints": make_hitpoints_bar(battle["player_state"].get("hitpoints_left", 6)),
        "mob_hitpoints": make_hitpoints_bar(battle["mob_state"].get("hitpoints_left", 6)),
        "mirror_event": battle.get("mirror_event", False),
        "fog_full": battle.get("fog_full", False),
        "fog_partial": battle.get("fog_partial", False),
        "player_message": battle["player_state"].get("message", ""),
        # "event_image": event_image,
        # "has_event_image": has_event_image,
    }

async def round_result_getter(dialog_manager: DialogManager, **kwargs) -> Dict[str, Any]:
    context = dialog_manager.current_context()
    battle_id = context.dialog_data["battle_id"]
    mob_id = context.dialog_data["mob_id"]
    battle = battles.find_one({"_id": ObjectId(battle_id)})
    round_number = str(battle.get("round_number", 1))
    round_data = battle.get("rounds", {}).get(round_number, {})

    winner = round_data.get("winner")
    mob_hitpoints_removed = round_data.get("mob_hitpoints_removed", 0)
    player_hitpoints_removed = round_data.get("player_hitpoints_removed", 0)
    mob_data = mobs.find_one({"_id": ObjectId(mob_id)})
    if winner == 'player':
        try:
            spell_name = battle['player_state']['hand'][-1].get('name')
        except:
            spell_name = 'Искры Страсти'
        round_text = cast_spell(spell_name, mob_data.get('name', 'Офелия'), is_mob=False, is_player=True)
        mob_phrase = random.choice(QUOTES['hurt'][mob_data['persona']])
    elif winner == 'mob':
        try:
            spell_name = battle['player_state']['hand'][-1].get('name')
        except:
            spell_name = 'Искры Страсти'
        round_text = cast_spell(spell_name, mob_data.get('name', 'Офелия'), is_mob=True, is_player=False)
        mob_phrase = random.choice(QUOTES['cast'][mob_data['persona']])
    else:
        round_text = random.choice(DRAW_EFFECTS)
        round_text += ' Раунд завершился ничейным результатом.'
        mob_phrase = random.choice(QUOTES["draw"][mob_data["persona"]])
    event_text = (battle.get("event_description", "") if battle['mirror_event'] == True else '')
    player_total = sum(card["power"] for card in battle["player_state"]["hand"])
    mob_total = sum(card["power"] for card in battle["mob_state"]["hand"])
    if battle.get("mirror_event", False):
        player_total, mob_total = mob_total, player_total

    if not round_data.get("text"):
        battles.update_one(
            {"_id": battle["_id"]},
            {"$set": {f"rounds.{round_number}.text": round_text}},
        )
    return {
        "winner": winner,
        "player_hitpoints": battle["player_state"].get("hitpoints_left", 6),
        "mob_hitpoints": battle["mob_state"].get("hitpoints_left", 6),
        "mob_hitpoints_removed": mob_hitpoints_removed,
        "player_hitpoints_removed": player_hitpoints_removed,
        "hitpoints_remove_text": f'{round_text}\n'.strip(),
        'mob_phrase': mob_phrase,
        'event_text': event_text,
        "player_bar": make_bar(player_total),
        "mob_bar": make_bar(mob_total),
        "player_message": battle["player_state"].get("message", ""),
    }

async def get_battle_result(dialog_manager: DialogManager, **kwargs) -> Dict[str, str]:
    context = dialog_manager.current_context()
    battle_id = context.dialog_data["battle_id"]
    battle = battles.find_one({"_id": ObjectId(battle_id)})
    winner = battle.get("battle_winner")
    mob_id = context.dialog_data["mob_id"]
    mob_data = mobs.find_one({"_id": ObjectId(mob_id)})
    # if winner == 'player':
    #     image, has_image = get_stage_image('defeat', mob_data.get('meta_id'))
    # elif winner == 'mob':
    #     image, has_image = get_stage_image('victory', mob_data.get('meta_id'))
    # else:
    #     image, has_image = get_stage_image('demonstration_legs', mob_data.get('meta_id'))
    result_text = (
        WIN_TEXT if winner == "player" else LOSE_TEXT if winner == "mob" else DRAW_TEXT
    )
    return {
        "result_text": result_text,
        # 'has_image': has_image,
        # 'image': image
    }

async def get_magic_types(dialog_manager: DialogManager, **kwargs) -> Dict[str, list]:
    return {"magic_types": MAGIC_TYPE}
