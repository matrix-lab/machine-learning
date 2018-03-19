# 测试内置函数
print(22)


def cylinder_volume(height, radius):
    pi = 3.14159
    return height * pi * radius ** 2


print(cylinder_volume(20, 10))


def print_greeting():
    print('Hello world')


print_greeting()


# 计算人口密度


def population_density(population, land_area=0):
    """用于计算人口密度的函数
    :param population:
    :param land_area:
    :return:
    """
    """
    :param population: 
    :param land_area: 
    :return: 
    """
    #  如果陆地面积小于0 ，则不用计算
    if land_area <= 0:
        return '当前无陆地面积，无法计算人口密度'
    return population / land_area;


density = population_density(1000)

print(density)
print(333)
