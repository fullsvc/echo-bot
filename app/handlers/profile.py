import logging
from aiogram import Router, types, F
from aiogram.filters import Command

from app.states.profile import Profile
from aiogram.fsm.context import FSMContext
from app.keyboards.reply import main_menu_keyboard, back_keyboard
from app.services.text_buttons import PROFILE_BUTTON_TEXT, BACK_BUTTON_TEXT


logging.basicConfig(level=logging.INFO)

router = Router()

@router.message(F.text == BACK_BUTTON_TEXT)
async def city_entered(message: types.Message, state: FSMContext):
    await message.answer(f"Возврат в главное меню", reply_markup=main_menu_keyboard)


@router.message(F.text == PROFILE_BUTTON_TEXT)
@router.message(Command("profile"))
async def profile_start(message: types.Message, state: FSMContext):
    await state.clear()
    await state.set_state(Profile.name)

    await message.answer("Введите имя", reply_markup=back_keyboard)


@router.message(Profile.name)
async def job_entered(message: types.Message, state: FSMContext):
    person_name = message.text

    await state.update_data(name=person_name)
    await state.set_state(Profile.city)
    await message.answer("Введите город проживания", reply_markup=back_keyboard)


@router.message(Profile.city)
async def city_entered(message: types.Message, state: FSMContext):
    person_city = message.text
    data = await state.get_data()
    person_name = data.get("name")

    result_text = f'''Ваше имя {person_name}\nВаш город проживания {person_city}'''

    await message.answer(result_text)
    await state.clear()

    await message.answer(f"Возврат в главное меню", reply_markup=main_menu_keyboard)




