#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unicodecsv
import pandas
# def read_csv(filename):
#     with open(filename, 'rb') as f:
#         reader = unicodecsv.DictReader(f)
#         return list(reader)
# daily_csv =read_csv('daily-engagement-full.csv')
#
# print(daily_csv)
#
# def get_unique_student(data):
#     unique_student = set()
#     for data_point in data:
#         unique_student.add(data_point['acct'])
#     return unique_student
# unique_csv_student =get_unique_student(daily_csv)
# print(len(unique_csv_student))

daily_csv = pandas.read_csv('daily-engagement-full.csv')
print(len(daily_csv['acct'].unique()))

