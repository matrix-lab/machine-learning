"""
Intro to Python Project 1, Task 1

Complete each task in the file for that task. Submit the whole folder
as a zip file or GitHub repo. 
Full submission instructions are available on the Project Preparation page.
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
TASK 1: 
How many different telephone numbers are there in the records? 
Print a message: 
"There are <count> different telephone numbers in the records."
"""

text_send = [text[0] for text in texts]
text_receive = [text[1] for text in texts]

call_send = [call[0] for call in calls]
call_receive = [call[1] for call in calls]

dif_tel_num = set(text_send + text_receive + call_send + call_receive)

print("There are {} different telephone numbers in the records.".format(len(dif_tel_num)))
