import logging

from aiogram import Router, types, F

from app.keyboards.reply import main_menu_keyboard


logging.basicConfig(level=logging.INFO)

router = Router()


@router.message(F.text)
async def echo(message: types.Message):
    text = message.text
    await message.reply(f"Ты написал {message.text}", reply_markup=main_menu_keyboard)

