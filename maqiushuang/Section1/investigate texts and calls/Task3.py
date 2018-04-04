import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
任务3:
(080)是班加罗尔的固定电话区号。
固定电话号码包含括号，
所以班加罗尔地区的电话号码的格式为(080)xxxxxxx。

第一部分: 找出被班加罗尔地区的固定电话所拨打的所有电话的区号和移动前缀（代号）。
 - 固定电话以括号内的区号开始。区号的长度不定，但总是以 0 打头。
 - 移动电话没有括号，但数字中间添加了一个空格，以增加可读性。
   一个移动电话的移动前缀指的是他的前四个数字，并且以7,8或9开头。
 - 电话促销员的号码没有括号或空格 , 但以140开头。

输出信息:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
代号不能重复，每行打印一条，按字典顺序排序后输出。

"""

prefix = ''
def get_phone_prefix(phone):
    """
        通过区号，获取被这个区号呼叫的电话前缀集合
        phone[0:2]前两位
        i = phone.index(')')  获取）所在下标
    """
    if phone[0:2] == '(0':
        i = phone.index(')')
        prefix = phone[0:i+1]
    else:
        prefix = phone[0:4]
    return prefix

# 获取被 (080) 这个区号呼叫的电话前缀集合
def get_phone_called(calls):
    """
       call[0][0:5]   呼出电话区号
    """
    prefixs = set()
    for call in calls:
        if call[0][0:5] == '(080)':
            prefixs.add(get_phone_prefix(call[1]))
    return sorted(prefixs)

called_prefixs = get_phone_called(calls)
for called in called_prefixs:
    print('<{}>'.format(called))

"""
第二部分: 由班加罗尔固话打往班加罗尔的电话所占比例是多少？
换句话说，所有由（080）开头的号码拨出的通话中，
打往由（080）开头的号码所占的比例是多少？

输出信息:
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
注意：百分比应包含2位小数。
"""
send = 0
receive = 0
for call in calls:
    if get_phone_prefix(call[0]) == '(080)':
        send += 1
    if get_phone_prefix(call[0]) == '(080)' and get_phone_prefix(call[1]) == '(080)':
        receive += 1

print(round(receive/send * 100, 2))










