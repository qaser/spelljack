from aiogram_dialog import Dialog, Window, DialogManager
from aiogram_dialog.widgets.text import Format
from aiogram_dialog.widgets.kbd import Button, Row
from aiogram.types import CallbackQuery
from bson import ObjectId
from aiogram.filters.state import State, StatesGroup
from aiogram_dialog.widgets.text import Const
from config.mongo_config import mobs, players, battles


class BattleRoundSG(StatesGroup):
    ROUND = State()


def get_total(hand):
    return sum(card["power"] for card in hand)


async def get_battle_state(dialog_manager: DialogManager, **kwargs):
    battle_id = dialog_manager.start_data["battle_id"]
    battle = battles.find_one({"_id": ObjectId(battle_id)})

    player_hand = battle["player_state"]["hand"]
    mob_hand = battle["mob_state"]["hand"]

    total = get_total(player_hand)
    mob_total = get_total(mob_hand)

    player_bar = "▓" * (total // 2) + "░" * ((21 - total) // 2)
    mob_bar = "▓" * (mob_total // 2) + "░" * ((21 - mob_total) // 2)

    spell_names = ", ".join(f"{c['name']} ({c['power']})" for c in player_hand)

    return {
        "player_bar": f"💖 Ты: {player_bar} ({total})",
        "mob_bar": f"🖤 Она: {mob_bar} ({mob_total})",
        "spells": spell_names,
        "battle_id": str(battle_id)
    }

async def on_cast(callback: CallbackQuery, button: Button, manager: DialogManager):
    user_id = callback.from_user.id
    battle_id = ObjectId(manager.start_data["battle_id"])
    battle = battles.find_one({"_id": battle_id})

    player_state = battle["player_state"]
    hand = player_state["hand"]
    shared_deck = battle.get("shared_deck", [])

    if not shared_deck:
        await callback.answer("❗ Общая колода пуста!")
        return

    # Вытянуть верхнюю карту
    new_card = shared_deck.pop(0)
    hand.append(new_card)

    total = get_total(hand)

    update = {
        "player_state.hand": hand,
        "shared_deck": shared_deck
    }

    history_entry = {
        "actor": "player",
        "action": "draw",
        "card": new_card,
        "result": None,
        "timestamp": callback.message.date
    }

    if total > 21:
        update["status"] = "finished"
        update["winner"] = "mob"
        history_entry["result"] = "overload"

        battles.update_one({"_id": battle_id}, {
            "$set": update,
            "$push": {"history": history_entry}
        })

        await callback.answer("💥 Ты перегрузился чарами!")
        # Здесь позже переход к сцене поражения
        return

    # Обновление БД
    battles.update_one({"_id": battle_id}, {
        "$set": update,
        "$push": {"history": history_entry}
    })

    await callback.answer("✨ Ты вплёл новое заклинание!")
    await manager.switch_to(BattleRoundSG.ROUND)



async def on_stop(callback: CallbackQuery, button: Button, manager: DialogManager):
    await callback.answer("🧘 Пока не реализовано: стоп")


battle_round_dialog = Dialog(
    Window(
        Format("{player_bar}\n{mob_bar}"),
        Format("Твои чары: {spells}"),
        Row(
            Button(Const("🔥 Кастовать ещё"), id="cast", on_click=on_cast),
            Button(Const("🧘 Стоп"), id="stop", on_click=on_stop),
        ),
        state=BattleRoundSG.ROUND,
        getter=get_battle_state
    )
)
