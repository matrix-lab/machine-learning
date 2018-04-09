"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
import re

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
 - 移动电话没有括号，但数字中间添加了
   一个空格，以增加可读性。一个移动电话的移动前缀指的是他的前四个
   数字，并且以7,8或9开头。
 - 电话促销员的号码没有括号或空格 , 但以140开头。

输出信息:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
代号不能重复，每行打印一条，按字典顺序排序后输出。

第二部分: 由班加罗尔固话打往班加罗尔的电话所占比例是多少？
换句话说，所有由（080）开头的号码拨出的通话中，
打往由（080）开头的号码所占的比例是多少？

输出信息:
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
注意：百分比应包含2位小数。
"""


# 获取电话区号
def get_call_mobile_prefix(mobile):
    prefix_number = ''
    if mobile.find('(0') != -1:
        prefix_number = get_prefix_number(mobile)

    # 只获取固定电话
    else:
        if mobile.find(' ', 0, 5):
            # 移动号码
            prefix_number = mobile[0:4]
        # else:
        #     prefix_number = mobile[0:3]
    return prefix_number


def get_prefix_number(phone):
    search_obj = re.search(r'(0\d+)', phone, re.M | re.I).group()
    if search_obj:
        return search_obj

    return ''


# 获取被这个区号拨打的所有电话
def get_called_mobile_by_prefix_code(calls, code):
    prefixs = set();
    for call in calls:
        # 如果区号== 当前所查询区号，则进行归类
        if call[0][1:4] == code:
            prefixs.add(get_call_mobile_prefix(call[1]))
    return sorted(list(prefixs))


def sum_called_from_caller_mobile(calls, caller_code, called_code=None):
    """
    统计从一个区到另一个区的电话数量
    :param called_code:
    :param caller_code:
    :param calls:
    :return:
    """
    count = 0
    for call in calls:
        if (caller_code == get_call_mobile_prefix(call[0])) \
                and (called_code == None or called_code == get_call_mobile_prefix(call[1])):
            count += 1

    return count


prefixes = get_called_mobile_by_prefix_code(calls, '080')
# 统计输出
for prefix in prefixes:
    print('The numbers called by people in Bangalore have codes: < {} >'.format(prefix))

# 统计拨打电话数量
count_percent = round(
    (sum_called_from_caller_mobile(calls, '080', '080') / sum_called_from_caller_mobile(calls, '080') * 100), 2)
print("<{}> percent of calls from fixed lines in Bangalore are calls \
to other fixed lines in Bangalore.".format(count_percent))