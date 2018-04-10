names 		= input("请输入学生的姓名列表：")
assignments = input("请输入学生的未交作业数量列表：")
grades   	= input("请输入学生的分数列表：")

names_list = names.title().split(',')
assignments_list = assignments.title().split(',')
grades_list = grades.title().split(',')

i = 0
student_num = len(names_list)
message = "Hi {},\n This is a reminder that you have {} assignments left to submit before you can graduate. Your current grade is {} and can increase to {} if you submit all assignments before the due date."
while (i < student_num):
	name 		= names_list[i]
	assignment 	= int(assignments_list[i])
	grade 		= int(grades_list[i])
	print(message.format(name,assignment,grade,2*assignment + grade))
	i += 1
	



