from unittest import TestCase


class TestNumber_generator(TestCase):

    @patch('functions.roll_die', return_value=18)
    def test_number_generator(self, mock_roll_die):

        self.assertTrue()