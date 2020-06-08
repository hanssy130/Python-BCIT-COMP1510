from unittest import TestCase
from A4.question1 import *


class TestEratosthenes(TestCase):
    def test_eratosthenes_validTest(self):
        self.assertEqual([2, 3, 5, 7], eratosthenes(10))

    def test_eratosthenes_typeTest(self):
        self.assertEqual(list, type(eratosthenes(10)))

    def test_eratosthenes_ErrorTest(self):
        self.assertRaises(ValueError, eratosthenes(-5))