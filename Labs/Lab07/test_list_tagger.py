from unittest import TestCase
from Lab07.midterm import list_tagger


class TestList_tagger(TestCase):
    def test_list_tagger_empty_list(self):
        self.assertEqual(0, list_tagger([])[0])


    def test_list_tagger_oneitem(self):
        self.assertEqual(1, list_tagger([5])[0])


    def test_list_tagger_multipleitems(self):
        self.assertEqual(3, list_tagger([8,7,6])[0])
