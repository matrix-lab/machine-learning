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


# 统计所有被叫电话
def get_called_numbers(calls):
    mobiles = set()
    for call in calls:
        mobiles.add(call[1])

    return mobiles


def get_text_mobile_numebers(texts):
    text_mobiles = set()
    for text in texts:
        text_mobiles.add(text[0])
        text_mobiles.add(text[1])
    return text_mobiles


def get_phone_mark_users(calls, texts):
    called_mobiles = get_called_numbers(calls)
    text_mobiles = get_text_mobile_numebers(texts)
    find_phones = set()
    for call in calls:
        if (call[0] not in called_mobiles) and (call[0] not in text_mobiles):
            find_phones.add(call[0])
    return sorted(list(find_phones))


find_numbers = get_phone_mark_users(calls, texts)
for phone in find_numbers:
    print("These numbers could be telemarketers: {}".format(phone))
