import io
import unittest.mock
from unittest import TestCase


from Lab04.roman_numerals import convert_to_roman_numeral


class TestConvert_to_roman_numeral(TestCase):


    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_convert_to_roman_numeral_1(self,mockoutput1):
        number_to_convert = 1
        convert_to_roman_numeral(number_to_convert)
        self.assertEqual("I\n", mockoutput1.getvalue())


    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_convert_to_roman_numeral_4(self, mockoutputfour):
        number_to_convert = 4
        convert_to_roman_numeral(number_to_convert)
        self.assertEqual("IV\n", mockoutputfour.getvalue())


    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_convert_to_roman_numeral_5(self, mockoutputfive):
        number_to_convert = 5
        convert_to_roman_numeral(number_to_convert)
        self.assertEqual("V\n", mockoutputfive.getvalue())


    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_convert_to_roman_numeral_6(self, mockoutputsix):
        number_to_convert = 6
        convert_to_roman_numeral(number_to_convert)
        self.assertEqual("VI\n", mockoutputsix.getvalue())


    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_convert_to_roman_numeral_9(self, mockoutputnine):
        number_to_convert = 9
        convert_to_roman_numeral(number_to_convert)
        self.assertEqual("IX\n", mockoutputnine.getvalue())


    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_convert_to_roman_numeral_20(self, mockoutputtwenty):
        number_to_convert = 20
        convert_to_roman_numeral(number_to_convert)
        self.assertEqual("XX\n", mockoutputtwenty.getvalue())


    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_convert_to_roman_numeral_40(self, mockoutputforty):
        number_to_convert = 40
        convert_to_roman_numeral(number_to_convert)
        self.assertEqual("XL\n", mockoutputforty.getvalue())


    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_convert_to_roman_numeral_50(self, mockoutputfifty):
        number_to_convert = 50
        convert_to_roman_numeral(number_to_convert)
        self.assertEqual("L\n", mockoutputfifty.getvalue())


    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_convert_to_roman_numeral_60(self, mockoutputsixty):
        number_to_convert = 60
        convert_to_roman_numeral(number_to_convert)
        self.assertEqual("LX\n", mockoutputsixty.getvalue())


    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_convert_to_roman_numeral_90(self, mockoutputninety):
        number_to_convert = 90
        convert_to_roman_numeral(number_to_convert)
        self.assertEqual("XC\n", mockoutputninety.getvalue())


    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_convert_to_roman_numeral_100(self, mockoutputhundred):
        number_to_convert = 100
        convert_to_roman_numeral(number_to_convert)
        self.assertEqual("C\n", mockoutputhundred.getvalue())


    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_convert_to_roman_numeral_400(self, mockoutputfourhundred):
        number_to_convert = 400
        convert_to_roman_numeral(number_to_convert)
        self.assertEqual("CD\n", mockoutputfourhundred.getvalue())


    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_convert_to_roman_numeral_500(self, mockoutputfivehundred):
        number_to_convert = 500
        convert_to_roman_numeral(number_to_convert)
        self.assertEqual("D\n", mockoutputfivehundred.getvalue())


    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_convert_to_roman_numeral_600(self, mockoutputsixhundred):
        number_to_convert = 600
        convert_to_roman_numeral(number_to_convert)
        self.assertEqual("DC\n", mockoutputsixhundred.getvalue())


    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_convert_to_roman_numeral_1000(self, mockoutputonethousand):
        number_to_convert = 900
        convert_to_roman_numeral(number_to_convert)
        self.assertEqual("CM\n", mockoutputonethousand.getvalue())


    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_convert_to_roman_numeral_1000(self, mockoutputonethousand):
        number_to_convert = 1000
        convert_to_roman_numeral(number_to_convert)
        self.assertEqual("M\n", mockoutputonethousand.getvalue())


    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_convert_to_roman_numeral_10000(self, mockoutputtenthousand):
        number_to_convert = 10000
        convert_to_roman_numeral(number_to_convert)
        self.assertEqual("MMMMMMMMMM\n", mockoutputtenthousand.getvalue())
