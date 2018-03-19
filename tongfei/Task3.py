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


prefix_num = []
count_from = 0
count_to = 0

for call in calls:
    if call[0][:5] == '(080)':
        # question 2  --start
        count_from += 1

        if call[1][:5] == '(080)':
            count_to += 1
        # question 2  --end
        number = call[1]
        fixed = ''

        if number.startswith('(0'):
            # 固定电话以括号内的区号开始。区号的长度不定，但总是以 0 打头。
            end_index = number.find(')')
            fixed = int(number[1:end_index])

        elif number[0] in ['7', '8', '9']:
            # 移动电话没有括号，但数字中间添加了 ' ' 并且以7,8或9开头
            fixed = int(number[:4])

        elif number[:3] == '140':
            fixed = 140

        if fixed and fixed not in prefix_num:
            prefix_num.append(fixed)


# question 2
message = '{:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.'
print(message.format(count_to * 100 / count_from))

# question 1
print('The numbers called by people in Bangalore have codes:')

for num in sorted(prefix_num):
    print(num)
