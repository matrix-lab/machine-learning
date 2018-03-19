# if else


def which_prize(scores):
    message = "恭喜！您获得了 【{}】"
    if scores <= 50:
        return message.format('wooden')
    elif scores <= 150:
        return '亲爱的，本次没有中奖哦'
    return message


print(which_prize(80))
# boolean 类型获取
altitude = 1000
speed = 1000
prolulsion = "ProPeller"


# 计算圆柱面积


def cylinder_surface_area(radius, height, has_top_and_bottom):
    pi = 3.14
    side_area = 2 * pi * height * radius
    if has_top_and_bottom:
        top_area = pi * radius ** 2
        side_area += 2 * top_area
        return side_area
    else:
        return side_area


print(cylinder_surface_area(10, 5, True))

""" bool 中 if 条件真值
 数字 0 、 空对象 None 、 空字符串 '' 在bool 中都将返回false 

"""


## 计算分值


def which_prize(points):
    message = "您本次的获奖产品为 【{}】"
    prize = None
    if points <= 80:
        prize = message.format('礼品盒')
    elif 120 <= points <= 150:
        prize = message.format('iPad')
    elif points >= 180:
        prize = "战斗机"
    if prize:
        return "Congratulations ! you win the " + prize + "!"
    else:
        return prize


print(which_prize(135))