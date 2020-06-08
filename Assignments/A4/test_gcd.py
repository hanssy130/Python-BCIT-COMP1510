from unittest import TestCase
from A4.question2 import gcd


class TestGcd(TestCase):
    def test_gcd_validTest(self):
        self.assertEqual(6, gcd(270, 192))

    def test_gcd_negativeTest(self):
        self.assertEqual(6, gcd(-18, 192))

    def test_gcd_zeroTest(self):
        self.assertEqual("You cannot divide by zero!", gcd(199, 0))