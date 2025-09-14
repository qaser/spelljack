import datetime as dt
import random
from typing import Dict
from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from bson import ObjectId
from .states import Registration

from config.mongo_config import players


async def on_age_confirm(callback: CallbackQuery, widget, manager):
    await manager.switch_to(Registration.select_name)


async def on_select_name(callbackwidget, widget, manager, selected_name):
    context = manager.current_context()
    context.dialog_data["name"] = selected_name
    await manager.switch_to(Registration.reg_confirm)


async def on_reg_confirm(callback: CallbackQuery, widget, manager):
    context = manager.current_context()
    name = context.dialog_data.get('name', 'Люциан')
    players.insert_one(
        {
            '_id': callback.message.chat.id,
            'name': name,
            'title': 'Уснувший',
            'exp': 0,
            'dream_level': 100,
            'is_age_confirmed': True,
            'is_active': True,
            'is_premium': False,
            'reg_date': dt.datetime.now(),
            'magic_balance': 'Спокойный',  # порывистый, агрессивный, спокойный
            'magic': {
                'Страсть': 0,
                'Соблазн': 0,
                'Флирт': 0,
                'Искушение': 0,
            },
            'stats': {
                'battles': 0,
                'wins': 0,
                'defeats': 0,
                'draws': 0,
            }
        }
    )
    await manager.done()
