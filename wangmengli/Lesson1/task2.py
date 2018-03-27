# 定义函数
def cylinder_volume(height, radius):
    pi = 3.14159
    return height * pi * radius ** 2
volume = cylinder_volume(10, 3)
print(volume)

def population_density(population, land_area):
    '''
    :param population: int
    :param land_area: int or float
    :return:
    '''
    return population/land_area
test1 = population_density(10, 1)
expected_result1 = 10
print("expected result: {}, actual result: {}".format(expected_result1, test1))
test2 = population_density(864816, 121.4)
expected_result2 = 7123.6902801
print("expected result: {}..., actual result: {}".format(expected_result2, test2))

return_value = print("I wish to register a complaint.")
print(return_value)

def readable_timedelta(day):
    '''
    :param day: 传入的天数
    :return: 表示传入的天数有几星期零几天
    '''
    weeks = int(day/7)
    days = day%7
    return '{} week(s) and {} day(s)'.format(weeks, days)
print(readable_timedelta(15))
print(readable_timedelta(2))

# if    elif    else
number = 10
if number%2 == 0:
    print('The number ' + str(number) + ' is even.')
else:
    print('The number ' + str(number) + ' is odd.')

def which_prize(point):
    '''
    :param point:  积分
    '''
    point = int(point)
    msg = "Congratulations! You have won a {}!"
    if 0 < point <= 50:
        return msg.format('wooden rabbit')
    elif 51 < point <= 150:
        return msg.format('Oh dear, no prize this time')
    elif 151 <= point <= 180:
        return msg.format('wafer-thin mint')
    elif 181 <= point <= 200:
        return msg.format('penguin')
    else:
        return 'Oh dear, no prize this time.'
print(which_prize(95))

altitude = 10000
speed = 250
propulsion = "Propeller"
print(altitude < 1000 and speed > 100)
print((propulsion == "Jet" or propulsion == "Turboprop") and speed < 300 and altitude > 20000)
print(not (speed > 400 and propulsion == "Propeller"))


def which_prize(prize=None):
    message = "亲，您本次中奖的产品 为 【{}】"
    if prize == None:
        return "您未中奖"
    else:
        return message.format('电磁炉')
print(which_prize('11'))

def convert_to_numeric(score):
    return int(score)
def sum_of_middle_three(scores1, scores2, scores3, scores4, scores5):
    return scores1 + scores2 + scores3 + scores4 + scores5 - min(scores1, scores2, scores3, scores4, scores5) - max(scores1, scores2, scores3, scores4, scores5)
def score_to_rating_string(av_score):
    if av_score < 1:
        rating = 'Terrible'
    elif av_score < 2:
        rating = "Bad"
    elif av_score < 3:
        rating = "OK"
    elif av_score < 4:
        rating = "Good"
    else:
        rating = "Excellent"
    return rating
def scores_to_rating(scores1, scores2, scores3, scores4, scores5):
    '''
        取出3个平均值
    '''
    scores1 = convert_to_numeric(scores1)
    scores2 = convert_to_numeric(scores2)
    scores3 = convert_to_numeric(scores3)
    scores4 = convert_to_numeric(scores4)
    scores5 = convert_to_numeric(scores5)

    average_score = sum_of_middle_three(scores1, scores2, scores3, scores4, scores5)/3
    rating = score_to_rating_string(average_score)
    return rating
print(scores_to_rating(5, 9, 2, 3, 4))





