from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import Message, TelegramObject

from config.mongo_config import players
import logging
from cachetools import TTLCache
import time


# Глобальный кэш для игроков (1000 записей, время жизни 5 минут)
player_cache = TTLCache(maxsize=1000, ttl=300)


class PlayerCheckMiddleware(BaseMiddleware):
    PUBLIC_COMMANDS = ['/start', '/registration', '/help', '/about']

    def __init__(self):
        super().__init__()
        self.cache_hits = 0
        self.cache_misses = 0

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        if not isinstance(event, Message) or not event.text:
            return await handler(event, data)

        # Проверяем только личные сообщения
        if event.chat.type != 'private':
            return await handler(event, data)

        parts = event.text.split()
        first_word = parts[0].split('@')[0].lower()

        # Пропускаем некоманды и публичные команды
        if not first_word.startswith('/') or first_word in self.PUBLIC_COMMANDS:
            return await handler(event, data)

        user_id = event.from_user.id

        # Проверяем кэш
        cache_key = f"player_{user_id}"
        if cache_key in player_cache:
            self.cache_hits += 1
            player = player_cache[cache_key]
        else:
            self.cache_misses += 1
            player = players.find_one({'_id': user_id})
            if player:
                player_cache[cache_key] = player

        if not player:
            await self._handle_unauthorized(event)
            return

        return await handler(event, data)

    async def _handle_unauthorized(self, event: Message):
        """Обработка неавторизованных запросов"""
        try:
            await event.delete()
        except Exception as e:
            logging.warning(f"Failed to delete message: {e}")

        try:
            await event.answer(
                "⚠️ Для использования команд необходимо зарегистрироваться!\n"
                "Используйте /registration для регистрации"
            )
        except Exception as e:
            logging.error(f"Failed to send message: {e}")
