# -*- coding: utf-8 -*-

import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

call_records = set()

# set() 是一组key的集合，不存储value。由于key不能重复，所以，在set中，没有重复的key。
# 通过 add(key) 方法可以添加元素到set中，可以重复添加，但不会有效果。

for text in texts:
    call_records.add(text[0])
    call_records.add(text[1])

for call in calls:
    call_records.add(call[0])
    call_records.add(call[1])


print('There are {} different telephone numbers in the records.'.format(len(call_records)))
