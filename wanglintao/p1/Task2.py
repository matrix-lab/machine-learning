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

# print(calls[0])
temp_list = list()
phone_dict = dict()
for call in calls:
    if call[0] not in temp_list:
        #此处计算时长如不转成int型后边排序会有问题/汉
        phone_dict[call[0]] = int(call[3])
    else:
        phone_dict[call[0]] += int(call[3])
for call in calls:
    if call[1] not in temp_list:
        phone_dict[call[1]] = int(call[3])
    else:
        phone_dict[call[1]] += int(call[3])


# print(phone_dict)
# print(phone_dict.keys())
# test = {'Sex': 1, 'Sex': 3, 'Name': 2}
# print(list(test.values()))
print(max(phone_dict, key=phone_dict.get))
print(phone_dict[min(phone_dict, key=phone_dict.get)])
print({phone_dict[max(phone_dict, key=phone_dict.get)], max(phone_dict, key=phone_dict.get)})
# temp_value = 0
# values = list(phone_dict.values())
# print(values)
# values.sort()
# print(values)
# print(values)
# print(max(values))
# for value in values:
#     if values.count(value) >1:
#         temp_value += 1
# print(temp_value)
