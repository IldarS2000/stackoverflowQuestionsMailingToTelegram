from aiogram.dispatcher.filters.state import State, StatesGroup


class MainForm(StatesGroup):
    nextQuestion = State()
