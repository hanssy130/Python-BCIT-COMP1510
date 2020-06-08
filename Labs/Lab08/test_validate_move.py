from unittest import TestCase
from Lab08.maze import validate_move


class TestValidate_move(TestCase):
    def test_validate_move_down(self):
        self.assertEqual(True, validate_move((0, 0), "s"))


    def test_validate_move_up(self):
        self.assertEqual(True, validate_move((1, 1), "w"))


    def test_validate_move_right(self):
        self.assertEqual(True, validate_move((0, 0), "d"))


    def test_validate_move_left(self):
        self.assertEqual(True, validate_move((1, 1), "a"))


    def test_validate_move_upfail(self):
        self.assertEqual(False, validate_move((0, 0), "w"))


    def test_validate_move_downfail(self):
        self.assertEqual(False, validate_move((4, 0), "s"))


    def test_validate_move_rightfail(self):
        self.assertEqual(False, validate_move((0, 0), "a"))


    def test_validate_move_leftfail(self):
        self.assertEqual(False, validate_move((0, 4), "d"))


    def test_validate_move_is_valid_movement_boolean(self):
        self.assertEqual(bool, type(validate_move((0, 0), "d")))