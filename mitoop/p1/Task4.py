# coding:utf-8
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


def get_called_tels(records):
    called_tels = set()
    for record in records:
        called_tels.add(record[1])
    return list(called_tels)


def get_sms_tels(records):
    sms_tels = set()
    for record in records:
        sms_tels.add(record[0])
        sms_tels.add(record[1])
    return list(sms_tels)


telemarketers_tels = set()
called_tels = get_called_tels(calls)
sms_tels = get_sms_tels(texts)
for call in calls:
    if call[0] not in called_tels and call[0] not in sms_tels:
        telemarketers_tels.add(call[0])

print("These numbers could be telemarketers: ")

for tel in sorted(list(telemarketers_tels)):
    print(tel)
