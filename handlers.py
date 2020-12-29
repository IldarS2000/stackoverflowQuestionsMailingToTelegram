from aiogram import types
from aiogram.dispatcher import FSMContext

from states import MainForm
from bot import dp

from stackoverflowAPI import form_message

button = types.KeyboardButton('Получить вопросы')


@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def handler(message: types.Message):
    await MainForm.nextQuestion.set()
    await message.answer('сколько вопросов хотите получить?', reply_markup=types.ReplyKeyboardRemove())


def is_positive_number(msg):
    text = msg.text
    if text.isdigit():
        if int(text) > 0:
            return True
    return False


@dp.message_handler(lambda message: not is_positive_number(message), state=MainForm.nextQuestion,
                    content_types=types.ContentTypes.TEXT)
async def handler(message: types.Message):
    await message.reply('необходимо положительное число')


@dp.message_handler(lambda message: is_positive_number(message), state=MainForm.nextQuestion,
                    content_types=types.ContentTypes.TEXT)
async def handler(message: types.Message):
    questions_count = int(message.text)
    messages = form_message()[:questions_count]
    for msg in messages:
        await message.answer(msg)
