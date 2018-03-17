# coding:utf-8
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

first_text = texts[0]
text_str = "First record of texts, {} texts {} at time {}"

last_call = calls[-1]
call_str = "Last record of calls, {} calls {} at time {}, lasting {} seconds"

print(text_str.format(first_text[0], first_text[1], first_text[2]))
print(call_str.format(last_call[0], last_call[1], last_call[2], last_call[3]))
