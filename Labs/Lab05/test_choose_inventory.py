from unittest import TestCase
from unittest.mock import patch

from Lab05.functions import choose_inventory


class TestChoose_inventory(TestCase):
    def test_choose_inventory_validtest(self):
        my_list = ["Bahamut Shackle", "Dragon Fang", "Gorgon Scale", "Chimera Fur", "Obsidian Fang"]
        my_choice = 3
        chosen_inventory = choose_inventory(my_list, my_choice)
        for item in chosen_inventory:
            self.assertTrue(item in my_list)


    def test_choose_inventory_zerocase(self):
        my_list = []
        my_choice = 0
        chosen_inventory = choose_inventory(my_list, my_choice)
        self.assertEqual([], chosen_inventory)


    def test_choose_inventory_negativeselection(self):
        my_list = ["Bahamut Shackle", "Dragon Fang", "Gorgon Scale", "Chimera Fur", "Obsidian Fang"]
        my_choice = -5
        chosen_inventory = choose_inventory(my_list, my_choice)
        self.assertEqual([], chosen_inventory)


    def test_choose_inventory_greaterselection(self):
        my_list = ["Bahamut Shackle", "Dragon Fang", "Gorgon Scale", "Chimera Fur", "Obsidian Fang"]
        sorted_my_list = sorted(my_list)
        my_choice = 20
        chosen_inventory = choose_inventory(my_list, my_choice)
        self.assertEqual(sorted_my_list, chosen_inventory)


    def test_choose_inventory_sameselection(self):
        my_list = ["Bahamut Shackle", "Dragon Fang", "Gorgon Scale", "Chimera Fur", "Obsidian Fang"]
        my_choice = 5
        chosen_inventory = choose_inventory(my_list, my_choice)
        self.assertEqual(chosen_inventory, sorted(my_list))


    def test_choose_inventory_sameselection(self):
        my_list = ["Bahamut Shackle", "Dragon Fang", "Gorgon Scale", "Chimera Fur", "Obsidian Fang"]
        my_choice = 3
        chosen_inventory = choose_inventory(my_list, my_choice)
        self.assertTrue(type(chosen_inventory) == list)