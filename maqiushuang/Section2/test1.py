#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math
import random
from datetime import datetime
import pytz

how_many_snakes = 2
snake_string = """
Welcome to Python3!

             ____
            / . .\\
            \  ---<
             \  /
   __________/ /
-=:___________/

<3, Juno
"""
print(snake_string * how_many_snakes)

# lili,see,mem
# 1,1,3
# 80,60,70
# names = input("Enter names separated by commas:").title().split(",")
#
# assignments = input("Enter assignment counts separated by commas:").split(",")
# grades = input("Enter grades separated by commas:").split(",")
# message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
# submit before you can graduate. You're current grade is {} and can increase \
# to {} if you submit all assignments before the due date.\n\n"
#
# for name, assignment, grade in zip(names, assignments, grades):
#     print(message.format(name, assignment, grade, int(grade) + int(assignment)*2))

#ValueError        向内置操作或函数中传入类型正确但是值不合适的对象作为输入。
#AssertionError    断言语句失败了。
#IndexError       序列下标超出了范围。
#KeyError         在字典中找不到某个键。
#TypeError       向操作或函数中传入类型不受支持的对象作为输入。
#UnboundLocalError 错误名称 local variable 是没有引用具体代码


def create_groups(items, num_groups):
    try:
        size = len(items) // num_groups
    except ZeroDivisionError:
        print("WARNING: Returning empty list. Please use a nonzero number.")
        return []
    else:
        groups = []
        for i in range(0, len(items), size):
            groups.append(items[i:i + size])
        return groups
    finally:
        print("{} groups returned.".format(num_groups))

print("Creating 6 groups...")
for group in create_groups(range(32), 6):
    print(list(group))

print("\nCreating 0 groups...")
for group in create_groups(range(32), 0):
    print(list(group))


print ('\n'.join(['\t'.join(['%d * %d = %d'%(y,x,x*y) for y in range(1,x+1)])for x in range(1,10)]))

#读取文件下一行  readline()

def create_cast_list(filename):
    cast_list = []
    with open(filename) as f:
        for line in f:
            line_data = line.split(',')
            cast_list.append(line_data[0])
    return cast_list
cast_list = create_cast_list('flying_circus_cast.txt')
for actor in cast_list:
    print(actor)

print (math.exp(3))

#strip()  移除字符串头尾指定的字符（默认为空格）
#lower() 方法转换字符串中所有大写字符为小写
word_list = []
with open('words.txt','r') as words:
    for line in words:
        word = line.strip().lower()
        if 3 < len(word) < 8:
            word_list.append(word)

# def generate_password(word_list):
#     password = ''
#     i = 0
#     while i < 3:
#         random_word = word_list[random.randint(0, len(word_list))]
#         password += random_word
#         i += 1
#     return password
# print(generate_password(word_list))


#choice() 方法返回一个列表，元组或字符串的随机项
def generate_password(word_list):
    return random.choice(word_list) + random.choice(word_list) + random.choice(word_list)

print(generate_password(word_list))

#sample 不重复抽样
#randrange 从范围中选择的随机整数
#random.randint(a,b)函数返回数字 N ，N 为 a 到 b 之间的数字（a <= N <= b），包含 a 和 b
print(random.randrange(6))

def generate_password(word_list):
    return ''.join(random.sample(word_list,3))
print(generate_password(word_list))


utc = pytz.utc
ist = pytz.timezone('Asia/Kolkata')

now = datetime.now(tz=utc)
ist_now = now.astimezone(ist)
print(now)
print(ist_now)