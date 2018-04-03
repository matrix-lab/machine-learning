# -*- coding: utf-8 -*-

import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

t_tels = set()
c_tels = set()
s_tels = set()

for text in texts:
    t_tels.add(text[0])
    t_tels.add(text[1])

for call in calls:
    c_tels.add(call[1])


for call in calls:
    if call[0] not in t_tels and call[0] not in c_tels:
        s_tels.add(call[0])

print("These numbers could be telemarketers: ")

for tel in sorted(list(s_tels)):
    print(tel)


