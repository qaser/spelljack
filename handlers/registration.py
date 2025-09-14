from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram_dialog import Dialog, DialogManager, StartMode

from dialogs.for_registration import windows
from dialogs.for_registration.states import Registration
from config.mongo_config import players
from utils.utils import report_error

router = Router()

dialog =  Dialog(
    windows.age_confirmation_window(),
    windows.select_name_window(),
    windows.reg_confirm_window(),
)


@router.message(Command('registration'))
async def registration_request(message: Message, dialog_manager: DialogManager):
    try:
        await message.delete()
        user_id = message.from_user.id
        # Проверка на бота
        if message.from_user.is_bot:
            return
        # Проверка существования игрока
        player_check = players.find_one({'_id': user_id})

        if player_check:
            await message.answer("✅ Вы уже зарегистрированы в игре!")
        else:
            # Запуск диалога регистрации
            await dialog_manager.start(Registration.age_confirmation, mode=StartMode.RESET_STACK)
    except Exception as e:
        report_error(e)
        await message.answer("❌ Произошла ошибка при регистрации")
