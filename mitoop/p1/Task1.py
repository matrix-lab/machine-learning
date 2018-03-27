# coding:utf-8
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

records = set()

for text in texts:
    records.add(text[0])
    records.add(text[1])

for call in calls:
    records.add(call[0])
    records.add(call[1])

text_str = "There are {} different telephone numbers in the records."
print(text_str.format(len(records)))
