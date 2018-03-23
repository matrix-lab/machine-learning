print((23 + 32 + 64) / 3)

print((17*6) - (9*7 + 5*7))

print(14/2)

print(3/5)

print(6//5)

print(3 + 0.1 + 0.1 + 0.1)

# int整数  float浮点数
print(int(3 + 0.1 + 0.1 + 0.1))

print(float(6/2))

manila_pop = 120
print(manila_pop)

# 5e6 等于 5 * 10 ** 6（5乘以10的六次方）
print(5e6)

aa = 4.445e8
bb = 5e6
print(aa)
print(bb)

bb = bb*(1-0.1)
aa += bb
bb -= 5e5
print(aa)
print(bb)

manila_pop, manila_area = 1780148, 16.56
manila_pop_density = manila_pop/manila_area
print(int(manila_pop_density))
manila_pop = 1781573
manila_pop_density = manila_pop/manila_area
print(int(manila_pop_density))

# 比较运算符
sf_pop, sf_area = 864816, 231.89
rio_pop, rio_area = 6453682, 486.5
sf_density = sf_pop/sf_area
rio_density = rio_pop/rio_area
print(sf_density>rio_density)

ford = 'Whether you think you can, can\'t'
ford_quote = 'Whether you think you can, or you think you can\'t--you\'re right.'
print(ford)
print(ford_quote)

coconut_count = "34"
mango_count = "15"
tropical_fruit_count = coconut_count + mango_count
print(tropical_fruit_count)

username = 'MenyLi'
timestamp = '16:20'
url = 'http://www.baidu.com'
print(username + ' accessed the site ' + url + ' at ' + timestamp + '.')

# 内置函数 len()
given_name = "Charlotte"
middle_names = "Hippopotamus"
family_name = "Turner"
name_length = len(given_name + ' ' + middle_names+ ' '  + family_name)
print(name_length)
driving_licence_character_limit = 28
print(name_length <= driving_licence_character_limit)

# 类型： int整数    float浮点数   bool布尔    str字符串
# type()
# title()
print(type(835))
print(type(835.2))
print(type('aaa'))
print(type("hippo" *12))

house_number = 13
print(type(house_number))

# islower()
str = "charlotte hippopotamus turner".title()
print(str)
print('3.153islower'.islower())

# count()
prophecy = "And there shall in that time be rumours of things going astray"
vowel_count = 0
prophecy = prophecy.lower()
print(prophecy)
vowel_count = prophecy.count('a') + prophecy.count('e') + prophecy.count('i') + prophecy.count('o') + prophecy.count('u')
print(vowel_count)

print(prophecy.count('a', 4, 15))

# format()
log_message = 'IP address {} accessed {} at {}'.format('127.0.0.1', '/base/koala', '16:40')
print(log_message)

name = 'liuyun'
age = 24
sex = 'female'
alert = "Hello dear {} ,I know your age is {},your sex is {}.".format(name, age, sex)
print(alert)
