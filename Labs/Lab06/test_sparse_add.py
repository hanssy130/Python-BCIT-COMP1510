from unittest import TestCase
from Lab06.sparsevector import sparse_add

class TestSparse_add(TestCase):
    def test_sparse_add_blank(self):
        sum = sparse_add({}, {})
        self.assertEqual({}, sum)


    def test_sparse_add_blankparameter1(self):
        sum = sparse_add({}, {1:1, 10:10, 30:30})
        self.assertEqual({1:1, 10:10, 30:30}, sum)


    def test_sparse_add_blankparameter2(self):
        sum = sparse_add({2:4, 6:8, 3:5}, {})
        self.assertEqual({2:4, 6:8, 3:5}, sum)


    def test_sparse_add_samekeys(self):
        sum = sparse_add({0:5, 1:5, 2:5}, {0:1, 1:2, 2:3})
        self.assertEqual({0:6, 1:7, 2:8}, sum)


    def test_sparse_add_differentkeys(self):
        sum = sparse_add({0:1, 3:4, 6:5}, {2:1, 4:7, 10:4})
        self.assertEqual({0: 1, 3: 4, 6: 5, 2: 1, 4: 7, 10: 4}, sum)


    def test_sparse_add_somekeys(self):
        sum = sparse_add({0:4, 1:5, 2:7}, {0:3, 1:4, 3:9})
        self.assertEqual({0: 7, 1: 9, 2: 7, 3: 9}, sum)


    def test_sparse_add_zerovalue(self):
        sum = sparse_add({0:-5, 4:-3}, {0:5, 4:3})
        self.assertEqual({}, sum)


    def test_sparse_add_type(self):
        sum = sparse_add({1:1, 2:2}, {2:2, 3:3})
        self.assertTrue(type(sum) == dict)
        #But I guess this isn't necessary, as I was able to verify the above, which are dictionaries already, right?

    def test_sparse_add_len(self):
        sum = sparse_add({1:1, 2:2}, {2:2, 3:3})
        self.assertTrue(len(sum) == 3)
        #But I guess this isn't necessary, as I was able to verify the above, which are dictionaries already, right?
