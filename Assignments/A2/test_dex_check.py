from unittest import TestCase
from unittest.mock import patch

from A2.dungeonsanddragons import dex_check


class TestDex_check(TestCase):
    @patch('A2.dungeonsanddragons.roll_die', return_value=10)
    def test_dex_check_hit(self, roll):
        Character = {'Dexterity': 5}
        self.assertEqual(1, dex_check(Character))


    @patch('A2.dungeonsanddragons.roll_die', return_value=1)
    def test_dex_check_miss(self, roll):
        Character = {'Dexterity': 5}
        self.assertEqual(0, dex_check(Character))


    @patch('A2.dungeonsanddragons.roll_die', return_value=1)
    def test_dex_check_miss(self, roll):
        Character = {'Dexterity': 5}
        self.assertEqual(int, type(dex_check(Character)))