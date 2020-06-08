from unittest import TestCase
from unittest.mock import patch
from A3.mud import monster_roll


class TestMonster_roll(TestCase):
    @patch('random.randint', return_value=2)
    def test_monster_roll_false(self, randint):
        self.assertEqual(False, monster_roll())

    @patch('random.randint', return_value=1)
    def test_monster_roll_true(self, randint):
        self.assertEqual(True, monster_roll())

    @patch('random.randint', return_value=1)
    def test_monster_roll_type(self, randint):
        self.assertEqual(bool, type(monster_roll()))