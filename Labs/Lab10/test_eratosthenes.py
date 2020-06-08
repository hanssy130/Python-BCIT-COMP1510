from unittest import TestCase
from A4.question1 import eratosthenes


class TestEratosthenes(TestCase):
    def test_eratosthenes_type(self):
        self.assertEqual(list, type(eratosthenes(30)))

    def test_eratosthenes_examplesolution(self):
        numlist = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        self.assertEqual(numlist, eratosthenes(30))

    def test_eratosthenes_smallnumber(self):
        numlist = [2, 3, 5, 7]
        self.assertEqual(numlist, eratosthenes(10))