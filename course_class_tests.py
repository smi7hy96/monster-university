import unittest
from course_class import *


class CourseTest(unittest.TestCase):
    def setUp(self):
        self.course = Course('Scaring', ['Mike', 'Sully'], '20/08/2020')

    def test_add_student(self):
        self.assertEqual(self.course.add_student('randall'), 'Student added')

    def test_get_students(self):
        self.assertEqual(self.course.get_students(), 'Mike, Sully')


if __name__ == '__main__':
    unittest.main()
