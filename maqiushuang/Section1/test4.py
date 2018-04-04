#!/usr/bin/python
# -*- coding: UTF-8 -*-


def cylinder_volume(height, radius):
    pi = 3.14159
    return height * pi * radius ** 2
print(cylinder_volume(10, 3))

def read_time(day):
    weeks = int(day/7)
    days = day%7
    return "{} week(s) and {} day(s)".format(int(weeks),days)
print(read_time(7))

def nice(girl):
    if girl == 'li':
        print('lili')
    elif girl == 'jingjing':
        print('jingjing')
    else:
        print("don't konw")
nice('lili')

errors = 3
if errors:
    print("There are " + str(errors) + " mistakes. Please correct.")
else:
    print("No mistakes here!")



# 第 1 步：convert_to_numeric
# 第 2、3 步：sum_of_middle_three
# 第 4 步：score_to_rating_string
def convert_to_numeric(score):
    return int(score)


def sum_of_middle_three(score1, score2, score3, score4, score5):
    return score1 + score2 + score3 + score4 + score5 -\
           max(score1, score2, score3, score4, score5) -\
           min(score1,score2,score3,score4,score5)

def score_to_rating_string(score):
    return score


def scores_to_rating(score1, score2, score3, score4, score5):
    """
    Turns five scores into a rating by averaging the
    middle three of the five scores and assigning this average
    to a written rating.
    """
    # STEP 1 convert scores to numbers
    score1 = convert_to_numeric(score1)
    score2 = convert_to_numeric(score2)
    score3 = convert_to_numeric(score3)
    score4 = convert_to_numeric(score4)
    score5 = convert_to_numeric(score5)

    # STEP 2 and STEP 3 find the average of the middle three scores
    average_score = sum_of_middle_three(score1, score2, score3, score4, score5) / 3

    # STEP 4 turn average score into a rating
    rating = score_to_rating_string(average_score)

    return rating

print(scores_to_rating(1, 2, 2, 4, 4))

# 变量作用域是指可以在程序的哪个部分引用或使用某个变量
# Python不允许函数修改不在函数作用域内的变量


numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]

def mean(num_list):
    return sum(num_list) / len(num_list)

averages = list(map(mean, numbers))
print(averages)

cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

def is_short(name):
    return len(name) < 10

short_cities = list(filter(is_short, cities))
print(short_cities)

# 迭代器是一种表示数据流的对象。这与列表不同，列表是可迭代对象，但不是迭代器，因为它不是数据流。
# 生成器是使用函数创建迭代器的简单方式。也可以使用类定义迭代。