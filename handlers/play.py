from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram_dialog import Dialog, DialogManager, StartMode

from dialogs.for_play import windows
from dialogs.for_play.states import Play


router = Router()
dialog = Dialog(
    windows.player_info_window(),
    # windows.settings_window(),
    # windows.show_enemy_window(),
    # windows.battle_round_window(),
    # windows.round_result_window(),
    # windows.battle_result_window(),
)


@router.message(Command("play"))
async def start_play(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(Play.player_info, mode=StartMode.RESET_STACK)
