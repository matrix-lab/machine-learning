# -*- coding: utf-8 -*-
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    longest_time_call = calls[0]
    for call in calls:
        if int(longest_time_call[-1]) < int(call[-1]):
            longest_time_call = call

print("%s spent the longest time, %s seconds, on the phone duringSeptember 2016." %
      (longest_time_call[0], longest_time_call[-1]))
