# coding:utf-8
import csv

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


def get_tel_prefix(tel):
    tel = str(tel)
    if tel.startswith('(0'):
        tel = tel.split(')')
        return tel[0][1:]
    elif tel.startswith('7') or tel.startswith('8') or tel.startswith('9'):
        tel = tel.split(' ')
        return tel[0]
    elif tel.startswith('140'):
        return '140'
    else:
        return None


tel_prefix = set()
called_by_bangalore = []

for call in calls:
    if str(call[0]).startswith('(080)'):
        called_by_bangalore.append(list(call))
        prefix = get_tel_prefix(call[1])
        if prefix:
            tel_prefix.add(str(prefix))

bangalore_total_records = len(called_by_bangalore)
bangalore_to_bangalore_records = 0

for record in called_by_bangalore:
    if record[0].startswith('(080)') and record[1].startswith('(080)'):
        bangalore_to_bangalore_records += 1

# The first question
print("The numbers called by people in Bangalore have codes:")

for item in sorted(tel_prefix):
    print(item)

# the second question
text_str = "{:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore."

print(text_str.format(float(bangalore_to_bangalore_records)/float(bangalore_total_records) * 100))
