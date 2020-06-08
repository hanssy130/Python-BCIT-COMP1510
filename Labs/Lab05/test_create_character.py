from unittest import TestCase
from unittest.mock import patch

from Lab05.functions import create_character

class TestCreate_character(TestCase):
    def test_create_character_lengthcheck(self):
        NameSize = 4
        Created = create_character(NameSize)
        self.assertTrue(len(Created) == 7)


    def test_create_character_lengthcheckfail(self):
        NameSize = 4
        Created = create_character(NameSize)
        self.assertFalse(len(Created) == 8)

    def test_create_character_attrcheck(self):
        NameSize = 4
        Created = create_character(NameSize)
        self.assertTrue(len(Created[2]) == 2)


    def test_create_character_attrcheckfail(self):
        NameSize = 4
        Created = create_character(NameSize)
        self.assertFalse(len(Created[2]) == 4)


    def test_create_character_namecheck(self):
        NameSize = 4
        Created = create_character(NameSize)
        self.assertTrue(type(Created[0]) == str)


    def test_create_character_listcheck(self):
        NameSize = 4
        Created = create_character(NameSize)
        self.assertTrue(type(Created[1]) == list)