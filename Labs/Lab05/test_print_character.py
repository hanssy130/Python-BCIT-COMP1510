import unittest
from unittest import TestCase
from unittest.mock import patch
from Lab05.functions import print_character


import io

class TestPrint_character(TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character_bobo(self, mock_stdout):
        character = ["Bobo", ["Strength", 3], ["Dexterity", 10], ["Constitution", 8], ["Intelligence", 15], ["Wisdom", 8], [
            "Charisma", 9]]
        print_character(character)
        self.assertEqual("Adventurer: Bobo\nStrength: 3\nDexterity: 10\nConstitution: 8\nIntelligence: 15\nWisdom: 8\nCharisma: 9\n", mock_stdout.getvalue())
