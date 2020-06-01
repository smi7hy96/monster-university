import unittest
from course_class import *
from student_monster_class import *


class CourseTest(unittest.TestCase):

    def setUp(self):
        mike = StudentMonster('Mike', '666S', 'green', 25, ['small', 'smart'])
        sully = StudentMonster('Sully', '456A', 'Blue', 23, ['huge', 'scary'])
        self.course = Course('Scaring', [mike, sully], '20/08/2020')

    def test_add_student(self):
        randall = StudentMonster('Randall', '123C', 'Purple', 24, ['sneaky', 'chameleon skin'])
        self.assertEqual(self.course.add_student(randall), 'Student Added')

    def test_get_students(self):
        self.assertEqual(self.course.get_students(), 'Mike, Sully, ')
        randall = StudentMonster('Randall', '123C', 'Purple', 24, ['sneaky', 'chameleon skin'])
        self.course.add_student(randall)
        self.assertEqual(self.course.get_students(), 'Mike, Sully, Randall, ')


if __name__ == '__main__':
    unittest.main()
