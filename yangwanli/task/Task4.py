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
任务4:
电话公司希望辨认出可能正在用于进行电话推销的电话号码。
找出所有可能的电话推销员:
这样的电话总是向其他人拨出电话，
但从来不发短信、接收短信或是收到来电


请输出如下内容
"These numbers could be telemarketers: "
<list of numbers>
电话号码不能重复，每行打印一条，按字典顺序排序后输出。
"""
all_arr = []
call_arr = []
def all_calls_arr(lists,type):
    for list in lists:
        if type == 'call':
            all_arr.append(list[1])
        else:
            all_arr.append(list[0])
            all_arr.append(list[1])

all_calls_arr(calls,'call')
all_calls_arr(texts,'text')
set_arr = set(all_arr)
for call in calls:
    if call[0] not in set_arr and call[0] not in call_arr:
        call_arr.append(call[0])

call_str='These numbers could be telemarketers: '+'\n'
def print_result(dicts):
    str = '\n'.join(dicts)
    print(call_str + str)

print_result(call_arr)

