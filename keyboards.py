from aiogram import types

button_ru = types.KeyboardButton('ru')
button_en = types.KeyboardButton('en')
stack_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).row(button_ru, button_en)

button_votes = types.KeyboardButton('votes')
button_activity = types.KeyboardButton('activity')
sort_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).row(button_votes, button_activity)

get_question_button = types.KeyboardButton('получить вопросы')
change_parameters_button = types.KeyboardButton('/start')
get_question_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).row(get_question_button,
                                                                            change_parameters_button)
