from unittest import TestCase
from unittest.mock import patch
from A2.dungeonsanddragons import select_race


class TestSelect_race(TestCase):
    @patch('builtins.input', return_value="Dragonborn")
    def test_select_race_goodtest(self, mock_input):
        self.assertEqual("Dragonborn", select_race())

    @patch('builtins.input', return_value="Dragonborn")
    def test_select_race_typetest(self, mock_input):
        self.assertTrue(type(select_race()) == str)

    @patch('builtins.input', side_effect=["oh no", "yeet", "asdf", "Dragonborn"])
    def test_select_race_multiplemistakes(self, mock_input):
        self.assertEqual("Dragonborn", select_race())

    @patch('builtins.input', side_effect=["oh no", "Dragonborn"])
    def test_select_race_onemistake(self, mock_input):
        self.assertEqual("Dragonborn", select_race())
