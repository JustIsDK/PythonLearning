import requests
import unittest
#测试提交试用
class TestCookies(unittest.TestCase):

    def test_cookies(self):
        url="http://pqfavavk.dnat.tech/user/refresh_token"
        header = {
            "Cookie":"connect.sid=s%3A0H-MGX--Nl9yQPFg7auz2vqqWkyR1B4Z.0DcdtPqujQap%2BcO7yIck9txucLaJexLnMEgAfp19WrU; node_club=s%3A612f90cab821962e9699d2fc%24%24%24%24.ne2zWHXP2fjLB2GoO3LdmGaYyUp2xTQpFV4rE8g752s"
        }
        r = requests.post(url=url,headers=header)
        print(r.json())