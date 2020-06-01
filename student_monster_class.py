from monster_class import *


class StudentMonster(Monster):

    def __init__(self, name, tax_number, fur, student_no, skill_list):
        super().__init__(name, tax_number, fur)
        self.student_no = student_no
        self.skill_list = skill_list
