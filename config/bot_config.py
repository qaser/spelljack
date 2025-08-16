from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.base import DefaultKeyBuilder
from aiogram.fsm.storage.mongo import MongoStorage
from motor.motor_asyncio import AsyncIOMotorClient

# from config.redis_config import storage
from config.telegram_config import TELEGRAM_TOKEN

mongo_client = AsyncIOMotorClient("mongodb://localhost:27017")

storage = MongoStorage(
    client=mongo_client,
    db_name="aiogram_fsm",
    collection_name="states",
    key_builder=DefaultKeyBuilder(with_destiny=True),  # <-- Добавьте это
)

bot = Bot(token=TELEGRAM_TOKEN, default=DefaultBotProperties(parse_mode='HTML'))
dp = Dispatcher(storage=storage)
