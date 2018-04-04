d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59,
    'Paul': 75
}
d['aaaa'] = 72
d= {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
for key in d:
    print key + ':', d[key]

s = set(['A', 'B', 'C'])
print s
print 'A' in s

s = set([('Adam', 95), ('Lisa', 85), ('Bart', 59)])
for x in s:
    print x[0] + ':', x[1]


def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

print (my_abs(11))


def square_of_sum(L):
    sum = 0
    for x in L:
        sum = sum + x * x
    return sum
print square_of_sum([1, 2, 3, 4, 5])
print square_of_sum([-5, 0, 5, 15, 25])

import math
def quadratic_equation(a, b, c):
    t = math.sqrt(b * b - 4 * a * c)
    return (-b + t) / (2 * a),( -b - t )/ (2 * a)
print quadratic_equation(2, 3, 0)
print quadratic_equation(1, -6, 5)


def average(*args):
    sum = 0.0
    if len(args) == 0:
        return sum
    for x in args:
        sum = sum + x
    return sum / len(args)
print average()
print average(1, 2)
print average(1, 2, 2, 3, 4)