# with  自动关闭文件手柄
# with open('countries.py','r') as f:
#     file_data = f.read()
#
# print(file_data[3])
# print(file_data.read(3))
# print(file_data)


# camelot_lines = []
# with open('camelot.py') as f:
    # file_data = f.read()
    # for line in f:
    #     camelot_lines.append(line.strip())

# print(file_data)
# print(camelot_lines)

# with open('actor.py') as f:
#     file_data = f.read()
# print(file_data)

# 获取演员列表
# def create_actor_list(file_name):
#     actor_list = []
#     with open(file_name) as f:
#         for line in f:
#             print(line[0:line.find('a')])
            # print(line[0:line.find(line.find(','))])
            # actor_list.append(get_name_from_line(line.strip()))
    # return actor_list

# def get_name_from_line(line):
#     return line[0:line.find(',')]
# print(create_actor_list('actor.py'))
# create_actor_list('actor.py')



def create_cast_list(file_name):
    cast_list = [];
    with open(file_name) as f:
        for line in f:
            line_data = line.split(',')
            cast_list.append(line_data[0])
    return cast_list


# create_cast_list('actor.py')
# print(create_cast_list('actor.py'))





