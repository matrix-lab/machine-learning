# -*- coding: utf-8 -*-
import csv


def get_code_calls(code, some_calls):
    call_codes = []
    code = '(' + code + ')'
    code_len = len(code)
    for call in some_calls:
        if call[0][:code_len] == code:
            call_codes.append(call)
    return call_codes


def print_code(some_calls):
    codes = set([])
    for call in some_calls:
        if ' ' in call[1]:
            codes.add(call[1][:4])
        if ')' in call[1]:
            codes.add(call[1][1:call[1].index(')')])
    print("The numbers called by people in Bangalore have codes:")
    codes = list(codes)
    codes.sort()
    for code in codes:
        print(code)


def print_percentage(code, some_calls):
    call_count = 0
    code = '(' + code + ')'
    for call in some_calls:
        if code in call[1]:
            call_count += 1
    percentage = call_count / len(some_calls)
    print(
        "%.2f percent of calls from fixed lines in Bangalore are callsto other fixed lines in Bangalore." % percentage)


with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    bangalore_calls = get_code_calls('080', calls)
    print_code(bangalore_calls)
    print_percentage('080', bangalore_calls)
