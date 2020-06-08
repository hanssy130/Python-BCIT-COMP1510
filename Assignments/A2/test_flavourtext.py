from unittest import TestCase
from unittest.mock import patch

from A2.dungeonsanddragons import flavourtext


class TestFlavourtext(TestCase):
    @patch('random.choice', return_value="Good *hic* choice! Anything else? (-1 to finish): ")
    def test_flavourtext_validtest(self, mock):
        self.assertEqual("Good *hic* choice! Anything else? (-1 to finish): ", flavourtext())
