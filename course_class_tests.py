import unittest
from course_class import *


class CourseTest(unittest.TestCase):
    def setUp(self):
        self.course = Course('Scaring', ['Mike', 'Sully'], '20/08/2020')


if __name__ == '__main__':
    unittest.main()
