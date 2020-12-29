from aiogram import types
from aiogram.dispatcher import FSMContext

from states import Form
from bot import dp

from stackoverflowAPI import form_message
from keyboards import stack_keyboard, sort_keyboard, get_question_keyboard, change_parameters_button, stack_buttons, \
    sort_buttons, get_question_button


@dp.message_handler(state='*', commands='start')
async def handler(message: types.Message):
    await Form.choosing_stack.set()
    await message.answer('русский или английский stack?', reply_markup=stack_keyboard)


@dp.message_handler(lambda message: message.text == change_parameters_button.text,
                    state=Form.get_questions_with_same_parameters,
                    content_types=types.ContentTypes.TEXT)
async def handler(message: types.Message):
    await Form.choosing_stack.set()
    await message.answer('русский или английский stack?', reply_markup=stack_keyboard)


@dp.message_handler(lambda message: message.text in stack_buttons,
                    state=Form.choosing_stack,
                    content_types=types.ContentTypes.TEXT)
async def handler(message: types.Message, state: FSMContext):
    await Form.choosing_sort.set()
    await state.update_data(stack=message.text)
    await message.answer('выберите как отсортировать вопросы', reply_markup=sort_keyboard)


@dp.message_handler(lambda message: message.text in sort_buttons,
                    state=Form.choosing_sort,
                    content_types=types.ContentTypes.TEXT)
async def handler(message: types.Message, state: FSMContext):
    await Form.choosing_tagged.set()
    await state.update_data(sort_type=message.text)
    await message.answer('выберите теги через следующий разделитель: \';\'', reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(state=Form.choosing_tagged,
                    content_types=types.ContentTypes.TEXT)
async def handler(message: types.Message, state: FSMContext):
    await Form.get_questions.set()
    await state.update_data(tags=message.text)
    await message.answer('выберите число вопросов')


def is_positive_number(msg):
    text = msg.text
    if text.isdigit():
        if int(text) > 0:
            return True
    return False


@dp.message_handler(lambda message: not is_positive_number(message), state=Form.get_questions,
                    content_types=types.ContentTypes.TEXT)
async def handler(message: types.Message):
    await message.reply('необходимо положительное число')


@dp.message_handler(lambda message: is_positive_number(message), state=Form.get_questions,
                    content_types=types.ContentTypes.TEXT)
async def handler(message: types.Message, state: FSMContext):
    await Form.get_questions_with_same_parameters.set()
    questions_count = int(message.text)
    await state.update_data(questions_count=questions_count)

    user_data = await state.get_data()
    stack = user_data['stack']
    sort_type = user_data['sort_type']
    tags = user_data['tags']

    messages = form_message(stack, sort_type, tags)[:questions_count]
    if messages:
        for msg in messages:
            await message.answer(msg)
    else:
        await message.answer('нет вопросов подходящих под параметры')
    await message.answer('получить вопросы с теми же параметрами?', reply_markup=get_question_keyboard)


@dp.message_handler(lambda message: message.text == get_question_button.text,
                    state=Form.get_questions_with_same_parameters,
                    content_types=types.ContentTypes.TEXT)
async def handler(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    questions_count = int(user_data['questions_count'])

    user_data = await state.get_data()
    stack = user_data['stack']
    sort_type = user_data['sort_type']
    tags = user_data['tags']

    messages = form_message(stack, sort_type, tags)[:questions_count]
    if messages:
        for msg in messages:
            await message.answer(msg)
    else:
        await message.answer('нет вопросов подходящих под параметры')
    await message.answer('получить вопросы с теми же параметрами?', reply_markup=get_question_keyboard)


@dp.message_handler(state='*', content_types=types.ContentTypes.ANY)
async def send_default_message(message: types.Message):
    await message.answer('извините, не могу разобрать вашу команду, есть ошибка ввода')
