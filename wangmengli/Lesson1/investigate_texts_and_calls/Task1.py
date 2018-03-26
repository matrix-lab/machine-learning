import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
任务1：
短信和通话记录中一共有多少电话号码？每个号码只统计一次。
输出信息：
"There are <count> different telephone numbers in the records."
"""

phones = []
def phone_exist(lists):
    for list in lists:
        if list[0] not in phones:
            phones.append(list[0])
        if list[1] not in phones:
            phones.append(list[1])
phone_exist(texts)
phone_exist(calls)
print(len(phones))
