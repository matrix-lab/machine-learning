"""
Intro to Python Lab 1, Task 3

Complete each task in the file for that task. Submit the whole folder
as a zip file or GitHub repo. 
Full submission instructions are available on the Lab Preparation page.
"""

"""
Read file into texts and calls. 
It's ok if you don't understand how to read files
You will learn more about reading files in future lesson
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore. 
Fixed line numbers include parentheses, so Bangalore numbers 
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. 
 - Fixed lines start with an area code enclosed in brackets. The area 
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# Part A
call_sends = [call[0] for call in calls]
call_receives = [call[1] for call in calls]

def get_called_area_code(call_number):
	if call_number[0] == '(':
		return call_number[1:call_number.find(')')]
	elif call_number.find('140') == 0:
		return '140'
	else:
		return call_number[0:4]

area_code_list = []
area_code_count = {}
for index in range(len(call_sends)):
	if call_sends[index].find('(080)') == 0:
		area_code = get_called_area_code(call_receives[index])
		area_code_count[area_code] = area_code_count.get(area_code, 0) + 1
		if area_code not in area_code_list:
			area_code_list.append(area_code)

sorted_called_list = sorted(area_code_list)
print('Part A')
print("The numbers called by people in Bangalore have codes:")
print('\n'.join(sorted_called_list))

#Part B
sum_count = sum(area_code_count.values())
if sum_count == 0:
	sum_count = 1
percent = area_code_count['080'] / sum_count * 100
percent = "%.2f%%"%percent

part_b_print_message = "{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore."

print('\nPart B')
print(part_b_print_message.format(percent))