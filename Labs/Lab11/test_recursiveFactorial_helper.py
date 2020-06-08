from unittest import TestCase
from Lab11.functions import recursiveFactorial_helper


class TestRecursiveFactorial_helper(TestCase):
    def test_recursiveFactorial_helper_validtest(self):
        self.assertEqual(6, recursiveFactorial_helper(3))

    def test_recursiveFactorial_helper_type(self):
        self.assertEqual(int, type(recursiveFactorial_helper(3)))

    def test_recursiveFactorial_helper_zero(self):
        self.assertEqual(1, recursiveFactorial_helper(0))

    def test_recursiveFactorial_helper_one(self):
        self.assertEqual(1, recursiveFactorial_helper(1))
