from aiogram import types

button_ru = types.KeyboardButton('ru')
button_en = types.KeyboardButton('en')
stack_buttons = [button_ru.text, button_en.text]
stack_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).row(button_ru, button_en)

button_votes = types.KeyboardButton('votes')
button_activity = types.KeyboardButton('activity')
button_creation = types.KeyboardButton('creation')
button_hot = types.KeyboardButton('hot')
button_week = types.KeyboardButton('week')
button_month = types.KeyboardButton('month')
sort_buttons = [button_votes.text, button_activity.text, button_hot.text, button_week.text, button_month.text]
sort_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(button_votes).add(button_activity).add(
    button_creation).row(button_hot, button_week, button_month)

get_question_button = types.KeyboardButton('получить вопросы c теми же параметрами')
change_parameters_button = types.KeyboardButton('поменять параметры')
get_question_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(get_question_button).add(
    change_parameters_button)
