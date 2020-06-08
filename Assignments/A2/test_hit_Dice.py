from unittest import TestCase
from unittest.mock import patch

from A2.dungeonsanddragons import Hit_Dice

class TestHit_Dice(TestCase):
    @patch('random.randint', return_value=2)
    def test_Hit_Dice_validtest(self, mock_input):
        self.assertEqual(2, Hit_Dice("Wizard"))


    @patch('random.randint', return_value=7)
    def test_Hit_Dice_invalidtest(self, mock_input):
        self.assertEqual(int, type(Hit_Dice("Wizard")))
