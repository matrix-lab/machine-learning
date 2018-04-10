import random

def generate_password():
	word_list = []
	#读取文件里的单词
	with open('words.txt') as w:
		for line in w:
			word_list.append(line.strip())
	#打乱字符串
	random.shuffle(word_list) 
	return ''.join(word_list[:3])

print(generate_password())
	
	

	