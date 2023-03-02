from aiogram.dispatcher.filters.state import State, StatesGroup


class Kuriers(StatesGroup):
    ids = State()
    xabar = State()
