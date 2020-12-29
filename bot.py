from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import logging

logging.basicConfig(level=logging.INFO)
bot = Bot(token='1437884548:AAGxC953mG_QhEygt3n_H0uJrKDw1w52OE0')
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
