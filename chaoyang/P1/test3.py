"""
字典 in 检查列表或集合中是否存在  get() 取值
"""
elements = {'Shanghai': 17.8, 'Istanbul': 13.3, 'Karachi': 13.0, 'Mumbai': 12.5}

if 'Zhengzhou'  in elements:
	print('Yes')
else:
	print('No')
	

print(elements.get('Zhengzhou'))

print(elements.get('Zhengzhou','Home'))


monthly_takings = {'January': [54, 63], 'February': [64, 60], 'March': [63, 49],
                   'April': [57, 42], 'May': [55, 37], 'June': [34, 32],
                   'July': [69, 41, 32], 'August': [40, 61, 40], 'September': [51, 62],
                   'October': [34, 58, 45], 'November': [67, 44], 'December': [41, 58]}
def total_takings(monthly_takings):
    total_money = 0
    for months in monthly_takings:
        for item in monthly_takings[months]:
            total_money += item

    return total_money
	

"""
zip 返回一个将多个可迭代对象组合成一个元组序列的迭代器。每个元组都包含所有可迭代对象中该位置的元素
"""
letters = ['a', 'b', 'c']
nums = [1, 2, 3]

for letter, num in zip(letters, nums):
    print("{}: {}".format(letter, num))
	
	
"""
enumerate 是一个会返回元组迭代器的内置函数，这些元组包含列表的索引和值。当你需要在循环中获取可迭代对象的每个元素及其索引时，将经常用到该函数
"""	
letters = ['a', 'b', 'c', 'd', 'e']
for i, letter in enumerate(letters):
    print(i, letter)


"""
列表推导式
"""
#squares = [x**2 for x in range(9) if x % 2 == 0]
squares = [x**2 if x % 2 == 0 else x + 3 for x in range(9)]

print(squares)	