def scores_to_rating(score1, score2, score3, score4, score5):
    rating = None
    """返回五个分数的平均值
    
    """
    # step 1 数值转化成可计算的值
    score1 = convert_to_numberic(score1)
    score2 = convert_to_numberic(score2)
    score3 = convert_to_numberic(score3)
    score4 = convert_to_numberic(score4)
    score5 = convert_to_numberic(score5)

    # setp 2 取平均值
    average_score = sum_of_middle_three(score1, score2, score3, score4, score5) / 3

    return score_to_rating_string(average_score)


def convert_to_numberic(score):
    """
    分值转化成数值
    :param score:
    :return:
    """
    return int(score)


def sum_of_middle_three(score1, score2, score3, score4, score5):
    return score1 + score2 + score3 + score4 + score5 \
           - min(score5, score4, score3, score2, score1) \
           - max(score1, score2, score3, score4, score5)


def score_to_rating_string(average_score):
    if 0 <= average_score < 1:
        return "Terrible"
    elif 1 <= average_score <= 2:
        return "Bad"
    elif 2 <= average_score <= 3:
        return "OK"
    elif 3 <= average_score <= 4:
        return "Good"
    elif 4 <= average_score <= 5:
        return "Excellent"
    else:
        return "Great"


print(scores_to_rating(10, 20, 26, 30, 10))
