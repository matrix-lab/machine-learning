# -*- coding: utf-8 -*-

import csv

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


def print_longest_call_talk_time (calls):

    records = {}

    for call in calls:
        records[call[0]] = records.get(call[0], 0) + int(call[3])
        records[call[1]] = records.get(call[1], 0) + int(call[3])

    longest_record_phone = ''
    longest_record_time = 0

    for record in records:
        if records[record] > longest_record_time:
            longest_record_phone = record
            longest_record_time = records[record]


    print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(longest_record_phone,longest_record_time));


print_longest_call_talk_time(calls)