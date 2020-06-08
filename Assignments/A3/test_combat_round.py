from unittest import TestCase
from unittest.mock import patch
from A3.mud import combat_round


class TestCombat_round(TestCase):
    @patch('random.randint', return_value=1)
    def test_combat_round_GoFirstAndLive(self, randint):
        self.assertEqual(1, combat_round(5))

    @patch('random.randint', return_value=1)
    def test_combat_round_GoFirstAndDie(self, randint):
        self.assertEqual(0, combat_round(3))

    @patch('random.randint', return_value=2)
    def test_combat_round_GoSecondAndLive(self, randint):
        self.assertEqual(4, combat_round(10))

    @patch('random.randint', return_value=2)
    def test_combat_round_GoSecondAndDie(self, randint):
        self.assertEqual(-1, combat_round(3))

    @patch('random.randint', return_value=1)
    def test_combat_round_assertType(self, randint):
        self.assertEqual(int, type(combat_round(5)))
