# coding:utf-8
import csv

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

records = {}

for call in calls:
    time = int(call[3])
    records[call[0]] = records.get(call[0], 0) + time
    records[call[1]] = records.get(call[1], 0) + time

records = sorted(records.items(), key=lambda x: x[1])

target_record = records.pop()

text_str = "{} spent the longest time, {} seconds, on the phone during September 2016."

print(text_str.format(target_record[0], target_record[1]))
