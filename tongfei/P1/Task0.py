
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

    first_text = texts[0]
    text_message = 'First record of texts, <{}> texts <{}> at time <{}>'
    print(text_message.format(first_text[0], first_text[1], first_text[2]))

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

    last_call = calls.pop()
    call_message = 'Last record of calls, <{}> calls <{}> at time <{}>, lasting <{}> seconds'
    print(call_message.format(last_call[0], last_call[1], last_call[2], last_call[3]))


