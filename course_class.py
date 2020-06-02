from student_monster_class import *


class Course:

    def __init__(self, module_name, start_date, list_of_students=None):
        if list_of_students is None:
            list_of_students = []
        self.__module_name = module_name.title()
        self.list_of_students = list_of_students
        self.start_date = start_date

    def set_module_name(self, module_name):
        self.__module_name = module_name.title()

    def get_module_name(self):
        return self.__module_name

    def add_student(self, student):
        self.list_of_students.append(student)
        return 'Student Added'

    def get_students(self):
        return ', '.join(self.__get_names())

    def __get_names(self):
        all_students = []
        for student in self.list_of_students:
            all_students.append(student.get_name())

        return all_students

