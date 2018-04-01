"""
下面的文件将会从csv文件中读取读取短信与电话记录
"""
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
"""


def get_diff_phone_num(data, phone_index):
    phones = set()
    for item in data:
        for index in phone_index:
            phones.add(item[index])

    return len(phones)


total = get_diff_phone_num(texts, [0, 1]) + get_diff_phone_num(calls, [0, 1])

print("There are {} different telephone numbers in the records.".format(total))
