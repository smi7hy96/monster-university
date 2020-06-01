import unittest
from monster_class import *


class MonsterTest(unittest.TestCase):
    def setUp(self):
        self.monster = Monster('Mike', '666S', 'green')


if __name__ == '__main__':
    unittest.main()
