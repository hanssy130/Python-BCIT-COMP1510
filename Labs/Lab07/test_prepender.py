from unittest import TestCase
from Lab07.midterm import prepender


class TestPrepender(TestCase):
    def test_prepender_blank_list_and_test(self):
        my_list = []
        my_string = ""
        prepender(my_list, my_string)
        self.assertEqual(my_list, [])


    def test_prepender_blank_and_Python(self):
        my_list = []
        my_string = "Python"
        prepender(my_list, my_string)
        self.assertEqual(my_list, [])


    def test_prepender_Python_and_blank(self):
        my_list = ["Python"]
        my_string = ""
        prepender(my_list, my_string)
        self.assertEqual(my_list, ["Python"])


    def test_prepender_I_love_Python(self):
        my_list = ["Python"]
        my_string = "I love "
        prepender(my_list, my_string)
        self.assertEqual(my_list, ["I love Python"])


    def test_prepender_Long_List_and_Blank_String(self):
        my_list = ["Python", "is", "better", "than", "JavaScript"]
        my_string = ""
        prepender(my_list, my_string)
        self.assertEqual(my_list, ["Python", "is", "better", "than", "JavaScript"])


    def test_prepender_Long_List_and_String(self):
        my_list = ["Python", "is", "better", "than", "JavaScript"]
        my_string = "Umm... "
        prepender(my_list, my_string)
        self.assertEqual(my_list, ['Umm... Python', 'Umm... is', 'Umm... better', 'Umm... than', 'Umm... JavaScript'])


    def test_prepender_multiple_blanks_and_string(self):
        my_list = ["", "", ""]
        my_string = "Check"
        prepender(my_list, my_string)
        self.assertEqual(my_list, ["Check", "Check", "Check"])
