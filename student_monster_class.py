from monster_class import *


class StudentMonster(Monster):

    def __init__(self, name, tax_number, fur, student_no, skill_list):
        super().__init__(name, tax_number, fur)
        self.__student_no = student_no
        self.skill_list = skill_list

    def set_student_no(self, student_no):
        self.__student_no = student_no

    def get_student_no(self):
        return self.__student_no

    def add_skill(self, skill):
        self.skill_list.append(skill)
        return 'Skill Added'

    def get_skills(self):
        return ', '.join(self.skill_list)
