from aiogram.fsm.state import StatesGroup, State
import logging

logging.basicConfig(level=logging.INFO)


class Profile(StatesGroup):
    '''Класс состояний для анкеты пользователя'''
    
    name = State()
    city = State()

__all__ = ["Profile"]