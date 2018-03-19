
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)


with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)




def get_first_record_of_texts(texts):

    first_text = texts[0]

    return "First record of texts, {} texts {} at time {}".format(first_text[0],first_text[1],first_text[2])


print(get_first_record_of_texts(texts))


def get_last_record_of_calls(calls):

    last_text = calls[-1]

    return "Last record of calls, {} calls {} at time {}, lasting {} seconds".format(last_text[0],last_text[1],last_text[2],last_text[3])


print(get_last_record_of_calls(calls))


