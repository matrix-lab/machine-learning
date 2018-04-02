#!/usr/bin/python
# -*- coding: UTF-8 -*-

print ("hello,world")
print(45678+0x12fd2)

print("Learn Python")

print(0xff==255)
a = 'imooc'   # a变为字符串
print (a)
print u'中文'
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)

L = ['Adam', 'Lisa', 'Bart']
L.append('Paul')
print L
['Adam', 'Lisa', 'Bart', 'Paul']
t = ('Adam', 'Lisa', 'Bart')
age = 20
if age >= 18:
    print 'your age is', age
    print 'adult'
print 'END'

if age >= 18:
    print 'adult123'
elif age >= 6:
    print 'teenager'
elif age >= 3:
    print 'kid'
else:
    print 'baby'

    L = ['Adam', 'Lisa', 'Bart']
for name in L:
    print name