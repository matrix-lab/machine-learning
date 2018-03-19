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
