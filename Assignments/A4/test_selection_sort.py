from unittest import TestCase
from A4.question4 import selection_sort


class TestSelection_sort(TestCase):
    def test_selection_sort_numbers(self):
        self.assertEqual([-4, 1, 3, 5, 9], selection_sort([3, 5, 1, 9, -4]))

    def test_selection_sort_strings(self):
        self.assertEqual(['A', 'B', 'a'], selection_sort(["a", "B", "A"]))

    def test_selection_sort_type(self):
        self.assertEqual(list, type(selection_sort([3, 5, 1, 9, -4])))

    def test_selection_sort_error(self):
        self.assertRaise(TypeError, selection_sort([3, "a", 1, 9, -4]))