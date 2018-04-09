how_many_snakes = 2
snake_string = """
Welcome to Python3!

             ____
            / . .\\
            \  ---<
             \  /
   __________/ /
-=:___________/

<3, Juno
"""
print(snake_string * how_many_snakes)

# name = input('Enter a name:')
# print('Hello',name.title())

stu_name = input('Enter a name:')
ass_num = int(input('Enter a number:'))
curr_grades = int(input('Enter a number:'))
poten_grades = curr_grades + ass_num*2
msg = """
Hi %s:

This is a reminder that you have %s assignments left to submit before you can graduate. Your current grade is %s and can increase to %s if you submit all assignments before the due date.
"""%(stu_name,ass_num,curr_grades,poten_grades)

print(msg)

names = input("Enter names separated by commas: ").title().split(",")
assignments = input("Enter assignment counts separated by commas: ").split(",")
grades = input("Enter grades separated by commas: ").split(",")

message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

for name, assignment, grade in zip(names, assignments, grades):
    print(message.format(name, assignment, grade, int(grade) + int(assignment)*2))