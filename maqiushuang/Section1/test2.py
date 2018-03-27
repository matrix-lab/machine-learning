#!/usr/bin/python
# -*- coding: UTF-8 -*-

manila_pop = 15

manila_area = 3

manila_pop_density = manila_pop/manila_area

print(manila_pop_density)

#变量名中只能使用普通字母、数字和下划线，且以字母或下划线开头。
#变量命名有一些不能用于变量名的保留字
#虽然在变量名中使用任何内置的标识符不会立即导致错误，但我们也不建议使用

manila_pop +=3
manila_pop -= 2
manila_pop *= 0.9
manila_pop /=  2
print(manila_pop)

#此代码使用科学计数法定义大的数字。4.445e8 等于 4.445 * 10 ** 8，也等于 444500000.0。
a = 4.445e8
fall = 5e6
fall = fall*(1 - 0.1)
a += fall
a += a*0.05
a -= a*0.05
a -= 2.5e5
print(a)

savings, salary = 514.86, 320.51


manila_pop = 1780148
manila_area = 16.56
manila_pop_density = manila_pop/manila_area
print(int(manila_pop_density))