from aiogram.fsm.state import StatesGroup, State
import logging

logging.basicConfig(level=logging.INFO)


class Profile(StatesGroup):
    name = State()
    city = State()

__all__ = ["Profile"]