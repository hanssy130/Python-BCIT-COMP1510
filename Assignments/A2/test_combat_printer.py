import unittest
from unittest import TestCase
from unittest.mock import patch
import io

from A2.dungeonsanddragons import combat_printer

player1 = {'Name': 'Lymy', 'Race': 'Dwarf', 'Class': 'Bard', 'HP': [3, 3], 'Strength': 11, 'Dexterity': 12,
           'Constitution': 9, 'Intelligence': 8, 'Wisdom': 9, 'Charisma': 8, 'XP': 0}
player2 = {'Name': 'Vevy', 'Race': 'Elf', 'Class': 'Rogue', 'HP': [6, 6], 'Strength': 10, 'Dexterity': 11,
           'Constitution': 15, 'Intelligence': 12, 'Wisdom': 11, 'Charisma': 10, 'XP': 0}


class TestCombat_printer(TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_printer_miss(self, mock_output):
        firstdex = 0
        seconddex = 0
        firstdamage = 5
        seconddamage = 5
        combat_printer(player1, player2, firstdex, seconddex, firstdamage, seconddamage)
        self.assertEqual("---FIGHT!---\nLymy goes first!\nLymy missed!\nVevy missed!\n", mock_output.getvalue())


    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_printer_p2hit_p1die(self, mock_output):
        firstdex = 0
        seconddex = 1
        firstdamage = 5
        seconddamage = 5
        combat_printer(player1, player2, firstdex, seconddex, firstdamage, seconddamage)
        self.assertEqual("---FIGHT!---\nLymy goes first!\nLymy missed!\nVevy inflicts 5!\nLymy has been slain!\n", mock_output.getvalue())


    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_printer_p2hit_p1liv(self, mock_output):
        firstdex = 0
        seconddex = 1
        firstdamage = 5
        seconddamage = 2
        combat_printer(player1, player2, firstdex, seconddex, firstdamage, seconddamage)
        self.assertEqual("---FIGHT!---\nLymy goes first!\nLymy missed!\nVevy inflicts 2!\n", mock_output.getvalue())


    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_printer_p1hit_p2die(self, mock_output):
        firstdex = 1
        seconddex = 0
        firstdamage = 10
        seconddamage = 5
        combat_printer(player1, player2, firstdex, seconddex, firstdamage, seconddamage)
        self.assertEqual("---FIGHT!---\nLymy goes first!\nLymy inflicts 10!\nVevy has been slain!\n", mock_output.getvalue())


    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_printer_p1hit_p2liv_p2mis(self, mock_output):
        firstdex = 1
        seconddex = 0
        firstdamage = 5
        seconddamage = 5
        combat_printer(player1, player2, firstdex, seconddex, firstdamage, seconddamage)
        self.assertEqual("---FIGHT!---\nLymy goes first!\nLymy inflicts 5!\nVevy missed!\n", mock_output.getvalue())


    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_printer_p1hit_p2liv_p2hit_p1die(self, mock_output):
        firstdex = 1
        seconddex = 1
        firstdamage = 5
        seconddamage = 3
        combat_printer(player1, player2, firstdex, seconddex, firstdamage, seconddamage)
        self.assertEqual("---FIGHT!---\nLymy goes first!\nLymy inflicts 5!\nVevy inflicts 3!\nLymy has been slain!\n", mock_output.getvalue())


    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_printer_p1hit_p2liv_p2hit_p1liv(self, mock_output):
        firstdex = 1
        seconddex = 1
        firstdamage = 5
        seconddamage = 2
        combat_printer(player1, player2, firstdex, seconddex, firstdamage, seconddamage)
        self.assertEqual("---FIGHT!---\nLymy goes first!\nLymy inflicts 5!\nVevy inflicts 2!\n", mock_output.getvalue())
