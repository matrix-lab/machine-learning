# -*- coding: utf-8 -*-

import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)


with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

# list 是一种有序的集合，支持添加和删除元素，类似php中的索引数组。
# len() 函数可以获得集合中元素个数，类似php中的count()函数
# 索引越界会抛出IndexError的错误，想要获取最后一个元素的索引是len(classmates) - 1。

# -1做索引，直接获取最后一个元素，-2 ...

# format() 是一种格式化字符串的方法，参数会填充占位符位置的内容


def get_first_record_of_texts(texts):

    first_text = texts[0]

    return "First record of texts, {} texts {} at time {}".format(first_text[0],first_text[1],first_text[2])


print(get_first_record_of_texts(texts))


def get_last_record_of_calls(calls):

    last_text = calls[-1]

    return "Last record of calls, {} calls {} at time {}, lasting {} seconds".format(last_text[0],last_text[1],last_text[2],last_text[3])


print(get_last_record_of_calls(calls))


