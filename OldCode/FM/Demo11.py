from ddt import file_data
import random
import unittest
from ddt import  ddt,data


# 定义test类<必须继承 unittest.TestCase>


def get_radom_date():
    return random.random

@ddt
class TestDDT(unittest.TestCase):

    @unittest.skip('这个跳过')
    @data(get_radom_date(),get_radom_date())
    def test01(self,value):
        print(value)
        self.assertTrue(value>2)

    @file_data('../data/login.json')
    def test_login_json(self,loginname,passwd):
        self.user.user_login(loginname,passwd)

if __name__ == '__main__':
    unittest.main(verbosity=2)
