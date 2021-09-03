import unittest
from ddt import ddt,data

@ddt
class TestDDT(unittest.TestCase):
    @data(10,5,4,8)
    def test_datas(self,test_value):
        print('value is ',test_value)
        self.assertGreater(test_value,1)


