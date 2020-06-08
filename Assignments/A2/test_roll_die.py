from unittest import TestCase
from unittest.mock import patch

from A2.dungeonsanddragons import roll_die


class TestRoll_die(TestCase):
    @patch('random.randint', return_value=2)
    def test_roll_die_mock_roll(self, mock_roll):
        self.assertEqual(6, roll_die(3, 2))


    def test_roll_die_mock_zero(self):
        self.assertEqual(0, roll_die(0, 0))
