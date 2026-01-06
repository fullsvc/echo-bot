# Reply клавиатура

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from app.services.text_buttons import FAQ_BUTTON_TEXT, PROFILE_BUTTON_TEXT, ABOUT_BUTTON_TEXT, BACK_BUTTON_TEXT


faq_button = KeyboardButton(text=FAQ_BUTTON_TEXT)
profile_button = KeyboardButton(text=PROFILE_BUTTON_TEXT)
about_button = KeyboardButton(text=ABOUT_BUTTON_TEXT)
back_button = KeyboardButton(text=BACK_BUTTON_TEXT)

main_menu_layout = [
    [faq_button, profile_button, about_button],
]

back_layout = [
    [back_button]
]

main_menu_keyboard = ReplyKeyboardMarkup(
    keyboard=main_menu_layout,
    resize_keyboard=True
)

back_keyboard = ReplyKeyboardMarkup(
    keyboard=back_layout,
    resize_keyboard=True
)
