from unittest import TestCase

from A3.mud import heal_char


class TestHeal_char(TestCase):
    def test_heal_char_validtest(self):
        self.assertEqual(7, heal_char(5))

    def test_heal_char_zero(self):
        self.assertEqual(2, heal_char(0))

    def test_heal_char_overTen(self):
        self.assertEqual(10, heal_char(9))

    def test_heal_char_type(self):
        self.assertEqual(int, type(heal_char(9)))
