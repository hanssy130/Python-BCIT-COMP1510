from unittest import TestCase
from unittest.mock import patch

from A2.dungeonsanddragons import generate_syllable


class TestGenerate_syllable(TestCase):
    @patch("A2.dungeonsanddragons.generate_consonant", return_value="b")
    @patch("A2.dungeonsanddragons.generate_vowel", return_value="a")
    def test_generate_syllable_abtest(self, vowel, consonant):
        self.assertEqual("ba", generate_syllable())

    @patch("A2.dungeonsanddragons.generate_consonant", return_value="z")
    @patch("A2.dungeonsanddragons.generate_vowel", return_value="y")
    def test_generate_syllable_zytest(self, vowel, consonant):
        self.assertEqual("zy", generate_syllable())


    def test_generate_syllable_twochar(self):
        doublechar = generate_syllable()
        self.assertTrue(len(doublechar) == 2)


    def test_generate_syllable_str(self):
        value = generate_syllable()
        self.assertTrue(type(value) == str)