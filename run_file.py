from monster_class import *
from student_monster_class import *
from course_class import *

print('WELCOME TO MONSTERS UNIVERSITY')

# CREATE 2 STUDENTS
mike = StudentMonster('Mike', '666S', 'green', 25, ['small', 'smart'])
sully = StudentMonster('Sully', '456A', 'Blue', 23, ['huge', 'scary'])

# ADD SKILL
mike.add_skill('scary python')
sully.add_skill('milking goats')

# CREATE COURSE
course1 = Course('scaring 6 year olds', '02/06/2020')


# ENROLL STUDENTS
# first we need our course instance
# then we need to call a method add student and pass in the student
course1.add_student(mike)
course1.add_student(sully)
print(course1.get_students())
