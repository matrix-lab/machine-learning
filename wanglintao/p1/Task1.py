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


"""
任务1：
短信和通话记录中一共有多少电话号码？每个号码只统计一次。
输出信息：
"There are <count> different telephone numbers in the records."
"""

text1 = []
text2 = []
lists = texts + calls

for list_a in lists:
    if list_a[0] not in text1:
        text1.append(list_a[0])
    if list_a[1] not in text2:
        text2.append(list_a[1])
temp_lists = text1 + text2

print(format(len(set(temp_lists))))
# print(type(temp_lists))
# print(temp_lists[1])
# print(temp_lists.count('90365 06212'))


