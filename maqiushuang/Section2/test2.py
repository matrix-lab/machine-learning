#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unicodecsv
import pandas
import numpy
# # def read_csv(filename):
# #     with open(filename, 'rb') as f:
# #         reader = unicodecsv.DictReader(f)
# #         return list(reader)
# # daily_csv =read_csv('daily-engagement-full.csv')
# #
# # print(daily_csv)
# #
# # def get_unique_student(data):
# #     unique_student = set()
# #     for data_point in data:
# #         unique_student.add(data_point['acct'])
# #     return unique_student
# # unique_csv_student =get_unique_student(daily_csv)
# # print(len(unique_csv_student))
#
# daily_csv = pandas.read_csv('daily-engagement-full.csv')
# # print(len(daily_csv['acct'].unique()))
#
# countries = numpy.array([
#     'Afghanistan', 'Albania', 'Algeria', 'Angola', 'Argentina',
#     'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas',
#     'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium',
#     'Belize', 'Benin', 'Bhutan', 'Bolivia',
#     'Bosnia and Herzegovina'
# ])
# employment = numpy.array([
#     55.70000076,  51.40000153,  50.5       ,  75.69999695,
#     58.40000153,  40.09999847,  61.5       ,  57.09999847,
#     60.90000153,  66.59999847,  60.40000153,  68.09999847,
#     66.90000153,  53.40000153,  48.59999847,  56.79999924,
#     71.59999847,  58.40000153,  70.40000153,  41.20000076
# ])
# if False:
#     print (countries[0])
#     print (countries[3])
#
# # Slicing
# if False:
#     print (countries[0:3])
#     print (countries[:3])
#     print (countries[17:])
#     print (countries[:])
#
# #Element types
# if False:
#     print (countries.dtype)
#     print (employment.dtype)
#     print (numpy.array([0, 1, 2, 3]).dtype)
#     print (numpy.array([1.0, 1.5, 2.0, 2.5]).dtype)
#     print (numpy.array([True, False, True]).dtype)
#     print (numpy.array(['AL', 'AK', 'AZ', 'AR', 'CA']).dtype)
#
# # Looping
# if False:
#     for country in countries:
#         print ('Examining country {}'.format(country))
#
#     for i in range(len(countries)):
#         country = countries[i]
#         country_employment = employment[i]
#         print ('Country {} has employment {}'.format(country,
#                 country_employment))
#
#
# if False:
#     print (employment.mean()) #均值
#     print (employment.std()) #标准差
#     print (employment.max())
#     print (employment.sum())
#
# # numpy.argmax(a, axis=None, out=None)
# # 返回沿轴axis最大值的索引。 最大值的索引值
# def max_employment(countries, employment):
#     max_index 	= employment.argmax()
#     max_value 	= employment.max()
#     max_country = countries[max_index]
#
#     return (max_country, max_value,max_index)
#
# print(max_employment(countries, employment))
#
# female_completion = numpy.array([
#     97.35583, 104.62379, 103.02998, 95.14321, 103.69019,
#     98.49185, 100.88828, 95.43974, 92.11484, 91.54804,
#     95.98029, 98.22902, 96.12179, 119.28105, 97.84627,
#     29.07386, 38.41644, 90.70509, 51.7478, 95.45072
# ])
#
# # Male school completion rate in 2007 for those 20 countries
# male_completion = numpy.array([
#     95.47622, 100.66476, 99.7926, 91.48936, 103.22096,
#     97.80458, 103.81398, 88.11736, 93.55611, 87.76347,
#     102.45714, 98.73953, 92.22388, 115.3892, 98.70502,
#     37.00692, 45.39401, 91.22084, 62.42028, 90.66958
# ])
#
# def overall_completion_rate(female_completion, male_completion):
#     return (female_completion + male_completion) / 2.
# print(overall_completion_rate(female_completion, male_completion))
#
#
# def standardize_data(values):
#     print(values - values.mean())
#     return (values - values.mean()) / values.std()
# print(standardize_data(employment))

if False:
    a = numpy.array([1, 2, 3, 4])
    b = numpy.array([True, True, False, False])
    print(a[b])
    print(a[numpy.array([True, False, True, False])])

if False:
    a = numpy.array([1, 2, 3, 2, 1])
    b = (a >= 2)
    print(a[b])
    print(a[a >= 2])

if False:
    a = numpy.array([1, 2, 3, 4, 5])
    b = numpy.array([1, 2, 3, 2, 1])
    print(b == 2)
    print(a[b == 2])
    
def mean_time_for_paid_students(time_spent, days_to_cancel):
    return numpy.mean(time_spent[days_to_cancel >= 7])
time_spent = numpy.array([
    12.89697233, 0., 64.55043217, 0.,
    24.2315615, 39.991625, 0., 0.,
    147.20683783, 0., 0., 0.,
    45.18261617, 157.60454283, 133.2434615, 52.85000767,
    0., 54.9204785, 26.78142417, 0.
])

days_to_cancel = numpy.array([
    4, 5, 37, 3, 12, 4, 35, 38, 5, 37, 3, 3, 68,
    38, 98, 2, 249, 2, 127, 35
])

print(mean_time_for_paid_students(time_spent, days_to_cancel))
