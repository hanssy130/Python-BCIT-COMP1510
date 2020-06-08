from unittest import TestCase

from Lab08.maze import move_character


class TestMove_character(TestCase):
    def test_move_character_up(self):
        self.assertEqual([1, 2], move_character([2, 2], "w"))


    def test_move_character_down(self):
        self.assertEqual([3, 2], move_character([2, 2], "s"))


    def test_move_character_right(self):
        self.assertEqual([2, 3], move_character([2, 2], "d"))


    def test_move_character_left(self):
        self.assertEqual([2, 1], move_character([2, 2], "a"))


    def test_move_character_list(self):
        self.assertEqual(list, type(move_character([2, 2], "a")))
