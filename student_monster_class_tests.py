import unittest
from student_monster_class import *


class StudentMonsterTest(unittest.TestCase):
    def setUp(self):
        self.student_monster = StudentMonster('Mike', '666S', 'green', 25, ['small', 'smart'])

    def test_add_skill(self):
        self.assertEqual(self.student_monster.add_skill('nimble'), 'Skill Added')

    def test_get_skills(self):
        self.assertEqual(self.student_monster.get_skills(), 'small, smart, ')
        self.student_monster.add_skill('nimble')
        self.assertEqual(self.student_monster.get_skills(), 'small, smart, nimble, ')


if __name__ == '__main__':
    unittest.main()
