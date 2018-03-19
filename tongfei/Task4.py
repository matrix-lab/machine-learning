"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


def get_number(items):
    """
    获取拨打电话的列表和被拨打电话的列表，用字典的形式返回
    :param items:
    :return:
    """
    from_numbers = []
    to_numbers = []

    for item in items:
        if item[0] not in from_numbers:
            from_numbers.append(item[0])

        if item[1] not in to_numbers:
            to_numbers.append(item[1])

    return {'from': from_numbers, 'to': to_numbers}


call_dict = get_number(calls)
text_dict = get_number(texts)

all_numbers = set(call_dict['to'] + text_dict['from'] + text_dict['to'])

print('These numbers could be telemarketers:')

for item in call_dict['from']:
    if item not in all_numbers:
        print(item)
