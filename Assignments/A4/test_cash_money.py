from unittest import TestCase
from A4.question5 import cash_money


class TestCash_money(TestCase):
    def test_cash_money_validtest(self):
        self.assertEqual({20: 1, 2: 1, 0.1: 2, 0.01: 2}, cash_money(22.22))

    def test_cash_money_type(self):
        self.assertEqual(dict, type(cash_money(22.22)))

    def test_cash_money_99(self):
        self.assertEqual({100: 9, 50: 1, 20: 1, 10: 1, 2: 2, 0.25: 3, 0.1: 1, 0.05: 1, 0.01: 4}
, cash_money(984.94))

    def test_cash_money_zero(self):
        self.assertEqual({}, cash_money(0))