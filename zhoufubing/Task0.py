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


textLen = len(texts);
callLen = len(calls);

firstText = texts[0]
lastCall = calls[callLen-1]

firstTextRecord = "First record of texts, {} texts {} at time {}"
firstCallRecord = "Last record of calls, {} calls {} at time {}"

print(firstTextRecord.format(firstText[0],firstText[1],firstText[2]))
print(firstCallRecord.format(lastCall[0],lastCall[1],lastCall[2]))
"""
任务0:
短信记录的第一条记录是什么？通话记录最后一条记录是什么？
输出信息:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

