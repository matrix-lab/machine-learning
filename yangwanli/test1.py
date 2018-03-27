#函数定义:关键字 def，参数后为冒号，使用四个空格缩进函数体

def show():
    print('Hello world!')

show()

def cylinder_volume(height,radius):
    pi=3.14159
    return pi*radius**2*height

print(cylinder_volume(10,3))

#注意缩进：四个空格或者四个空格的倍数

#文档字符串Docstings
def population_density(population, land_area):
    """Calculate the population density of an area.
    population: int. The population of the area
    land_area: int or float. This function is unit-agnostic, if you pass
               in values in terms of square km or square miles the
               function will return a density in those units.
    """
    return population / land_area


#练习：接收一个整数型变量，返回一个字符串，判断是几星期几天
def readable_timedelta(day):
    weeks=day//7
    days=day%7
    return "{} week(s) and {} day(s)".format(weeks,days)

print(readable_timedelta(3))

#练习：获得哪种奖项
def which_price(point):
    point=int(point)
    msg = "Congratulations!You have won a {}!"
    if point <= 50:
        return msg.format('wooden rabbit')
    elif point <= 150:
        return 'Oh dear,no price this time!'
    elif point <= 180:
        return msg.format('wafer-thin min')
    else:
        return msg.format('penguin')

print(which_price(57))
print(which_price(250))
#改进：
def which_prize2(points):
    """
    Returns the number of prize-winning message, given a number of points
    """
    prize = None
    if points <= 50:
        prize = "a wooden rabbit"
    elif 151 <= points <= 180:
        prize = "a wafer-thin mint"
    elif points >= 181:
        prize = "a penguin"
    if prize:
        return "Congratulations! You have won " + prize + "!"
    else:
        return "Oh dear, no prize this time."

#布尔运算关键式：not and or

test_num1,test_num2=7,8
print(test_num1<10 and test_num2<8) #False
print(test_num1<10 or test_num2<8)#true
print(not test_num1<10 or test_num2<8)#False
print(not test_num1<10)#False

#列表
python_versions = [1.0, 1.5, 1.6, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6]
print(type(python_versions)) #<class 'list'>,list也是一种类型

#列表长度
print(len(python_versions))

#列表切片
print(python_versions[6:9]) #[startIndex,endIndex]，值从python_versions[startIndex]开始，# 取到python_versions[endIndex-1]

#列表切片简化方式
print(python_versions[6:]) #[startIndex:]，值从python_versions[startIndex]开始，取到列表结尾
print(python_versions[:6]) #[:endIndex]，值从python_versions[0]开始，取到python_versions[endIndex-1]

#列表、字符串：都支持len()、切片以及in,就可变性（对象是否可以修改）而言，列表是可变的，字符串是不可变的
str = 'women me mine'
arr = ['women','me','mine']
print('me' in str)
print('me' in arr)

#列表函数
#len(list):返回列表元素个数
#max(list):返回列表中的最大元素。最大元素的确定取决于列表中的对象类型,数字列表中返回最大数字，字符串列表返回字母顺序最后的元素。
           #不适用于包含不同且不可比较类型元素的列表
#min(list)
#sorted(list)
#join
#append