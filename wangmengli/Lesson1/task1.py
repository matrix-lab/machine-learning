print((23 + 32 + 64) / 3)

print((17*6) - (9*7 + 5*7))

print(14/2)

print(3/5)

print(6//5)

print(3 + 0.1 + 0.1 + 0.1)

# int整数  float浮点数
print(int(3 + 0.1 + 0.1 + 0.1))

print(float(6/2))

manila_pop = 120
print(manila_pop)

# 5e6 等于 5 * 10 ** 6（5乘以10的六次方）
print(5e6)

aa = 4.445e8
bb = 5e6
print(aa)
print(bb)

bb = bb*(1-0.1)
aa += bb
bb -= 5e5
print(aa)
print(bb)

manila_pop, manila_area = 1780148, 16.56
manila_pop_density = manila_pop/manila_area
print(int(manila_pop_density))
manila_pop = 1781573
manila_pop_density = manila_pop/manila_area
print(int(manila_pop_density))