# -*- coding: utf-8 -*-
import csv


def get_normal_call_numbers(some_calls):
    calls = set([])
    for call in some_calls:
        calls.add(call[1])
    return calls


def get_normal_text_numbers(some_calls):
    texts = set([])
    for call in some_calls:
        texts.add(call[0])
        texts.add(call[1])
    return texts


def print_telemarketers(some_numbers, some_calls):
    print("These numbers could be telemarketers: ")
    numbers = set([])
    for call in some_calls:
        if call[0] not in some_numbers:
            numbers.add(call[0])
    numbers = list(numbers)
    numbers.sort()
    for number in numbers:
        print(number)


with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    normal_text_numbers = get_normal_text_numbers(texts)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    normal_call_numbers = get_normal_call_numbers(calls)

normal_numbers = normal_text_numbers | normal_call_numbers
print_telemarketers(normal_numbers, calls)
