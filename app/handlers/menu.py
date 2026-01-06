import logging
from aiogram import Router, types, F
from app.keyboards.reply import main_menu_keyboard
from app.services.text_buttons import FAQ_BUTTON_TEXT, ABOUT_BUTTON_TEXT


logging.basicConfig(level=logging.INFO)


router = Router()


@router.message(F.text == FAQ_BUTTON_TEXT)
async def on_faq_button(message: types.Message):
        await message.reply(f"Частозадаваемые вопросы", reply_markup=main_menu_keyboard)

@router.message(F.text == ABOUT_BUTTON_TEXT)
async def on_about_button(message: types.Message):
        await message.reply(f"Информация о нас", reply_markup=main_menu_keyboard)

