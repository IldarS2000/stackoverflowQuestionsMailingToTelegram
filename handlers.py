from aiogram import types

from states import MainForm
from stackoverflowAPI import form_message
from bot import dp

button = types.KeyboardButton('Получить вопросы')


@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def process_menu(message: types.Message):
    await MainForm.mainState.set()
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).row(button)
    await message.answer('хотите получить вопросы?', reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == button.text, state=MainForm.mainState,
                    content_types=types.ContentTypes.TEXT)
async def process_menu(message: types.Message):
    msg = form_message()
    await message.answer(msg[0])
