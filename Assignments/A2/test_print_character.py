import unittest
from unittest import TestCase
from unittest.mock import patch
from A2.dungeonsanddragons import print_character


import io

@unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
class TestPrint_character(TestCase):
    def test_print_character_validtest(self, mock_stdout):
        character = {'Name': 'Gyga', 'Race': 'Elf', 'Class': 'Bard', 'HP': [2, 2], 'Strength': 16, 'Dexterity': 11, 'Constitution': 13, 'Intelligence': 13, 'Wisdom': 13, 'Charisma': 13, 'XP': 0}
        print_character(character)
        self.assertEqual("\nName: Gyga\nRace: Elf\nClass: Bard\nHP: 2/2\nStrength: 16\nDexterity: 11\nConstitution: 13\nIntelligence: 13\nWisdom: 13\nCharisma: 13\nXP: 0\n", mock_stdout.getvalue())

    def test_print_character_validinventory(self, mock_stdout):
        character = {'Name': 'Gyga', 'Race': 'Elf', 'Class': 'Bard', 'HP': [2, 2], 'Strength': 16, 'Dexterity': 11, 'Constitution': 13, 'Intelligence': 13, 'Wisdom': 13, 'Charisma': 13, 'XP': 0, 'Inventory': ["Gorgon Shield", "Shadow Daggers"]}
        print_character(character)
        self.assertEqual("\nName: Gyga\nRace: Elf\nClass: Bard\nHP: 2/2\nStrength: 16\nDexterity: 11\nConstitution: 13\nIntelligence: 13\nWisdom: 13\nCharisma: 13\nXP: 0\nInventory: Gorgon Shield, Shadow Daggers\n", mock_stdout.getvalue())

    def test_print_character_type(self, mock_stdout):
        character = {'Name': 'Gyga', 'Race': 'Elf', 'Class': 'Bard', 'HP': [2, 2], 'Strength': 16, 'Dexterity': 11, 'Constitution': 13, 'Intelligence': 13, 'Wisdom': 13, 'Charisma': 13, 'XP': 0, 'Inventory': ["Gorgon Shield", "Shadow Daggers"]}
        print_character(character)
        self.assertEqual(str, type(mock_stdout.getvalue()))

