from unittest import TestCase
from Lab07.midterm import cutoff


class TestCutoff(TestCase):
    def test_cutoff_emptylist_and_zero(self):
        self.assertEqual(cutoff([], 0), 0)


    def test_cutoff_emptylist_and_five(self):
        self.assertEqual(cutoff([], 5), 0)


    def test_cutoff_zero_and_zero(self):
        self.assertEqual(cutoff([0], 0), 0)


    def test_cutoff_zero_and_five(self):
        self.assertEqual(cutoff([0], 5), 0)


    def test_cutoff_zero_and_zero(self):
        self.assertEqual(cutoff([0], 0), 0)


    def test_cutoff_two_and_two(self):
        self.assertEqual(cutoff([2], 2), 1)


    def test_cutoff_two_and_four(self):
        self.assertEqual(cutoff([2], 4), 0)


    def test_cutoff_list_and_zero(self):
        self.assertEqual(cutoff([1, 2, 3, 4, 5], 0), 0)


    def test_cutoff_list_and_two(self):
        self.assertEqual(cutoff([1, 2, 3, 4, 5], 2), 2)


    def test_cutoff_twos_list_and_two(self):
        self.assertEqual(cutoff([2, 2, 2, 2, 2], 2), 5)


    def test_cutoff_twos_list_and_ten(self):
        self.assertEqual(cutoff([2, 2, 2, 2, 2], 10), 0)


    def test_cutoff_multiples_of_three(self):
        self.assertEqual(cutoff([3, 6, 9, 12, 15], 3), 5)


    def test_cutoff_list_and_zero(self):
        self.assertEqual(cutoff([3, 2, 1], 0), 0)
