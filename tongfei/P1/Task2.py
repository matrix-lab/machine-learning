"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


call_dict = {}

for call in calls:
    call_time = int(call[3])

    if call_dict.get(call[0]):
        call_dict[call[0]] += call_time
    else:
        call_dict[call[0]] = call_time

    if call_dict.get(call[1]):
        call_dict[call[1]] += call_time
    else:
        call_dict[call[1]] = call_time


# call_dict = sorted(call_dict.items(), key=lambda x: x[1])
# max_time = call_dict[-1][1]
# number = call_dict[-1][0]

call_temp = zip(call_dict.values(), call_dict.keys())
max_call = sorted(call_temp)[-1]
max_time = max_call[0]
number = max_call[1]

# import operator
#
# call_temp = sorted(call_dict.items(), key=operator.itemgetter(1))
# max_call = call_temp[-1]
# max_time = max_call[1]
# number = max_call[0]

message = '<{}> spent the longest time, <{}> seconds, on the phone during September 2016.'
print(message.format(number, max_time))
