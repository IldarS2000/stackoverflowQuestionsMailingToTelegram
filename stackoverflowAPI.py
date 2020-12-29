import json

import requests


def form_message(stack, sort_type, tags):
    query = 'https://api.stackexchange.com/2.2/questions?page=1'

    valid_order_arguments = ['desc', 'asc']
    valid_sort_arguments = ['activity', 'votes', 'creation', 'hot', 'week', 'month']

    stack = 'ru.' if stack == 'ru' else ''

    query += f'&sort={sort_type}&tagged={tags}&site={stack}stackoverflow'

    response = requests.get(query)
    raw_json = response.text

    processed_json = json.loads(raw_json)

    questions = processed_json['items']

    messages = []
    for index, q in enumerate(questions, 1):
        message = f'{index}) голосов за вопрос: {q["score"]}\n'
        message += f'{q["link"]}\n'
        messages.append(message)

    return messages
