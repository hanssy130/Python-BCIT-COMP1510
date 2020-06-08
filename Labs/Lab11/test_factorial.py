from unittest import TestCase
from Lab11.functions import factorial


class TestFactorial(TestCase):
    def test_factorial_validtest(self):
        self.assertEqual(6, factorial(3))

    def test_factorial_type(self):
        self.assertEqual(int, type(factorial(3)))

    def test_factorial_zero(self):
        self.assertEqual(1, factorial(0))

    def test_factorial_one(self):
        self.assertEqual(1, factorial(1))