#!/usr/bin/python
# -*- coding: UTF-8 -*-


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

def cylinder_volume(height, radius):
    pi = 3.14159
    return height * pi * radius ** 2


cylinder_volume(10, 3)

mv_population = 74728
mv_area = 11.995
mv_density = mv_population/mv_area
print(mv_density)
print(.1)

a = [1, 5, 8]
b = [2, 6, 9, 10]
c = [100, 200]
print(len(b))
print(max([len(a), len(b), len(c)]))
print(min([len(a), len(b), len(c)]))

names = ["Carol", "Albert", "Ben", "Donna"]
print(" & ".join(sorted(names)))

fruit = {"apple", "banana", "orange", "grapefruit"}  # define a set

print("watermelon" in fruit)  # check for element

fruit.add("watermelon")  # add an element
print(fruit)

print(fruit.pop())  # remove a random element
print(fruit)

#元组是一种不可变有序元素数据类型
#集合是一个包含唯一元素的可变无序集合数据类型
#字典是可变数据类型，其中存储的是唯一键到值的映射


elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}}
print(elements['hydrogen']['is_noble_gas'])

print(elements['helium']['is_noble_gas'])