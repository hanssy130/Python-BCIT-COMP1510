from unittest import TestCase

from A2.dungeonsanddragons import first_strike


class TestFirst_strike(TestCase):
    def test_first_strike_type(self):
        self.assertEqual(list, type(first_strike()))


    def test_first_strike_size(self):
        self.assertEqual(2, len(first_strike()))


    def test_first_strike_integer1(self):
        self.assertEqual(int, type(first_strike()[0]))


    def test_first_strike_integer2(self):
        self.assertEqual(int, type(first_strike()[1]))