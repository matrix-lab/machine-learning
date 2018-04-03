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
import Common

text_phones = list(set(Common.merge_lists(texts)))
called_phones = list(set(Common.merge_call_lists(calls, 'called')))
telemarketer_phons = list()
for call in calls:
    if Common.check_telemarketer_phone(call[0]) and call[0] not in called_phones and call[0] not in text_phones:
        if call[0] not in telemarketer_phons:
            telemarketer_phons.append(call[0])

return_str = '\n' +  '\n'.join(telemarketer_phons)
print("These numbers could be telemarketers:  %s" % return_str)
