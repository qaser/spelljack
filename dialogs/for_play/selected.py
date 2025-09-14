from aiogram_dialog import StartMode

from dialogs.for_battle.states import Battle


async def on_battle_start(callback, widget, manager):
    await manager.done()
    await manager.start(Battle.select_magic_type, mode=StartMode.RESET_STACK)
