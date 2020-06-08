from unittest import TestCase
from unittest.mock import patch

from A2.dungeonsanddragons import choose_inventory


class TestChoose_inventory(TestCase):


    @patch('builtins.input', side_effect=["-1"])
    def test_choose_inventory_zerotest(self, mock_input):
        my_list = ["Bahamut Shackle", "Dragon Fang", "Gorgon Scale", "Chimera Fur", "Obsidian Fang"]
        chosen_inventory = choose_inventory(my_list)
        self.assertEqual([], chosen_inventory)

    @patch('builtins.input', side_effect=["3", "-1"])
    def test_choose_inventory_validtest(self, mock_input):
        my_list = ["Bahamut Shackle", "Dragon Fang", "Gorgon Scale", "Chimera Fur", "Obsidian Fang"]
        chosen_inventory = choose_inventory(my_list)
        self.assertEqual(["Gorgon Scale"], chosen_inventory)


    @patch('builtins.input', side_effect=["1", "2", "3", "3", "5", "-1"])
    def test_choose_inventory_validtest(self, mock_input):
        my_list = ["Bahamut Shackle", "Dragon Fang", "Gorgon Scale", "Chimera Fur", "Obsidian Fang"]
        chosen_inventory = choose_inventory(my_list)
        self.assertEqual(["Bahamut Shackle", "Dragon Fang", "Gorgon Scale", "Gorgon Scale", "Obsidian Fang"], chosen_inventory)


    @patch('builtins.input', side_effect=["6", "-2", "2", "-1"])
    def test_choose_inventory_outofbounds(self, mock_input):
        my_list = ["Bahamut Shackle", "Dragon Fang", "Gorgon Scale", "Chimera Fur", "Obsidian Fang"]
        chosen_inventory = choose_inventory(my_list)
        self.assertEqual(["Dragon Fang"], chosen_inventory)


    @patch('builtins.input', side_effect=["1", "2", "3", "3", "5", "-1"])
    def test_choose_inventory_type(self, mock_input):
        my_list = ["Bahamut Shackle", "Dragon Fang", "Gorgon Scale", "Chimera Fur", "Obsidian Fang"]
        chosen_inventory = choose_inventory(my_list)
        self.assertEqual(list, type(chosen_inventory))


    @patch('builtins.input', side_effect=["1", "2", "3", "3", "5", "-1"])
    def test_choose_inventory_length(self, mock_input):
        my_list = ["Bahamut Shackle", "Dragon Fang", "Gorgon Scale", "Chimera Fur", "Obsidian Fang"]
        chosen_inventory = choose_inventory(my_list)
        self.assertEqual(5, len(chosen_inventory))



    # def test_choose_inventory_zerocase(self):
    #     my_list = []
    #     chosen_inventory = choose_inventory(my_list)
    #     self.assertEqual([], chosen_inventory)
    #
    #
    # def test_choose_inventory_negativeselection(self):
    #     my_list = ["Bahamut Shackle", "Dragon Fang", "Gorgon Scale", "Chimera Fur", "Obsidian Fang"]
    #     chosen_inventory = choose_inventory(my_list)
    #     self.assertEqual([], chosen_inventory)
    #
    #
    # def test_choose_inventory_greaterselection(self):
    #     my_list = ["Bahamut Shackle", "Dragon Fang", "Gorgon Scale", "Chimera Fur", "Obsidian Fang"]
    #     sorted_my_list = sorted(my_list)
    #     chosen_inventory = choose_inventory(my_list)
    #     self.assertEqual(sorted_my_list, chosen_inventory)
    #
    #
    # def test_choose_inventory_sameselection(self):
    #     my_list = ["Bahamut Shackle", "Dragon Fang", "Gorgon Scale", "Chimera Fur", "Obsidian Fang"]
    #     chosen_inventory = choose_inventory(my_list)
    #     self.assertEqual(chosen_inventory, sorted(my_list))
    #
    #
    # def test_choose_inventory_sameselection(self):
    #     my_list = ["Bahamut Shackle", "Dragon Fang", "Gorgon Scale", "Chimera Fur", "Obsidian Fang"]
    #     chosen_inventory = choose_inventory(my_list)
    #     self.assertTrue(type(chosen_inventory) == list)
