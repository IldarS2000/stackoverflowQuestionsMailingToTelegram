from aiogram import types
from aiogram.dispatcher import FSMContext

from states import MainForm
from stackoverflowAPI import form_message
from bot import dp

button = types.KeyboardButton('Получить вопросы')


@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def handler(message: types.Message):
    await MainForm.nextQuestion.set()
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).row(button)
    await message.answer('хотите получить вопросы?', reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == button.text, state=MainForm.nextQuestion,
                    content_types=types.ContentTypes.TEXT)
async def handler(message: types.Message, state: FSMContext):
    msg = form_message()
    await message.answer(msg[0])
