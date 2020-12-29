import json

import requests

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor
from aiogram import types
from aiogram.dispatcher.filters.state import State, StatesGroup

import logging

logging.basicConfig(level=logging.INFO)
bot = Bot(token='1437884548:AAGxC953mG_QhEygt3n_H0uJrKDw1w52OE0')
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


def form_message():
    query = 'https://api.stackexchange.com/2.2/questions?page=1'

    valid_order_arguments = ['desc', 'asc']
    valid_sort_arguments = ['activity', 'votes', 'creation', 'hot', 'week', 'month']

    order = 'desc'
    sort = 'week'
    tagged = 'c++'

    query += f'&order={order}&sort={sort}&tagged={tagged}&site=stackoverflow'

    response = requests.get(query)
    raw_json = response.text

    processed_json = json.loads(raw_json)

    questions = processed_json['items']

    messages = []
    for index, q in enumerate(questions, 1):
        message = f'{index}) title: {q["title"]}\n'
        message += f'score: {q["score"]}\n'
        message += f'link: {q["link"]}\n'
        messages.append(message)

    return messages


button = types.KeyboardButton('Получить вопросы')


class MainForm(StatesGroup):
    mainState = State()


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


if __name__ == '__main__':
    form_message()
    executor.start_polling(dp, skip_updates=True)
