from unittest import TestCase
from unittest.mock import patch

from Lab05.functions import generate_consonant


class TestGenerate_consonant(TestCase):
    @patch('random.choice', return_value="z")
    def test_generate_consonant_ztest(self, z):
        self.assertEqual("z", generate_consonant())

    @patch('random.choice', return_value="a")
    def test_generate_consonant_atest(self, a):
        self.assertEqual("a", generate_consonant())


    def test_generate_consonant_singlechar(self):
        singlechar = generate_consonant()
        self.assertTrue(len(singlechar) == 1)


    def test_generate_consonant_str(self):
        value = generate_consonant()
        self.assertTrue(type(value) == str)