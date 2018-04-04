import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
任务2: 哪个电话号码的通话总时间最长? 不要忘记，用于接听电话的时间也是通话时间的一部分。
输出信息:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".

提示: 建立一个字典，并以电话号码为键，通话总时长为值。
这有利于你编写一个以键值对为输入，并修改字典的函数。
如果键已经存在于字典内，为键所对应的值加上对应数值；
如果键不存在于字典内，将此键加入字典，并将它的值设为给定值。
"""


all_call = {}
for call in calls:
    call_seconds = int(call[3])
    all_call[call[0]] = all_call.get(call[0], 0) + call_seconds
    all_call[call[1]] = all_call.get(call[1], 0) + call_seconds
# max(iterable, key, default)
max_call = max(all_call, key=all_call.get)

print(calls)
print(all_call)
print(max_call)

print('{} spent the longest time, {} seconds, on the phone duringSeptember 2016.'.format(max_call, all_call[max_call]))
