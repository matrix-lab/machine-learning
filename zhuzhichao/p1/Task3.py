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


def get_telephone_prefix(telephone):
    """
    获取电话的前缀
    :param telephone:
    :return:
    """
    prefix = ''
    if telephone[0:2] == '(0':
        prefix = telephone[1:get_char_index_for_string(telephone, ')')]
    else:
        prefix = telephone[0:4]

    return prefix


def get_char_index_for_string(string, end_char):
    """
    获取某个字符在字符串中的位置
    :param string:
    :param end_char:
    :return:
    """
    end = None
    for _ in range(len(string)):
        if string[_ - 1] == end_char:
            end = _ - 1
            break
    return end


def get_called_telephone_prefixes_by_code(calls, code):
    """
    通过区号，获取被这个区号呼叫的电话前缀集合
    :param calls:
    :param code:
    :return:
    """
    prefixes = set()
    for call in calls:
        if call[0][0:5] == code:
            prefixes.add(get_telephone_prefix(call[1]))

    return sorted(list(prefixes))


def count_calls_by_caller_code_and_called_code(calls, caller_code, called_code=None):
    """
    统计从一个区号打到另外一个区号的电话数
    :param calls:
    :param caller_code:
    :param called_code:
    :return:
    """
    count = 0
    for call in calls:
        if get_telephone_prefix(call[0]) == caller_code \
                and (called_code is None or called_code == get_telephone_prefix(call[1])):
            count += 1

    return count


print("The numbers called by people in Bangalore have codes:")
called_prefixes = get_called_telephone_prefixes_by_code(calls, '(080)')
for called_prefix in called_prefixes:
    print('< {} >'.format(called_prefix))

percentage = round(count_calls_by_caller_code_and_called_code(calls, '080', '080')
                   / count_calls_by_caller_code_and_called_code(calls, '080') * 100, 2)
print(
    "{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(percentage))
