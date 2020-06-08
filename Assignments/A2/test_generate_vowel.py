from unittest import TestCase
from unittest.mock import patch

from A2.dungeonsanddragons import generate_vowel


class TestGenerate_vowel(TestCase):
    @patch('random.choice', return_value="e")
    def test_generate_vowel_etest(self, e):
        self.assertEqual("e", generate_vowel())


    @patch('random.choice', return_value="o")
    def test_generate_vowel_otest(self, o):
        self.assertEqual("o", generate_vowel())


    def test_generate_vowel_singlechar(self):
        singlechar = generate_vowel()
        self.assertTrue(len(singlechar) == 1)


    def test_generate_vowel_str(self):
        value = generate_vowel()
        self.assertTrue(type(value) == str)