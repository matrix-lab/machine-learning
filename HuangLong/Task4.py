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

# call_list 是拨出的手机号列表
# other_list 是收到来电、发送短信或接收短信的列表总和
call_list 	= []
other_list  = []

for call_phone in calls:
	call_list.append(call_phone[0])
	other_list.append(call_phone[1])
	
for text_phone in texts:
	other_list.append(text_phone[0])
	other_list.append(text_phone[1])	
	
# other_list 去重
other_all = set(other_list)

# 获取只有拨出电话的列表
only_call_list = {}
for call in call_list:
	if call not in other_all:
		only_call_list[call] = only_call_list.get(call,0) + 1

only_call_list_sort = sorted(only_call_list)

print("These numbers could be telemarketers: ")
for only_call in only_call_list_sort:
	print("<{}> the call times <{}>".format(only_call,only_call_list[only_call]))
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
