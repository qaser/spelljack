import datetime as dt

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import FSInputFile, Message
from pytz import timezone

from config.bot_config import bot
from config.telegram_config import MY_TELEGRAM_ID
from utils import constants as const

router = Router()


@router.message(Command('log'))
async def send_logs(message: Message):
    user_id = message.from_user.id
    if user_id == int(MY_TELEGRAM_ID):
        document = FSInputFile(path=r'logs_bot.log')
        await message.answer_document(document=document)
    await message.delete()
