#   -*- coding: UTF-8 -*-
from countries import country_list
country_counts = {}
for country in country_list:
    country_counts[country] = country_counts.get(country, 0) + 1

print(country_counts)


def total_takings(monthly_takings):
    list = []
    for taking in monthly_takings:
        for item in monthly_takings[taking]:
            list.append(item)

    return sum(list)


monthly_takings = {'January': [54, 63], 'February': [64, 60], 'March': [63, 49],
                   'April': [57, 42], 'May': [55, 37], 'June': [34, 32],
                   'July': [69, 41, 32], 'August': [40, 61, 40], 'September': [51, 62],
                   'October': [34, 58, 45], 'November': [67, 44], 'December': [41, 58]}

print(total_takings(monthly_takings))

print('你好世界')

import sys; x = 'runoob'; sys.stdout.write(x + '\n')
