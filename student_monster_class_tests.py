import unittest
from student_monster_class import *


class StudentMonsterTest(unittest.TestCase):
    def setUp(self):
        self.student_monster = StudentMonster('Mike', '666S', 'green', 25, ['small', 'smart'])


if __name__ == '__main__':
    unittest.main()
