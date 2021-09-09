import unittest
import requests

class GetToken(unittest.TestCase):
    def test_get_qa_token(self):
        get_header = {
            'origin': 'https://uat-ecp-site.adidas.com.cn',
            'referer': 'https://uat-ecp-site.adidas.com.cn/',
            'source': 'A001',
            'Content-Type':'application/x-www-form-urlencoded'
        }
        get_post = {
            'smsOtp': '000000',
            'phone': '18437909853'
        }
        url = 'https://sit-auth-api.adidas.com.cn/v1/users/login/sms'

        r = requests.post(url=url,data=get_post,headers=get_header,verify=False)
        accesstoken = r.json()['data']['access_token']
        print(accesstoken)