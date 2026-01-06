import logging

from aiogram import Router, types, F
from aiogram.filters import Command

from app.keyboards.reply import main_menu_keyboard


logging.basicConfig(level=logging.INFO)

router = Router()

@router.message(Command("start"))
async def command_start(message: types.Message):
    user_name = message.chat.username
    await message.answer(f"Hello {user_name}", reply_markup=main_menu_keyboard)

@router.message(Command("help"))
async def command_help(message: types.Message):
    help_text = '''
        Помощь:
        1) /start - начало работы с ботом
        2) /help - помощь
        3) /profile - заполнить анкету пользователя
        4) Эхо бот - отвечаю на сообщения
    '''
    
    await message.answer(help_text, reply_markup=main_menu_keyboard)
