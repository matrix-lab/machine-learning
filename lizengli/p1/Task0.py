# -*- coding: utf-8 -*-
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    print("First record of texts, %s texts %s at time %s" %
          (texts[0][0], texts[0][1], texts[0][2]))

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    print(
        "Last record of calls, %s calls %s at time %s, lasting %s seconds" % (
            calls[-1][0], calls[-1][1], calls[-1][2], calls[-1][3]))
