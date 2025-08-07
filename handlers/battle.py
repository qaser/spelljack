from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram_dialog import Dialog, DialogManager, StartMode

from dialogs.for_battle import windows
from dialogs.for_battle.states import Battle


router = Router()
dialog =  Dialog(
    windows.select_magic_window(),
    windows.select_enemy_window(),
    windows.show_enemy_window(),
    windows.battle_round_window(),
    windows.round_result_window(),
    windows.battle_result_window(),
    windows.outfit_review_window(),
)


@router.message(Command("battle"))
async def start_battle(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(Battle.select_magic_type, mode=StartMode.RESET_STACK)
