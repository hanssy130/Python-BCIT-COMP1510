from unittest import TestCase
from unittest.mock import patch

from A3.mud import flee


class TestFlee(TestCase):
    @patch('random.randint', return_value=2)
    def test_flee_safeFlee(self, randint):
        self.assertEqual(0, flee())

    @patch('random.randint', return_value=1)
    def test_flee_getHurt(self, randint):
        self.assertEqual(1, flee())

    @patch('random.randint', return_value=1)
    def test_flee_assertType(self, randint):
        self.assertEqual(int, type(flee()))
