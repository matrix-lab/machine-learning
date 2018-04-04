import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

def count_total(records):
	for record in records:
		if record[0] not in number:
				number.append(record[0])
		elif record[1] not in number:
				number.append(record[1])

number = [];
count_total(texts)
count_total(calls)								
print(len(number))