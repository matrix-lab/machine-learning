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

numbers = []

for text in texts:
    if text[0] not in numbers:
        numbers.append(text[0])

    if text[1] not in numbers:
        numbers.append(text[1])

for call in calls:
    if call[0] not in numbers:
        numbers.append(call[0])

    if call[1] not in numbers:
        numbers.append(call[1])

message = 'There are <{}> different telephone numbers in the records.'
print(message.format(len(numbers)))

