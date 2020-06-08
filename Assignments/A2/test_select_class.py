from unittest import TestCase
from unittest.mock import patch
from A2.dungeonsanddragons import select_class


class TestSelect_class(TestCase):
    @patch('builtins.input', return_value="Monk")
    def test_select_class_validtest(self, mock_input):
        self.assertEqual("Monk", select_class())


    @patch('builtins.input', return_value="Monk")
    def test_select_class_typetest(self, mock_input):
        self.assertEqual(str, type(select_class()))


    @patch('builtins.input', side_effect=["oh no", "Monk"])
    def test_select_class_onemistake(self, mock_input):
        self.assertEqual("Monk", (select_class()))


    @patch('builtins.input', side_effect=["oh no", "yeet", "asdf", "Monk"])
    def test_select_class_multiplemistake(self, mock_input):
        self.assertEqual("Monk", (select_class()))