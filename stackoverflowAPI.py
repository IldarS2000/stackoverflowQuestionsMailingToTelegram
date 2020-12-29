import json

import requests


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
