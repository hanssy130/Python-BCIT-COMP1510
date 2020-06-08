from unittest import TestCase
from unittest.mock import patch
from A3.mud import get_user_choice


class TestGet_user_choice(TestCase):
    @patch('builtins.input', return_value="w")
    def test_get_user_choice_up(self, mock_input):
        self.assertEqual("w", get_user_choice())

    @patch('builtins.input', return_value="s")
    def test_get_user_choice_down(self, mock_input):
        self.assertEqual("s", get_user_choice())

    @patch('builtins.input', return_value="a")
    def test_get_user_choice_left(self, mock_input):
        self.assertEqual("a", get_user_choice())

    @patch('builtins.input', return_value="d")
    def test_get_user_choice_right(self, mock_input):
        self.assertEqual("d", get_user_choice())

    @patch('builtins.input', return_value="quit")
    def test_get_user_choice_quit(self, mock_input):
        self.assertEqual("quit", get_user_choice())

    @patch('builtins.input', return_value="quit")
    def test_get_user_assertType(self, mock_input):
        self.assertEqual(str, type(get_user_choice()))