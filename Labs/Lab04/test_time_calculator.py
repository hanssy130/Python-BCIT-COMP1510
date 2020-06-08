import io
import unittest.mock
from unittest import TestCase


from Lab04.time_calculator import time_calculator


 class TestTime_calculator(TestCase):


    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_time_calculator_zero_seconds(self, mockzerooutput):
        number_of_seconds = 0
        time_calculator(number_of_seconds)
        self.assertEqual("0 days, 0 hours, 0 minutes, and 0 seconds.\n", mockzerooutput.getvalue())


    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_time_calculator_999999_seconds(self, highoutput):
        number_of_seconds = 999999
        time_calculator(number_of_seconds)
        self.assertEqual("11 days, 13 hours, 46 minutes, and 39 seconds.\n", highoutput.getvalue())


    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_time_calculator_1_day(self, oneday):
        number_of_seconds = 86400
        time_calculator(number_of_seconds)
        self.assertEqual("1 days, 0 hours, 0 minutes, and 0 seconds.\n", oneday.getvalue())


    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_time_calculator_1_hour(self, onehour):
        number_of_seconds = 3600
        time_calculator(number_of_seconds)
        self.assertEqual("0 days, 1 hours, 0 minutes, and 0 seconds.\n", onehour.getvalue())


    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_time_calculator_1_minute(self, oneminute):
        number_of_seconds = 60
        time_calculator(number_of_seconds)
        self.assertEqual("0 days, 0 hours, 1 minutes, and 0 seconds.\n", oneminute.getvalue())


    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_time_calculator_1_second(self, onesecond):
        number_of_seconds = 1
        time_calculator(number_of_seconds)
        self.assertEqual("0 days, 0 hours, 0 minutes, and 1 seconds.\n", onesecond.getvalue())
