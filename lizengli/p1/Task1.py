# -*- coding: utf-8 -*-
import csv

text_numbers = set([])
call_numbers = set([])

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    for text in texts:
        text_numbers.add(text[0])

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for call in calls:
        call_numbers.add(call[0])

print("There are %d different telephone numbers in the records" % len(text_numbers | call_numbers))
