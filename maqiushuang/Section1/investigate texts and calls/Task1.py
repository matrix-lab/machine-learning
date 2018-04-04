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
list_number = []
def tel_exist(lists):
    for list in lists:
        list_number.append(list[0])
        list_number.append(list[1])
tel_exist(texts)
tel_exist(calls)
print(len(set(list_number)))

