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

# 所有被叫电话
def get_phones(calls):
    phones = set()
    for call in calls:
        phones.add(call[1])
    return phones

# 所有接/收短信电话
def get_texts(texts):
    text_phones = set()
    for text in texts:
        text_phones.add(text[0])
        text_phones.add(text[1])
    return text_phones

called_phone = get_phones(calls)
text_phones = get_texts(texts)
tel_phones = set()
for call in calls:
    if call[0] not in called_phone and call[0] not in text_phones:
        tel_phones.add(call[0])
print('These numbers could be telemarketers: ')
for tel in sorted(list(tel_phones)):
    print('<{}>'.format(tel))

