from aiogram.dispatcher.filters.state import State, StatesGroup


class Form(StatesGroup):
    choosing_stack = State()
    choosing_sort = State()
    choosing_tagged = State()
    get_questions = State()
    get_questions_with_same_parameters = State()
    back_to_choosing = State()
