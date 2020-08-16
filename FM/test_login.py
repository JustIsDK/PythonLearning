import unittest
from ddt import  ddt,data,unpack,file_data
from bussiness.main_model import MainModel

# 定义test类<必须继承 unittest.TestCase>
from pom.base import BaseUtil

@ddt
class TestLogin(unittest.TestCase):

    def setUp(self) -> None:
        """每一个testcase 执行之前的操作"""
        pass


    def tearDown(self) -> None:
        """ 每一个testcase 执行完成之后的操作"""
        BaseUtil.save_screenshot()

    @classmethod
    def setUpClass(cls) -> None:
        """整个类运行执行前操作"""
        BaseUtil.max_window()
        main = MainModel()
        cls.user = main.go_to_login_page()

    @classmethod
    def tearDownClass(cls) -> None:
        """整个类运行执行之后操作"""
        BaseUtil.close_window()

    # 测试方法  test开头
    @file_data('../data/login.json')
    def test_login_json(self, loginname, passwd):
        self.user.user_login(loginname, passwd)

        # login_name = main.user_name_text
        # self.assertEqual(login_name,'test10')

if __name__ == '__main__':
    unittest.main(verbosity=2)