import os

# divide.py
div_result = int(input()) / int(input())

file = open('division_result.txt', 'w', encoding='utf-8')
file.write(str(div_result))
file.close()

print('The current working directory is', os.getcwd())
# The current working directory is /home/user/PycharmProjects/project

os.chdir('/home/user')
print('The current working directory is', os.getcwd())
# The current working directory is /home/user

# Creating Directory
os.mkdir('some_new_project')
os.makedirs('course/students/year')

print(os.listdir('course'))
# ['student_list.txt', 'students', 'course_plan.txt']

os.rename('course/student_list.txt', 'course/list_of_students.txt')
