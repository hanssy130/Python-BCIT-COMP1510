from unittest import TestCase
from unittest.mock import patch
from A3.mud import fight_or_flee


class TestFight_or_flee(TestCase):
    @patch('builtins.input', return_value="1")
    def test_fight_or_flee_validFight(self, mock_input):
        self.assertEqual("fight", fight_or_flee())

    @patch('builtins.input', return_value="2")
    def test_fight_or_flee_validFlee(self, mock_input):
        self.assertEqual("flee", fight_or_flee())

    @patch('builtins.input', return_value="quit")
    def test_fight_or_flee_validQuit(self, mock_input):
        self.assertEqual("quit", fight_or_flee())

    @patch('builtins.input', return_value="quit")
    def test_fight_or_flee_assertType(self, mock_input):
        self.assertEqual(str, type(fight_or_flee()))
