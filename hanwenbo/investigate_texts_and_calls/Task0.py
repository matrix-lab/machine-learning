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
任务0:
短信记录的第一条记录是什么？通话记录最后一条记录是什么？
输出信息:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""


def print_text(data, index):
    text = data[index]
    print(
        "First record of texts, {} texts {} at time {}".format(text[0], text[1], text[2]))


def print_call(data, index):
    call = data[index]
    print(
        "Last record of calls, {} calls {} at time {}, lasting {} seconds".format(call[0], call[1],
                                                                                  call[2], call[3]))


print_text(texts, 0)

print_call(calls, -1)
