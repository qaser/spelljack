import asyncio
import logging

from aiogram import F
from aiogram.filters.command import Command, CommandObject
from aiogram.fsm.context import FSMContext
from aiogram.types import (
    BotCommand, BotCommandScopeAllPrivateChats, Message, ReplyKeyboardRemove)
from aiogram_dialog import setup_dialogs

import utils.constants as const
from config.bot_config import bot, dp
from config.mongo_config import admins
from config.telegram_config import ADMIN_PASSWORD, MY_TELEGRAM_ID
from handlers import battle, service


@dp.message(Command('reset'))
async def reset_handler(message: Message, state: FSMContext):
    await message.delete()
    await state.clear()
    await message.answer(
        'Текущее состояние бота сброшено',
        reply_markup=ReplyKeyboardRemove()
    )


@dp.message(Command('help'))
async def help_handler(message: Message):
    await message.answer(const.HELP_ADMIN)


@dp.message(Command("admin"))
async def admin_handler(message: Message, command: CommandObject):
    user = message.from_user
    # Проверка: передан ли пароль
    if not command.args:
        await message.answer(
            "❗ Пожалуйста, укажите пароль:",
            parse_mode="Markdown"
        )
        return
    # Проверка: правильный ли пароль
    if command.args.strip() != ADMIN_PASSWORD:
        await message.answer("🚫 Неверный пароль")
        return
    # Регистрация администратора
    admins.update_one(
        {"user_id": user.id},
        {"$set": {"directions": ["gpa"], "username": user.full_name}},
        upsert=True
    )
    await message.answer("✅ Администратор добавлен")
    await bot.send_message(
        MY_TELEGRAM_ID,
        f"➕ Добавлен администратор {user.full_name}"
    )
    await message.delete()


@dp.message(Command('start'))
async def start_handler(message: Message):
    await message.answer(const.INITIAL_TEXT)


async def setup_bot_commands(bot):
    # Установим команды только для приватных чатов
    private_commands = [
        BotCommand(command="ao", description="Создание группы расследования"),
    ]
    await bot.set_my_commands(private_commands, scope=BotCommandScopeAllPrivateChats())
    # Очистим команды по умолчанию (чтобы в группах ничего не отображалось)
    await bot.set_my_commands([], scope=None)


# удаление сервисных сообщений
@dp.message(
        F.content_type.in_([
            'pinned_message',
            'left_chat_member',
            'forum_topic_created',
            'forum_topic_closed',
            'forum_topic_edited',
            'forum_topic_reopened',
            'new_chat_members'
        ])
    )
async def delete_service_pinned_message(message: Message):
    try:
        await message.delete()
    except:
        pass


async def main():
    dp.include_routers(
        service.router,
        battle.router,
        battle.dialog,
    )
    await setup_bot_commands(bot)
    setup_dialogs(dp)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(
        filename='logs_bot.log',
        level=logging.INFO,
        filemode='a',
        format='%(asctime)s - %(message)s',
        datefmt='%d.%m.%y %H:%M:%S',
        encoding='utf-8',
    )
    asyncio.run(main())
