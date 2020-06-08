from unittest import TestCase
from unittest.mock import patch

from A2.dungeonsanddragons import generate_name


@patch("A2.dungeonsanddragons.generate_syllable", return_value="ba")
class TestGenerate_name(TestCase):
    def test_generate_name_1syllable(self, mock_input):
        self.assertEqual("Ba", generate_name(1))


    def test_generate_name_3syllables(self, mock_input):
        self.assertEqual("Bababa", generate_name(3))


    def test_generate_name_type(self, mock_input):
        self.assertEqual(str, type(generate_name(15)))


    def test_generate_name_capitalized(self, mock_input):
        string = list(generate_name(4))
        self.assertTrue(string[0].isupper())

