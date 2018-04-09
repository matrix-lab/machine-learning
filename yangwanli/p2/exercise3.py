def create_cast_list(filename):
    cast_list = []
    with open(filename) as f:
        for line in f:
            line_data = line.split(',')
            cast_list.append(line_data[0])
    return cast_list

cast_list = create_cast_list('flying_circus_cast.txt')
for actor in cast_list:
    print(actor)