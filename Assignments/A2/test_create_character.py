from unittest import TestCase
from unittest.mock import patch

from A2.dungeonsanddragons import create_character

class TestCreate_character(TestCase):
    @patch("A2.dungeonsanddragons.generate_name", return_value="Gyga")
    @patch('A2.dungeonsanddragons.roll_die', return_value=10)
    @patch('builtins.input', side_effect=["Elf", "Bard"])
    def test_create_character_validtest(self, raceclass, die, name):
        character = {'Name': 'Gyga', 'Race': 'Elf', 'Class': 'Bard', 'HP': [10, 10], 'Strength': 10, 'Dexterity': 10, 'Constitution': 10, 'Intelligence': 10, 'Wisdom': 10, 'Charisma': 10, 'XP': 0}
        self.assertEqual(character, create_character(2))

    @patch("A2.dungeonsanddragons.generate_name", return_value="Gyga")
    @patch('A2.dungeonsanddragons.roll_die', return_value=10)
    @patch('builtins.input', side_effect=["Elf", "Bard"])
    def test_create_character_type(self, raceclass, die, name):
        character = {'Name': 'Gyga', 'Race': 'Elf', 'Class': 'Bard', 'HP': [10, 10], 'Strength': 10, 'Dexterity': 10, 'Constitution': 10, 'Intelligence': 10, 'Wisdom': 10, 'Charisma': 10, 'XP': 0}
        self.assertEqual(dict, type(create_character(2)))

    @patch('builtins.input', side_effect=["Elf", "Bard"])
    def test_create_character_size(self, raceclass):
        character = create_character(5)
        self.assertEqual(10, len(character["Name"]))


    @patch('builtins.input', side_effect=["Elf", "Bard"])
    def test_create_character_size(self, raceclass):
        character = create_character(5)
        self.assertEqual(10, len(character["Name"]))