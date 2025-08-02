from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode
from dialogs.battle_start import BattleSG
from dialogs.battle_round import BattleRoundSG
from services.battle_factory import create_battle

router = Router()

@router.message(Command("battle"))
async def start_battle(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(BattleSG.CHOOSE, mode=StartMode.RESET_STACK)
