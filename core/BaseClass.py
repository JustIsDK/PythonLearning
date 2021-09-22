# import unittest
# class BaseCase(unittest.TestCase):
#     def __init__(self,methodNmae = 'runTest'):
#         super(BaseCase, self).__init__(methodNmae)
#         self.token = '123456'

"""
所有的测试用例的基本父类
所有的测试用例类继承父类
"""


import unittest
import requests
from config import config_data

# 继承unittest
class BaseCase(unittest.TestCase):

    def __init__(self,methodName='runTest'):
        super(BaseCase, self).__init__(methodName) # 构造器显式调用父类构造器
        # 设置token

    @classmethod
    def get_token(cls,secret):
        """
        定义为类方法，主要为 OA类继承的时候在 setUpClass 中可以直接调用生成token
        定义类的私有方法，获取用户的token值
        :return:
        """
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={config_data['id']}&corpsecret={secret}"
        res = requests.get(url)
        # 添加断言
        # self.assertIn("access_token", res.json())
        assert "access_token" in res.json()
        # 更改testdata 的值
        token = res.json()["access_token"]
        return token


