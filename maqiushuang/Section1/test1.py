#!/usr/bin/python
# -*- coding: UTF-8 -*-

print ("你好，世界")


print(4+5)
print(1 + 2*3)
print(2**3)


print( 9*7 + 5*7 )
print( (17*6) - (9*7 + 5*7) )

print((3 + 32) - 15//2)

print((1 + 2 + 4)/13)

# " // "来表示整数除法，返回不大于结果的一个最大的整数，而" / " 则单纯的表示浮点数除法

print(15//2)

# floating-point number
print(3/4)

print(3 + 2.5)

print(16/4)
print(16//4)

print(int(49.9))

print(float(3278+273827))

print(0.2)

print(0.2 + 0.2 + 0.2)

# Traceback（回溯）表示“程序出错而停止时正在执行的内容”！
#print(4/0)
manila_pop = 15

manila_area = 3

manila_pop_density = manila_pop/manila_area

print(manila_pop_density)

#变量名中只能使用普通字母、数字和下划线，且以字母或下划线开头。
#变量命名有一些不能用于变量名的保留字
#虽然在变量名中使用任何内置的标识符不会立即导致错误，但我们也不建议使用

manila_pop +=3
manila_pop -= 2
manila_pop *= 0.9
manila_pop /=  2
print(manila_pop)

#此代码使用科学计数法定义大的数字。4.445e8 等于 4.445 * 10 ** 8，也等于 444500000.0。
a = 4.445e8
fall = 5e6
fall = fall*(1 - 0.1)
a += fall
a += a*0.05
a -= a*0.05
a -= 2.5e5
print(a)

savings, salary = 514.86, 320.51


manila_pop = 1780148
manila_area = 16.56
manila_pop_density = manila_pop/manila_area
print(int(manila_pop_density))

rainfall = 5

# decrease the rainfall variable by 10% to account for runoff
rainfall *= .9

print(rainfall)

print(1 < 2)

str_1 = 'qbc'
str_2 = 'ABLVG'

print(str_1 + str_2)

salesman = '"I think you\'re an encyclopaedia salesman"'
print(salesman)

ai_length = len("dflkjdlkfjdljf");
print(ai_length)
print(type(6))
print(type('6'))
print(type(6.56))
count = int(4.0)
print(count)
print(type(count))

mon_sales = "121"
tues_sales = "105"
wed_sales = "110"
thurs_sales = "98"
fri_sales = "95"

total_sales = int(mon_sales) + int(tues_sales) + int(wed_sales) + int(thurs_sales) + int(fri_sales)

str_total_sales = str(total_sales)

print("This week's total sales: " + str_total_sales)
#title 方法。该方法返回首字母大写的字符串，即每个单词的第一个字母都被大写。
print("charlotte hippopotamus turner".title())
#islower 返回一个布尔值，说明该字符串对象中的字母是否都是小写字母（不区分大小写的字符不计算在内，比如标点符号）。
print("charlotte hippopotamus turner".islower())
num = 'ad '.islower()
print(num)

prophecy = "And"

vowel_count = 0

prophecy = prophecy.lower()

print(prophecy)

vowel_count = prophecy.count('a') + prophecy.count('e') + prophecy.count('i') + prophecy.count('o') + prophecy.count('u')

# Print the final count
print(vowel_count)

user_ip = '208.94.117.90'
url = 'classroom.udacity.com'
now = '16:04'
log_message = "IP address {} accessed {} at {}".format(user_ip, url, now)

print(log_message)

name = 'li'
age = 24
sex = 'female'

alert = "Hello dear {} ,I know your age is {},your sex is {}.".format(name, age, sex)
print(alert)

mon_sales = "121"
tues_sales = "105"
wed_sales = "110"
thurs_sales = "98"
fri_sales = "95"
total_sales = int(mon_sales) + int(tues_sales) + int(wed_sales) + int(thurs_sales) + int(fri_sales)

str_total_sales = str(total_sales)

print("This week's total sales: " + str_total_sales)

#python 保留字
import keyword
print(keyword.kwlist)
if True:
    print('true')
else:
    print('false')

print('hello\nrunoob')
print(r'hello\nrunoob')

#print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""：
print(3**2)