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

# 设置变量
mobile_numbers = set()

# 统计短信电话数量
for text in texts:
    mobile_numbers.add(text[0])
    mobile_numbers.add(text[1])

# 统计电话记录个数
for call in calls:
    mobile_numbers.add(call[0])
    mobile_numbers.add(call[1])

# 将重复的电话进行过滤
unique_mobiles = set()
for mobile_number in mobile_numbers:
    if mobile_number not in unique_mobiles:
        unique_mobiles.add(mobile_number)

print("There are {} different telephone numbers in the records.".format(len(unique_mobiles)))
