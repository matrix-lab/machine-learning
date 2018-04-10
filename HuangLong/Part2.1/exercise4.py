def create_cast_list(file_name):
	cast_list = []
	with open(file_name) as f:
		for line in f:
			cast_list.append(line.split(',')[0])
	return cast_list

print(create_cast_list('flying_circus_cast.txt'))
			