print("Hello Loop for while")


# for while study

def how_many_days(month_number):
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return days_in_months[month_number - 1]


print("当前月份有 {} 天".format(how_many_days(3)))

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December']
print(months[6:9])

eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']

# TODO: Modify this line so it prints the last three elements of the list
print(eclipse_dates[-3:])

# List 具有可变性质(mutability) 列表是可变的，字符串是不可改变的
# 不可变字符串对象保存在内存中， 可变对象保存在栈中

# max 函数不适用于包含不同且不可比较类型元素的列表：

# 连接符号 url 的拼接
url_param = '&'.join(['name=123', 'sex=man', 'mobile=15137159615'])

print(url_param)


def top_tree():
    numbers = [2, 4, 6, 3, 7, 8]
    return sorted(numbers)[-3:]


print(top_tree())


# print("前三名依次是:{}".format('、'.join(top_tree())))

def nearest_square(limit):
    i = 1
    while i ** 2 <= limit:
        i += 1

    return (i - 1) ** 2


print(nearest_square(37))
