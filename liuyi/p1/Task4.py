"""
Intro to Python Lab 1, Task 4

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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers: 
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message: 
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

text_sends = [text[0] for text in texts]
text_receives = [text[1] for text in texts]

call_sends = [call[0] for call in calls]
call_receives = [call[1] for call in calls]

all_call_expect_send = set(text_sends + text_receives + call_receives)

marketing_calls = []
for call_send in call_sends:
	if (call_send not in all_call_expect_send) and (call_send not in marketing_calls):
		marketing_calls.append(call_send)

print("These numbers could be telemarketers: ")
print('\n'.join(sorted(marketing_calls)))